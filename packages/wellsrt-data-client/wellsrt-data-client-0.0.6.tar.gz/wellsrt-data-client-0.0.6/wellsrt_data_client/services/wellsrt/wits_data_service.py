import logging
import json

from typing import Optional, Union
from datetime import datetime, timezone

from azure.kusto.data.helpers import dataframe_from_result_table

import pandas as pd

from wellsrt_data_client.commons import EnvVariables

from wellsrt_data_client.services.adx import AzAdxDataService

from enum import auto, IntEnum
from strenum import UppercaseStrEnum

class WitsDataService(AzAdxDataService):

    def __init__(self, env_vars:EnvVariables):
        AzAdxDataService.__init__(self, env_vars=env_vars)

    def execute_query(self, kql_query:str) -> Optional[pd.DataFrame]:
        """
        Execute a KQL Query and convert result to pd.DataFrame
        """

        if kql_query is None and len(kql_query) == 0:
            return None
        client = self.get_kusto_client()
        db_name = self.get_database_name()

        response = client.execute(database=db_name, query= kql_query)
        if len(response.primary_results) > 0:
            return dataframe_from_result_table(response.primary_results[0])
        else:
            return None

    def query_logs_names(self, wellboreId: str)  -> Optional[pd.DataFrame]:
        """
        Get all avaliable logs names of a Wellbore in the WellsRT Data (ADX Database)
        """
        kql_query = f"""
            let wellbore_id = '{wellboreId}';

            let dtime_logs = WitsDtimes
            | where WellboreId == wellbore_id
            | project WellId, WellName, WellboreId, WellboreName, IndexType, LogName
            | distinct WellId, WellName, WellboreId, WellboreName, IndexType, LogName
            ;

            let depths_logs = WitsDepths
            | where WellboreId == wellbore_id
            | project WellId, WellName, WellboreId, WellboreName, IndexType, LogName
            | distinct WellId, WellName, WellboreId, WellboreName, IndexType, LogName
            ;

            union dtime_logs, depths_logs
            | project WellId, WellName, WellboreId, WellboreName, IndexType, LogName
            ;
        """
        return self.execute_query(kql_query=kql_query)
        
    def query_data_gap(self, well: str, wellbore:str=None, log:str=None, threshold_diff_in_sec=60)  -> Optional[pd.DataFrame]:
        """
        Get all avaliable logs names of a Wellbore in the WellsRT Data (ADX Database)
        """
        let_query:list[str] = []
        where_query:list[str] = []

        if wellbore is not None and len(wellbore) > 0:
            let_query.append(f'let wellbore = "{wellbore}";')
            where_query.append(f'| where WellboreId == wellbore or WellboreName == wellbore')

        if log is not None and len(log) > 0:
            let_query.append(f'let log = "{log}";')
            where_query.append(f'| where LogName == log')

        kql_query = f"""
            let well = "{well}";
            {" ".join(let_query)}

            WitsDtimes
            | where WellName == well or WellId == well
            {" ".join(where_query)}
            | project WellId, WellboreId, WellboreName, Dtime, LogName
            | distinct WellId, WellboreId, WellboreName, Dtime, LogName
            | order by WellId, WellboreId, LogName, Dtime asc
            | extend  Prev_WellboreId = prev(WellboreId), Prev_LogName = prev(LogName), Prev_Dtime = prev(Dtime)
            | project WellId, WellboreId, WellboreName, LogName, Dtime, Prev_Dtime, Diff = case(Prev_WellboreId == WellboreId and Prev_LogName == LogName, (Dtime - Prev_Dtime)/1s, double(null))
            | where isnotnull(Diff) and Diff > {threshold_diff_in_sec}
        """
        return self.execute_query(kql_query=kql_query)



    def query_dtime_logcurve_names(self, wellboreId: str, logName:str)  -> list[str]:
        """
        Get all avaliable log_curve names of a Log in the ADX
        """
        kql_query = f"""
            let wellbore_id = "{wellboreId}";
            let log_name = "{logName}";

            WitsDtimes
            | where WellboreId == wellbore_id and LogName == log_name
            | order by Dtime
            | take 1
            | project  Datas
            | evaluate bag_unpack(Datas)
            ;
        """
        df = self.execute_query(kql_query=kql_query)
        if df is None:
            return []
        return df.columns.to_list()

    def query_dtimes_range(self, wellboreId:str, logNames:Union[str | list[str]]) -> Optional[pd.DataFrame]:
        """
        Get Min and Max DTime of a Wellbore in the ADX
        """
        logs_names = []
        if isinstance(logNames,str):
            logs_names.append(logNames)
        elif isinstance(logNames,list):
            logs_names = logNames

        json_log_names = json.dumps(logs_names)

        kql_query = f"""
            let wellbore_id = '{wellboreId}';
            let log_names = dynamic({json_log_names});

            WitsDtimes
            | where WellboreId == wellbore_id and LogName in (log_names)
            | project WellboreId, LogName, Dtime
            | distinct  WellboreId, LogName, Dtime
            | summarize MinDtime = min(Dtime), MaxDtime = max(Dtime), LogCount=count() by  WellboreId,  LogName
            ;
        """
        return self.execute_query(kql_query=kql_query)
        
    def query_dtimes_data(self, wellboreId:str, logName:str, curveNames:list[str], startTime:Optional[datetime] = None, endTime:Optional[datetime] = None, showUnits:bool=False, limit=50000) -> Optional[pd.DataFrame]:
        """
        Query DTime log data based on wellboreId, logName, curveNames, Optional[startTime], Optional[endTime]  from ADX
        """

        if wellboreId is None or logName is None or curveNames is None or len(curveNames) == 0:
            return None
        
        # get current start_dtime, end_dtime fromADX
        df_min_max_dtime = self.query_dtimes_range(wellboreId=wellboreId, logNames=logName)
        if df_min_max_dtime is None or len(df_min_max_dtime) == 0:
            # there is no data in ADX
            return None
        start_dtime = df_min_max_dtime.at[0, 'MinDtime']
        end_dtime = df_min_max_dtime.at[0, 'MaxDtime']

        # compare start_dtime and end_dtime with startTime and endTime in the parameters
        if startTime is not None and startTime > start_dtime:
            start_dtime = startTime

        if endTime is not None and endTime < end_dtime:
            end_dtime = endTime

        # process query data
        df_result:Optional[pd.DataFrame] = None
        
        client = self.get_kusto_client()
        db_name = self.get_database_name()

        if limit < 1:
            limit = 50000
        
        is_process_next_query = True

        # build curve_name query
        project_curve_names, distinct_curve_names, curve_names_mapping = self._build_wits_curve_query(curveNames=curveNames, showUnits=showUnits)

        while is_process_next_query:
            #print(f"Process - start_dtime: {start_dtime} - end_dtime: {end_dtime} - limit: {limit}")
            kql_dtime_query = self._build_dtimes_query(
                wellboreId=wellboreId, 
                logName=logName, 
                projectCurveNames=project_curve_names,
                distinctCurveNames=distinct_curve_names,
                startDtime=start_dtime, 
                endDtime=end_dtime, 
                limit=limit
            )

            response = client.execute(db_name, kql_dtime_query)
            # we also support dataframes:
            df_query_result = dataframe_from_result_table(response.primary_results[0])
            total_query_item = len(df_query_result)
            # print(f"Process - total_query_item: {total_query_item}")

            if total_query_item > 0:
                if df_result is None:
                    df_result = df_query_result
                else:
                    if hasattr(df_result, 'concat'):
                        # process with Pandas v2.x
                        df_result = pd.concat([df_result, df_query_result])
                    elif hasattr(df_result, 'append'):
                        # process with Pandas v1.x
                        df_result = df_result.append(df_query_result)
                    else:
                        # process with Pandas v2.x
                        df_result = pd.concat([df_result, df_query_result])

            if total_query_item < limit:
                # quick - end of process
                is_process_next_query = False
                break
            else:
                # get Dtime of the last record
                start_dtime = df_query_result.at[df_query_result.index[-1],'Dtime']
                is_process_next_query = True

        # logging.debug("df_result - curve_names_mapping: {curve_names_mapping}", curve_names_mapping)
        if curve_names_mapping is not None and len(curve_names_mapping) > 0:
            # reformat dataframe name
            try:
                df_result.rename(columns=curve_names_mapping,inplace=True)
            except Exception as ex:
                logging.warning("df_result - rename: {error}", ex)
        
        return df_result

    def _build_dtimes_query(self, wellboreId:str, logName:str, projectCurveNames:list[str], distinctCurveNames:list[str], startDtime:datetime, endDtime:datetime, limit=10000) -> str:
        """
        Build KQL query WITS DTime Data
        """

        # reset default limit item
        if limit < 1:
            limit = 10000

        utc_format = '%Y-%m-%dT%H:%M:%S%z'
        str_start_dtime = startDtime.strftime(utc_format)
        str_end_dtime = endDtime.strftime(utc_format)
        
        return  f"""
            let wellbore_id = '{wellboreId}';
            let log_name = '{logName}';
            let start_dtime = datetime('{str_start_dtime}');
            let end_dtime = datetime('{str_end_dtime}');
            let limit_item = {limit};

            WitsDtimes
            | where WellboreId == wellbore_id and LogName == log_name
            | where Dtime between (start_dtime .. end_dtime)
            | project Dtime, {",".join(projectCurveNames)}
            | distinct Dtime, {",".join(distinctCurveNames)}
            | order by Dtime asc  
            | take limit_item
            ;
            """

    def query_depths_logcurve_names(self, wellboreId: str, logName:str)  -> list[str]:
        """
        Get all avaliable log_curve names of a Log in the ADX
        """
        kql_query = f"""
            let wellbore_id = "{wellboreId}";
            let log_name = "{logName}";

            WitsDepths
            | where WellboreId == wellbore_id and LogName == log_name
            | order by Depth
            | take 1
            | project  Datas
            | evaluate bag_unpack(Datas)
            ;
        """
        df = self.execute_query(kql_query=kql_query)
        if df is None:
            return []
        return df.columns.to_list()

    def query_depths_range(self, wellboreId:str, logNames:Union[str | list[str]]) -> Optional[pd.DataFrame]:
        """
        Get Min and Max Depth of a Wellbore in the ADX
        """
        logs_names = []
        if isinstance(logNames,str):
            logs_names.append(logNames)
        elif isinstance(logNames,list):
            logs_names = logNames

        json_log_names = json.dumps(logs_names)

        kql_query = f"""
            let wellbore_id = '{wellboreId}';
            let log_names = dynamic({json_log_names});

            WitsDepths
            | where WellboreId == wellbore_id and LogName in (log_names)
            | project WellboreId, LogName, Depth
            | distinct  WellboreId, LogName, Depth
            | summarize MinDepth = min(Depth), MaxDepth = max(Depth), LogCount=count() by  WellboreId,  LogName
            ;
        """
        return self.execute_query(kql_query=kql_query)
        
    def query_depths_data(self, wellboreId:str, logName:str, curveNames:list[str], startDepth:Optional[float] = None, endDepth:Optional[float] = None, showUnits:bool=False, limit=50000) -> Optional[pd.DataFrame]:
        """
        Query Depth log data based on wellboreId, logName, curveNames, Optional[startDepth], Optional[endDepth]  from ADX
        """
        if wellboreId is None or logName is None or curveNames is None or len(curveNames) == 0:
            return None
        
        # get current start_depth, end_depth fromADX
        df_min_max_depth = self.query_depths_range(wellboreId=wellboreId, logNames=logName)
        if df_min_max_depth is None or len(df_min_max_depth) == 0:
            # there is no data in ADX
            return None
        start_depth = df_min_max_depth.at[0, 'MinDepth']
        end_depth = df_min_max_depth.at[0, 'MaxDepth']

        # compare start_depth and end_depth with startDepth and endDepth in the parameters
        if startDepth is not None and startDepth > start_depth:
            start_depth = startDepth

        if endDepth is not None and endDepth < end_depth:
            end_depth = endDepth

        # process query data
        df_result:Optional[pd.DataFrame] = None
        
        client = self.get_kusto_client()
        db_name = self.get_database_name()

        if limit < 1:
            limit = 50000
        
        is_process_next_query = True

        # build curve_name query
        project_curve_names, distinct_curve_names, curve_names_mapping = self._build_wits_curve_query(curveNames=curveNames, showUnits=showUnits)

        while is_process_next_query:
            #print(f"Process - start_depth: {start_depth} - end_depth: {end_depth} - limit: {limit}")
            kql_depth_query = self._build_depth_query(
                wellboreId=wellboreId, 
                logName=logName, 
                projectCurveNames=project_curve_names,
                distinctCurveNames=distinct_curve_names,
                startDepth=start_depth, 
                endDepth=end_depth, 
                limit=limit
            )

            response = client.execute(db_name, kql_depth_query)
            # we also support dataframes:
            df_query_result = dataframe_from_result_table(response.primary_results[0])
            total_query_item = len(df_query_result)
            # print(f"Process - total_query_item: {total_query_item}")

            if total_query_item > 0:
                if df_result is None:
                    df_result = df_query_result
                else:
                    if hasattr(df_result, 'concat'):
                        # process with Pandas v2.x
                        df_result = pd.concat([df_result, df_query_result])
                    elif hasattr(df_result, 'append'):
                        # process with Pandas v1.x
                        df_result = df_result.append(df_query_result)
                    else:
                        # process with Pandas v2.x
                        df_result = pd.concat([df_result, df_query_result])

            if total_query_item < limit:
                # quick - end of process
                is_process_next_query = False
                break
            else:
                # get Depth of the last record
                start_depth = df_query_result.at[df_query_result.index[-1],'Depth']
                is_process_next_query = True

        # logging.debug("df_result - curve_names_mapping: {curve_names_mapping}", curve_names_mapping)
        if curve_names_mapping is not None and len(curve_names_mapping) > 0:
            # reformat dataframe name
            try:
                df_result.rename(columns=curve_names_mapping,inplace=True)
            except Exception as ex:
                logging.warning("df_result - rename: {error}", ex)
        
        return df_result

    def _build_depth_query(self, wellboreId:str, logName:str, projectCurveNames:list[str], distinctCurveNames:list[str], startDepth:float, endDepth:float, limit=10000) -> str:
        """
        Build KQL query WITS Depth Data
        """

        # reset default limit item
        if limit < 1:
            limit = 10000
        
        start_depth = startDepth
        end_depth = endDepth

        return  f"""
            let wellbore_id = '{wellboreId}';
            let log_name = '{logName}';
            let start_depth = {start_depth};
            let end_depth = {end_depth};
            let limit_item = {limit};

            WitsDepths
            | where WellboreId == wellbore_id and LogName == log_name
            | where Depth between (start_depth .. end_depth)
            | project Depth, {",".join(projectCurveNames)}
            | distinct Depth, {",".join(distinctCurveNames)}
            | order by Depth asc  
            | take limit_item
            ;
            """

    def _build_wits_curve_query(self, curveNames:list[str], showUnits:bool=False) -> tuple[list[str], list[str], dict[str, str]]:
        """
        Build list of curve data and units query
        e.g:
            | project Dtime, d_az=todouble(Datas['az']), u_az=tostring(Units['az']), d_bdep=todouble(Datas["bdep"])
            | distinct Dtime, d_az, u_az, d_bdep
        Params:
            - curveNames: list of curve name of a Logs
            - showUnits: add units information to result
        Return
            Tuple with format:
                - {0} is list of project_curve_names, 
                - {1} is list of distinct_curve_names,
                - {2} is dict of curve_names mappings (formated_curve_name = curve_name)
        """

        project_curve_names:list[str] = []
        distinct_curve_names:list[str] = []

        # mapping d_[curve_name] = curve_name, u_[curve_name] = u_curve_name
        curve_names_mapping:dict[str,str] = {}

        for curve_name in curveNames:
            formated_curve_name = self._format_curve_name(curveName=curve_name)
            project_curve_names.append(f"d_{formated_curve_name}=todouble(Datas['{curve_name}'])")
            distinct_curve_names.append(f"d_{formated_curve_name}")
            # keep mapping formated_curve_name = curve_name
            curve_names_mapping.update({f"d_{formated_curve_name}" : curve_name})
            if showUnits:
                project_curve_names.append(f"u_{formated_curve_name}=tostring(Units['{curve_name}'])")
                distinct_curve_names.append(f"u_{formated_curve_name}")
                # keep mapping formated_curve_name = u_[curve_name]
                curve_names_mapping.update({f"u_{formated_curve_name}" : f"u_{curve_name}"})

        return (project_curve_names, distinct_curve_names, curve_names_mapping)

    def _format_curve_name(self, curveName:str) -> str:
        """
        Remove all special characters from curve_name
        e.g:  from ts1-4 to ts1_4
        """
        special_characters=['@','#','$','*','&', '-', '|']
        normal_curve_name = curveName
        for c in special_characters:
            normal_curve_name = normal_curve_name.replace(c, "_")
        return normal_curve_name