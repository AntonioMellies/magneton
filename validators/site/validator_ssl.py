import logging
from ssl import SSLError

import requests

from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from validators.site.base.validator_site_simple_base import ValidatorSiteSimpleBase


class ValidatorSSL(ValidatorSiteSimpleBase):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ValidatorSSL")
        request.ssl = AnalyticResultType.REPROVED

        if self.valid_ssl():
            request.ssl = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def valid_ssl(self):
        try:
            try:
                if not self.url:
                    return False

                response = requests.get(self.url)

                if not response.url.lower().startswith('https'):
                    raise SSLError()

            except SSLError as e:
                logging.error(e)
                return False
            else:
                return True

        except Exception as e:
            logging.error(e)
            return False
