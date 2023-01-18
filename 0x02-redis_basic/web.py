import requests
from functools import lru_cache


@lru_cache(maxsize=None)
def get_page(url: str) -> str:
    requests.get(url)
    count = "count:" + url
    if count in get_page.cache:
        get_page.cache[count] += 1
    else:
        get_page.cache[count] = 1
    return requests.get(url).text
