from __future__ import annotations

from abc import abstractmethod

from models.base.response import Response
from agents.validators.site.base.validator_site import ValidatorSite


class ValidatorSiteSimpleBase(ValidatorSite):

    @abstractmethod
    def handle(self, request: Response = Response()) -> Response:
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
