import requests
import json
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    # params = {"query": [city, state]}
    params = {
        "query": city + " " + state + " skyline",
        "per_page": 1,
        }

    r = requests.get(url, headers=headers, params=params)
    # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n", r.url, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    content = json.loads(r.content)
    # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n", content, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": None}
