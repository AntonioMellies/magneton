import logging
import re

from extractors.html.base.extractor_html_filter_base import ExtractorHtmlFilterBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from utils.extractor_utils import sanitize_phone, concat_tuples


class ExtractorHtmlPhone(ExtractorHtmlFilterBase):

    def __init__(self, filters) -> None:
        super().__init__(filters)

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ExtractorHtmlPhone")
        request.phonePublic = AnalyticResultType.REPROVED

        if self.phone_exists():
            request.phonePublic = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def phone_exists(self) -> bool:
        pattern = r"(\+\d{2})?(\(?\d{2,3}\)?\s*)?(\d*(\-|\s|\.)?\d+){1,15}"

        if not self.html:
            return False

        phone_filter = self.filters.phone
        if not (phone_filter and phone_filter.strip()):
            return False

        strings_phones = self.html.findAll(string=re.compile(pattern))
        for x in strings_phones:
            found_phones_list = re.findall(pattern, str(x))
            group_concatenated_list = list(map(concat_tuples, found_phones_list))
            if group_concatenated_list:
                phones_sanitized_list = list(map(sanitize_phone, group_concatenated_list))
                filter_sanitized = sanitize_phone(phone_filter)

                if phones_sanitized_list.__contains__(filter_sanitized):
                    return True

        return False
