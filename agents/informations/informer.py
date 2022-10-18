from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any

from models.base.response import Response


class Informer(ABC):
    _next_handler: Informer = None

    def set_next(self, informer: Informer) -> Informer:
        self._next_handler = informer
        return informer

    @abstractmethod
    def handle(self, request: Response = Response()) -> Optional[Any]:
        pass
