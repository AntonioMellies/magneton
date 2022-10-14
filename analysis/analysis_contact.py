from analysis.analysis_base import AnalysisBase
from extractors.html.extractor_email import ExtractorHtmlEmail
from extractors.html.extractor_phone import ExtractorHtmlPhone
from models.filters import Filters


class AnalysisContact(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlEmail(filters),
            ExtractorHtmlPhone(filters),
        ]
        validatorsSite = []
        super().__init__(extractorsHtml, validatorsSite)
