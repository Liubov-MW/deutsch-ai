import json

# завантажуємо всe з vocabular
with open("content/A0/vocabulary/vocabulary.json", "r", encoding="utf-8") as file:
    vocabulary = json.load(file)

# нова функція
def find_word(word):
    for item in vocabulary:
        if item["word"].lower() == word.lower():
            return item
    return None

word_input = input("Gib ein deutsches Wort ein: ")
result = find_word(word_input)
if result != None:
     print("Wort:", result["word"])
     print("Artikel:", result["article"])
     print("Plural:", result["plural"])
     print("Übersetzung:", result["translation_uk"])
     print("Niveau:", result["level"])
else:
     print("Wort nicht gefunden.")