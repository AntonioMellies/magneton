import logging
import whois

from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from validators.site.base.validator_site_simple_base import ValidatorSiteSimpleBase


class ValidatorWhoIs(ValidatorSiteSimpleBase):

    def __init__(self) -> None:
        super().__init__()
        self.whois_info = None

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ValidatorWhoIs")
        request.whois = AnalyticResultType.REPROVED

        if self.valid_whois():
            request.whois = AnalyticResultType.APPROVED
            request.whois_info = self.whois_info

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def valid_whois(self):

        if not self.url:
            return False

        try:
            response = whois.whois(self.url)
        except Exception:
            return False
        else:
            self.whois_info = response
            return bool(response.domain_name)
