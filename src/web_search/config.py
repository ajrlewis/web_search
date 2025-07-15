# web_search/config.py
import os

from dotenv import load_dotenv

load_dotenv()


BRAVE_SEARCH_API_KEY = os.getenv("BRAVE_SEARCH_API_KEY")
BRAVE_SEARCH_API_URL = "https://api.search.brave.com/res/v1/web/search"

DEFAULT_TIMEOUT = 10
