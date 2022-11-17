import logging
from typing import List

import cfscrape
from bs4 import BeautifulSoup

from agents.extractors.extract_service import ExtractService
from agents.extractors.html.base.extractor_html import ExtractorHtml
from models.base.response import Response
from utils.url_utils import valid_and_return_url


def valid_and_return_depth(depth):
    if depth is None or depth == 0:
        return 1
    return depth


class ExtractServiceHtml(ExtractService):

    def __init__(self, url: str, depth: int, extractors: List[ExtractorHtml]) -> None:
        super().__init__()
        self.url = valid_and_return_url(url)
        self.depth = valid_and_return_depth(depth)
        self.extractors = extractors

    def get_html_from_url(self) -> BeautifulSoup:
        try:
            scraper = cfscrape.create_scraper()
            html = scraper.get(self.url)
            if html.status_code == 200:
                return BeautifulSoup(html.content, "html.parser")
        except Exception as e:
            logging.error(e)

    def extract(self, response: Response = Response()) -> Response:
        if len(self.extractors) == 0:
            return response

        html = self.get_html_from_url()
        for extractor in self.extractors:
            extractor.set_html(html)

        for x in range(1, len(self.extractors)):
            self.extractors[x - 1].set_next(self.extractors[x])

        return self.extractors[0].handle(response)
