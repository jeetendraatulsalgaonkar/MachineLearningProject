from dataclasses import dataclass


@dataclass
class DataIngestionArtifactEntity:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifactEntity:
    validation_status: bool
    message: str
    drift_report_file_path: str

@dataclass
class DataValidationArtifactEntity:
    validation_status: bool
    message: str
    drift_report_file_path: str
