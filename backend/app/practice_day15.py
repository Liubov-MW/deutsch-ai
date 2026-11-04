def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == " ".strip().lower():
        return "Keine Antwort"
    elif user_answer.strip().lower() == correct_answer.strip().lower():
        return True
    else:
        return False
if __name__ == "__main__":
    print(check_answer("Haus", "haus"))
    print(check_answer(" Buch ", "buch"))
    print(check_answer("Katze", "Hund"))
    print(check_answer(" ", "Haus"))

def find_word(vocabulary, word):
    for item in vocabulary:
        if item["word"].strip().lower() == word.strip().lower():
            return item
    return None

vocabulary = [
    {"word": "Haus", "translation": "будинок"},
    {"word": "Buch", "translation": "книга"},
    {"word": "Katze", "translation": "кішка"}
]

print(find_word(vocabulary, "Haus"))
print(find_word(vocabulary, "Katze"))
print(find_word(vocabulary, "Hund"))
print(find_word(vocabulary, "haus"))
print(find_word(vocabulary, " BUCH "))
print(find_word(vocabulary, "kAtZe"))
print(find_word(vocabulary, "Auto"))