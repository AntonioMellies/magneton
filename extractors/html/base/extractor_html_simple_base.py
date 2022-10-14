from __future__ import annotations

from abc import abstractmethod

from extractors.html.base.extractor_html import ExtractorHtml
from models.base.response import Response


class ExtractorHtmlSimpleBase(ExtractorHtml):

    @abstractmethod
    def handle(self, request: Response = Response()) -> Response:
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
