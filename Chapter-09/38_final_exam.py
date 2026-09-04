# employees = {
#     "E101": {"name": "Rahim", "salary": 30000},
#     "E102": {"name": "Karim", "salary": 45000},
#     "E103": {"name": "Hasan", "salary": 38000}
# }

# highest_salary = 0

# for emp_id in employees:
#     emp_info = employees[emp_id]
#     if emp_info['salary'] > highest_salary:
#         highest_salary = emp_info['salary']

# print("Highest Salary:", highest_salary)

# student = {
#     "name": "Shahadat",
#     "score": 85
# }

# for key in student:
#     print(student[key])

# for key, value in student.items():
#     print(key, value)    


# students = {
#     "S101": {"name": "Shahadat", "score": 85},
#     "S102": {"name": "Rahim", "score": 72},
#     "S103": {"name": "Karim", "score": 45},
#     "S104": {"name": "Hasan", "score": 90}
# }

# pass_count = 0
# fail_count = 0

# for student_id in students:
#     student_info = students[student_id]
#     print(f"Student ID: {student_id}, Name: {student_info['name']}, Score: {student_info['score']}")

#     if student_info['score'] >= 50:
#         print("Result: Pass")
#         pass_count += 1
#     else:
#         print("Result: Fail")
#         fail_count += 1

# print(f"\nTotal Pass: {pass_count}")
# print(f"Total Fail: {fail_count}")


# students = {
#     "S101": {
#         "name": "Shahadat",
#         "age": 33,
#         "score": 85
#     },
#     "S102": {
#         "name": "Rahim",
#         "age": 25,
#         "score": 72
#     }
# }

# # students["S101"]["email"] = "xyz@gmail.com"

# students["S102"].pop("age")

# # students["S102"]["score"] = 80

# if "S102" in students:
#     print(students["S102"]["name"])


# students = {
#     "S101": {
#         "name": "Shahadat",
#         "score": 85
#     },
#     "S102": {
#         "name": "Rahim",
#         "score": 72
#     }
# }

# for student_id in students:
#     student = students[student_id]
#     print(student["name"], student["score"])

# students = {
#     "S101": {"name": "Shahadat", "math": 85, "python": 92},
#     "S102": {"name": "Rahim", "math": 72, "python": 80},
#     "S103": {"name": "Karim", "math": 58, "python": 65}
# }

# student_total_marks = 0

# for student_id in students:
#     student = students[student_id]
#     student_info = student

#     total_marks = student_info["math"] + student_info["python"]
#     student_total_marks += total_marks
#     print(f"Total marks for {student_info['name']}: {total_marks}")

# students = {
#     "S101": {"name": "Shahadat", "math": 85, "python": 92},
#     "S102": {"name": "Rahim", "math": 72, "python": 80},
#     "S103": {"name": "Karim", "math": 58, "python": 65}
# }

# highest_python_marks = 0


# for student_id in students:
#     student = students[student_id]
#     if student["python"] > highest_python_marks:
#         highest_python_marks = student["python"]
#         highest_python_marks_student = student
#     print(f"{student['name']}, Python Marks: {student['python']}")

# print('=========================')    

# print("Student Name:", highest_python_marks_student["name"], ","," With Highest Python marks:", highest_python_marks)

# customers = {
#     "C101": {"name": "Shahadat", "due": 3000},
#     "C102": {"name": "Rahim", "due": 0},
#     "C103": {"name": "Karim", "due": 2500},
#     "C104": {"name": "Hasan", "due": 0}
# }

# for customer_id in customers:
#     customer = customers[customer_id]
#     if customer["due"] > 0:
#         print(f"Customer ID: {customer_id}, Name: {customer['name']}, Due Amount: {customer['due']}")

# if "C103" in customers:
#     print(customers["C103"]["name"])
# else:
#     print("Customer not found.")    


# customers = {
#     "C101": {"name": "Shahadat", "due": 3000},
#     "C102": {"name": "Rahim", "due": 0},
#     "C103": {"name": "Karim", "due": 2500},
#     "C104": {"name": "Hasan", "due": 0}
# }

# count = 0

# for customer_id in customers:
#     customer = customers[customer_id]
#     if customer["due"] > 0:
#         count += 1

