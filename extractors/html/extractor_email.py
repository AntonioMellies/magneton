import re

from extractors.html.base.extractor_html_filter_base import ExtractorHtmlFilterBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType


class ExtractorHtmlEmail(ExtractorHtmlFilterBase):

    def __init__(self, filters) -> None:
        super().__init__(filters)

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        print("ExtractorHtmlEmail")
        request.emailPublic = AnalyticResultType.REPROVED
        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def get_magnet_liks(self):
        re_magnet = ('magnet{1}:\?xt=urn:btih:[a-zA-Z0-9&=%.-]*')
        for link in self.bsObj.findAll("a", href=re.compile(re_magnet)):
            link_magnet = link.attrs['href']
            if link_magnet not in self.magnet_liks:
                self.magnet_liks.add(link_magnet)
