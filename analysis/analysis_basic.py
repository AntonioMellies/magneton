from analysis.analysis_base import AnalysisBase
from extractors.html.extractor_cnpj import ExtractorHtmlCNPJ
from models.filters import Filters


class AnalysisBasic(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlCNPJ(filters),
        ]
        validatorsSite = []
        super().__init__(extractorsHtml, validatorsSite)
