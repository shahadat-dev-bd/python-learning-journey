# students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
# status = ["Present", "Absent", "Present", "Absent", "Present"]

# for index, student in enumerate(students):
#     if status[index] == "Absent":
#         pass
#     else:
#         print(student, "→", status[index])

# for index, student in enumerate(students):
#     if status[index] != "Absent":
#       print(student, "→", status[index])

print("=============")           

products = ["Laptop", "Phone", "Tablet", "Watch", "Camera"]
status = ["Available", "Coming Soon", "Available", "Coming Soon", "Available"]

for index, product in enumerate(products):
    if status[index] == "Coming Soon":
        pass
    else:
        print(product, "→", status[index])
    