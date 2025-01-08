import json

with open("tafsir/all_tafsir_data/tafsir.json", "r") as file:
    data = dict(json.load(file))
    tafsir =list(data["tafsirs"])

    mapOfResources = {}

    for (tafsir_data) in tafsir:
        current_tafsir = dict(tafsir_data)
        id =  current_tafsir["resource_id"]
        if(id in mapOfResources):
            mapOfResources[id].append(current_tafsir["text"])
        else:
            mapOfResources[id] = []
            mapOfResources[id].append(current_tafsir["text"])

    for (key, value) in mapOfResources.items():
        with open(f"tafsir/all_tafsir_data/{key}.json", "w") as outfile:
            json.dump(value, outfile)