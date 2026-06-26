
# PYTHON DAY 3 - DECISION MAKING & LOOPS

# 1. SIMPLE IF STATEMENT

age = 20

if age >= 18:
    print("You are eligible to vote")


# 2. IF ELSE STATEMENT

age = int(input("Enter Your Age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# 3. IF ELIF ELSE STATEMENT

marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

# 4. POSITIVE, NEGATIVE OR ZERO

number = int(input("Enter Number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# 5. EVEN OR ODD


number = int(input("Enter Number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 6. LARGEST OF TWO NUMBERS

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print(a, "is Greater")
else:
    print(b, "is Greater")


# ==========================================
# 7. LARGEST OF THREE NUMBERS
# ==========================================

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print(a, "is Largest")
elif b >= a and b >= c:
    print(b, "is Largest")
else:
    print(c, "is Largest")


# 8. FOR LOOP


for i in range(5):
    print(i)


# 9. RANGE FUNCTION

print(list(range(5)))

print(list(range(1, 6)))

print(list(range(2, 11, 2)))


# 10. FOR LOOP WITH RANGE

for i in range(1, 11):
    print(i)



# 11. PRINT EVEN NUMBERS

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 12. PRINT ODD NUMBERS


for i in range(1, 21):
    if i % 2 != 0:
        print(i)



# 13. COUNT EVEN NUMBERS


count = 0

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
        count += 1

print("Total Even Numbers =", count)


# ==========================================
# 14. LOOP THROUGH STRING
# ==========================================

name = "Python"

for letter in name:
    print(letter)


# ==========================================
# 15. LOOP THROUGH LIST
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# ==========================================
# 16. NESTED LOOP
# ==========================================

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# ==========================================
# 17. BREAK STATEMENT
# ==========================================

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# ==========================================
# 18. CONTINUE STATEMENT
# ==========================================

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# ==========================================
# 19. FOR ELSE
# ==========================================

for i in range(1, 6):
    print(i)
else:
    print("Loop Completed Successfully")


# ==========================================
# 20. BREAK WITH ELSE
# ==========================================

for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop Finished")


# ==========================================
# 21. MULTIPLICATION TABLE
# ==========================================

number = int(input("Enter Number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ==========================================
# 22. SUM OF FIRST N NUMBERS
# ==========================================

n = int(input("Enter Number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# ==========================================
# 23. FACTORIAL
# ==========================================

n = int(input("Enter Number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


# ==========================================
# 24. STAR PATTERN
# ==========================================

for i in range(1, 6):
    print("*" * i)


# ==========================================
# 25. INVERTED STAR PATTERN
# ==========================================

for i in range(5, 0, -1):
    print("*" * i)


# ==========================================
# 26. NUMBER PATTERN
# ==========================================

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==========================================
# 27. PYRAMID PATTERN
# ==========================================

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)


# ==========================================
# 28. WHILE LOOP
# ==========================================

i = 1

while i <= 5:
    print(i)
    i += 1


# ==========================================
# 29. NUMBER CLASSIFICATION PROGRAM
# ==========================================

number = int(input("Enter Number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif number < 0:
    if number % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")


# ==========================================
# 30. SEARCH USING BREAK
# ==========================================

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter Number to Search: "))

for num in numbers:
    if num == search:
        print("Number Found")
        break
else:
    print("Number Not Found")

