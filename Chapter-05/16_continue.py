# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     if number == 30:
#         continue
#     print(number)

# print("=============")

# marks = [85, 45, 72, 0, 90, 35, 100]

# for mark in marks:
#     if mark == 0:
#         continue
#     print(mark)


# print("=============")

# students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal", "HOSSAIN", "MD"]
# marks = [85, 0, 72, 0, 90, 98, 45]

# for index, student in enumerate(students):
#     if marks[index] == 0:
#         continue
#     if marks[index] >= 50:
#         print(student,"→", marks[index], "→", "PASS")
#     else:
#         print(student,"→", marks[index], "→", "Fail")  

# print("=============")          

students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal", "Sakib"]
marks = [85, 0, 72, 45, 90, 0]

for index, student in enumerate(students):
    if marks[index] == 0:
        continue
    if marks[index] >= 80:
        print(student, "→", marks[index], "→", "A")
    elif marks[index] >= 60:
        print(student, "→", marks[index], "→", "B")
    elif marks[index] >= 50: 
        print(student, "→", marks[index], "→", "C")
    else:
        print(student, "→", marks[index], "→", "Fail") 