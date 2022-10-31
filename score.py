"""
Copy broken_score.py from prac 1 and rename it to score.py , then commit.
Your main function should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
FOLLOW SRP: The function should not print it.
Now add a new part to the bottom of your main function that generates a random score and prints the result.
You do NOT need to write a different function to determine the result for the random score.
If you've written your new function properly, you can use it.
If you've breached SRP, then you'll see that you can't.

"""


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


# WOW! It worked first try! I think I'm finally getting it. YAY!
#

#
# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# else:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Passable")
#     elif score < 50:
#         print("Bad")




"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# TODO: Fix this!
# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
"""Fixed code"""
# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# else:
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Passable")
#     elif score < 50:
#         print("Bad")