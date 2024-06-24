from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ReportType(Enum):
    TXT = 'txt'
    PDF = 'pdf'


@dataclass
class ReportModel:
    name: str
    type: str
    data: dict[str, str]


@dataclass
class ViewModel:
    header: str
    lines: list[str]
