import logging

import requests

from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from agents.validators.site.base.validator_site_simple_base import ValidatorSiteSimpleBase


class ValidatorHttps(ValidatorSiteSimpleBase):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ValidatorHttps")
        request.https = AnalyticResultType.REPROVED

        if self.valid_https():
            request.https = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def valid_https(self):
        try:
            if not self.url:
                return False

            response = requests.get(self.url, verify=False)

            if not response.url.lower().startswith('https'):
                return False

        except Exception as e:
            logging.error(e)
            return False
        else:
            return True
