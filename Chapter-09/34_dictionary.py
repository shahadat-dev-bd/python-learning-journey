student = {
    "name": "Rahim",
    "age": 20
}

print(student)

student = {
    "name": "Rahim",
    "age": 20
}
student["course"] = "Python"
print(student)

student = {
    "name": "Rahim",
    "course": ["Python"]
}

student["course"].append("Web Development")

print(student["name"])

#Practice - value add
employee = {
    "name": "Karim",
    "skills": ["Python"]
}

employee["skills"].append("SQL")
employee["skills"].append("Power BI")
print(employee)

#value update
student = {
    "name": "Rahim",
    "age": 20,
    
}

student["course"]=["Python"]
student["age"]="21"
print(student)

#Practice
employee = {
    "customer_id" : "C101",
    "name": "Karim",
    "age": 28,
    "due": 5000
}

due = 5000
payment =2000

new_due = due - payment
employee["due"] = new_due
print(employee["due"])

#Practice
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 5000
}
payments = 2000
customer["due"] -= payments
print(customer)

#Item Delete
student = {
    "name": "Rahim",
    "age": 20,
    "course": "Python",
    "city": "Dhaka"
}

del student["city"]
student.pop("course")
print(student)

