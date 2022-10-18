from abc import ABC

from bs4 import BeautifulSoup

from agents.extractors.extractor import Extractor


class ExtractorHtml(Extractor, ABC):
    html: BeautifulSoup = None

    def set_html(self, html):
        self.html = html
