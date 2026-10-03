words = ["Haus", "Buch", "Frau", "Mann", "Kind"]

word_input = input("Gib ein deutsches Wort ein: ")

found = False

for item in words:
    if item.lower() == word_input.lower():
        print("Wort gefunden!")
        found = True
        break

if not found:
        print("Wort nicht gefunden.")