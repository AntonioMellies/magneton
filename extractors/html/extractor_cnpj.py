import logging
import re

from extractors.html.base.extractor_html_filter_base import ExtractorHtmlFilterBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from utils.extractor_utils import sanitize_cnpj


class ExtractorHtmlCNPJ(ExtractorHtmlFilterBase):

    def __init__(self, filters) -> None:
        super().__init__(filters)

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ExtractorHtmlCNPJ")
        request.cnpjPublic = AnalyticResultType.REPROVED

        if self.cnpj_exists():
            request.cnpjPublic = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def cnpj_exists(self) -> bool:
        pattern = r"(\d{2}\.?\d{3}\.\d{3}/?\d{4}-?\d{2})"

        if not self.html:
            return False

        cnpj_filter = self.filters.cnpj
        if not (cnpj_filter and cnpj_filter.strip()):
            return False

        strings_cnpj = self.html.findAll(string=re.compile(pattern))
        for x in strings_cnpj:
            list_cnpj = re.findall(pattern, str(x))
            if list_cnpj:
                list_cnpj_sanitized = list(map(sanitize_cnpj, list_cnpj))
                cnpj_filter_sanitized = sanitize_cnpj(cnpj_filter)

                if list_cnpj_sanitized.__contains__(cnpj_filter_sanitized):
                    return True

        return False
