# Aufgabe 1 
# return
def check_age(age):
    if age >=18:
        return "Volljährig"
    else:
        return "Minderjährig"
print(check_age(17))
print(check_age(25))

# Aufgabe 2

words = ["Haus", "Buch", "Frau", "Mann", "Kind"]
def is_word_known(word):
    for item in words:
        if item.lower() == word.lower():
            return True
    return False
print(is_word_known("BUCH"))
print(is_word_known("Auto"))

# Aufgabe 3

def check_skore(score):
    if score >= 80:
        return "Sehr gut"
    elif score >= 50:
        return "Bestanden"
    else:
        return "Nicht bestanden"
print(check_skore(90))
print(check_skore(65))
print(check_skore(30))      

# Final Aufgabe

def check_temperature(temperature):
    if temperature >=25:
        return "Warm"
    elif temperature >=10:
        return "Normal"
    else:
        return "Kalt"
print(check_temperature(30))
print(check_temperature(15))
print(check_temperature(5))