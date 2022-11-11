import logging
import re

from agents.extractors.html.base.extractor_html_simple_base import ExtractorHtmlSimpleBase
from models.company_analytic_response import CompanyAnalyticResponse
from models.enums.analytic_result_type_enum import AnalyticResultType


class ExtractorHtmlRAVSeal(ExtractorHtmlSimpleBase):

    def __init__(self) -> None:
        super().__init__()

    def handle(self, request: CompanyAnalyticResponse = CompanyAnalyticResponse()) -> CompanyAnalyticResponse:
        logging.info("ExtractorHtmlRavSeal")
        request.ravSealPublic = AnalyticResultType.REPROVED

        if self.rav_seal_exists():
            request.ravSealPublic = AnalyticResultType.APPROVED

        if self._next_handler:
            return self._next_handler.handle(request)

        return request

    def rav_seal_exists(self) -> bool:
        try:
            ids_seals = ["ra-widget-verified", "ra-widget-verified-wrapper"]
            if not self.html:
                return False

            for id_seal in ids_seals:
                elements_with_id = self.html.findAll(id=id_seal)
                if len(elements_with_id) > 0:
                    return True

        except Exception as e:
            logging.error(e)
            return False
        else:
            return False
