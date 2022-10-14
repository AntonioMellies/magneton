from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType
from validators.site.base.validator_site_simple_base import ValidatorSiteSimpleBase


class ValidatorSSL(ValidatorSiteSimpleBase):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        print("ExtractorHtmlSSL")
        request.ssl = AnalyticResultType.REPROVED
        if self._next_handler:
            return self._next_handler.handle(request)

        return request
