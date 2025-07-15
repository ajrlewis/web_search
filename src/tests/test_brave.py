import asyncio

from loguru import logger
import pytest

from web_search.providers import brave


@pytest.mark.asyncio
async def test_get_search_results_async():
    results = await brave.get_search_results_async("Hello World", max_results=5)
    logger.info(f"{results = }")
    assert isinstance(results, list)
    if results:
        assert len(results) == 5
        formatted = brave.format_search_result(results[0])
        assert "title" in formatted
        assert "href" in formatted
        assert "snippet" in formatted
