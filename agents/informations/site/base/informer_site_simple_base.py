from __future__ import annotations

from abc import abstractmethod

from agents.informations.site.base.informer_site import InformerSite
from models.base.response import Response


class InformerSiteSimpleBase(InformerSite):

    @abstractmethod
    def handle(self, request: Response = Response()) -> Response:
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
