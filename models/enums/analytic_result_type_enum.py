from enum import Enum


class AnalyticResultType(Enum):
    NOT_PERFORMED = 'NOT_PERFORMED'
    APPROVED = 'APPROVED'
    REPROVED = 'REPROVED'
    FOUND = 'FOUND'
    NOT_FOUND = 'NOT_FOUND'
