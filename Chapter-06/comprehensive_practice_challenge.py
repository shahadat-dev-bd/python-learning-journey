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