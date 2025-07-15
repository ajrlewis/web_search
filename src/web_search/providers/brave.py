from typing import Optional, Any, List, Dict

import httpx
from loguru import logger

from web_search.config import (
    BRAVE_SEARCH_API_KEY,
    BRAVE_SEARCH_API_URL,
    DEFAULT_TIMEOUT,
)
from web_search.types import SearchResult


def get_search_results(
    query: str, max_results: int = 20, api_key: Optional[str] = None
) -> List[SearchResult]:
    token = api_key or BRAVE_SEARCH_API_KEY
    if not token:
        logger.error(
            "Brave API key not provided and BRAVE_SEARCH_API_KEY not set in environment."
        )
        return []

    params = {"q": query, "count": max_results}
    headers = {"X-Subscription-Token": token}

    try:
        with httpx.Client(timeout=DEFAULT_TIMEOUT) as client:
            response = client.get(BRAVE_SEARCH_API_URL, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            raw_results = data.get("web", {}).get("results", [])
            return format_search_results(raw_results)
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Brave API request failed for query '{query}': {e}")
    except ValueError as e:
        logger.error(f"Failed to decode Brave API response for query '{query}': {e}")
    return []


async def get_search_results_async(
    query: str, max_results: int = 20, api_key: Optional[str] = None
) -> List[SearchResult]:
    token = api_key or BRAVE_SEARCH_API_KEY
    if not token:
        logger.error(
            "Brave API key not provided and BRAVE_SEARCH_API_KEY not set in environment."
        )
        return []

    params = {"q": query, "count": max_results}
    headers = {"X-Subscription-Token": token}

    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            response = await client.get(
                BRAVE_SEARCH_API_URL, params=params, headers=headers
            )
            response.raise_for_status()
            data = response.json()
            raw_results = data.get("web", {}).get("results", [])
            return format_search_results(raw_results)
    except (httpx.RequestError, httpx.HTTPStatusError) as e:
        logger.error(f"Brave API request failed for query '{query}': {e}")
    except ValueError as e:
        logger.error(f"Failed to decode Brave API response for query '{query}': {e}")
    return []


def format_search_results(raw_results: List[Dict[str, Any]]) -> List[SearchResult]:
    formatted_results = []
    for raw_result in raw_results:
        title = raw_result.get("title", "")
        url = raw_result.get("url", "")
        description = raw_result.get("description", "")
        extra_snippets = " ".join(raw_result.get("extra_snippets", []))
        snippet = f"{description} {extra_snippets}".strip()

        formatted_results.append(
            {
                "title": title,
                "href": url,
                "snippet": snippet,
            }
        )

    return formatted_results
