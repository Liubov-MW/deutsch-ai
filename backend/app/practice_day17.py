from services.vocabulary_service import search_words

vocabulary = [
    {"word": "Haus", "translation": "будинок"},
    {"word": "Haustür", "translation": "вхідні двері"},
    {"word": "Buch", "translation": "книга"},
    {"word": "Arbeit", "translation": "робота"}
]

print(search_words(vocabulary, "haus"))
print(search_words(vocabulary, " HAUS "))
print(search_words(vocabulary, "bu"))
print(search_words(vocabulary, "   "))
print(search_words(vocabulary, ""))
print(search_words(vocabulary, "XYZ"))

# Test 1: empty query
result = search_words(vocabulary, "")
assert result == []
print("Test 1 passed")

# Test 2
result = search_words(vocabulary, " ")
assert result == []
print("Test 2 passed")

# Test 3
result = search_words(vocabulary, "XYZ")
assert result == []
print("Test 3 passed")

# Test 4 partial search
result = search_words(vocabulary, "bu")
assert len(result) == 1
assert result[0]["word"] == "Buch"
print("Test 4 passed")

# Test 5 case insensitive search
result = search_words(vocabulary, " HAUS ")
assert len(result) == 2
assert result[0]["word"] == "Haus"
assert result[1]["word"] == "Haustür"
print("Test 5 passed")