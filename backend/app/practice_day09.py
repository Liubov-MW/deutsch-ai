# Aufgabe 1. Kontrolieren Day08

def check_age(age):
    if age < 18:
        return "Mindestjährig"
    elif age < 65:
        return "Erwachsen"
    else:
        return "Senior"
print(check_age(15))
print(check_age(34))
print(check_age(70))

# Aufgabe 2. Die neue Thema 
# .append() - додати елемент у список

words = ["Haus", "Buch"]
words.append("Frau")
words.append("Mann")
print(words)

# Aufgabe 3.

words = ["Haus" , "Buch"]
def add_word(word):
    words.append(word)
add_word("Kind")
print(words)

# Aufgabe 4.1
# dict - dictionary словник Python
new_word = {
    "word": "Kind",
    "article": "das",
    "plural": "Kinder"
}
print(new_word)
print(new_word["plural"])

# Aufgabe 4.2

vocabulary = []
vocabulary.append(new_word)
print(vocabulary)

# Aufgabe 5

vocabulary =[]
def add_word(word):
    vocabulary.append(word)
add_word(new_word)
print(vocabulary)

# Aufgabe 6
# not - оператор (not in - не знаходиться в)

words = ["Haus", "Buch", "Kind"]
def add_word(word):
    if word not in words:
        words.append(word)
add_word("Auto")
add_word("Kind")
print(words)

# Aufgabe 7

for item in vocabulary:
    print(item["article"], item["word"])
