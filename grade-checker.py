def get_valid_grade():
    num = int(input("Enter a number: "))

    while num < 0 or num > 100:
        print("\nInvalid Number")
        print("Please choose a number 0 - 100")
        num = int(input("Enter a number: "))

    return num

def get_letter_grade(num):
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"

while True:
    print("\nWelcome to the Grade Checker")
    print("1. Check Grade")
    print("2. Exit")

    choice = int(input("Enter option 1 or 2: "))

    if choice == 1:
        grade = get_valid_grade()
        result = get_letter_grade(grade)
        print(result)
    elif choice == 2:
        print("Goodbye")
        break
    else:
        print("Invalid Option")
        