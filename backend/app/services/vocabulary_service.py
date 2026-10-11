def find_word(vocabulary, word):
    for item in vocabulary:
        if item["word"].lower() == word.lower():
            return item
    return None