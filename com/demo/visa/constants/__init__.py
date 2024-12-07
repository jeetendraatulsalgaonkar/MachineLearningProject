MODEL_FILE_NAME = "model.pkl"
RAW_DATA_CSV_FILE_LOCATION = "notebook/Visadataset.csv"

PGHOST = "localhost"
PGDB = "us_visa"
PGUSER = "postgres"
PGPASSWORD = "postgres"
PGPORT = "54320"

# Database related constants
column_list = [
    'case_id',
    'continent',
    'education_of_employee',
    'has_job_experience',
    'requires_job_training',
    'no_of_employees',
    'yr_of_estab',
    'region_of_employment',
    'prevailing_wage',
    'unit_of_wage',
    'full_time_position',
    'case_status'
]

sql_select_all_query = '''
    SELECT case_id, continent, education_of_employee, has_job_experience, requires_job_training,
    no_of_employees, yr_of_estab, region_of_employment, prevailing_wage, unit_of_wage, full_time_position,
    case_status FROM us.visa
'''

## Data Ingestion
DATA_INGESTION_TABLE_NAME = "us.visa"
DATA_INGESTION_DIRECTORY_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIRECTORY: str = "feature_store"
DATA_INGESTION_GENERATED_DIRECTORY: str = "generated"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

FEATURE_STORE_EXPORT_FILE_NAME = "feature_store.csv"
TRAINING_FILE_NAME = "train.csv"
TESTING_FILE_NAME = "test.csv"
