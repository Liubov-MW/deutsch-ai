from services.vocabulary_service import search_words

vocabulary = [
    {"word": "Haus", "translation": "будинок"},
    {"word": "Haustür", "translation": "вхідні двері"},
    {"word": "Baum", "translation": "дерево"},
    {"word": "Buch", "translation": "книга"}
]
print(search_words(vocabulary, "haus"))
print(search_words(vocabulary, "BU"))
print(search_words(vocabulary, "Auto"))