# students = ["Shahadat", "Rahim"]
# new_students = ["Karim", "Hasan", "Jamal"]

# students.extend(new_students)
# print(students)

# students = ["Shahadat", "Rahim", "Karim"]

# students.clear()

# print(students)
# print(len(students))

# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# fruits.remove("Banana")
# removed_fruit = fruits.pop(1)
# del fruits[1]

# print("Removed:", removed_fruit)
# print("Fruits:", fruits)
# print("Length:", len(fruits))

# students = ["Shahadat", "Rahim", "Karim", "Hasan", "Rahim"]
# print(students.count("Shahadat"))

# numbers = [10, 20, 30, 40]

# for number in numbers:
#     if number >= 25:
#         print(number)

# students = ["Shahadat", "Rahim", "Karim"]

# for number, student in enumerate(students, start=1):
#     print(number, "→", student)

# numbers = [40, 10, 30, 20]

# new_numbers = numbers.copy()

# new_numbers.sort()

# print("Original:", numbers)
# print("Copy:", new_numbers)

# students = ["Jamal", "Shahadat", "Karim", "Hasan", "Rahim"]

# sorted_students = sorted(students)

# print("Original:", students)
# print("Sorted:", sorted_students)

# students = ["Shahadat", "Rahim", "Karim", "Hasan"]
# for number, student in enumerate(students, start=1):
#     print(number,".", student)

# students = [
#     ["Shahadat", 85],
#     ["Rahim", 72],
#     ["Karim", 90],
#     ["Hasan", 65]
# ]

# students[3][1] = 75
# print(students)

# students = [
#     ["Shahadat", 85],
#     ["Rahim", 72],
#     ["Karim", 90]
# ]

# for student in students:
#     print(student[0], "→", student[1])

# students = [
#     ["Shahadat", 85],
#     ["Rahim", 45],
#     ["Karim", 72],
#     ["Hasan", 35]
# ]

# for student in students:
#     if student[1] >= 50:
#         print(student[0], "→", student[1], "→", "PASS")
#     else:
#         print(student[0], "→", student[1], "→", "FAIL")

# students = [
#     ["Shahadat", 85],
#     ["Rahim", 72],
#     ["Karim", 90]
# ]

# print(students[2][0])

# fruits = ["Apple", "Banana", "Mango", "Orange"]

# print(fruits[3])

# students = ["Shahadat", "Rahim", "Karim", "Hasan"]

# students.remove("Hasan")
# print(students)

# numbers = [40, 10, 30, 20]

# new_numbers = sorted(numbers)

# print("Numbers:", numbers)
# print("New Numbers:", new_numbers)

# students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

# del students[1]

# print(students[3])


#Final Comprehensive Challenge
# students = [
#     ["Shahadat", 85],
#     ["Rahim", 45],
#     ["Karim", 72],
#     ["Hasan", 35],
#     ["Jamal", 90]
# ]

# search = input("Enter Student Name: ")

# for student in students:
#     if search.lower() == student[0].lower():
#         print("Checking: ", student[0])

#         if student[1] >= 50:
#             print(student[0], "→", student[1], "→", "PASS")

#         else:
#             student[1] += 10
#             if student[1] >= 50:
#                 print(student[0], "→", student[1], "→", "PASS")
#             else:
#                 print(student[0], "→", student[1], "→", "FAIL")    
#         print("Student Found")
#         break
# else:
#     print("Student Not Found")         

#Final Comprehensive Challenge 2
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
            student[1] += 10
            if student[1] >= 50:
                print(student[0], "→", student[1], "→", "PASS")
            else:
                print(student[0], "→", student[1], "→", "FAIL")
        print("Student Found")
        break    
else:
    print("Student Not Found")                        
