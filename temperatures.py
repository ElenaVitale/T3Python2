"""
Use 2 functions (NOT ones!) for converting Celsius to Fahrenheit and vice versa
Important: Remember SRP - functions should do one thing, so these should be simple calculation functions.
Do not get user input or print output in the functions - do those things outside
"""


# The second attempt worked as I ensured that during the refactor process a variable was named in the wizard box.

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")



def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()








# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""

"""only one refactor worked....try again"""
# def main():
#     print(MENU)
#     celsius = 0
#
#     choice = input(">>> ").upper()
#     while choice != "Q":
#         if choice == "C":
#             fahrenheit = celsius_to_fahrenheit()
#             print("Result: {:.2f} F".format(fahrenheit))
#         elif choice == "F":
#             fahrenheit_to_celsius()
#             print(celsius)
#             #print("Result: {:.2f} C".format(celsius))
#         else:
#             print("Invalid option")
#         print(MENU)
#         choice = input(">>> ").upper()
#     print("Thank you.")
#
#
# def celsius_to_fahrenheit() -> float:
#     celsius = float(input("Celsius: "))
#     fahrenheit = celsius * 9.0 / 5 + 32
#     return fahrenheit
#
#
# def fahrenheit_to_celsius(celsius) -> float:
#     fahrenheit = float(input("Fahrenheit: "))
#     celsius = 5 / 9 * (fahrenheit - 32)
#     return celsius
#

main()



#Look in github for example
"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")