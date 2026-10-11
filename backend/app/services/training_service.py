def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(check_answer(" Haus ", "haus"))
    print(check_answer("Guten Abend", "Guten Morgen"))
