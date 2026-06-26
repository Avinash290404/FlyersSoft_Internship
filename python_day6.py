# ==========================================
# PYTHON DAY 6 - FUNCTIONS
# ==========================================


# ==========================================
# 1. SIMPLE FUNCTION
# ==========================================

def greet():
    print("Hello, Welcome to Python!")

greet()


# ==========================================
# 2. FUNCTION WITH PARAMETERS
# ==========================================

def greet_user(name):
    print("Hello", name)

greet_user("Avinash")
greet_user("Rahul")


# ==========================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ==========================================

def student(name, age):
    print("Name :", name)
    print("Age :", age)

student("Avinash", 22)


# ==========================================
# 4. FUNCTION WITH RETURN
# ==========================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# ==========================================
# 5. PRINT vs RETURN
# ==========================================

def sum_print(a, b):
    print(a + b)

def sum_return(a, b):
    return a + b

sum_print(10, 20)

result = sum_return(10, 20)
print(result)


# ==========================================
# 6. FUNCTION TO FIND SQUARE
# ==========================================

def square(number):
    return number * number

print(square(5))


# ==========================================
# 7. FUNCTION TO FIND CUBE
# ==========================================

def cube(number):
    return number ** 3

print(cube(4))


# ==========================================
# 8. FUNCTION TO CHECK EVEN OR ODD
# ==========================================

def even_odd(number):

    if number % 2 == 0:
        return "Even"

    else:
        return "Odd"

print(even_odd(20))
print(even_odd(17))


# ==========================================
# 9. FUNCTION TO FIND LARGEST NUMBER
# ==========================================

def largest(a, b):

    if a > b:
        return a

    else:
        return b

print(largest(100, 50))


# ==========================================
# 10. FUNCTION TO FIND LARGEST OF THREE
# ==========================================

def largest_three(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c

print(largest_three(10, 50, 30))


# ==========================================
# 11. FUNCTION TO FIND FACTORIAL
# ==========================================

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

print(factorial(5))


# ==========================================
# 12. FUNCTION TO FIND SUM
# ==========================================

def total(n):

    result = 0

    for i in range(1, n + 1):
        result += i

    return result

print(total(10))


# ==========================================
# 13. FUNCTION TO PRINT TABLE
# ==========================================

def table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

table(7)


# ==========================================
# 14. FUNCTION TO CHECK PRIME
# ==========================================

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(12))


# ==========================================
# 15. FUNCTION TO REVERSE STRING
# ==========================================

def reverse(text):

    return text[::-1]

print(reverse("Python"))


# ==========================================
# 16. FUNCTION TO COUNT VOWELS
# ==========================================

def vowels(text):

    count = 0

    for letter in text.lower():

        if letter in "aeiou":
            count += 1

    return count

print(vowels("Programming"))


# ==========================================
# 17. FUNCTION TO FIND MAXIMUM
# ==========================================

def maximum(numbers):

    return max(numbers)

print(maximum([10, 40, 20, 80, 30]))


# ==========================================
# 18. FUNCTION TO FIND MINIMUM
# ==========================================

def minimum(numbers):

    return min(numbers)

print(minimum([10, 40, 20, 80, 30]))


# ==========================================
# 19. FUNCTION-BASED CALCULATOR
# ==========================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    if b == 0:
        return "Division by Zero Not Allowed"

    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == 1:
    print(add(num1, num2))

elif choice == 2:
    print(subtract(num1, num2))

elif choice == 3:
    print(multiply(num1, num2))

elif choice == 4:
    print(divide(num1, num2))

else:
    print("Invalid Choice")


# ==========================================
# 20. FUNCTION WITH DEFAULT PARAMETER
# ==========================================

def greet(name="Guest"):
    print("Welcome", name)

greet()
greet("Avinash")


# ==========================================
# 21. FUNCTION RETURNING MULTIPLE VALUES
# ==========================================

def calculate(a, b):

    return a + b, a - b, a * b

add, sub, mul = calculate(20, 10)

print(add)
print(sub)
print(mul)


# ==========================================
# 22. FUNCTION CALLING ANOTHER FUNCTION
# ==========================================

def message():
    print("Welcome")

def display():
    message()
    print("Python Full Stack")

display()


# ==========================================
# 23. LOCAL VARIABLE
# ==========================================

def demo():

    x = 100

    print(x)

demo()


# ==========================================
# 24. GLOBAL VARIABLE
# ==========================================

x = 500

def test():
    print(x)

test()

print(x)


# ==========================================
# 25. MINI PROJECT - STUDENT RESULT
# ==========================================

def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "Fail"

marks = int(input("Enter Marks: "))

print("Grade =", grade(marks))

