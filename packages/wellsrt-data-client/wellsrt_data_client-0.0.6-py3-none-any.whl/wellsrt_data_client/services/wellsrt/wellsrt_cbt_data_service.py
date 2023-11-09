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

class WellsRtCbtDataService(AzAdxDataService):

    def __init__(self, env_vars:EnvVariables):
        AzAdxDataService.__init__(self, env_vars=env_vars, conf_name="cbtdata")

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

    def query_logs_names(self, well:str=None,  wellbore:str = None)  -> Optional[pd.DataFrame]:
        """
        Get all avaliable logs names of a Wellbore in the WellsRT Data (ADX Database)
        """
        let_query:list[str] = []
        where_query:list[str] = []

        if well is not None and len(well) > 0:
            let_query.append(f" let _well = '{well}'; ")
            where_query.append(f"| where WellId == _well or WellName == _well")

        if wellbore is not None and len(wellbore) > 0:
            let_query.append(f" let _wellbore = '{wellbore}'; ")
            where_query.append(f"| where WellboreId == _wellbore ")

        kql_query = f"""
            {" ".join(let_query)}

            FracData
            {" ".join(where_query)}
            | project WellId, WellName, WellboreId, WellboreName, LogId, LogName, DataType
            | distinct WellId, WellName, WellboreId, WellboreName, LogId, LogName, DataType
        """
        return self.execute_query(kql_query=kql_query)
        
        
    def query_data_gap(self, well: str, wellbore:str=None, log:str=None, threshold_diff_in_sec=60)  -> Optional[pd.DataFrame]:
        """
        Get all avaliable logs names of a Wellbore in the WellsRT Data (ADX Database)
        """
        let_query:list[str] = []
        where_query:list[str] = []

        if wellbore is not None and len(wellbore) > 0:
            let_query.append(f'let _wellbore = "{wellbore}";')
            where_query.append(f'| where WellboreId == _wellbore or WellboreName == _wellbore')

        if log is not None and len(log) > 0:
            let_query.append(f'let _log = "{log}";')
            where_query.append(f'| where LogId == _log or LogName == _log')

        kql_query = f"""
            let _well = "{well}";
            {" ".join(let_query)}

            FracData
            | where WellName == _well or WellId == _well
            {" ".join(where_query)}
            | project WellId, WellboreId, WellboreName, DTimeIndex=todatetime(DTimeIndex), LogId, LogName
            | distinct WellId, WellboreId, WellboreName, DTimeIndex, LogId,LogName
            | order by WellId, WellboreId, LogId, DTimeIndex asc
            | extend  Prev_WellboreId = prev(WellboreId), Prev_LogName = prev(LogName), Prev_DTimeIndex = prev(DTimeIndex)
            | project WellId, WellboreId, WellboreName, LogId, LogName, 
                    DTimeIndex, Prev_DTimeIndex, 
                    Diff = case(Prev_WellboreId == WellboreId and Prev_LogName == LogName, (DTimeIndex - Prev_DTimeIndex)/1s, double(null))
            | where isnotnull(Diff) and Diff > {threshold_diff_in_sec}
            ;
        """
        return self.execute_query(kql_query=kql_query)


    def query_dtime_logcurve_names(self, log:str)  -> list[str]:
        """
        Get all avaliable log_curve names of a Log in the ADX
        """

        kql_query = f"""
            let _log = "{log}";

            FracData
            | where LogId == _log or LogName == _log
            | order by DTimeIndex
            | take 1
            | project  Dataset
            | evaluate bag_unpack(Dataset)
            ;
        """
        df = self.execute_query(kql_query=kql_query)
        if df is None:
            return []
        return df.columns.to_list()

    def query_dtimes_range(self, well:str, logs:Union[str | list[str]],  wellbore:str = None) -> Optional[pd.DataFrame]:
        """
        Get Min and Max DTime of a Wellbore in the ADX
        """
        _logs = []
        if isinstance(logs,str):
            _logs.append(logs)
        elif isinstance(logs,list):
            _logs = logs

        let_query:list[str] = []
        where_query:list[str] = []

        if well is not None and len(well) > 0:
            let_query.append(f" let _well = '{well}'; ")
            where_query.append(f"| where WellId == _well or WellName == _well ")
        
        if wellbore is not None and len(wellbore) > 0:
            let_query.append(f" let _wellbore = '{wellbore}'; ")
            where_query.append(f"| where WellboreId == _wellbore or WellboreName == _wellbore ")
        
        if len(_logs) > 0:
            let_query.append(f" let _logs = dynamic({json.dumps(_logs)}); ")
            where_query.append(f"| where LogId in (_logs) or LogName in (_logs) ")

        kql_query = f"""
            {" ".join(let_query)}

            FracData
            {" ".join(where_query)}
            | project WellId, WellboreId, LogId, LogName, DTimeIndex=todatetime(DTimeIndex)
            | distinct  WellId, WellboreId, LogId, LogName, DTimeIndex
            | summarize MinDtime = min(DTimeIndex), MaxDtime = max(DTimeIndex), LogCount=count() by  WellId, WellboreId,  LogId, LogName
            ;
        """
        return self.execute_query(kql_query=kql_query)
        
    def query_dtimes_data(self, well:str, log_id:str, curve_names:list[str], start_time:Optional[datetime] = None, end_time:Optional[datetime] = None, limit=50000) -> Optional[pd.DataFrame]:
        """
        Query DTime log data based on wellbore_id, logName, curveNames, Optional[startTime], Optional[endTime]  from ADX
        """

        if well is None or len(well) == 0 or log_id is None or len(log_id) == 0 or curve_names is None or len(curve_names) == 0:
            return None
        
        # get current start_dtime, end_dtime fromADX
        df_min_max_dtime = self.query_dtimes_range(well=well, logs=log_id)
        if df_min_max_dtime is None or len(df_min_max_dtime) == 0:
            # there is no data in ADX
            return None
        start_dtime = df_min_max_dtime.at[0, 'MinDtime']
        end_dtime = df_min_max_dtime.at[0, 'MaxDtime']

        # compare start_dtime and end_dtime with startTime and endTime in the parameters
        if start_time is not None and start_time > start_dtime:
            start_dtime = start_time

        if end_time is not None and end_time < end_dtime:
            end_dtime = end_time

        # process query data
        df_result:Optional[pd.DataFrame] = None
        
        client = self.get_kusto_client()
        db_name = self.get_database_name()

        if limit < 1:
            limit = 50000
        
        is_process_next_query = True

        # build curve_name query
        project_curve_names, distinct_curve_names, curve_names_mapping = self._build_wits_curve_query(curve_names=curve_names)

        while is_process_next_query:
            #print(f"Process - start_dtime: {start_dtime} - end_dtime: {end_dtime} - limit: {limit}")
            kql_dtime_query = self._build_dtimes_query(
                log_id=log_id, 
                project_curve_names=project_curve_names,
                distinct_curve_names=distinct_curve_names,
                start_dtime=start_dtime, 
                end_dtime=end_dtime, 
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
                start_dtime = df_query_result.at[df_query_result.index[-1],'DTimeIndex']
                is_process_next_query = True

        # logging.debug("df_result - curve_names_mapping: {curve_names_mapping}", curve_names_mapping)
        if df_result is not None and curve_names_mapping is not None and len(curve_names_mapping) > 0:
            # reformat dataframe name
            try:
                df_result.rename(columns=curve_names_mapping,inplace=True)
            except Exception as ex:
                logging.warning("df_result - rename: {error}", ex)
        
        return df_result

    def _build_dtimes_query(self, log_id:str, project_curve_names:list[str], distinct_curve_names:list[str], start_dtime:datetime, end_dtime:datetime, limit=10000) -> str:
        """
        Build KQL query Frac DTime Data
        """

        # reset default limit item
        if limit < 1:
            limit = 10000

        utc_format = '%Y-%m-%dT%H:%M:%S%z'
        str_start_dtime = start_dtime.strftime(utc_format)
        str_end_dtime = end_dtime.strftime(utc_format)
        
        return  f"""
            let log_id = '{log_id}';
            let start_dtime = datetime('{str_start_dtime}');
            let end_dtime = datetime('{str_end_dtime}');
            let limit_item = {limit};

            FracData
            | where LogId == log_id
            | where DTimeIndex between (start_dtime .. end_dtime)
            | project DTimeIndex, {",".join(project_curve_names)}
            | distinct DTimeIndex, {",".join(distinct_curve_names)}
            | order by DTimeIndex asc  
            | take limit_item
            ;
            """

    def _build_wits_curve_query(self, curve_names:list[str]) -> tuple[list[str], list[str], dict[str, str]]:
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

        for curve_name in curve_names:
            formated_curve_name = self._format_curve_name(curve_name=curve_name)
            project_curve_names.append(f"d_{formated_curve_name}=todouble(Dataset['{curve_name}'])")
            distinct_curve_names.append(f"d_{formated_curve_name}")
            # keep mapping formated_curve_name = curve_name
            curve_names_mapping.update({f"d_{formated_curve_name}" : curve_name})

        return (project_curve_names, distinct_curve_names, curve_names_mapping)

    def _format_curve_name(self, curve_name:str) -> str:
        """
        Remove all special characters from curve_name
        e.g:  from ts1-4 to ts1_4
        """
        special_characters=['@','#','$','*','&', '-', '|']
        normal_curve_name = curve_name
        for c in special_characters:
            normal_curve_name = normal_curve_name.replace(c, "_")
        return normal_curve_name