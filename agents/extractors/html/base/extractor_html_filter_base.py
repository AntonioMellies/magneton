from __future__ import annotations

from abc import abstractmethod

from agents.extractors.html.base.extractor_html import ExtractorHtml
from models.base.response import Response
from models.filters import Filters


class ExtractorHtmlFilterBase(ExtractorHtml):

    def __init__(self, filters: Filters) -> None:
        super().__init__()
        self.filters = filters

    @abstractmethod
    def handle(self, request: Response = Response()) -> Response:
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
