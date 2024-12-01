from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from repository_sqlalchemy import BaseRepository, Base, transaction
from typing import List, Dict, Any


class VisaModel(Base):
    __tablename__ = 'us.visa'
    case_id = Column(Integer, primary_key=True, autoincrement=True)
    continent = Column(String(20))
    education_of_employee = Column(String(20))
    has_job_experience = Column(String(1))
    requires_job_training = Column(String(1))
    no_of_employees = Column(Integer)
    yr_of_estab = Column(Integer)
    region_of_employment = Column(String(20))
    prevailing_wage = Column(Numeric)
    unit_of_wage = Column(String(10))
    full_time_position = Column(String(1))
    case_status = Column(String(10))