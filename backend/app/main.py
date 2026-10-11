import json
from services.vocabulary_service import find_word
from services.training_service import check_answer
from services.progress_service import calculate_score

# завантажуємо всe з vocabular
with open("content/A0/vocabulary/vocabulary.json", "r", encoding="utf-8") as file:
    vocabulary = json.load(file)

word_input = input("Gib ein deutsches Wort ein: ")
result = find_word(vocabulary, word_input)
if result != None:
     print("Wort:", result["word"])
     print("Artikel:", result["article"])
     print("Plural:", result["plural"])
     print("Übersetzung:", result["translation_uk"])
     print("Niveau:", result["level"])
else:
     print("Wort nicht gefunden.")
print("Training Test:")

result = check_answer("Haus", "haus")
print("Antwort richtig:", result)

percentage = calculate_score(3,1)
print("Ergebnis:", percentage, "%")