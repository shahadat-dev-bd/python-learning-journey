# student = ("Shahadat", 33, 5.8)

# name, age, height = student

# print(name)
# print(age)
# print(height)

# numbers = (10, 20, 30)

# a, b, c = numbers

# print(b)

# student = ("Rahim", 72)

# name, marks = student

# print(name)
# print(marks)

# fruits = ("Apple", "Banana", "Mango")

# first, second, third = fruits

# print(second)

# numbers = (10, 20, 30)

# a, b = numbers

#Tuple Unpacking-এর Advanced ব্যবহার
# numbers = (10, 20, 30, 40, 50)

# first, *rest = numbers

# print(first)
# print(rest)

# first, *middle, last = numbers

# print(first)
# print(middle)
# print(last)

# first, second, *rest = numbers

# print(first)
# print(second)
# print(rest)

# def calculate(a, b):
#     total = a + b
#     multiply = a * b

#     return total, multiply

# result = calculate(10, 20)
# print(result)

# def calculate(a, b):
#     total = a + b
#     multiply = a * b

#     return total, multiply

# total, multiply = calculate(10, 5)

# print("Total:", total)
# print("Multiply:", multiply)


# def get_info():
#     return "Python", 3.14

# result = get_info()

# print(result)

# def get_info():
#     return "Python", 3.14

# name, version = get_info()

# print(name)
# print(version)

# def calculate(a, b):
#     return a + b, a - b

# result = calculate(20, 5)

# print(result)

# def calculate(a, b):
#     return a + b, a - b

# total, difference = calculate(20, 5)

# print(total)
# print(difference)

# marks = (80, 75, 90)

# marks[1] = 85

# colors = ["Red", "Green", "Blue"]
# colors[1] = "Yellow"
# print(colors)

# colors = ("Red", "Green", "Blue")
# colors[1] = "Yellow"
# print(colors)

# a, b = (10, 20)

# print(a)
# print(b)

# x = 50
# y = 100

# x, y = y, x

# print(x)
# print(y)

# a = 10
# b = 20
# c = 30

# a, b, c = c, a, b

# print(a)
# print(b)
# print(c)

# name, age = "Shahadat", 33

# print(name)
# print(age)

# first = "Shahadat"
# second = "Rahim"

# first, second = second, first
# print(first)
# print(second)

# students = (
#     ("Shahadat", 85),
#     ("Rahim", 72),
#     ("Karim", 90),
#     ("Hasan", 65)
# )
# students[0] = ("Hasan", 80)

# numbers = (40, 10, 30, 20)
# new_numbers = sorted(numbers)
# print(type(new_numbers))
# print(new_numbers)

# fruits = ("Apple", "Banana", "Mango")
# print("Grapes" in fruits)

#🐛Small Debugging Challenge
#Challenge 1
# fruits = ["Apple", "Banana", "Mango"]
# fruits[1] = "Orange"
# print(fruits)

#Challenge 2
# numbers = (10, 20, 30, 40)
# print(numbers[3])

# Challenge 3
# fruits = ("Apple", "Banana", "Mango")
# if "Grapes" in fruits:
#     print(fruits.index("Grapes"))
# else:
#     print("Grapes Not Found")    

#Challenge ৪ 🔥
# numbers = (40, 10, 30, 20)
# new_numbers = sorted(numbers)
# new_numbers.append(50)
# print(new_numbers)

# #Challenge ৫ — Final Small Challenge 🧠
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 72),
#     ("Karim", 90)
# )

# search = input("Enter Student Name: ")
# for student in students:
#     if student[0].lower() == search.lower():
#         print(student)
#         break
# else:
#     print("Student Not Found")


#Practical 1 — Student Information
# student = ("Shahadat", 33, 85)
# name, age, marks = student
# print("Name:", name)
# print("Age:", age)
# print("Marks:", marks)

#Practical 2 — Student Marks
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 72),
#     ("Karim", 90)
# )

# print(students[1][0], "→", students[1][1])

#Practical 3
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 72),
#     ("Karim", 90),
#     ("Hasan", 65)
# )

# for name, marks in students:
#     print(name, "→", marks)

#Practical 4  
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35)
# )  

