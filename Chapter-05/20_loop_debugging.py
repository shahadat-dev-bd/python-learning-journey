# #wrong code
# number = 1

# while number <= 5:
#     print(number)
#     number -= 1

# #right code
# while number <= 5:
#     print(number)
#     number += 1

# print("===================")

# #wrong code
# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     if number >= 30:
#         print(number)

# #right code
# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     if number <= 30:
#         print(number)

# print("===================")

# #wrong code

# students = ["Shahadat", "Rahim", "Karim", "Hasan"]
# marks = [85, 45, 72, 90]

# for number, student in enumerate(students, start= 1):
#     if marks[number] >= 50:
#         print(number, ".", student, "→", marks[number], "→ Pass")
#     else:
#         print(number, ".", student, "→", marks[number], "→ Fail")    

#right code
students = ["Shahadat", "Rahim", "Karim", "Hasan"]
marks = [85, 45, 72, 90]

for number, student in enumerate(students, start= 1):
    if marks[number - 1] >= 50:
        print(number, ".", student, "→", marks[number - 1], "→ Pass")
    else:
        print(number, ".", student, "→", marks[number - 1], "→ Fail")    