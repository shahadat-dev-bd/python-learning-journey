students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
search = ""

search = input("Enter Student Name: ")

for student in students:
    print("Checking", student)

    if student == search:
        print("Student Found:", student)
        break
else:
    print("Student Not Found")
