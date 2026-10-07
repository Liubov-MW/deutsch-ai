# Aufgabe 1

correct_article = "das"
article_input = input("Welcher Artikel? Haus: ")
if article_input.lower() == correct_article.lower():
    print("Richtig!")
else:
    print("Falsch!")

# Aufgabe 2

word = {
    "word": "Buch",
    "article": "das",
    "translation_uk": "книга",
    "explanation_uk": "Buch - середнього роду, тому артикль das."
}
print(word["word"])

# Aufgabe 3 (Aufgabe 1+2)

article_input = input("Welcher Artikel? Buch: ")
if article_input.lower() == word["article"].lower():
    print("Richtig!")
else:
    print("Falsch!")

# Aufgabe 4, # Day 11 Aufgabe 1,2,3

def check_article(user_answer, correct_article):
    if user_answer.lower() == correct_article.lower():
        return True
    else:
        return False


# Day 11 Aufgabe 3

result = check_article(article_input, word["article"])
if result == True:
    print("Richtig!")
else:
    print("Falsche!")
    print("Richtige Antwort: ", word["article"], word["word"])
    print(word["explanation_uk"])

# Day 11 Aufgabe 4

word2 = {
    "word": "Haus",
    "article": "das",
    "translation_uk": "будинок",
    "explanation_uk": "Haus - середнього роду, тому артикль das."
}

# Aufgabe 5

vocabulary = [word, word2] 

# Aufgabe 6

for item in vocabulary:
    print(item["word"])

# Aufgabe 7

for item in vocabulary:
    answer = input("Welcher Artikel? " + item["word"] + ": ")
    result = check_article(answer, item["article"])
    if result == True:
        print("Richtig!")
    else:
        print("Falsch!")
        print("Richtige Antwort: ", item["article"], item["word"])
        print(item["explanation_uk"])