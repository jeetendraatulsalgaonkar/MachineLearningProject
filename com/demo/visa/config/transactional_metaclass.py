from typing import Dict, Any, Type


class TransactionalMetaclass(type):
    def __new__(cls, name: str, bases: tuple, attrs: Dict[str, Any]) -> Type:
        cls.apply_transactional_wrapper(attrs)
        new_class = super().__new__(cls, name, bases, attrs)
        cls.set_model_attribute(new_class, bases)
        return new_class

    @classmethod
    def apply_transactional_wrapper(cls, attrs: Dict[str, Any]) -> None:
        transactional_prefixes = (
            "find",
            "create",
            "delete",
        )

        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and any(
                attr_name.startswith(prefix) for prefix in transactional_prefixes
            ):
                attrs[attr_name] = cls.add_transactional(attr_value)