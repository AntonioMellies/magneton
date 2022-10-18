from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any

from models.base.response import Response


class Validator(ABC):
    _next_handler: Validator = None

    def set_next(self, validator: Validator) -> Validator:
        self._next_handler = validator
        return validator

    @abstractmethod
    def handle(self, request: Response = Response()) -> Optional[Any]:
        pass
