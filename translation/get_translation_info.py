import requests
import json

url = "https://api.quran.com/api/v4/resources/translations"

data = requests.get(url)

with open("translation/translation_info.json", "w") as outfile:
    json.dump(data.json(), outfile)