from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any

from models.base.response import Response


class Extractor(ABC):
    _next_handler: Extractor = None

    def set_next(self, extractor: Extractor) -> Extractor:
        self._next_handler = extractor
        return extractor

    @abstractmethod
    def handle(self, request: Response = Response()) -> Optional[Any]:
        pass
