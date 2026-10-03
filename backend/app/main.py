import json

with open("content/A0/vocabulary/vocabulary.json", "r", encoding="utf-8") as file:
    vocabulary = json.load(file)

word_input = input("Gib ein deutsches Wort ein: ")

found = False

for item in vocabulary:
    if item["word"] == word_input:
        print("Wort:", item["word"])
        print("Artikel:", item["article"])
        print("Plural:", item["plural"])
        print("Übersetzung:", item["translation_uk"])
        print("Niveau:", item["level"])
        found = True
        break

if not found:
        print("Wort nicht gefunden.")