from agents.extractors.html.extractor_email import ExtractorHtmlEmail
from agents.extractors.html.extractor_phone import ExtractorHtmlPhone
from analysis.analysis_base import AnalysisBase
from models.filters import Filters


class AnalysisContact(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlEmail(filters),
            ExtractorHtmlPhone(filters),
        ]
        validatorsSite = []
        informersSite = []
        super().__init__(extractorsHtml, validatorsSite, informersSite)
