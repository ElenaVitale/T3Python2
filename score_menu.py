"""
Menu.
The menu should have four separate options:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit

Handle each of these (except quit) separately, and consider how you can reuse your functions.
In main(), before the menu loop, get the valid score
When the user quits, say some kind of "farewell". 
"""


MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    print(choice)
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            if score < 0 or score > 100:
                print("Invalid score")
                score = float(input("Enter score: "))
            print(score)
        elif choice == "P":
            pass
        elif choice == "S":
            pass

        else:
            print("invalid choice")
            print(MENU)
            choice = input("Choice: ").upper()

    print("Goodbye!!!")


main()