# print(f"Total number of customers with due amounts: {count}")


# customers = {
#     "C101": {"name": "Shahadat", "due": 3000},
#     "C102": {"name": "Rahim", "due": 0},
#     "C103": {"name": "Karim", "due": 2500},
#     "C104": {"name": "Hasan", "due": 0}
# }

# total_due_amount = 0

# for customer_id in customers:
#     customer = customers[customer_id]
#     total_due_amount += customer["due"]
   
# print(f"Total due amount across all customers: {total_due_amount}")


# customers = {
#     "C101": {"name": "Shahadat", "due": 3000},
#     "C102": {"name": "Rahim", "due": 0},
#     "C103": {"name": "Karim", "due": 2500},
#     "C104": {"name": "Hasan", "due": 0}
# }

# payment_amount = 1000

# for customer_id in customers:
#     customer = customers[customer_id]
#     if customer_id == "C101":
#         old_due_amount = customer["due"]
#         customer["due"] -= payment_amount
#         break

# print(f"Customer ID: {customer_id}, Name: {customer['name']}, Old Due Amount: {old_due_amount}, Payment Amount: {payment_amount}, New Due Amount: {customer['due']}")
    

# employees = {
#     "E101": {"name": "Rahim", "salary": 30000},
#     "E102": {"name": "Karim", "salary": 45000},
#     "E103": {"name": "Hasan", "salary": 38000},
#     "E104": {"name": "Jamal", "salary": 52000}
# }

# highest_salary = 0
# highest_salary_employee = None

# for emp_id, emp_info in employees.items():
#     if emp_info['salary'] > highest_salary:
#         highest_salary = emp_info['salary']
#         highest_salary_employee = emp_info

# print(f"Employee with highest salary: {highest_salary_employee['name']}, Salary: {highest_salary}")


# employees = {
#     "E101": {"name": "Rahim", "salary": 30000},
#     "E102": {"name": "Karim", "salary": 45000},
#     "E103": {"name": "Hasan", "salary": 38000},
#     "E104": {"name": "Jamal", "salary": 52000}
# }

# lowest_salary = 0
# lowest_salary_employee = None

# for emp_id, emp_info in employees.items():
#     if lowest_salary == 0 or emp_info['salary'] < lowest_salary:
#         lowest_salary = emp_info['salary']
#         lowest_salary_employee = emp_info   
# print(f"Employee with lowest salary: {lowest_salary_employee['name']}, Salary: {lowest_salary}")     


# products = {
#     "P101": {"name": "Keyboard", "price": 1500, "stock": 10},
#     "P102": {"name": "Mouse", "price": 800, "stock": 15},
#     "P103": {"name": "Monitor", "price": 18000, "stock": 5},
#     "P104": {"name": "Headphone", "price": 2500, "stock": 8}
# }

# total_stock_value = 0

# for product_id, product_info in products.items():
#     stock_value = product_info["price"] * product_info["stock"]
#     total_stock_value += stock_value
#     print(f"Product: {product_info['name']}, Stock Value: {stock_value}")

# print('========================')
# print(f"Total stock value: {total_stock_value}")


# products = {
#     "P101": {"name": "Keyboard", "price": 1500, "stock": 10},
#     "P102": {"name": "Mouse", "price": 800, "stock": 15},
#     "P103": {"name": "Monitor", "price": 18000, "stock": 5},
#     "P104": {"name": "Headphone", "price": 2500, "stock": 8}
# }

# highest_stock_product = 0
# highest_stock_product_info = None

# highest_price_product = 0
# highest_price_product_info = None

# highest_stock_value_product = 0
# highest_stock_value_product_info = None

# low_stock_count = 0

# for product_id, product_info in products.items():
#     if product_info["stock"] > highest_stock_product:
#         highest_stock_product = product_info["stock"]
#         highest_stock_product_info = product_info

#     if product_info["price"] > highest_price_product:
#         highest_price_product = product_info["price"]
#         highest_price_product_info = product_info

#     stock_value = product_info["price"] * product_info["stock"]

#     if stock_value > highest_stock_value_product:
#         highest_stock_value_product = stock_value
#         highest_stock_value_product_info = product_info

