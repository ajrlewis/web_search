import asyncio
import sys

from loguru import logger

from web_search.providers import brave
from web_search.formatters import format_search_results_markdown


def main(query: str) -> str:
    search_results = brave.get_search_results(query)
    search_results_markdown = format_search_results_markdown(search_results)
    return search_results_markdown


async def async_main(query: str) -> str:
    search_results = await brave.get_search_results_async(query)
    search_results_markdown = format_search_results_markdown(search_results)
    return search_results_markdown


if __name__ == "__main__":
    query = sys.argv[1]
    logger.info(f"Searching Brave for: '{query}'")
    # search_results_markdown = asyncio.run(async_main(query))
    search_results_markdown = main(query)
    print(search_results_markdown)
