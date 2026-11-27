def find_word(vocabulary, word):
    for item in vocabulary:
        if item["word"].lower() == word.lower():
            return item
    return None


def search_words(vocabulary, query):
    clean_query = query.strip().lower()

    if not clean_query:
        return []
    
    results = []

    for item in vocabulary:
        if clean_query in item["word"].lower():
            results.append(item)
    return results
