import re


def sanitize_cnpj(cnpj: str) -> str:
    return re.sub(r"\D", "", cnpj)
