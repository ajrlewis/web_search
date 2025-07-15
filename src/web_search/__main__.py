import asyncio

from loguru import logger

from web_search.providers import brave


def main():
    query = "Peter Howson"
    logger.info(f"Searching Brave for: '{query}'\\n")

    results = brave.get_search_results(query, max_results=5)
    for i, result in enumerate(results, 1):
        formatted = brave.format_search_result(result)
        logger.info(f"{i}. {formatted['title']}")
        logger.info(f"   {formatted['href']}")
        logger.info(f"   {formatted['snippet']}")


async def async_main():
    query = "Hello World!"
    logger.info(f"Searching Brave for: '{query}'\\n")

    # results = await brave.get_search_results_async(query, max_results=5)
    # for i, result in enumerate(results, 1):
    #     formatted = brave.format_search_result(result)
    #     logger.info(f"{i}. {formatted['title']}")
    #     logger.info(f"   {formatted['href']}")
    #     logger.info(f"   {formatted['snippet']}")


if __name__ == "__main__":
    asyncio.run(async_main())
    # main()
