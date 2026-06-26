# ==========================================
# PYTHON DAY 5 - MENU DRIVEN PROGRAMS
# ==========================================


# ==========================================
# 1. SIMPLE MENU
# ==========================================

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Your Choice: "))

print("You Selected:", choice)


# ==========================================
# 2. MENU USING IF ELSE
# ==========================================

print("\n===== MENU =====")
print("1. Say Hello")
print("2. Say Welcome")
print("3. Exit")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Hello")
elif choice == 2:
    print("Welcome")
elif choice == 3:
    print("Program Closed")
else:
    print("Invalid Choice")


# ==========================================
# 3. MENU DRIVEN CALCULATOR
# ==========================================

print("\n===== CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == 1:
    print("Answer =", num1 + num2)

elif choice == 2:
    print("Answer =", num1 - num2)

elif choice == 3:
    print("Answer =", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Division by Zero Not Allowed")

else:
    print("Invalid Choice")


# ==========================================
# 4. MENU USING WHILE LOOP
# ==========================================

while True:

    print("\n===== MENU =====")
    print("1. Hello")
    print("2. Python")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Hello User")

    elif choice == 2:
        print("Welcome to Python")

    elif choice == 3:
        print("Program Closed")
        break

    else:
        print("Invalid Choice")


# ==========================================
# 5. MENU DRIVEN CALCULATOR WITH LOOP
# ==========================================

while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 5:
        print("Calculator Closed")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid Choice")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:

        if num2 == 0:
            print("Cannot Divide by Zero")
        else:
            print("Result =", num1 / num2)


# ==========================================
# 6. CASE INSENSITIVE INPUT
# ==========================================

choice = input("Enter Y or N: ").lower()

if choice == "y":
    print("You Selected YES")

elif choice == "n":
    print("You Selected NO")

else:
    print("Invalid Input")


# ==========================================
# 7. STRING MENU
# ==========================================

print("\n===== FOOD MENU =====")
print("Pizza")
print("Burger")
print("Coffee")

food = input("Enter Food Name: ").lower()

if food == "pizza":
    print("Pizza Ordered")

elif food == "burger":
    print("Burger Ordered")

elif food == "coffee":
    print("Coffee Ordered")

else:
    print("Food Not Available")


# ==========================================
# 8. NUMBER GUESS MENU
# ==========================================

import random

while True:

    print("\n===== GUESS GAME =====")
    print("1. Play")
    print("2. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 2:
        print("Game Closed")
        break

    elif choice == 1:

        secret = random.randint(1, 10)

        guess = int(input("Guess Number: "))

        if guess == secret:
            print("Correct")

        else:
            print("Wrong")
            print("Correct Number =", secret)

    else:
        print("Invalid Choice")


# ==========================================
# 9. STUDENT MENU
# ==========================================

students = []

while True:

    print("\n===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter Student Name: ")
        students.append(name)

    elif choice == 2:

        print(students)

    elif choice == 3:

        print("Thank You")
        break

    else:

        print("Invalid Choice")


# ==========================================
# 10. SIMPLE LOGIN
# ==========================================

username = "admin"
password = "1234"

user = input("Username: ")
pwd = input("Password: ")

if user == username and pwd == password:
    print("Login Successful")

else:
    print("Invalid Username or Password")


# ==========================================
# 11. ERROR HANDLING FOR WRONG MENU CHOICE
# ==========================================

try:

    choice = int(input("Enter Menu Choice: "))

    if choice in [1, 2, 3]:
        print("Valid Choice")

    else:
        print("Invalid Menu Choice")

except ValueError:

    print("Please Enter Numbers Only")


# ==========================================
# 12. TYPE MISMATCH EXAMPLE
# ==========================================

choice = input("Enter Number: ")

if choice == "1":
    print("Correct")

else:
    print("Wrong Input")


# ==========================================
# 13. CASE CONVERSION
# ==========================================

text = input("Enter YES or NO: ")

print(text.lower())
print(text.upper())


# ==========================================
# 14. MENU USING MATCH (Python 3.10+)
# ==========================================

choice = int(input("Enter Choice (1-3): "))

match choice:

    case 1:
        print("Addition")

    case 2:
        print("Subtraction")

    case 3:
        print("Exit")

    case _:
        print("Invalid Choice")


# ==========================================
# 15. MINI PROJECT - ATM MENU
# ==========================================

balance = 10000

while True:

    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        print("Balance =", balance)

    elif choice == 2:

        amount = float(input("Enter Amount: "))
        balance += amount
        print("Deposit Successful")

    elif choice == 3:

        amount = float(input("Enter Amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    elif choice == 4:

        print("Thank You")
        break

    else:

        print("Invalid Choice")
