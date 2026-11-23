
from backend.app.services.vocabulary_service import search_words


def test_search_word():
    vocabulary = [
        {"word": "Haus", "translation": "будинок"},
        {"word": "Baum", "translation": "дерево"},
        {"word": "Buch", "translation": "книга"}
    ]

    results = search_words(vocabulary, "haus")

    assert len(results) == 1
    assert results[0]["word"] == "Haus"
