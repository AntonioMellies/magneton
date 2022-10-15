import re


def sanitize_cnpj(cnpj: str) -> str:
    return re.sub(r"\D", "", cnpj)


def sanitize_phone(phone: str) -> str:
    return re.sub(r"\D", "", phone)


def concat_tuples(item: tuple) -> [str]:
    return ''.join(item)
