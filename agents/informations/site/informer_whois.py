import logging

import whois

from agents.informations.site.base.informer_site_simple_base import InformerSiteSimpleBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType


class InformerWhoIs(InformerSiteSimpleBase):

    def __init__(self) -> None:
        super().__init__()
        self.whois_info = None

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("InformerWhoIs")
        request.whois = AnalyticResultType.REPROVED

        if self.valid_whois():
            request.whois = AnalyticResultType.APPROVED
            request.whois_info = self.whois_info

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def valid_whois(self):
        try:
            if not self.url:
                return False

            response = whois.whois(self.url)

        except Exception as e:
            logging.error(e)
            return False
        else:
            self.whois_info = response
            return bool(response.domain_name)
