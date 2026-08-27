#Comprehensive Practice — Challenge 1
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

for name, marks in students:
    if marks >= 50:
        print(name, "→", marks, "→", "PASS")
    else:
        print(name, "→", marks, "→", "FAIL")    

#Comprehensive Practice — Challenge 2
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

total_marks = 0
average_count = 0
for name, marks in students:
    total_marks += marks
average_marks = total_marks / len(students)
print("Average Marks:", average_marks)

for name, marks in students:
    if marks > average_marks:
        average_count += 1
print("Above Average Students:", average_count)

#Comprehensive Practice — Challenge 3
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

students = sorted(students, key=lambda student: student[1])

for name, marks in students:
    print(name, "→", marks)

#Comprehensive Practice — Challenge 4
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

search = input("Enter Student Name: ")

for index, (name, marks) in enumerate(students):
    if name.lower() == search.lower():
        print("Student Found")
        print("Index:", index)
        print(name, "→", marks)
        break
else:
    print("Student Not Found")

#Comprehensive Practice — Challenge 5
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Rahim", 90),
    ("Hasan", 35)
)

count = 0
first_index = None
found_student = None

search = input("Enter Student Name: ")

for index, (name, marks) in enumerate(students):
    if name.lower() == search.lower():

        if first_index is None:
            first_index = index
        count += 1

if count > 0:
    print("Student Found")
    print("First Index:", first_index)

    found_student = students[first_index]

    print(found_student[0], "→", found_student[1])
    print(search, "Count:", count)  

else:
    print("Student Not Found")

#Comprehensive Practice — Challenge 6
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

total_marks = 0

for rank, (name, marks) in enumerate(students):
    total_marks += marks
average = total_marks / len(students)
print("Average Marks: ", average)

students = sorted(students, key=lambda student: student[1], reverse=True)

for rank, (name, marks) in enumerate(students, start=1):
    if marks >= 50:
        print(rank,".", name, "→", marks, "→", "PASS")
    else:
        print(rank,".", name, "→", marks, "→", "FAIL")    

#Comprehensive Practice — Challenge 7
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Rahim", 90),
    ("Hasan", 35)
)

students = sorted(students, key=lambda student: student[1], reverse=True)

for rank, (name, marks) in enumerate(students, start=1):
    if rank == 2:
        print("Second Highest: ", name, "→", marks)
        break
else: None

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

#Comprehensive Practice — Challenge 9
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

a_count = 0
b_count = 0
c_count = 0
f_count = 0

for name, marks in students:
    if marks >= 80:
        a_count +=1
    elif marks >= 60:
        b_count += 1
    elif marks >= 50:
        c_count += 1   
    else:
        f_count += 1

print("A Grade: ", a_count)
print("B Grade: ", b_count)
print("C Grade: ", c_count) 
print("F Grade: ", f_count)     

#Comprehensive Practice — Challenge 10
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

top_name, top_marks = students[0]
a_count = 0
b_count = 0
c_count = 0
f_count = 0

for name, marks in students:
    if marks >= 80:
        print(name, "→", marks, "→", "A")
    elif marks >= 60:
        print(name, "→", marks, "→", "B")  
    elif marks >= 50:
        print(name, "→", marks, "→", "C") 
    else:
        print(name, "→", marks, "→", "F") 
print("=====================")
for name, marks in students:
    if marks >= 80:
        a_count +=1
    elif marks >= 60:
        b_count += 1
    elif marks >= 50:
        c_count += 1   
    else:
        f_count += 1

print("A Grade: ", a_count)
print("B Grade: ", b_count)
print("C Grade: ", c_count) 
print("F Grade: ", f_count)            
print("=====================")
for name, marks in students:
    if marks >= 50:
        if marks > top_marks:
            top_name = name
            top_marks = marks
print("Top Student: ", top_name, "→", top_marks)

#Comprehensive Practice — Challenge 11
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)
total_marks = 0
count = 0


for name, marks in students:
    total_marks += marks
average_marks = total_marks/len(students)
print("Average Marks:", average_marks)

for name, marks in students:
    if marks >=80:
        if marks > average_marks:
            count += 1
print("Above Average A Students: ", count)

#Comprehensive Practice — Challenge 12
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

search = input("Enter Student Name: ")
students= sorted(students, key=lambda student: student[1], reverse=True)

for rank, (name, marks) in enumerate(students, start=1):
    if search.lower() == name.lower():
        print("Student Found")
        if marks >= 50:
            print(name, "→", marks, "→", "PASS")
        else:
            print(name, "→", marks, "→", "FAIL")
        print("Rank: ", rank)
        break 
else:
    print("Student Not Found")  