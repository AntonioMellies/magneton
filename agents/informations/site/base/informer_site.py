from abc import ABC

from agents.informations.informer import Informer


class InformerSite(Informer, ABC):
    url: str = None

    def set_url(self, url):
        self.url = url
