from typing import List
from urllib.request import Request, urlopen
import ssl

from bs4 import BeautifulSoup

from extractors.extract_service import ExtractService
from extractors.html.base.extractor_html import ExtractorHtml
from models.base.response import Response
from utils.request_utils import get_user_agent
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
        req = Request(self.url)
        req.add_header('User-Agent', get_user_agent())

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urlopen(req, context=ctx)
        return BeautifulSoup(html, "html.parser")

    def extract(self, response: Response = Response()) -> Response:
        if len(self.extractors) == 0:
            return response

        html = self.get_html_from_url()
        for extractor in self.extractors:
            extractor.set_html(html)

        for x in range(1, len(self.extractors)):
            self.extractors[x - 1].set_next(self.extractors[x])

        return self.extractors[0].handle(response)

