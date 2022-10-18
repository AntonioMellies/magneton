from abc import abstractmethod

from models.base.response import Response


class InformService:

    @abstractmethod
    def inform(self) -> Response:
        pass
