fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print(fruits[-5:-1])

numbers = (10, 20, 30, 40, 50)
print(numbers[4])

colors = ("Red", "Green", "Blue", "Yellow", "Black")

print(colors[1:4])
print(colors[-4:-1])
print(colors[0])
print(colors[-1])

students = ("Shahadat", "Rahim", "Karim", "Hasan")
print(students[3])

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[-4:-1])

students = ("Shahadat", "Rahim", "Karim", "Rahim", "Hasan")
print(students.index("Jamal"))

numbers = (10, 20, 30, 40, 50)
print(len(numbers))

fruits = ("Apple", "Banana", "Mango", "Orange")
print("Mango" in fruits)
print("Grapes" in fruits)
print("Grapes" not in fruits)
print("Mango" not in fruits)

numbers = (40, 10, 30, 20)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = (40, 10, 30, 20)

new_numbers = sorted(numbers)

print(type(new_numbers))
print(new_numbers)

fruits = ("Apple", "Banana", "Mango")
new_fruits = list(fruits)
new_fruits = tuple(fruits)
print(new_fruits)

student = ("Shahadat", 33, 5.8)
print(type(student))

#Tuple Loop
fruits = ("Apple", "Banana", "Mango", "Orange")
for fruit in fruits:
    print(fruit)

#enumerate()
students = ("Shahadat", "Rahim", "Karim")
for number, student in enumerate(students):
    print(number, "→", student)

#enumerate(start=1)
students = ("Shahadat", "Rahim", "Karim")
for number, student in enumerate(students, start=1):
    print(number, "→", student)  

#Basic Tuple Unpacking
student = ("Shahadat", 33, 85)

name, age, marks = student

print(name)
print(age)
print(marks)

#Unpacking Error
numbers = (10, 20, 30)
a, b = numbers

#Extended Unpacking
numbers = (10, 20, 30, 40, 50)
first, *rest = numbers
print(first)
print(rest)

#Extended Unpacking
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

#Variable Swap
a = 10
b = 20

a, b = b, a

print(a)
print(b)

#Three Variable Assignment
a = 10
b = 20
c = 30

a, b, c = c, a, b

print(a)
print(b)
print(c)

#Code Writing
students = ("Shahadat", "Rahim", "Karim", "Hasan")

for index, student in enumerate(students, start=1):
    print(index,student)

#Nested Tuple
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90),
    ("Hasan", 65)
)
print(students[3][1])

#Nested Tuple Loop
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90),
    ("Hasan", 65)
)

for name, marks in students:
    print(name, "→", marks)

#Nested Tuple Update
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

students[1][1] = 80
print(students)

students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

students[1] = ("Hasan", 80)
print(students)

#Tuple-এর ভিতরে List
students = (
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90]
)

students[1][1] = 80
print(students)

#Debugging
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

print(students[2][0])

#Nested Tuple + Unpacking
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

for student in students:
    name, marks = student
    print(name, marks)

#Concept Challenge
A = (
    ("Shahadat", 85),
    ("Rahim", 72)
)

B = (
    ["Shahadat", 85],
    ["Rahim", 72]
)

B[0][1] = 90
print(B)

# A[0][1] = 90 # it will be TypeError
# print(A)

#IndexError
fruits = ("Apple", "Banana", "Mango")
print(fruits[2])

#TypeError
marks = (80, 75, 90)
marks[1] = 85

#ValueError
students = ("Shahadat", "Rahim", "Karim")
print(students.index("Hasan"))
if "Hasan" in students: #correct code
    print(students.index("Hasan"))
else:
    print("Hasan Not Found")

#Unpacking Debugging
student = ("Shahadat", 33, 85)
name, age, mark = student
print(name, age, mark)

#Nested Tuple Debugging
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)
print(students[2][0])

#sorted() Debugging
numbers = (40, 10, 30, 20)
new_numbers = sorted(numbers)
new_numbers[0] = 5
print(numbers)
print(new_numbers)

#count() বনাম index()
students = ("Rahim", "Karim", "Rahim", "Hasan")
print(students.index("Rahim"))

#Practical Debugging
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

search = input("Enter Student Name: ")

for name, marks in students:
    if name.lower() == search.lower():
        print(name, "→", marks)
        break
else:
    print("Student Not Found")


#Final Debugging Challenge
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72)
)

students[1][1] = 50
print(students)

#================================
#================================
#Final Practical Challenge
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

total_marks = 0

for name, marks in students:
    total_marks += marks

average_marks = total_marks / len(students)
print("Average Marks:", average_marks)

search = input("Enter Student Name: ")
students = sorted(students, key=lambda student: student[1], reverse=True)

for rank, (name, marks) in enumerate(students, start=1):
    if name.lower() == search.lower():
        print("Student Found")
        if marks >= 50:
            print(name, marks, "PASS")
        else:
            print(name, marks, "FAIL")
        print("Rank: ", rank)
        break

else:
    print("Student Not Found")           
