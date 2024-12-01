from typing import Generic, Dict, Any

from repository_sqlalchemy.base_repository import ModelType
from repository_sqlalchemy.transaction_metaclass import TransactionalMetaclass
from sqlalchemy.orm import Session

from com.demo.visa.config.session_management import session_context_var


class BaseRepository(Generic[ModelType], metaclass=TransactionalMetaclass):
    model = None

    @property
    def session(self) -> Session:
        return session_context_var.get()

    def create(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.flush()
        self.session.refresh(obj)
        return obj

    def update(self, obj: ModelType, data: Dict[str, Any]) -> ModelType:
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
            else:
                raise AttributeError(f"{type(obj).__name__} has no attribute '{key}'")
        self.session.flush()
        return obj

    def delete(self, obj: ModelType) -> ModelType:
        self.session.delete(obj)
        self.session.flush()