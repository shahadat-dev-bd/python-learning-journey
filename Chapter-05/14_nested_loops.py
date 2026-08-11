for i in range(3):
    print("Student:", i)

    for j in range(2):
        print("Subject: ", j)


print("=============") 

students = ["Shahadat", "Rahim", "Karim"]

subjects = ["Math", "English", "Python"]

for student in students:
    print("Student:", student)

    for subject in subjects:
        print("Subject: ", subject)

print("=====================")

products = ["Shirts", "Pants", "Jacket"]
sizes = ["M", "L"]

for product in products:
    for size in sizes:
        print( product, "→", size)

print("===================")

students = ["Shahadat", "Rahim", "Karim"]
subjects = ["Math", "English", "Python"]
marks = [
    [85, 90, 95],
    [75, 80, 88],
    [92, 85, 90],
    ]

for i in range(len(students)):
    print("Student:", students[i])

    for j in range(len(subjects)):
        print("  Subject:", subjects[j])
        print("  Marks:", marks[i][j])

    print()

print("=================")
#-- for, range(), len(), Nested Loop---#

products = ["Laptop", "Phone", "Tablet"]
colors = [
            ["Black", "Silver"],
            ["Black", "Blue"],
            ["Gray", "Black"]
        ]
prices = [
            ["50000", "55000"],
            ["30000", "32000"],
            ["25000", "27000"]
        ]

for i in range(len(products)):
    print("Product:", products[i])

    for j in range(len(colors[i])):
        print(" color:", colors[i][j])
        print(" Price:", prices[i][j])
    print()    


print("===============")

products = ["Shirt", "Pants", "Jacket", "T-Shirt"]

sizes = [
    ["S", "M", "L"],
    ["M", "L", "XL"],
    ["M", "L", "XL"],
    ["M", "L", "XL"]
]

stock = [
    [10, 15, 8],
    [12, 20, 7],
    [5, 9, 4],
    [5, 9, 4]
]

for a in range(len(products)):
    print("Product:", products [a])

    for b in range (len(sizes[a])):
        print(" Size:", sizes[a][b])
        print(" Stock:", stock[a][b])
    print()    