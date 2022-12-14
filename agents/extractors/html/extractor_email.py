import logging
import re

from agents.extractors.html.base.extractor_html_filter_base import ExtractorHtmlFilterBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType


class ExtractorHtmlEmail(ExtractorHtmlFilterBase):

    def __init__(self, filters) -> None:
        super().__init__(filters)

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ExtractorHtmlEmail")
        request.emailPublic = AnalyticResultType.REPROVED

        if self.email_exists():
            request.emailPublic = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def email_exists(self) -> bool:
        try:
            if not self.html:
                return False

            email_filter = self.filters.email
            if not (email_filter and email_filter.strip()):
                return False

            strings_emails = self.html.findAll(string=email_filter)
            for x in strings_emails:
                list_emails = re.findall(email_filter, str(x))
                if list_emails:
                    if list_emails.__contains__(email_filter):
                        return True

        except Exception as e:
            logging.error(e)
            return False
        else:
            return False
