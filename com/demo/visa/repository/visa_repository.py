from repository_sqlalchemy import BaseRepository
from repository_sqlalchemy.base_repository import ModelType

from com.demo.visa.entity.Visa_model import VisaModel


class VisaRepository(BaseRepository[VisaModel]):
    def find_by_id(self, id: int) -> VisaModel:
        return self.session.query(self.model).filter_by(id=id).first()