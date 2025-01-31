import os
import json

dirs = os.listdir("tafsir/all_tafsir_data")


tafsirInfo = [
        {
            "id": 169,
            "name": "Ibn Kathir (Abridged)",
            "author_name": "Hafiz Ibn Kathir",
            "slug": "en-tafisr-ibn-kathir",
            "language_name": "english",
            "translated_name": {
                "name": "Ibn Kathir (Abridged)",
                "language_name": "english"
            }
        },
        {
            "id": 381,
            "name": "Tafsir Fathul Majid",
            "author_name": "AbdulRahman Bin Hasan Al-Alshaikh",
            "slug": "tafisr-fathul-majid-bn",
            "language_name": "bengali",
            "translated_name": {
                "name": "Tafsir Fathul Majid",
                "language_name": "english"
            }
        },
        {
            "id": 16,
            "name": "Tafsir Muyassar",
            "author_name": "\u0627\u0644\u0645\u06cc\u0633\u0631",
            "slug": "ar-tafsir-muyassar",
            "language_name": "arabic",
            "translated_name": {
                "name": "Tafsir Muyassar",
                "language_name": "english"
            }
        },
        {
            "id": 165,
            "name": "Tafsir Ahsanul Bayaan",
            "author_name": "Bayaan Foundation",
            "slug": "bn-tafsir-ahsanul-bayaan",
            "language_name": "bengali",
            "translated_name": {
                "name": "Tafsir Ahsanul Bayaan",
                "language_name": "english"
            }
        },
        {
            "id": 166,
            "name": "Tafsir Abu Bakr Zakaria",
            "author_name": "King Fahd Quran Printing Complex",
            "slug": "bn-tafsir-abu-bakr-zakaria",
            "language_name": "bengali",
            "translated_name": {
                "name": "Tafsir Abu Bakr Zakaria",
                "language_name": "english"
            }
        },
        {
            "id": 93,
            "name": "Al-Tafsir al-Wasit (Tantawi)",
            "author_name": "Waseet",
            "slug": "ar-tafsir-al-wasit",
            "language_name": "arabic",
            "translated_name": {
                "name": "Al-Tafsir al-Wasit (Tantawi)",
                "language_name": "english"
            }
        },
        {
            "id": 14,
            "name": "Tafsir Ibn Kathir",
            "author_name": "Hafiz Ibn Kathir",
            "slug": "ar-tafsir-ibn-kathir",
            "language_name": "arabic",
            "translated_name": {
                "name": "Tafsir Ibn Kathir",
                "language_name": "english"
            }
        },
        {
            "id": 15,
            "name": "Tafsir al-Tabari",
            "author_name": "Tabari",
            "slug": "ar-tafsir-al-tabari",
            "language_name": "arabic",
            "translated_name": {
                "name": "Tafsir al-Tabari",
                "language_name": "english"
            }
        },
        {
            "id": 164,
            "name": "Tafseer ibn Kathir",
            "author_name": "Tawheed Publication",
            "slug": "bn-tafseer-ibn-e-kaseer",
            "language_name": "bengali",
            "translated_name": {
                "name": "Tafseer ibn Kathir",
                "language_name": "english"
            }
        },
        {
            "id": 90,
            "name": "Al-Qurtubi",
            "author_name": "Qurtubi",
            "slug": "ar-tafseer-al-qurtubi",
            "language_name": "arabic",
            "translated_name": {
                "name": "Al-Qurtubi",
                "language_name": "english"
            }
        },
        {
            "id": 168,
            "name": "Ma'arif al-Qur'an",
            "author_name": "Mufti Muhammad Shafi",
            "slug": "en-tafsir-maarif-ul-quran",
            "language_name": "english",
            "translated_name": {
                "name": "Ma'arif al-Qur'an",
                "language_name": "english"
            }
        },
        {
            "id": 91,
            "name": "\u0627\u0644\u0633\u0639\u062f\u064a Al-Sa'di",
            "author_name": "Saddi",
            "slug": "ar-tafseer-al-saddi",
            "language_name": "arabic",
            "translated_name": {
                "name": "\u0627\u0644\u0633\u0639\u062f\u064a Al-Sa'di",
                "language_name": "english"
            }
        },
        {
            "id": 170,
            "name": "Al-Sa'di",
            "author_name": "Saddi",
            "slug": "ru-tafseer-al-saddi",
            "language_name": "russian",
            "translated_name": {
                "name": "Al-Sa'di",
                "language_name": "english"
            }
        },
        {
            "id": 94,
            "name": "Tafseer Al-Baghawi",
            "author_name": "Baghawy",
            "slug": "ar-tafsir-al-baghawi",
            "language_name": "arabic",
            "translated_name": {
                "name": "Tafseer Al-Baghawi",
                "language_name": "english"
            }
        },
        {
            "id": 157,
            "name": "Fi Zilal al-Quran",
            "author_name": "Sayyid Ibrahim Qutb",
            "slug": "tafsir-fe-zalul-quran-syed-qatab",
            "language_name": "urdu",
            "translated_name": {
                "name": "Fi Zilal al-Quran",
                "language_name": "english"
            }
        },
        {
            "id": 804,
            "name": "Rebar Kurdish Tafsir",
            "author_name": "Rebar Kurdish Tafsir",
            "slug": "kurd-tafsir-rebar",
            "language_name": "Kurdish",
            "translated_name": {
                "name": "Rebar Kurdish Tafsir",
                "language_name": "english"
            }
        },
        {
            "id": 817,
            "name": "Tazkirul Quran(Maulana Wahiduddin Khan)",
            "author_name": "Maulana Wahid Uddin Khan",
            "slug": "tazkirul-quran-en",
            "language_name": "english",
            "translated_name": {
                "name": "Tazkirul Quran",
                "language_name": "english"
            }
        },
        {
            "id": 160,
            "name": "Tafsir Ibn Kathir",
            "author_name": "Hafiz Ibn Kathir",
            "slug": "tafseer-ibn-e-kaseer-urdu",
            "language_name": "urdu",
            "translated_name": {
                "name": "Tafsir Ibn Kathir",
                "language_name": "english"
            }
        },
        {
            "id": 818,
            "name": "Tazkir ul Quran",
            "author_name": "Maulana Wahid Uddin Khan",
            "slug": "tazkiru-quran-ur",
            "language_name": "urdu",
            "translated_name": {
                "name": "Tazkir ul Quran",
                "language_name": "english"
            }
        },
        {
            "id": 159,
            "name": "Bayan ul Quran",
            "author_name": "Dr. Israr Ahmad",
            "slug": "tafsir-bayan-ul-quran",
            "language_name": "urdu",
            "translated_name": {
                "name": "Bayan ul Quran",
                "language_name": "english"
            }
        }
    ]

validate = []

def findInfoByKey(key):
    for info in tafsirInfo:
        if(f"{info["id"]}"== f"{key}"):
            return info

for file in dirs:
    with open(f"tafsir/all_tafsir_data/{file}", "r") as f:
        data = json.load(f)
        if(len(data) == 6236) :
            validate.append({file : findInfoByKey(key=file.split(".")[0]) })
            print(file)

with open ("tafsir/valid_tafsir.json", "w") as outfile:
    json.dump(dict({"Data":validate}), outfile)