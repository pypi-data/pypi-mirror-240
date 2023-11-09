import logging

import pandas as pd

import snowflake.snowpark as snowpark
import snowflake.snowpark.functions as snowfunc

from wellsrt_data_client.commons import EnvVariables

from wellsrt_data_client.services.snow import SnowDataService

from enum import auto, IntEnum
from strenum import UppercaseStrEnum

class WellsRtMetadataTableEnum(UppercaseStrEnum):
    WRT_MASTER_DATA = auto()
    WRT_WELLS = auto()
    WRT_WELLBORE = auto()
    WRT_LOGS = auto()
    WRT_LOGCURVE = auto()

class WellsRtMasterDataName(UppercaseStrEnum):
    ID  = auto()
    DATA_TYPE = auto()
    DATASET = auto()
    ASSET = auto()
    UID = auto()
    NAME = auto()
    STATUS = auto()
    TIMEZONE = auto()

class WellsRtMetaName(UppercaseStrEnum):
    ID  = auto()
    MASTER_DATA_ID  = auto()
    DATA_TYPE = auto()

    WELL_ID = auto()
    WELL_NAME = auto()
    STATUS = auto()

    WELLBORE_ID = auto()
    WELLBORE_NAME = auto()
    API_NUMBER = auto()
    
    LOG_ID = auto()
    LOG_NAME = auto()
    LOG_TYPE = auto()
    INDEX_UNIT = auto()

    CURVE_ID = auto()
    CURVE_NAME = auto()
    UNITS = auto()
    DESCRIPTION = auto()

