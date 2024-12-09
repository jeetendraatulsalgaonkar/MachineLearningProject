from os import path
from dataclasses import dataclass

from com.demo.visa.constants import (RAW_DATA_CSV_FILE_LOCATION,
                                     DATA_INGESTION_DIRECTORY_NAME,
                                     DATA_INGESTION_FEATURE_STORE_DIRECTORY,
                                     DATA_INGESTION_GENERATED_DIRECTORY,
                                     DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO,
                                     TRAINING_FILE_NAME,
                                     TESTING_FILE_NAME,
                                     DATA_INGESTION_TABLE_NAME, PIPELINE_NAME, ARTIFACT_DIR, TIMESTAMP,
                                     DATA_VALIDATION_DIR_NAME, DATA_VALIDATION_DRIFT_REPORT_DIR,
                                     DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataCollectionConfigurationEntity:
    data_collection_location: path.join(RAW_DATA_CSV_FILE_LOCATION)


@dataclass
class DataIngestionConfigurationEntity:
    data_ingestion_directory: path.join(DATA_INGESTION_DIRECTORY_NAME)
    data_ingestion_feature_store_directory: path.join(DATA_INGESTION_FEATURE_STORE_DIRECTORY)
    data_ingestion_training_file_location: path.join(DATA_INGESTION_GENERATED_DIRECTORY, TRAINING_FILE_NAME)
    data_ingestion_testing_file_location: path.join(DATA_INGESTION_GENERATED_DIRECTORY, TESTING_FILE_NAME)
    data_ingestion_train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    data_ingestion_table_name = DATA_INGESTION_TABLE_NAME


@dataclass
class DataValidationConfigurationEntity:
    data_validation_directory: path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    drift_report_file_path: str = path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME,
                                            DATA_VALIDATION_DRIFT_REPORT_DIR, DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)


@dataclass
class USVisaPredictorConfig:
    dum_dum: any
