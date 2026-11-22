def find_word(vocabulary, word):
    for item in vocabulary:
        if item["word"].lower() == word.lower():
            return item
    return None


def search_words(vocabulary, query):
    results = []
    for item in vocabulary:
        if query.lower() in item["word"].lower():
            results.append(item)
    return results