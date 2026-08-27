#Practical 1 — Student Information
student = ("Shahadat", 33, 85)
name, age, marks = student
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

#Practical 2 — Student Marks
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90)
)

print(students[1][0], "→", students[1][1])

#Practical 3
students = (
    ("Shahadat", 85),
    ("Rahim", 72),
    ("Karim", 90),
    ("Hasan", 65)
)

for name, marks in students:
    print(name, "→", marks)

#Practical 4  
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35)
)  

for name, marks in students:
    if marks >= 50:
        print(name, "→", marks, "→", "PASS")
    else:
        print(name, "→", marks, "→", "FAIL")    

#Practical 5
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35)
)

search = input("Enter Student Name: ")
for student in students:
    if student[0].lower() == search.lower():
        print(student[0], "→", student[1])
        print("Student Found")
        break
else:
    print("Student Not Found")

#Practical 6
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35)
)
total_marks = 0

for name, marks in students:
    total_marks += marks

average_marks = total_marks/len(students)

print("Total Marks:", total_marks)
print("Students: ", len(students))
print("Average Marks:", average_marks)

#Practical 7
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)
highest_name, highest_marks = students[0]

for name, marks in students[1:]:
    if marks > highest_marks:
        
        highest_name = name
        highest_marks = marks
print("Highest Marks: ", highest_name, "→", highest_marks)    

#Practical 8
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

lowest_name, lowest_marks = students[0]

for name, marks in students[1:]:
    if marks < lowest_marks:
        
        lowest_name = name
        lowest_marks = marks
print("Lowest Marks: ", lowest_name, "→", lowest_marks)   

#Practical 9
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)
pass_count = 0

for name, marks in students:
    if marks >= 50:
        pass_count += 1
                
print("Pass Students: ", pass_count)        

#Practical 10
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)
total_marks = 0

for name, marks in students:
    total_marks += marks
average_marks = total_marks/len(students)
print("Average Marks:", average_marks)

for name, marks in students:
    if marks > average_marks:
        print(name, "→", marks)


#Practical 11
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)
pass_count = 0
fail_count = 0

for name, marks in students:
    if marks >= 50:
        print(name, "→", marks, "→", "PASS")
    else:
        print(name, "→", marks, "→", "FAIL")

for name, marks in students:
    if marks >= 50:
        pass_count += 1
    else:
        fail_count += 1
print()        
print("Pass Students: ", pass_count)
print("Fail Students: ", fail_count)

#Practical 12
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

search = input("Enter Student Name: ")

for name, marks in students:
    if name.lower() == search.lower():
        if marks >= 50:
            print(name, "→", marks, "→", "PASS")
        else:
            print(name, "→", marks, "→", "FAIL")   
        break
else:
    print("Student Not Found")  

#Practical 13
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

top_name, top_marks = students[0]

for name, marks in students[1:]:
    if marks > top_marks:
        top_name = name
        top_marks = marks
print("Top Student: ", top_name, "→", top_marks)

#Practical 14
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

lowest_name, lowest_marks = students[0]

for name, marks in students[1:]:
    if marks < lowest_marks:
        lowest_name = name
        lowest_marks = marks
print("Lowest Student: ", lowest_name, "→", lowest_marks)

#Practical 15
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

top_name, top_marks = students[0]
pass_count = 0

for name, marks in students:
    if marks >= 50:
        pass_count += 1
print("Pass Students: ", pass_count)

for name, marks in students:
    if marks > top_marks:
        top_name = name
        top_marks = marks
print("Top Student: ", top_name, "→", top_marks)

#Practical 16
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
average_marks = total_marks/len(students)
print("Average Marks: ", average_marks) 

for name, marks in students:
    if marks > average_marks:
        average_count += 1
print("Above Average Students: ", average_count)

#Practical 17
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

top_name, top_marks = students[0]

for name, marks in students:
    if marks >= 50:   
        print(name, marks)

for name, marks in students:
    if marks >= 50:
        if marks > top_marks:
            top_name = name
            top_marks = marks
print("Top Student: ", top_name, "→", top_marks)

#Practical 18
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

students= sorted(students, key=lambda student: student[1], reverse=True)
for name, marks in students:
    print(name, "→", marks, "→", "PASS")


#Practical 19
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

students= sorted(students, key=lambda student: student[1], reverse=True)
for name, marks in students:
    if marks >= 50:
        print("Rank:",students.index((name, marks))+1, name, "→", marks, "→", "PASS")
    else:
        print("Rank:",students.index((name, marks))+1, name, "→", marks, "→", "FAIL")    
    

#Practical 19 repeat
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

for rank, (name, marks) in enumerate(students, start=1):

    if marks >= 50:
        print(rank, ".", name, "→", marks, "→", "PASS")
    else:
        print(rank, ".", name, "→", marks, "→", "FAIL")

#Practical 20
students = (
    ("Shahadat", 85),
    ("Rahim", 45),
    ("Karim", 72),
    ("Hasan", 35),
    ("Jamal", 90)
)

students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

search = input("Enter Student Name: ")

for rank, (name, marks) in enumerate(students, start=1):
    if name.lower() == search.lower():
        print("Student Found")
        print("Rank:", rank) 
        if marks >= 50:
            print(name, "→", marks, "→", "PASS")
        else:
            print(name, "→", marks, "→", "FAIL")
        break    
else:
    print("Student Not Found")            
