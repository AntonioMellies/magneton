from agents.extractors.html.extractor_cnpj import ExtractorHtmlCNPJ
from agents.extractors.html.extractor_email import ExtractorHtmlEmail
from agents.extractors.html.extractor_phone import ExtractorHtmlPhone
from agents.extractors.html.extractor_rav_seal import ExtractorHtmlRAVSeal
from agents.informations.site.informer_whois import InformerWhoIs
from agents.validators.site.validator_https import ValidatorHttps
from agents.validators.site.validator_ssl import ValidatorSSL
from analysis.analysis_base import AnalysisBase
from models.filters import Filters


class AnalysisFull(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlCNPJ(filters),
            ExtractorHtmlEmail(filters),
            ExtractorHtmlPhone(filters),
            ExtractorHtmlRAVSeal(),
        ]
        validatorsSite = [
            ValidatorSSL(),
            ValidatorHttps()
        ]
        informersSite = [
            InformerWhoIs()
        ]
        super().__init__(extractorsHtml, validatorsSite, informersSite)
