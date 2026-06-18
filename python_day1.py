# ==========================================
# PYTHON DAY 1 - COMPLETE BASICS PRACTICE
# ==========================================


# ==========================================
# 1. HELLO WORLD
# ==========================================

print("Hello World")


# ==========================================
# 2. COMMENTS
# ==========================================

# This is a single-line comment

print("Python Basics")


# ==========================================
# 3. VARIABLES
# ==========================================

x = 10
print(x)

x = 20
print(x)

name = "Avinash"
age = 22
height = 5.6

print(name)
print(age)
print(height)


# ==========================================
# 4. MULTIPLE VARIABLE ASSIGNMENT
# ==========================================

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)


# ==========================================
# 5. DATA TYPES
# ==========================================

integer_num = 100
float_num = 10.5
string_value = "Python"
boolean_value = True

print(type(integer_num))
print(type(float_num))
print(type(string_value))
print(type(boolean_value))


# ==========================================
# 6. PRINT FUNCTION
# ==========================================

print("Hello World")

print("Python", "Java", "C++")

print("Python", "Java", "C++", sep="-")

print("Hello", end=" ")
print("World")


# ==========================================
# 7. INPUT FUNCTION
# ==========================================

name = input("Enter your name: ")
print("Welcome", name)


# ==========================================
# 8. TYPE CONVERSION
# ==========================================

age = int(input("Enter your age: "))
print(age)

salary = float(input("Enter your salary: "))
print(salary)

number = 100
text = str(number)

print(text)
print(type(text))


# ==========================================
# 9. ADDITION USING INPUT
# ==========================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)


# ==========================================
# 10. ARITHMETIC OPERATORS
# ==========================================

a = 10
b = 3

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)


# ==========================================
# 11. COMPARISON OPERATORS
# ==========================================

print(10 > 5)
print(10 < 5)
print(10 == 5)
print(10 != 5)
print(10 >= 5)
print(10 <= 5)


# ==========================================
# 12. LOGICAL OPERATORS
# ==========================================

print(True and False)
print(True or False)
print(not True)


# ==========================================
# 13. STRINGS
# ==========================================

name = "YouTube"

print(name)


# ==========================================
# 14. STRING INDEXING
# ==========================================

name = "YouTube"

print(name[0])
print(name[1])
print(name[2])
print(name[3])


# ==========================================
# 15. NEGATIVE INDEXING
# ==========================================

name = "YouTube"

print(name[-1])
print(name[-2])
print(name[-3])


# ==========================================
# 16. STRING SLICING
# ==========================================

name = "YouTube"

print(name[0:3])
print(name[3:7])

print(name[:3])
print(name[3:])
print(name[:])


# ==========================================
# 17. STRING LENGTH
# ==========================================

name = "Python"

print(len(name))


# ==========================================
# 18. STRING METHODS
# ==========================================

text = "python full stack"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.replace("python", "Java"))

print(text.find("full"))

print(text.count("o"))


# ==========================================
# 19. STRING IMMUTABILITY
# ==========================================

name = "Python"

new_name = "J" + name[1:]

print(new_name)


# ==========================================
# 20. ESCAPE CHARACTERS
# ==========================================

print("Hello\nWorld")

print("Hello\tWorld")

print("I am \"Avinash\"")

print("Python\\Java")


# ==========================================
# 21. BUILT-IN FUNCTIONS
# ==========================================

print(abs(-10))

print(max(10, 20, 30))

print(min(10, 20, 30))

print(round(3.56))

print(pow(2, 3))


# ==========================================
# 22. AREA OF RECTANGLE
# ==========================================

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width

print("Area =", area)


# ==========================================
# 23. SWAP TWO NUMBERS
# ==========================================

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)


# ==========================================
# 24. UNDERSCORE VARIABLE (INTERACTIVE SHELL)
# ==========================================

# Example in Python Shell

# >>> 10 + 5
# 15
#
# >>> _ * 2
# 30


# ==========================================
# 25. PRACTICE PROGRAM - USER DETAILS
# ==========================================

name = input("Enter Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")

print("Name :", name)
print("Age  :", age)
print("City :", city)


# ==========================================
# 26. PRACTICE PROGRAM - SIMPLE INTEREST
# ==========================================

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# ==========================================
# 27. PRACTICE PROGRAM - TEMPERATURE
# ==========================================

celsius = float(input("Enter Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Fahrenheit =", fahrenheit)


# ==========================================
# 28. PRACTICE PROGRAM - SQUARE AND CUBE
# ==========================================

number = int(input("Enter Number: "))

print("Square =", number ** 2)
print("Cube =", number ** 3)


# ==========================================
# END OF PYTHON DAY 1
# ==========================================
