import requests
import json
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {
        "query": city + " " + state + " skyline",
        "per_page": 1,
        }

    r = requests.get(url, headers=headers, params=params)
    content = json.loads(r.content)


    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": None}



def get_weather_data(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": f"{city},{state},US",
        "appid": OPEN_WEATHER_API_KEY,
    }

    result = requests.get(url, params=params)
    content = json.loads(result.content)
    lat = content[0]["lat"]
    lon = content[0]["lon"]

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "lat": lat,
        "lon": lon,
        "units": "imperial",
        "appid": OPEN_WEATHER_API_KEY,
    }

    r = requests.get(weather_url, params=weather_params)
    weather_content = json.loads(r.content)

    try:
        weather = {
                "temp": weather_content["main"]["temp"],
                "description": weather_content["weather"][0]["description"],
        }
        return weather
    except (KeyError):
        return {"weather": None}

    # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", weather, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
