from analysis.analysis_base import AnalysisBase
from extractors.html.extractor_cnpj import ExtractorHtmlCNPJ
from extractors.html.extractor_email import ExtractorHtmlEmail
from extractors.html.extractor_phone import ExtractorHtmlPhone
from models.filters import Filters
from validators.site.validator_https import ValidatorHttps
from validators.site.validator_ssl import ValidatorSSL
from validators.site.validator_whois import ValidatorWhoIs


class AnalysisFull(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlCNPJ(filters),
            ExtractorHtmlEmail(filters),
            ExtractorHtmlPhone(filters),
        ]
        validatorsSite = [
            ValidatorSSL(),
            ValidatorWhoIs(),
            ValidatorHttps()
        ]
        super().__init__(extractorsHtml, validatorsSite)
