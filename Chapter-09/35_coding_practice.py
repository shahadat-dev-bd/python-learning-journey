#Coding Practice
student = {
    "name": "Rahim",
    "age": 20,
    "course": "Python"
}

for key in student.keys():
    print(key)

#Task 2 — শুধু Value Print করো
student = {
    "name": "Rahim",
    "age": 20,
    "course": "Python"
}

for value in student.values():
    print(value)

#Task 3 — Key + Value একসাথে Print
student = {
    "name": "Rahim",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, value)

#Task 4 — একটু Real-Life Practice
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}

for key, value in customer.items():
    print(key, "→", value)

#Coding Practice
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000,
    "city": "Dhaka"
}

print("Customer Data:")
for key, value in customer.items():
    print(key, "→", value)

#Coding Practice — Task 2
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}
if "phone" in customer:
    print("Found phone")
else:
    print("Not Found Phone information")  

#Task 3
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000,
    "phone": "01700000000"
}
if "phone" in customer:
    print("Phone:", customer["phone"])
else:
    print("Phone information নেই")    

#Task 4
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}
if "due" in customer:
    print("Due:",customer["due"])
else:
    print("Due information নেই")    

#Final Challenge
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}
if "phone" in customer:
    print("Phone:",customer["phone"])
else:
    print("Phone information নেই")    

#Practice — Code
student = {
    "name": "Rahim",
    "age": 20,
    "course": "Python"
}
print(student.get("name", "Not Found"))

#get() Coding Practice
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}

print(customer.get("name", "not found"))

#Task 2
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}
print(customer.get("phone", "Phone information নেই"))

#Task 3
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}
payment = 1000
customer["due"] -= payment
print(customer.get("due", "not found"))

#Task 4
customer = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}

print(customer.get("phone", "No Phone"))

#Real-World Practice — Customer Phone
customer_1 = {
    "customer_id": "C101",
    "name": "Shahadat",
    "due": 3000
}

customer_2 = {
    "customer_id": "C102",
    "name": "Rahim",
    "due": 1500
}
print("Customer:", customer_1["name"], ",", "Due:", customer_2["due"])


#Nested Dictionar
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 3000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    }
}

print(customers["C101"]["name"])
print(customers["C102"]["due"])
print(customers["C101"]["due"])
print(customers["C102"]["name"], customers["C102"]["due"])
payment = 1000
customers["C101"]["due"] -= payment
print(customers["C101"]["due"])

customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    }
}
customers["C103"] = {
    "name": "Karim",
    "due": 2500
}

customers["C104"] = {
    "name": "Hasan",
    "due": 1800
}

customers.pop("C104")
delete_customer = customers.pop("C103")
print("Name:",delete_customer["name"], ",", "Due:", delete_customer["due"])

#Practice: Customer Management
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 3000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    }
}

payment = 1000
customers["C101"]["due"] -= payment

customers["C103"] = {
    "name": "Karim",
    "due": 2500
}

delete_customer = customers.pop("C102")
print("Name:",delete_customer["name"], ",", "Due:", delete_customer["due"])
print("Name:",customers["C101"]["name"], ",", "Due:", customers["C101"]["due"])
print("Name:",customers["C103"]["name"], ",", "Due:", customers["C103"]["due"])

#for_loop
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    }
}

for customer_id in customers:
    print("Customer ID:", customer_id, "Name:" ,customers[customer_id]["name"], "Due:", customers[customer_id]["due"])
    
   
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    }
}

for customer_id in customers:
    customer = customers[customer_id]
    print("Customer ID:",customer_id, "Name:" ,customer["name"],"Due:", customer["due"])

#for loop directly in Inner Dictionary
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    }
}

customer = customers["C101"]
# for key, value in customer.items():
#     print(key, "→", value)

# , "→", "Due:", customer["due"]
print("Due:", customer["due"])