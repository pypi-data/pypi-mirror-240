from typing import Any

from django.db import models
from django.db.utils import DEFAULT_DB_ALIAS


class RowLevelSecurityConstraint(models.BaseConstraint):
    def __init__(self, field: str, name: str):
        super().__init__(name=name)
        self.target_field: str = field

    def constraint_sql(self, model: Any, schema_editor: Any) -> str:
        return ""

    def create_sql(self, model: Any, schema_editor: Any) -> Any:
        return schema_editor._activate_rls(model, self.target_field, self.name)

    def remove_sql(self, model: Any, schema_editor: Any) -> Any:
        return schema_editor._deactivate_rls(model, self.target_field, self.name)

    def validate(
        self,
        model: Any,
        instance: Any,
        exclude: Any = None,
        using: Any = DEFAULT_DB_ALIAS,
    ) -> None:
        pass

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, RowLevelSecurityConstraint):
            return self.name == other.name and self.target_field == other.target_field
        return super().__eq__(other)

    def deconstruct(self) -> tuple[str, tuple, dict]:
        path, _, kwargs = super().deconstruct()
        return (path, (self.target_field,), kwargs)
