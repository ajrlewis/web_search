# web_search/types.py
from typing import TypedDict


class SearchResult(TypedDict):
    title: str
    url: str
    snippet: str