# for name, marks in students:
#     if marks >= 50:
#         print(name, "→", marks, "→", "PASS")
#     else:
#         print(name, "→", marks, "→", "FAIL")    

#Practical 5
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35)
# )

# search = input("Enter Student Name: ")
# for student in students:
#     if student[0].lower() == search.lower():
#         print(student[0], "→", student[1])
#         print("Student Found")
#         break
# else:
#     print("Student Not Found")

#Practical 6
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35)
# )
# total_marks = 0

# for name, marks in students:
#     total_marks += marks

# average_marks = total_marks/len(students)

# print("Total Marks:", total_marks)
# print("Students: ", len(students))
# print("Average Marks:", average_marks)

#Practical 7
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )
# highest_name, highest_marks = students[0]

# for name, marks in students[1:]:
#     if marks > highest_marks:
        
#         highest_name = name
#         highest_marks = marks
# print("Highest Marks: ", highest_name, "→", highest_marks)    

#Practical 8
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# lowest_name, lowest_marks = students[0]

# for name, marks in students[1:]:
#     if marks < lowest_marks:
        
#         lowest_name = name
#         lowest_marks = marks
# print("Lowest Marks: ", lowest_name, "→", lowest_marks)   

#Practical 9
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )
# pass_count = 0

# for name, marks in students:
#     if marks >= 50:
#         pass_count += 1
                
# print("Pass Students: ", pass_count)        

#Practical 10
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )
# total_marks = 0

# for name, marks in students:
#     total_marks += marks
# average_marks = total_marks/len(students)
# print("Average Marks:", average_marks)

# for name, marks in students:
#     if marks > average_marks:
#         print(name, "→", marks)


#Practical 11
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )
# pass_count = 0
# fail_count = 0

# for name, marks in students:
#     if marks >= 50:
#         print(name, "→", marks, "→", "PASS")
#     else:
#         print(name, "→", marks, "→", "FAIL")

# for name, marks in students:
#     if marks >= 50:
#         pass_count += 1
#     else:
#         fail_count += 1
# print()        
# print("Pass Students: ", pass_count)
# print("Fail Students: ", fail_count)

#Practical 12
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# search = input("Enter Student Name: ")

# for name, marks in students:
#     if name.lower() == search.lower():
#         if marks >= 50:
#             print(name, "→", marks, "→", "PASS")
#         else:
#             print(name, "→", marks, "→", "FAIL")   
#         break
# else:
#     print("Student Not Found")  

#Practical 13
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# top_name, top_marks = students[0]

# for name, marks in students[1:]:
#     if marks > top_marks:
#         top_name = name
#         top_marks = marks
# print("Top Student: ", top_name, "→", top_marks)

#Practical 14
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# lowest_name, lowest_marks = students[0]

# for name, marks in students[1:]:
#     if marks < lowest_marks:
#         lowest_name = name
#         lowest_marks = marks
# print("Lowest Student: ", lowest_name, "→", lowest_marks)

#Practical 15
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# top_name, top_marks = students[0]
# pass_count = 0

# for name, marks in students:
#     if marks >= 50:
#         pass_count += 1
# print("Pass Students: ", pass_count)

# for name, marks in students:
#     if marks > top_marks:
#         top_name = name
#         top_marks = marks
# print("Top Student: ", top_name, "→", top_marks)

#Practical 16
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# total_marks = 0
# average_count = 0

# for name, marks in students:
#     total_marks += marks
# average_marks = total_marks/len(students)
# print("Average Marks: ", average_marks) 

# for name, marks in students:
#     if marks > average_marks:
#         average_count += 1
# print("Above Average Students: ", average_count)

#Practical 17
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# top_name, top_marks = students[0]

# for name, marks in students:
#     if marks >= 50:   
#         print(name, marks)

# for name, marks in students:
#     if marks >= 50:
#         if marks > top_marks:
#             top_name = name
#             top_marks = marks
# print("Top Student: ", top_name, "→", top_marks)

#Practical 18
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# students= sorted(students, key=lambda student: student[1], reverse=True)
# for name, marks in students:
#     print(name, "→", marks, "→", "PASS")


