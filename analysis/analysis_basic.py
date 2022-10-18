from agents.extractors.html.extractor_cnpj import ExtractorHtmlCNPJ
from analysis.analysis_base import AnalysisBase
from models.filters import Filters


class AnalysisBasic(AnalysisBase):

    def __init__(self, filters: Filters) -> None:
        extractorsHtml = [
            ExtractorHtmlCNPJ(filters),
        ]
        validatorsSite = []
        informersSite = []
        super().__init__(extractorsHtml, validatorsSite, informersSite)
