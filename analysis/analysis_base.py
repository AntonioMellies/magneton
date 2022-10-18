from __future__ import annotations

from abc import ABC
from typing import List

from agents.extractors.html.base.extractor_html import ExtractorHtml
from agents.informations.site.base.informer_site import InformerSite
from agents.validators.site.base.validator_site import ValidatorSite


class AnalysisBase(ABC):
    extractorsHtml: List[ExtractorHtml]
    validatorsSite: List[ValidatorSite]
    informersSite: List[InformerSite]

    def __init__(self, extractors_html: List[ExtractorHtml],
                 validators_site: List[ValidatorSite],
                 informers_site: List[InformerSite]) -> None:
        super().__init__()
        self.extractorsHtml = extractors_html
        self.validatorsSite = validators_site
        self.informersSite = informers_site
