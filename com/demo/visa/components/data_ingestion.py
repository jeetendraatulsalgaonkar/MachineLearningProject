import os
import sys

import pandas as pd
from pandas import DataFrame

from sklearn.model_selection import train_test_split

from com.demo.visa.config.db_session_management import get_engine_from_settings
from com.demo.visa.constants import column_list, sql_select_all_query, FEATURE_STORE_EXPORT_FILE_NAME
from com.demo.visa.entity.artifact_entity import DataIngestionArtifactEntity
from com.demo.visa.entity.configuration_entity import DataIngestionConfigurationEntity
from com.demo.visa.exception import VisaException
from com.demo.visa.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_configuration_entity: DataIngestionConfigurationEntity):
        try:
            self.data_ingestion_configuration_entity = data_ingestion_configuration_entity
        except Exception as e:
            raise VisaException(e, sys)

    def export_data_from_database_into_csv(self) -> DataFrame:
        """
        Function name: export_data_from_database_into_feature_directory
        Description: Function to export data from database into a csv file.
        :return: DataFrame object, which is the export from the database
        On exception: Log the exception
        """
        try:
            logging.info("Initiating export of data from database into feature directory")
            with get_engine_from_settings().connect() as connection:
                data_frame = pd.DataFrame(
                    pd.read_sql_query(sql_select_all_query, connection),
                    columns=column_list
                )

            data_ingestion_feature_store_directory = (
                self.data_ingestion_configuration_entity.data_ingestion_feature_store_directory)
            os.makedirs(data_ingestion_feature_store_directory, exist_ok=True)

            logging.info("Exported data from database into feature directory: {data_ingestion_feature_store_directory}")
            data_frame.to_csv(os.path.join(data_ingestion_feature_store_directory, FEATURE_STORE_EXPORT_FILE_NAME), index=False, header=True)
            return data_frame
        except FileNotFoundError as e:
            raise VisaException(e, sys) from e
        except Exception as e:
            raise VisaException(e, sys)

    def perform_test_train_split_on_data(self, data_frame: DataFrame) -> None:
        try:
            logging.info("Initiating train split on data")
            train_set, test_set = train_test_split(
                data_frame,
                test_size=self.data_ingestion_configuration_entity.data_ingestion_train_test_split_ratio
            )

            logging.info("Saving test and train sets to csv files in the appropriate location")
            os.makedirs(self.data_ingestion_configuration_entity.data_ingestion_training_file_location, exist_ok=True)
            os.makedirs(self.data_ingestion_configuration_entity.data_ingestion_testing_file_location, exist_ok=True)
            train_set.to_csv(
                self.data_ingestion_configuration_entity.data_ingestion_training_file_location,
                index=False,
                header=True
            )
            test_set.to_csv(
                self.data_ingestion_configuration_entity.data_ingestion_testing_file_location,
                index=False,
                header=True
            )
            logging.info(f"Test-Train data split complete and required csvs generated.")
        except Exception as e:
            raise VisaException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifactEntity:
        """
        Method name: initiate_data_ingestion
        Description: This method initiates the data ingestion process of the pipeline
            Here, we fetch data from the database and convert it into data Frames Object
            Then we split the data into train and test sets
        :return: Data Ingestion Artifact in the form of train and test sets
        """
        logging.info("Initiating the data ingestion")

        try:
            logging.info("Exporting data from the database")
            data_frame = self.export_data_from_database_into_csv()

            logging.info("Performing train-test split on the exported data")
            self.perform_test_train_split_on_data(data_frame)

            logging.info("Data Ingestion performed. Returning the artifact.")
            return DataIngestionArtifactEntity(
                trained_file_path=self.data_ingestion_configuration_entity.data_ingestion_training_file_location,
                test_file_path=self.data_ingestion_configuration_entity.data_ingestion_testing_file_location
            )
        except Exception as e:
            raise VisaException(e, sys)
