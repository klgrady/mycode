#!/usr/bin/python3
from datetime import date
import requests

KEY = "Lf0UXoet5H9GvAIma6BqtR0sBNU7uVbbA4JIqVnE"
URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-08-05&api_key=" + KEY
resp = requests.get(URL)

death_dict = resp.json()
todays_death = death_dict['near_earth_objects']['2021-08-05']
for item in todays_death:
    print(item['id'])
