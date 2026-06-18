# ==========================================
# PYTHON DAY 2 - DATA TYPES & OPERATORS
# ==========================================


# ==========================================
# 1. NONE DATA TYPE
# ==========================================

value = None

print(value)
print(type(value))


# ==========================================
# 2. INTEGER (int)
# ==========================================

age = 22
marks = 100

print(age)
print(type(age))


# ==========================================
# 3. FLOAT
# ==========================================

height = 5.6
price = 99.99

print(height)
print(type(height))


# ==========================================
# 4. COMPLEX NUMBER
# ==========================================

complex_num = 6 + 9j

print(complex_num)
print(type(complex_num))


# ==========================================
# 5. BOOLEAN
# ==========================================

is_student = True
is_employed = False

print(is_student)
print(is_employed)

print(int(True))
print(int(False))

print(type(is_student))


# ==========================================
# 6. LIST
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))

print(fruits[0])
print(fruits[1])

fruits.append("Orange")

print(fruits)


# ==========================================
# 7. TUPLE
# ==========================================

colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))

print(colors[0])


# ==========================================
# 8. SET
# ==========================================

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

numbers.add(50)

print(numbers)


# ==========================================
# 9. RANGE
# ==========================================

numbers = range(1, 11)

print(numbers)

print(list(numbers))


# ==========================================
# 10. DICTIONARY
# ==========================================

student = {
    "name": "Avinash",
    "age": 22,
    "city": "Hyderabad"
}

print(student)
print(type(student))

print(student["name"])
print(student["age"])

student["course"] = "Python Full Stack"

print(student)


# ==========================================
# 11. ARITHMETIC OPERATORS
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
# 12. ASSIGNMENT OPERATORS
# ==========================================

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)


# ==========================================
# 13. MULTIPLE ASSIGNMENT
# ==========================================

a, b = 5, 6

print(a)
print(b)


# ==========================================
# 14. RELATIONAL OPERATORS
# ==========================================

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ==========================================
# 15. LOGICAL AND
# ==========================================

age = 22
has_id = True

print(age >= 18 and has_id)


# ==========================================
# 16. LOGICAL OR
# ==========================================

has_aadhar = False
has_passport = True

print(has_aadhar or has_passport)


# ==========================================
# 17. LOGICAL NOT
# ==========================================

is_raining = True

print(not is_raining)


# ==========================================
# 18. TYPE CHECKING
# ==========================================

num = 100

print(type(num))
print(isinstance(num, int))


# ==========================================
# 19. PRACTICE - CALCULATOR
# ==========================================

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)


# ==========================================
# 20. PRACTICE - BOOLEAN CHECK
# ==========================================

age = int(input("Enter Your Age: "))

print(age >= 18)


# ==========================================
# 21. PRACTICE - DICTIONARY
# ==========================================

employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

print(employee)

print(employee["name"])


# ==========================================
# 22. PRACTICE - LIST OPERATIONS
# ==========================================

languages = ["Python", "Java", "C++"]

print(languages)

languages.append("JavaScript")

print(languages)

languages.remove("Java")

print(languages)


# ==========================================
# 23. PRACTICE - SET OPERATIONS
# ==========================================

numbers = {1, 2, 3, 4}

numbers.add(5)

print(numbers)

numbers.remove(2)

print(numbers)


# ==========================================
# 24. PRACTICE - RANGE
# ==========================================

for i in range(1, 11):
    print(i)


# ==========================================
# 25. MINI PROJECT - STUDENT DATA
# ==========================================

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

student = {
    "Name": name,
    "Age": age,
    "Course": course
}

print(student)

