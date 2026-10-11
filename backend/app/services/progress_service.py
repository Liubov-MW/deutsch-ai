def calculate_score(score, mistakes):
    total = score + mistakes
    if total == 0:
        return 0
    percentage = score / total * 100
    return percentage
if __name__ == "__main__":
    print(calculate_score(3,1))
    print(calculate_score(5,0))
    print(calculate_score(0,0))
