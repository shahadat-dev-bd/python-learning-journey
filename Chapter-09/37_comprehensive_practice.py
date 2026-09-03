#Comprehensive Practice — Scenario
customers = {
    "C101": {"name": "Shahadat", "due": 3000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500},
    "C104": {"name": "Hasan", "due": 0}
}

payments = {
    "C101": 1000,
    "C102": 2000,
    "C103": 2500,
    "C104": 500
}

for customer_id in customers:
    payment = payments[customer_id]
    if payment > customers[customer_id]["due"]:
        old_due = customers[customer_id]["due"]
        extra_amount = payment - customers[customer_id]["due"]
        new_due = 0
        customers[customer_id]["due"] = new_due
        status = "Paid"
        print(customer_id, f"{customers[customer_id]['name']} has overpaid by {extra_amount}.","Taka.", "Old Due:", customers[customer_id]["due"] + payment, "New Due" , customers[customer_id]["due"],", Status:", status)
    else:
        customers[customer_id]["due"] -= payment
        print(customer_id, customers[customer_id]["name"],"'s","Old Due:", customers[customer_id]["due"] + payment, ",", "Payment:", payment, "," , "New due:", customers[customer_id]["due"],",", "Status:", "Paid" if customers[customer_id]["due"] == 0 else "Due")

#Comprehensive Practice - Student Result Management System
students = {
    "S101": {
        "name": "Shahadat",
        "math": 85,
        "english": 78,
        "python": 92
    },
    "S102": {
        "name": "Rahim",
        "math": 65,
        "english": 72,
        "python": 80
    },
    "S103": {
        "name": "Karim",
        "math": 45,
        "english": 58,
        "python": 50
    }
}

pass_count = 0
fail_count = 0
total_all_marks = 0
highest_marks = 0
highest_student = None
highest_student_id = None

for student_id in students:
    student = students[student_id]
    total_marks = student["math"] + student["english"] + student["python"]
    average_marks = total_marks/3
    if average_marks >= 50:
        result = "Pass"
        pass_count += 1
    else:
        result = "Fail"
        fail_count += 1
    print("Student ID:", student_id, "→", "Name:", student["name"], "→", "Total Marks:", total_marks, "→" , "Average:", average_marks, "→" , "Result:", result) 

    total_all_marks += total_marks

    # Check for highest marks
    if total_marks > highest_marks:
        highest_marks = total_marks
        highest_student = student["name"]
        highest_student_id = student_id

overall_average = total_all_marks/len(students)

print("--------------------------------------------------")
print("Total Summary:")
print("Total Students:", len(students), "→", "Total Pass:", pass_count, "→", "Total Fail:", fail_count)   
print("Total All Marks:", total_all_marks)
print("Overall Average:", overall_average)
print("Highest Marks:", highest_marks, "→", "Student ID:", highest_student_id, "→", "Name:", highest_student)


#Chapter 9 Final Challenge
students = {
    "S101": {"name": "Shahadat", "python": 85, "sql": 78},
    "S102": {"name": "Rahim", "python": 65, "sql": 72},
    "S103": {"name": "Karim", "python": 45, "sql": 58},
    "S104": {"name": "Hasan", "python": 90, "sql": 88}
}

pass_count = 0
fail_count = 0
total_all_marks = 0
highest_marks = 0
highest_student = None
highest_student_id = None

highest_python = 0
highest_python_student = None

highest_sql = 0
highest_sql_student = None


for student_id in students:
    student = students[student_id]
    total_marks = student["python"] + student["sql"]
    average_marks = total_marks / 2
    if average_marks >= 50:
        result = "Pass"
        pass_count += 1
    else:
        result = "Fail"
        fail_count += 1
    print("Student ID:", student_id, "→", "Name:", student["name"], "→", "Total Marks:", total_marks, "→", "Average:", average_marks, "→", "Result:", result)

    total_all_marks += total_marks

    # Check for highest marks
    if total_marks > highest_marks:
        highest_marks = total_marks
        highest_student = student["name"]
        highest_student_id = student_id

    # Check for highest python marks
    if student["python"] > highest_python:
        highest_python = student["python"]
        highest_python_student = student["name"]

    # Check for highest SQL marks 
    if student["sql"] > highest_sql:
        highest_sql = student["sql"]
        highest_sql_student = student["name"]   


overall_average = total_all_marks / len(students)

print("--------------------------------------------------")
print("Total Summary:")
print("Total Students:", len(students), "→", "Total Pass:", pass_count, "→", "Total Fail:", fail_count)
print("Total All Marks:", total_all_marks)
print("Overall Average:", overall_average)
print("Highest Marks:", highest_marks, "→", "Student ID:", highest_student_id, "→", "Name:", highest_student)
print("--------------------------------------------------")
print("Highest Python Marks:", highest_python, "→", "Student:", highest_python_student)
print("Highest SQL Marks:", highest_sql, "→", "Student:", highest_sql_student)