# ==========================================
# PYTHON DAY 4 - RANDOM MODULE
# ==========================================


# ==========================================
# 1. IMPORT RANDOM MODULE
# ==========================================

import random

print("Random Module Imported Successfully")


# ==========================================
# 2. RANDOM INTEGER (randint)
# ==========================================

number = random.randint(1, 10)

print(number)


# ==========================================
# 3. RANDOM RANGE (randrange)
# ==========================================

number = random.randrange(1, 10)

print(number)


# ==========================================
# 4. RANDOM FLOAT (random)
# ==========================================

number = random.random()

print(number)


# ==========================================
# 5. RANDOM DECIMAL NUMBER (uniform)
# ==========================================

number = random.uniform(1.5, 10.5)

print(number)


# ==========================================
# 6. RANDOM CHOICE
# ==========================================

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

fruit = random.choice(fruits)

print(fruit)


# ==========================================
# 7. RANDOM CHOICE FROM TUPLE
# ==========================================

colors = ("Red", "Green", "Blue", "Black", "White")

print(random.choice(colors))


# ==========================================
# 8. RANDOM SHUFFLE
# ==========================================

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

random.shuffle(cards)

print(cards)


# ==========================================
# 9. RANDOM PASSWORD
# ==========================================

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(8):
    password += random.choice(characters)

print("Password =", password)


# ==========================================
# 10. DICE ROLL
# ==========================================

dice = random.randint(1, 6)

print("Dice =", dice)


# ==========================================
# 11. COIN TOSS
# ==========================================

coin = random.choice(["Heads", "Tails"])

print(coin)


# ==========================================
# 12. RANDOM OTP
# ==========================================

otp = random.randint(100000, 999999)

print("OTP =", otp)


# ==========================================
# 13. RANDOM LOTTERY NUMBER
# ==========================================

lottery = random.randint(1000000, 9999999)

print("Lottery Number =", lottery)


# ==========================================
# 14. RANDOM EVEN NUMBER
# ==========================================

while True:
    number = random.randint(1, 100)

    if number % 2 == 0:
        print(number)
        break


# ==========================================
# 15. RANDOM ODD NUMBER
# ==========================================

while True:
    number = random.randint(1, 100)

    if number % 2 != 0:
        print(number)
        break


# ==========================================
# 16. GUESSING GAME
# ==========================================

secret = random.randint(1, 10)

guess = int(input("Guess a Number (1-10): "))

if guess == secret:
    print("Correct Guess")
else:
    print("Wrong Guess")
    print("Correct Number was", secret)


# ==========================================
# 17. GUESSING GAME WITH ATTEMPTS
# ==========================================

secret = random.randint(1, 20)

attempts = 5

while attempts > 0:

    guess = int(input("Guess Number: "))

    if guess == secret:
        print("Congratulations!")
        break

    elif guess > secret:
        print("Too High")

    else:
        print("Too Low")

    attempts -= 1
    print("Attempts Left =", attempts)

if attempts == 0:
    print("Game Over")
    print("Correct Number =", secret)


# ==========================================
# 18. GUESSING GAME WITH SCORE
# ==========================================

secret = random.randint(1, 20)

score = 100

while True:

    guess = int(input("Guess Number: "))

    if guess == secret:
        print("You Won")
        print("Final Score =", score)
        break

    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")

    score -= 10

    if score == 0:
        print("You Lost")
        print("Correct Number =", secret)
        break


# ==========================================
# 19. ROCK PAPER SCISSORS
# ==========================================

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

user = input("Enter Rock, Paper or Scissors: ")

print("Computer:", computer)

if user == computer:
    print("Match Draw")

elif user == "Rock" and computer == "Scissors":
    print("You Win")

elif user == "Paper" and computer == "Rock":
    print("You Win")

elif user == "Scissors" and computer == "Paper":
    print("You Win")

else:
    print("Computer Wins")


# ==========================================
# 20. RANDOM STUDENT
# ==========================================

students = ["Avinash", "Rahul", "Kiran", "Anil", "Ravi"]

print("Selected Student:", random.choice(students))


# ==========================================
# 21. RANDOM NUMBER LIST
# ==========================================

numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)


# ==========================================
# 22. SHUFFLE NUMBERS
# ==========================================

numbers = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(numbers)

print(numbers)


# ==========================================
# 23. RANDOM DECIMAL
# ==========================================

print(random.uniform(10, 50))


# ==========================================
# 24. RANDOM CHARACTER
# ==========================================

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(random.choice(letters))


# ==========================================
# 25. RANDOM COLOR
# ==========================================

colors = ["Red","Blue","Green","Black","White","Yellow"]

print(random.choice(colors))


# ==========================================
# 26. RANDOM MONTH
# ==========================================

months = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

print(random.choice(months))


# ==========================================
# 27. RANDOM DAY
# ==========================================

days = [
    "Monday","Tuesday","Wednesday",
    "Thursday","Friday","Saturday","Sunday"
]

print(random.choice(days))
