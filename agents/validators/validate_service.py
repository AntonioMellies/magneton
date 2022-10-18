from abc import abstractmethod

from models.base.response import Response


class ValidateService:

    @abstractmethod
    def validate(self) -> Response:
        pass
