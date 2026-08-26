students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

print(students[1]) #Positive Index

print(students[-5]) #Negative Index

#List-এর Item পরিবর্তন করা
students = ["Shahadat", "Rahim", "Karim"]
students[1] = "Hasan"
print(students[1])

students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

students[1] = "Rafi"
students[4] = "Sakib"
students[2] = "Arif"
print(students)
print(students[0], students[1], students[2], students[3], students[4])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

#List-এর মধ্যে Item যোগ করা
#append()
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits.append("Grapes")
print(fruits)

#insert()
fruits = ["Apple", "Banana", "Mango", "Grapes"]
fruits.insert(2, "Orange")
print(fruits)

#extend()
students = ["Shahadat", "Rahim"]
new_students = ["Karim", "Hasan", "Jamal"]
students.extend(new_students)
print(students)

#remove()
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
fruits.remove("Mango")
fruits.remove("Grapes")
print(fruits)

#pop()
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
removed_student = students.pop(2)
print("Removed:", removed_student)
print("Updated List:", students)

#del
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
del students[2]
del students[3]
print(students)

#clear()
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
fruits.clear()
print(fruits)
fruits.append("Pineapple")
print(fruits)

#len()
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
print(len(students))
print(len(students[-1]))
students.append("Sakib")
print(len(students))
students.clear()
print(len(students))

#in এবং not in
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Apple" in fruits)
print("Pineapple" not in fruits)

fruits = ["Apple", "Banana", "Mango"]
if "Mango" in fruits:
    print("Mango is Available")

#in + if দিয়ে List Search
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
search = input("Enter Student Name: ")

if search in students:
    print("Student Found")
else:
    print("Student Not Found")    

#count() method
students = ["Shahadat", "Rahim", "Shahadat", "Karim", "Rahim", "Shahadat"]
print(students.count("Karim"))

#index() Method
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Rahim"]
if "Sakib" in students:
    print(students.index("Hasan"))

#List-এর Loop
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)

numbers = [10, 20, 30, 40, 50]
for number in numbers:
    print("Number: ", number)


numbers = [10, 25, 30, 45, 50, 65]
for number in numbers:
    if number > 30:
      print("Number: ", number)

#enumerate()
students = ["Shahadat", "Rahim", "Karim", "Hasan"]

for number, student in enumerate(students, start=1):
    print(number, "→", student)

#enumerate() + if
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

for number, student in enumerate(students, start=1):
    if student == "Hasan":
        print(number, "→", student)

numbers = [5, 10, 15, 20]

for number in numbers:
    print(number + 5)

students = ["Shahadat", "Rahim", "Karim"]

new_students = students.copy()

new_students.append("Hasan")

print(students)
print(new_students)

students = ["Shahadat", "Rahim", "Karim"]
new_students = students
new_students.remove("Rahim")
print("Students: ", students)
print("New Students: ", new_students)

students = ["Shahadat", "Rahim", "Karim"]

new_students = students.copy()

students.append("Hasan")
new_students.remove("Rahim")

print("Students: ", students)
print("New Students: ", new_students)

#sort() #Ascending Order
numbers = [80, 20, 50, 10, 40, 30]
numbers.sort()
print(numbers)

#Descending Order
numbers = [80, 20, 50, 10, 40, 30]
numbers.sort(reverse=True)
print(numbers)

#sort() দিয়ে String সাজানো
students = ["Jamal", "Shahadat", "Karim", "Hasan", "Rahim"]
students.sort()
print(students)

students = ["Jamal", "Shahadat", "Karim", "Hasan", "Rahim"]
students.sort(reverse=True)
print(students)

#sorted()
students = ["Jamal", "Shahadat", "Karim", "Hasan", "Rahim"]
new_students = sorted(students)
print("Original: ", students)
print("Sorted: ", new_students)

#sorted() + reverse=True
numbers = [50, 10, 40, 20, 30]
new_numbers = sorted(numbers, reverse=True)
print(new_numbers)
print(numbers)

students = ["Jamal", "Shahadat", "Karim", "Hasan", "Rahim"]
new_students = sorted(students, reverse=True)
print("Original:", students)
print("Sorted:", new_students)

students = ["Shahadat", "Rahim", "Karim"]
students.append("Hasan")
students.insert(1, "Jamal")
students.remove("Karim")
print(students)

students = ["Shahadat", "Rahim", "Karim", "Hasan"]
removed_student = students.pop(2)
students.append("Jamal")
print("Removed:", removed_student)
print("Students:", students)

numbers = [50, 20, 40, 10, 30]
numbers.append(60)
numbers.remove(20)
numbers.sort()
removed_number = numbers.pop(2)
print("Removed:", removed_number)
print("Numbers:", numbers)

#Nested Lists
students = [
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90]
]
print(students[1][0])

#Nested List + মান পরিবর্তন
students = [
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90]
]
students[1][1] = 80
print(students)

#Nested List-এর Loop
students = [
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90],
    ["Hasan", 65]
]

for student in students:
    print(student[0], "→", student[1])

#Nested List + if
students = [
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90],
    ["Hasan", 65]
]
for student in students:
    if student[1] >= 50:
        print(student[0], "→", student[1], "→", "PASS")
    else:
        print(student[0], "→", student[1], "→", "FAIL")    

#Nested List-এ Data Update
students = [
    ["Shahadat", 85],
    ["Rahim", 72],
    ["Karim", 90],
    ["Hasan", 65]
]
students[3][1] = 75
print(students)

#List Debugging
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[3])

students = ["Shahadat", "Rahim", "Karim", "Hasan"]
students.remove("Hasan")
print(students)

students = ["Shahadat", "Rahim", "Karim", "Hasan"]
removed_student = students.pop(3)
print(removed_student)
print(students)

numbers = [50, 10, 30, 20]
numbers.sort()
print("Numbers:", numbers)

