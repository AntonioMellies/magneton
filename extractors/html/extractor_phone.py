import re

from extractors.html.base.extractor_html_filter_base import ExtractorHtmlFilterBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType


class ExtractorHtmlPhone(ExtractorHtmlFilterBase):

    def __init__(self, filters) -> None:
        super().__init__(filters)

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        print("ExtractorHtmlPhone")
        request.phonePublic = AnalyticResultType.REPROVED
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
