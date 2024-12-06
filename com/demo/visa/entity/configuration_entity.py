from os import path
from dataclasses import dataclass

from com.demo.visa.constants import RAW_DATA_CSV_FILE_LOCATION


@dataclass
class DataCollectionConfigurationEntity:
    data_collection_location: path.join(RAW_DATA_CSV_FILE_LOCATION)


@dataclass
class USVisaPredictorConfig:
    dum_dum: any
