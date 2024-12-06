import sys
import os.path as path

import pandas as pd

from com.demo.visa.config.db_session_management import get_engine_from_settings
from com.demo.visa.constants import RAW_DATA_CSV_FILE_LOCATION
from com.demo.visa.entity.configuration_entity import DataCollectionConfigurationEntity
from com.demo.visa.exception import VisaException


class DataCollection:
    def __init__(self,
                 data_collection_entity: DataCollectionConfigurationEntity
                 = DataCollectionConfigurationEntity(data_collection_location=RAW_DATA_CSV_FILE_LOCATION)
                 ):
        try:
            self.data_collection_entity = data_collection_entity
        except Exception as e:
            raise VisaException(e, sys)

    def import_data_into_database(self):
        try:
            with open(path.abspath(self.data_collection_entity.data_collection_location), 'r') as file:
                data_df = pd.read_csv(file)
            with get_engine_from_settings().connect() as connection:
                data_df.to_sql('visa', connection, schema='us', index=True, if_exists='replace')
        except Exception as e:
            raise VisaException(e, sys)
