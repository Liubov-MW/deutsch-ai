# Aufgabe 1

score = 0
score = score + 1
score = score + 1
score = score + 1
print(score)

# Aufgabe 2

score = 0
for i in range(1,6):
    score += 1
print(score)

# Aufgabe 3, 4, 5. рахуємо правильні відповіді (score) та помилки (mistakes). Відсотки (усі відповіді, відсоток)

word = {
    "word": "Buch",
    "article": "das",
    "translation_uk": "книга",
    "explanation_uk": "Buch - середнього роду, тому артикль das."
}
word2 = {
    "word": "Haus",
    "article": "das",
    "translation_uk": "будинок",
    "explanation_uk": "Haus - середнього роду, тому артикль das."
}
def check_article(user_answer, correct_article):
    if user_answer.lower() == correct_article.lower():
        return True
    else:
        return False
vocabulary = [word, word2]     
score = 0
mistakes = 0
for item in vocabulary:
    answer = input("Welcher Artikel? " + item["word"] + ": ")
    result = check_article(answer, item["article"])
    if result == True:
        print("Richtig!")
        score +=1
    else:
        print("Falsch!")
        print("Richtige Antwort: ", item["article"], item["word"])
        print(item["explanation_uk"])
        mistakes +=1
total = score + mistakes
percentage = score/total * 100
print ("Richtige Antworten: ", score)
print ("Falsche Antworten: ", mistakes)
print ("Ergebnis: ", percentage, "%")
