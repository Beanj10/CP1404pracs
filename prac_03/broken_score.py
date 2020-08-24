"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(score_check(score))
    import random
    rscore = random.randint(1, 100)
    print(rscore, score_check(rscore))


def score_check(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    return (result)



main()
