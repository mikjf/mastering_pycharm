from typing import List
import urllib.parse
import requests
from functools import lru_cache

# Reuse a single HTTP session for connection pooling
_session = requests.Session()


# Make faster by caching repeated identical searches
@lru_cache(maxsize=256)
def search(text: str) -> List[str]:
    url = build_url(text)
    response = perform_search(url)
    results = convert_results(response)
    return results


def build_url(text: str) -> str:
    # format is https://search.talkpython.fm/api/search?q=SEARCH
    encoded = urllib.parse.urlencode({'q': text})
    url = f'https://search.talkpython.fm/api/search?{encoded}'
    return url


def perform_search(url: str) -> requests.Response:
    # Add a small timeout and use session for keep-alive
    resp = _session.get(url, timeout=5)
    resp.raise_for_status()
    return resp


def convert_results(response: requests.Response) -> List[str]:
    data = response.json() or {}
    results = data.get('results') or []
    return [d.get('description') for d in results if isinstance(d, dict)]