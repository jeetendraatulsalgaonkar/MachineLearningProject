from sqlalchemy import Table, Metadata, Column, Integer, String, Numeric

from com.demo.visa.config.db_session_management import get_engine

metadata = Metadata()

visa_table = Table('us.visa', metadata,
                   Column('case_id', Integer, primary_key=True),
                   Column('continent', String(20)),
                   Column('education_of_employee', String(20)),
                   Column('has_job_experience', String(1)),
                   Column('requires_job_training', String(1)),
                   Column('no_of_employees', Integer),
                   Column('yr_of_estab', Integer),
                   Column('region_of_employment', String(20)),
                   Column('prevailing_wage', Integer),
                   Column('unit_of_wage', String(10)),
                   Column('full_time_position', String(1)),
                   Column('case_status', String(10)),)

metadata.create_all(get_engine())
