# 🐛Small Debugging Challenge

# Challenge 1
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

# Challenge 2
numbers = (10, 20, 30, 40)
print(numbers[3])

# Challenge 3
fruits = ("Apple", "Banana", "Mango")
if "Grapes" in fruits:
    print(fruits.index("Grapes"))
else:
    print("Grapes Not Found")    

# Challenge ৪ 🔥
numbers = (40, 10, 30, 20)
new_numbers = sorted(numbers)
new_numbers.append(50)
print(new_numbers)

#Challenge ৫ — Final Small Challenge 🧠
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

search = input("Enter Student Name: ")
for student in students:
    if student[0].lower() == search.lower():
        print(student)
        break
else:
    print("Student Not Found")