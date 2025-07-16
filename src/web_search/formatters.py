from typing import Optional, Any, List, Dict

from web_search.types import SearchResult


def format_search_results_markdown(search_results: List[SearchResult]) -> str:
    formatted_results = [
        f"### [{r['title']}]({r['url']})\n{r['snippet']}" for r in search_results
    ]
    return "\n\n".join(formatted_results)
