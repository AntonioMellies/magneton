from abc import abstractmethod

from models.base.response import Response


class ExtractService:

    @abstractmethod
    def extract(self, response: Response) -> Response:
        pass
