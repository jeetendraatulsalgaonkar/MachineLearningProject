import unittest
import os.path

from com.demo.visa.components.data_ingestion import DataIngestion
from com.demo.visa.constants import FEATURE_STORE_EXPORT_FILE_NAME, DATA_INGESTION_FEATURE_STORE_DIRECTORY, \
    DATA_INGESTION_DIRECTORY_NAME, DATA_INGESTION_GENERATED_DIRECTORY, TRAINING_FILE_NAME, TESTING_FILE_NAME, \
    DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO, DATA_INGESTION_TABLE_NAME
from com.demo.visa.entity.configuration_entity import DataIngestionConfigurationEntity
from com.demo.visa.exception import VisaException


class MyTestCase(unittest.TestCase):

    @staticmethod
    def assert_is_file(path):
        if not os.path.isfile(path):
            raise AssertionError("File does not exist: %s" % str(path))

    def test_export_data_from_database_into_csv_successful_test(self):
        data_ingestion_configuration_entity = DataIngestionConfigurationEntity(
            data_ingestion_directory=os.path.join(DATA_INGESTION_DIRECTORY_NAME),
            data_ingestion_feature_store_directory=os.path.join(DATA_INGESTION_FEATURE_STORE_DIRECTORY),
            data_ingestion_training_file_location=os.path.join(DATA_INGESTION_GENERATED_DIRECTORY, TRAINING_FILE_NAME),
            data_ingestion_testing_file_location=os.path.join(DATA_INGESTION_GENERATED_DIRECTORY, TESTING_FILE_NAME),
            data_ingestion_train_test_split_ratio=DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )
        DataIngestion(data_ingestion_configuration_entity).export_data_from_database_into_csv()
        path = os.path.join(DATA_INGESTION_FEATURE_STORE_DIRECTORY, FEATURE_STORE_EXPORT_FILE_NAME)
        self.assert_is_file(path)

    # Show throw exception
    def test_export_data_from_database_into_csv_empty_feature_dir_param(self):
        data_ingestion_configuration_entity_empty_feature_dir = DataIngestionConfigurationEntity(
            data_ingestion_directory=os.path.join(DATA_INGESTION_DIRECTORY_NAME),
            data_ingestion_feature_store_directory=os.path.join(''),
            data_ingestion_training_file_location=os.path.join(DATA_INGESTION_GENERATED_DIRECTORY, TRAINING_FILE_NAME),
            data_ingestion_testing_file_location=os.path.join(DATA_INGESTION_GENERATED_DIRECTORY, TESTING_FILE_NAME),
            data_ingestion_train_test_split_ratio=DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )
        data_ingestion: DataIngestion = DataIngestion(data_ingestion_configuration_entity_empty_feature_dir)
        with self.assertRaises(VisaException) as context:
            data_ingestion.export_data_from_database_into_csv()
        self.assertTrue('No such file or directory' in context.exception.error_message)


if __name__ == '__main__':
    unittest.main()
