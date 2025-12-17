from dataclasses import dataclass


@dataclass(frozen=True)
class GetFullCatalogInput:
    level: str
    white_label: str
    user_lang: str
