import json
import requests

url = "https://api.quran.com/api/v4/resources/tafsirs"

r = requests.get(url)
jsonData = r.json()

with open("tafsir_info.json", "w") as outfile:
    json.dump(jsonData, outfile)