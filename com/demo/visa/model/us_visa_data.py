import sys

from pandas import DataFrame

from com.demo.visa.exception import VisaException
from com.demo.visa.logger import logging


class USVisaData:
    def __init__(self,
                 continent,
                 education_of_employee,
                 has_job_experience,
                 requires_job_training,
                 no_of_employees,
                 region_of_employment,
                 prevailing_wage,
                 unit_of_wage,
                 full_time_position,
                 company_age
                 ):
        """
        Usvisa Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.continent = continent
            self.education_of_employee = education_of_employee
            self.has_job_experience = has_job_experience
            self.requires_job_training = requires_job_training
            self.no_of_employees = no_of_employees
            self.region_of_employment = region_of_employment
            self.prevailing_wage = prevailing_wage
            self.unit_of_wage = unit_of_wage
            self.full_time_position = full_time_position
            self.company_age = company_age


        except Exception as e:
            raise VisaException(e, sys) from e

    def get_usvisa_input_data_frame(self) -> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:

            us_visa_input_dict = self.get_us_visa_data_as_dict()
            return DataFrame(us_visa_input_dict)

        except Exception as e:
            raise VisaException(e, sys) from e

    def get_usvisa_data_as_dict(self):
        """
        This function returns a dictionary from USvisaData class input
        """
        logging.info("Entered get_usvisa_data_as_dict method as USvisaData class")

        try:
            input_data = {
                "continent": [self.continent],
                "education_of_employee": [self.education_of_employee],
                "has_job_experience": [self.has_job_experience],
                "requires_job_training": [self.requires_job_training],
                "no_of_employees": [self.no_of_employees],
                "region_of_employment": [self.region_of_employment],
                "prevailing_wage": [self.prevailing_wage],
                "unit_of_wage": [self.unit_of_wage],
                "full_time_position": [self.full_time_position],
                "company_age": [self.company_age],
            }

            logging.info("Created usvisa data dict")

            logging.info("Exited get_usvisa_data_as_dict method as USvisaData class")

            return input_data

        except Exception as e:
            raise VisaException(e, sys) from e