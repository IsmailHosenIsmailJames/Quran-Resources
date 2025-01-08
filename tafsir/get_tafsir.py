import json
import requests

url = "https://api.quran.com/api/v4/quran/tafsirs/165"

r = requests.get(url)
jsonData = r.json()

with open("tafsir/all_tafsir_data/tafsir.json", "w") as outfile:
    json.dump(jsonData, outfile)