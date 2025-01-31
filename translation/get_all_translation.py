import requests
import json

with open("translation/translation_info.json", "r") as file:
    data = dict(json.load(file))
    translations =list(data["translations"])
    for(translation_data) in translations:
        current_translation = dict(translation_data)
        id =  current_translation["id"]
        print("Getting : ", id)
        url = f"https://api.quran.com/api/v4/quran/translations/{id}"
        response = requests.get(url)
        with open(f"translation/all_translations/{id}.json", "w+") as outfile:
            json.dump(response.json(), outfile)

        