student = ("Shahadat", 33, 5.8)

name, age, height = student

print(name)
print(age)
print(height)

numbers = (10, 20, 30)

a, b, c = numbers

print(b)

student = ("Rahim", 72)

name, marks = student

print(name)
print(marks)

fruits = ("Apple", "Banana", "Mango")

first, second, third = fruits

print(second)

numbers = (10, 20, 30)

a, b = numbers

#Tuple Unpacking-এর Advanced ব্যবহার
numbers = (10, 20, 30, 40, 50)

first, *rest = numbers

print(first)
print(rest)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

first, second, *rest = numbers

print(first)
print(second)
print(rest)

def calculate(a, b):
    total = a + b
    multiply = a * b

    return total, multiply

result = calculate(10, 20)
print(result)

def calculate(a, b):
    total = a + b
    multiply = a * b

    return total, multiply

total, multiply = calculate(10, 5)

print("Total:", total)
print("Multiply:", multiply)


def get_info():
    return "Python", 3.14

result = get_info()

print(result)

def get_info():
    return "Python", 3.14

name, version = get_info()

print(name)
print(version)

def calculate(a, b):
    return a + b, a - b

result = calculate(20, 5)

print(result)

def calculate(a, b):
    return a + b, a - b

total, difference = calculate(20, 5)

print(total)
print(difference)

marks = (80, 75, 90)

marks[1] = 85

colors = ["Red", "Green", "Blue"]
colors[1] = "Yellow"
print(colors)

colors = ("Red", "Green", "Blue")
colors[1] = "Yellow"
print(colors)

a, b = (10, 20)

print(a)
print(b)

x = 50
y = 100

x, y = y, x

print(x)
print(y)

a = 10
b = 20
c = 30

a, b, c = c, a, b

print(a)
print(b)
print(c)

name, age = "Shahadat", 33

print(name)
print(age)

first = "Shahadat"
second = "Rahim"

first, second = second, first
print(first)
print(second)

students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90),
    ("Hasan", 65)
)
students[0] = ("Hasan", 80)

numbers = (40, 10, 30, 20)
new_numbers = sorted(numbers)
print(type(new_numbers))
print(new_numbers)

fruits = ("Apple", "Banana", "Mango")
print("Grapes" in fruits)