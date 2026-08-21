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

#Comprehensive Practice - Challenge 1

students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

del students[1]
print(students[3])

#Comprehensive Practice - Challenge 2
students = ["Shahadat", "Rahim", "Karim", "Rahim", "Hasan"]

removed_student = students.pop(1)

print("Removed:", removed_student)
print("Rahim Count:", students.count("Rahim"))
print("Karim Found:", "Karim" in students)
print("Students:", students)

#Comprehensive Practice - Challenge 3
numbers = [40, 10, 50, 20, 30]

new_numbers = numbers.copy()

numbers.sort(reverse=True)

sorted_numbers = sorted(new_numbers)

print("Original:", numbers)
print("Copy:", new_numbers)
print("Sorted Copy:", sorted_numbers)

#Comprehensive Practice — Challenge 4
students = [
    ["Shahadat", 85],
    ["Rahim", 45],
    ["Karim", 72],
    ["Hasan", 35],
    ["Jamal", 90]
]

for student in students:
    if student[1] < 50:
        student[1] += 10
    print(student)    

#Comprehensive Practice: Challenge 5
students = [
    ["Shahadat", 85],
    ["Rahim", 45],
    ["Karim", 72],
    ["Hasan", 35],
    ["Jamal", 90]
]
new_students = students.copy()
new_students.sort()

for new_student in new_students:
    if new_student[1] < 50:
        new_student[1] += 10
print("Original: ", students)
print("Processed: ", new_students)

#Comprehensive Practice — Challenge 6        
students = [
    ["Shahadat", 85],
    ["Rahim", 45],
    ["Karim", 72],
    ["Hasan", 35],
    ["Jamal", 90]
]
search = ""

search = input("Enter Student Name: ")

for student in students:
  print("Checking: ", student[0])

  if search.lower() == student[0].lower():
    if student[1] >= 50:
      print(student[0], "→", student[1], "→", "PASS")
    else:
      student[1] += 10
      print(student[0], "→", student[1], "→", "PASS") 
    break
else:
  print("Student Not Found") 


#Comprehensive Practice — Challenge 7
students = [
    ["Shahadat", 85],
    ["Rahim", 45],
    ["Karim", 72],
    ["Hasan", 35],
    ["Jamal", 90]
]

for student in students:
    if student[1] >= 50:
        print(student[0], "→", student[1], "→", "PASS")
    else:
        print(student[0], "→", student[1], "→", "FAIL")  
        student[1] += 10
print(students)   

#Comprehensive Practice: Challenge 7 — Student Search + Case-Insensitive Search

students = [
    ["Shahadat", 85],
    ["Rahim", 45],
    ["Karim", 72],
    ["Hasan", 35],
    ["Jamal", 90]
]

search = input("Enter Student Name: ")

for student in students:
    print("Checking: ", student[0])

    if search.lower() == student[0].lower():
        if student[1] >= 50:
            print(student[0], "→", student[1], "→", "PASS")
        else:
            print(student[0], "→", student[1], "→", "FAIL")
        print("Student Found")
        break
else:
    print("Student Not Found")  

#Challenge 8 — List Processing 
numbers = [50, 15, 80, 25, 100, 40] 
 
for number in numbers:
    if number < 50:
        number += 10
    print("Checking: ",number)

#Challenge 9 — Product List Processing
products = ["Laptop", "Phone", "Tablet", "Watch", "Camera"]

products.append("Headphone")
products.remove("Tablet")
products.sort()
print("Keyboard Found:","Keyboard" in products)
print(products)

#Comprehensive Challenge 10
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

new_students = students.copy()
removed_student = new_students.pop(1)
sorted_students = sorted(new_students)

print("Removed: ", removed_student)
print("Original: ", students)
print("Sorted Copy: ", sorted_students)

#Comprehensive Practice — Challenge 11
students = ["Shahadat", "Rahim", "Karim", "Rahim", "Hasan"]

new_students = students.copy()
print("Rahim Count: ",new_students.count("Rahim"))
print("Karim Found: ", "Karim" in new_students)
print("Hasan Index: ", new_students.index("Hasan"))
print("Original: ", students)
print("Copy: ", new_students)

#Comprehensive Practice — Challenge 12
products = ["Laptop", "Phone", "Tablet", "Watch", "Phone"]

new_products = products.copy()
new_products.remove("Phone")

print("Phone Count: ", products.count("Phone"))
print("Tablet Found: ", "Tablet" in products)
print("Watch Index: ", products.index("Watch"))
print("Camera Found: ", "Camera" in products)
print("Original: ", products)
print("Copy: ", new_products)

#Comprehensive Practice — Challenge 13
products = ["Laptop", "Phone", "Tablet", "Watch"]

products.append("Camera")
products.insert(1, "Keyboard")
products.remove("Tablet")
removed_product = products.pop(2)
products.sort()

print("Removed: ", removed_product)
print("Phone Found: ", "Phone" in products)
print("Phone Count: ", products.count("Phone"))
print("Products: ", products)