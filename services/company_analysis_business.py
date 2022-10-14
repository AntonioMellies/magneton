from analysis.analysis_factory import AnalysisFactory
from extractors.html.extract_service_html import ExtractServiceHtml
from models.company_analytic_request import CompanyAnalyticRequest
from models.company_analytic_response import CompanyAnalyticResponse
from validators.site.validate_service_site import ValidateServiceSite


class CompanyAnalysisBusiness:

    def analyze(self, request: CompanyAnalyticRequest):
        analysis = AnalysisFactory(request.type).get_analyse(request.filters)
        response = CompanyAnalyticResponse()
        response = ExtractServiceHtml(request.url, request.depth, analysis.extractorsHtml).extract(response)
        response = ValidateServiceSite(request.url, analysis.validatorsSite).validate(response)
        return response
