from dataclasses import dataclass
from typing import List



@dataclass
class Suggestion:
    symbol:str
    symbol_info:str
    url: str
    type: str
    sub_type: str


@dataclass
class Suggestions:
    symbolList: List[Suggestion]

