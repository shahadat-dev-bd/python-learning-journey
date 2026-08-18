#1st Comprehensive Challenge

# students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal", "Sakib"]
# marks = [85, 0, 72, 45, 90, 0]

# search = input("Enter Student Name: ")

# for index, student in enumerate(students):

#     print("Checking:", student)

#     if search == student:

#         print("Student Found")

#         if marks[index] == 0:
#             break

#         if marks[index] >= 50:
#             print(student, "→", marks[index], "→", "PASS")
#             print()
#         else:
#             print(student, "→", marks[index], "→", "FAIL")
#             print()
#         break

#     if marks[index] == 0:
#         continue

#     if marks[index] >= 50:
#         print(student, "→", marks[index], "→", "PASS")
#         print()
#     else:
#         print(student, "→", marks[index], "→", "FAIL")
#         print()
# else:
#     print("Student Not Found")

# #2nd Comprehensive Challenge
# products = ["Laptop", "Phone", "Tablet", "Watch", "Camera"]
# stock = [5, 0, 12, 0, 3]
# search = ""

# search = input("Enter Product Name: ")

# for index, product in enumerate(products):
#     print("Checking:", product)

#     if search == product:
        
#         if stock[index] == 0:
#             print("Product Found → Out of Stock")
#             break

#         if stock[index] >= 5:
#             print(product,"Available: ", stock[index], "QTY")
#         else:
#             print(product,"Low Stock: ", stock[index], "QTY")
#         print("Product Found")
#         break    

#     if stock[index] == 0:
#         continue
#     if stock[index] >= 5:
#         print(product,"Available")
#     else:
#         print(product,"Low Stock") 
        
# else:
#     print("Product Not Found")   

#3rd Comprehensive Challenge   
employees = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal", "Sakib"]
attendance = [25, 0, 22, 18, 30, 0]
salary = [30000, 25000, 28000, 22000, 35000, 27000]
search = ""

search = input("Enter Employee Name: ")

for index, employee in enumerate(employees):
    print("Checking:", employee)

    if search == employee:
        if attendance[index] == 0:
            print("Employee Found → No Attendance")
            break
        if attendance[index] >= 20:
            print(employee, "→", attendance[index], "Days", "→", "Regular", "→", "Salary: ", salary[index], "Taka")
        else:
            print(employee, "→", attendance[index], "Days", "→", "Irregular", "→", "Salary: ", salary[index], "Taka")
        print("Employee Found")    
        break

    if attendance[index] == 0:
        continue
    if attendance[index] >= 20:
        print(employee, "→", attendance[index], "Days", "→", "Regular", "→", "Salary: ", salary[index], "Taka")
    else:
        print(employee, "→", attendance[index], "Days", "→", "Irregular", "→", "Salary: ", salary[index], "Taka")   
else:
    print("Employee Not Found") 