#     if product_info["stock"] <= 5:
#         low_stock_count += 1
#         print()
#         print(f"Product: {product_info['name']}, Stock: {product_info['stock']}, Number of products with low stock: {low_stock_count}")      

# print('========================')
# print(f"Product with highest stock: {highest_stock_product_info['name']}, Stock: {highest_stock_product}")
# print(f"Product with highest price: {highest_price_product_info['name']}, Price: {highest_price_product}")
# print(f"Product with highest stock value: {highest_stock_value_product_info['name']}, Stock Value: {highest_stock_value_product}")


#Online Store Management System
products = {
    "P101": {
        "name": "Laptop",
        "price": 85000,
        "stock": 4
    },
    "P102": {
        "name": "Keyboard",
        "price": 2500,
        "stock": 12
    },
    "P103": {
        "name": "Mouse",
        "price": 1200,
        "stock": 3
    },
    "P104": {
        "name": "Monitor",
        "price": 22000,
        "stock": 7
    },
    "P105": {
        "name": "Headphone",
        "price": 3500,
        "stock": 6
    }
}

total_stock_value = 0
low_stock_product = 0

highest_stock_product = 0
highest_stock_product_info = None

lowest_stock_product = 0
lowest_stock_product_info = None

highest_price_product = 0
highest_price_product_info = None

# #Part 6 — Update Stock
product_id = "P103"
new_stock = 10

old_stock = products[product_id]["stock"]
update_stock = old_stock + new_stock
products[product_id]["stock"] = update_stock 


#Part 1 — Product Information
for product_id in products:
    product = products[product_id]
#     print("Product ID:", product_id, ",", "Product Name:",product["name"], ",", "Price:", product["price"], ",", "Stock:",product["stock"])
# print("======================")

# #Part 2 — Stock Value
for product_id, product_info in products.items():
    stock_value = product_info["price"] * product_info["stock"]
    total_stock_value +=  stock_value
#     # print("Stock Value:",stock_value)

# print("======================")
# print("Total Stock Value:", total_stock_value) 
# print("======================")

# #Part 3 — Low Stock Products
for product_id, product_info in products.items():
    if product_info["stock"] <= 5:
       low_stock_product += 1
#        print("Product ID:", product_id, "Name:", product["name"], "Stock:", product["stock"])
# print("Low Stock Product:", low_stock_product) 
# print("======================")   

# print("Old Stock:", old_stock)
# print("New Stock:", new_stock)
# print("New Stock After Update:", update_stock) 

# #Part 4 — Highest & Lowest
for product_id, product_info in products.items():
    if product_info["stock"] > highest_stock_product:
        highest_stock_product = product_info["stock"]
        highest_stock_product_info = product_info

    if lowest_stock_product_info is None or product_info["stock"] < lowest_stock_product:
        lowest_stock_product = product_info["stock"]
        lowest_stock_product_info = product_info

    if product_info["price"] > highest_price_product:
        highest_price_product = product_info["price"]
        highest_price_product_info = product_info

# print("Product Name:", highest_stock_product_info["name"], "," ,"Highest Stock Product:", highest_stock_product) 
# print("Product Name:", lowest_stock_product_info["name"], "," ,"Lowest Stock Product:", lowest_stock_product)
# print("Product Name:", highest_price_product_info["name"], "," ,"Highest Price Product:", highest_price_product)

# print("======================")

#Part 5 — Search Product
# search_id = "P103"
# for product_id, product_info in products.items():
#     if search_id == product_id:
#         print("Product Found")
#         print("Name:", product_info["name"], ",","Price:",product_info["price"], ",", "Stock:",product_info["stock"])
#         break
# else:
#     print("Product not found.")


#Total Products
total_product = len(products)
# print(total_product)


#Total Stock
total_stock = 0
for product_id, product_info in products.items():
    total_stock += product_info["stock"]
# print("Total Stock:",total_stock)

#Part 7 — Final Report
print("========== STORE REPORT ==========")
print("Total Products", total_product)
print("Total Stock:", total_stock)
print("Total Stock Value:", total_stock_value) 
print()
print("Low Stock Product:", low_stock_product)
print("Highest Stock Product:", highest_stock_product) 
print("Lowest Stock Product:", lowest_stock_product)
print("Highest Price Product:", highest_price_product)