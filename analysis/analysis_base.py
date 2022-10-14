from __future__ import annotations

from abc import ABC
from typing import List

from extractors.html.base.extractor_html import ExtractorHtml
from validators.site.base.validator_site import ValidatorSite


class AnalysisBase(ABC):
    extractorsHtml: List[ExtractorHtml]
    validatorsSite: List[ValidatorSite]

    def __init__(self, extractors_html: List[ExtractorHtml], validators_site: List[ValidatorSite]) -> None:
        super().__init__()
        self.extractorsHtml = extractors_html
        self.validatorsSite = validators_site
