from agents.extractors.html.extract_service_html import ExtractServiceHtml
from agents.informations.site.inform_service_site import InformServiceSite
from agents.validators.site.validate_service_site import ValidateServiceSite
from analysis.analysis_factory import AnalysisFactory
from models.company_analytic_request import CompanyAnalyticRequest
from models.company_analytic_response import CompanyAnalyticResponse


class CompanyAnalysisBusiness:

    def analyze(self, request: CompanyAnalyticRequest):
        analysis = AnalysisFactory(request.type).get_analyse(request.filters)
        response = CompanyAnalyticResponse()
        response = ExtractServiceHtml(request.url, request.depth, analysis.extractorsHtml).extract(response)
        response = ValidateServiceSite(request.url, analysis.validatorsSite).validate(response)
        response = InformServiceSite(request.url, analysis.informersSite).inform(response)
        return response