#Practical 19
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# students= sorted(students, key=lambda student: student[1], reverse=True)
# for name, marks in students:
#     if marks >= 50:
#         print("Rank:",students.index((name, marks))+1, name, "→", marks, "→", "PASS")
#     else:
#         print("Rank:",students.index((name, marks))+1, name, "→", marks, "→", "FAIL")    
    

#Practical 19 repeat
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# students = sorted(
#     students,
#     key=lambda student: student[1],
#     reverse=True
# )

# for rank, (name, marks) in enumerate(students, start=1):

#     if marks >= 50:
#         print(rank, ".", name, "→", marks, "→", "PASS")
#     else:
#         print(rank, ".", name, "→", marks, "→", "FAIL")

#Practical 20
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# students = sorted(
#     students,
#     key=lambda student: student[1],
#     reverse=True
# )

# search = input("Enter Student Name: ")

# for rank, (name, marks) in enumerate(students, start=1):
#     if name.lower() == search.lower():
#         print("Student Found")
#         print("Rank:", rank) 
#         if marks >= 50:
#             print(name, "→", marks, "→", "PASS")
#         else:
#             print(name, "→", marks, "→", "FAIL")
#         break    
# else:
#     print("Student Not Found")            

#Comprehensive Practice — Challenge 1 — Student Tuple Processing
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# for name, marks in students:
#     if marks >= 50:
#         print(name, "→", marks, "→", "PASS")
#     else:
#         print(name, "→", marks, "→", "FAIL")    

#Comprehensive Practice — Challenge 2
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# total_marks = 0
# average_count = 0
# for name, marks in students:
#     total_marks += marks
# average_marks = total_marks / len(students)

# print("Average Marks:", average_marks)

# for name, marks in students:
#     if marks > average_marks:
#         average_count += 1
# print("Above Average Students:", average_count)

#Comprehensive Practice — Challenge 3
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# students = sorted(students, key=lambda student: student[1])

# for name, marks in students:
#     print(name, "→", marks)

#Comprehensive Practice — Challenge 4
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# search = input("Enter Student Name: ")

# for index, (name, marks) in enumerate(students):
#     if name.lower() == search.lower():
#         print("Student Found")
#         print("Index:", index)
#         print(name, "→", marks)
#         break
# else:
#     print("Student Not Found")

#Comprehensive Practice — Challenge 5
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Rahim", 90),
#     ("Hasan", 35)
# )

# count = 0
# first_index = None
# found_student = None

# search = input("Enter Student Name: ")

# for index, (name, marks) in enumerate(students):
#     if name.lower() == search.lower():

#         if first_index is None:
#             first_index = index
#         count += 1

# if count > 0:
#     print("Student Found")
#     print("First Index:", first_index)

#     found_student = students[first_index]

#     print(found_student[0], "→", found_student[1])
#     print(search, "Count:", count)  

# else:
#     print("Student Not Found")

#Comprehensive Practice — Challenge 6
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Hasan", 35),
#     ("Jamal", 90)
# )

# total_marks = 0

# for rank, (name, marks) in enumerate(students):
#     total_marks += marks
# average = total_marks / len(students)
# print("Average Marks: ", average)

# students = sorted(students, key=lambda student: student[1], reverse=True)

# for rank, (name, marks) in enumerate(students, start=1):
#     if marks >= 50:
#         print(rank,".", name, "→", marks, "→", "PASS")
#     else:
#         print(rank,".", name, "→", marks, "→", "FAIL")    

#Comprehensive Practice — Challenge 7
# students = (
#     ("Shahadat", 85),
#     ("Rahim", 45),
#     ("Karim", 72),
#     ("Rahim", 90),
#     ("Hasan", 35)
# )

# students = sorted(students, key=lambda student: student[1], reverse=True)

# for rank, (name, marks) in enumerate(students, start=1):
#     if rank == 2:
#         print("Second Highest: ", name, "→", marks)
#         break
# else: None

#Challenge 8 — Student Grade Summary
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

for name, marks in students:
    if marks >= 80:
        print(name, "→", marks, "→", "A")
    elif marks >= 60:
        print(name, "→", marks, "→", "B")  
    elif marks >= 50:
        print(name, "→", marks, "→", "C") 
    else:
        print(name, "→", marks, "→", "F")         