class WellsRtMetadataService(SnowDataService):
    """
     WellsRtMetadataService provides a common/utility methods to access to WellsRT Metadata tables
     e.g. WRT_MASTER_DATA, WRT_WELLS, WRT_WELLBORE, WRT_LOGS, WRT_LOGCURVE
    """
    def __init__(self, env_vars:EnvVariables):
        SnowDataService.__init__(self, env_vars=env_vars)
        
    def metadata(self, table: WellsRtMetadataTableEnum, col_filters: list[tuple[str, str]]) -> snowpark.DataFrame:
        """
        Get  Well Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """       
        tbl = self.session.table(name=table.name)
        # filter data
        having_filter = False

        where_filter = None
        for col_filter in col_filters:
            # col_name = col_filter[0]
            # col_value = col_filter[1]
            col_name, col_value = col_filter
            if col_name is not None and col_value is not None:
                if where_filter is None:
                    where_filter = (snowfunc.col(col_name) == col_value)
                else:
                    where_filter = where_filter & (snowfunc.col(col_name) == col_value)

        if where_filter is not None:
            return tbl.filter(where_filter)
        else:
            return tbl

    def master_data(self, data_type:str = None, dataset:str = None, asset:str = None, uid:str = None, name:str = None, status:str = None, is_show_full=False) -> snowpark.DataFrame:
        """
        Get WITSML Well Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """
        df = self.metadata(
            table=WellsRtMetadataTableEnum.WRT_MASTER_DATA,
            col_filters=[
                (WellsRtMasterDataName.DATA_TYPE, data_type),
                (WellsRtMasterDataName.DATASET, dataset),
                (WellsRtMasterDataName.ASSET, asset),
                (WellsRtMasterDataName.UID, uid),
                (WellsRtMasterDataName.NAME, name),
                (WellsRtMasterDataName.STATUS, status),
            ]
        )
        if is_show_full:
            return df
        else:
            return df.select(
                WellsRtMasterDataName.ID, 
                WellsRtMasterDataName.DATA_TYPE, 
                WellsRtMasterDataName.DATASET,  
                WellsRtMasterDataName.ASSET, 
                WellsRtMasterDataName.UID,
                WellsRtMasterDataName.NAME,
                WellsRtMasterDataName.STATUS
            )

    def wells(self, data_type:str = None, well_id:str = None, is_show_full=False) -> snowpark.DataFrame:
        """
        Get WITSML Well Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """
        df = self.metadata(
            table=WellsRtMetadataTableEnum.WRT_WELLS,
            col_filters=[
                (WellsRtMetaName.DATA_TYPE, data_type),
                (WellsRtMetaName.WELL_ID, well_id),
            ]
        )
        if is_show_full:
            return df
        else:
            return df.select(
                 WellsRtMetaName.DATA_TYPE, WellsRtMetaName.WELL_ID,  WellsRtMetaName.WELL_NAME, WellsRtMetaName.STATUS
            )

    def wellbores(self, data_type:str = None, well_id:str = None, wellbore_id:str = None, wellbore_name:str = None, api_number:str = None, is_show_full=False) -> snowpark.DataFrame:
        """
        Get WITSML Wellbore Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """
        df = self.metadata(
            table=WellsRtMetadataTableEnum.WRT_WELLBORE,
            col_filters=[
                (WellsRtMetaName.DATA_TYPE, data_type), 
                (WellsRtMetaName.WELL_ID, well_id), 
                (WellsRtMetaName.WELLBORE_ID, wellbore_id),
                (WellsRtMetaName.WELLBORE_NAME, wellbore_name),
                (WellsRtMetaName.API_NUMBER, api_number),
            ]
        )

        if is_show_full:
            return df
        else:
            return df.select(
                WellsRtMetaName.DATA_TYPE,
                WellsRtMetaName.WELL_ID,  WellsRtMetaName.WELL_NAME,
                WellsRtMetaName.WELLBORE_ID, WellsRtMetaName.WELLBORE_NAME,
                WellsRtMetaName.API_NUMBER
            )

    def logs(self, data_type:str = None, well_id:str = None, wellbore_id:str = None, wellbore_name:str = None, log_id:str = None, log_name:str = None, is_show_full=False) -> snowpark.DataFrame:
        """
        Get WITSML Logs Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """
        df = self.metadata(
            table=WellsRtMetadataTableEnum.WRT_LOGS,
            col_filters=[
                (WellsRtMetaName.DATA_TYPE, data_type), 
                (WellsRtMetaName.WELL_ID, well_id), 
                (WellsRtMetaName.WELLBORE_ID, wellbore_id),
                (WellsRtMetaName.WELLBORE_NAME, wellbore_name),
                (WellsRtMetaName.LOG_ID, log_id),
                (WellsRtMetaName.LOG_NAME, log_name),
            ]
        )

        if is_show_full:
            return df
        else:
            return df.select(
                WellsRtMetaName.DATA_TYPE,
                WellsRtMetaName.WELL_ID, WellsRtMetaName.WELL_NAME,
                WellsRtMetaName.WELLBORE_ID, WellsRtMetaName.WELLBORE_NAME,
                WellsRtMetaName.LOG_ID, WellsRtMetaName.LOG_NAME,
                WellsRtMetaName.INDEX_UNIT
            )

    def logcurves(self, log_id:str, data_type:str = None, well_id:str = None, wellbore_id:str = None, wellbore_name:str = None,  log_name:str=None, curve_id:str = None, curve_name:str = None, is_show_full=False) -> snowpark.DataFrame:
        """
        Get WITSML LogCurve Metadata in the snowflake.snowpark.DataFrame format.
        Ref: https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/dataframe
        """
        df = self.metadata(
            table=WellsRtMetadataTableEnum.WRT_LOGCURVE,
            col_filters=[
                (WellsRtMetaName.LOG_ID, log_id),
                (WellsRtMetaName.DATA_TYPE, data_type), 
                (WellsRtMetaName.WELL_ID, well_id),
                (WellsRtMetaName.WELLBORE_ID, wellbore_id),
                (WellsRtMetaName.WELLBORE_NAME, wellbore_name),
                (WellsRtMetaName.LOG_NAME, log_name),
                (WellsRtMetaName.CURVE_ID, curve_id),
                (WellsRtMetaName.CURVE_NAME, curve_name),
            ]
        )

        if is_show_full:
            return df
        else:
            return df.select(
                WellsRtMetaName.DATA_TYPE,
                WellsRtMetaName.WELL_ID, WellsRtMetaName.WELL_NAME,
                WellsRtMetaName.WELLBORE_ID, WellsRtMetaName.WELLBORE_NAME,
                WellsRtMetaName.LOG_ID, WellsRtMetaName.LOG_NAME,
                WellsRtMetaName.CURVE_ID, WellsRtMetaName.CURVE_NAME, WellsRtMetaName.UNITS
            )