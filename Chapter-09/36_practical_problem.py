#Practical Problem 1 — Customer Due Management
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 3000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    }
}
payment = 1000
customers["C101"]["due"] -= payment
print("Customer Due Management:")
print("Customer:", customers["C101"]["name"])
print("Updated Due:", customers["C101"]["due"])

#Practical Problem 2
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    }
}

if "C105" in customers:
    print("Name:", customers["C105"]["name"], ",", "Due:", customers["C105"]["due"])
else:
    print("Customer not found")    

#Practical Problem 3
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C102": {
        "name": "Rahim",
        "due": 1500
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    }
}
total_due = 0
for customer in customers.values():
    total_due += customer["due"]
print("Total Due:", total_due)

#Practical Problem 4
customers = {
    "C101": {
        "name": "Shahadat",
        "due": 2000
    },
    "C102": {
        "name": "Rahim",
        "due": 0
    },
    "C103": {
        "name": "Karim",
        "due": 2500
    },
    "C104": {
        "name": "Hasan",
        "due": 0
    }
}

for customer in customers.values():
    if customer["due"] > 0:
        print("Customer:", customer["name"], "has a due amount of", customer["due"], ".")

#Practical Problem 5 — Customer Payment Processing
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500}
}

payment = 1000
if "C103" in customers:
    customers["C103"]["due"] -= payment
    print(customers["C103"]["name"],"'s", "New due:", customers["C103"]["due"])

#Practical Problem 6 — Payment Validation。
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500}
}

if "C103" in customers:
    payment = 500
    if payment > customers["C103"]["due"]:
        extra = payment - customers["C103"]["due"]
        new_due = 0
        customers["C103"]["due"] = new_due
        print(f"{customers['C103']['name']} has overpaid by {extra}.")
      
    else:
        customers["C103"]["due"] -= payment
        print(customers["C103"]["name"],"'s", "New due:", customers["C103"]["due"])

#Practical Problem 7
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500}
}
old_due = customers["C103"]["due"]
payment = 1000

if "C103" in customers:
    if payment > old_due:
        extra = payment - old_due
        new_due = 0
        customers["C103"]["due"] = new_due
        print(f"{customers['C103']['name']} has overpaid by {extra}.")
    else:
        customers["C103"]["due"] -= payment
        print(customers["C103"]["name"],"'s","Old Due:", old_due, ",", "Payment:", payment, "," , "New due:", customers["C103"]["due"])    

#Problem 8 — Multiple Customer Payment Processing
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500}
}

payments = {
    "C101": 500,
    "C102": 2000,
    "C103": 1000
}

for customer_id in customers:
    payment = payments[customer_id]
    if payment > customers[customer_id]["due"]:
        extra_amount = payment - customers[customer_id]["due"]
        new_due = 0
        customers[customer_id]["due"] = new_due
        print("**",f"{customers[customer_id]['name']} has overpaid by {extra_amount}.","Taka.")
    else:
        customers[customer_id]["due"] -= payment
        print("**", customers[customer_id]["name"],"'s","Old Due:", customers[customer_id]["due"] + payment, ",", "Payment:", payment, "," , "New due:", customers[customer_id]["due"])

#Problem 9 — Payment Records
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500}
}

payments = {
    "C101": 500,
    "C102": 2000,
    "C103": 1000
}

customers["C101"]["payment"] = 500
customers["C102"]["payment"] = 2000
customers["C103"]["payment"] = 1000
print(customers["C103"]["payment"])

for customer_id in customers:
    payment = payments[customer_id]
    customers[customer_id]["payment"] = payment

    if payment > customers[customer_id]["due"]:
        extra_amount = payment - customers[customer_id]["due"]
        new_due = 0
        customers[customer_id]["due"] = new_due
        print("**",f"{customers[customer_id]['name']} has overpaid by {extra_amount}.","Taka.")

    else:
        customers[customer_id]["due"] -= payment
        print("**", customers[customer_id]["name"],"'s","Old Due:", customers[customer_id]["due"] + payment, ",", "Payment:", payment, "," , "New due:", customers[customer_id]["due"])

#Problem 10 — Customer Payment Summary
customers = {
    "C101": {"name": "Shahadat", "due": 2000},
    "C102": {"name": "Rahim", "due": 1500},
    "C103": {"name": "Karim", "due": 2500},
    "C104": {"name": "Hasan", "due": 1000}
}

payments = {
    "C101": 2000,
    "C102": 500,
    "C103": 3000,
    "C104": 1000
}

for customer_id in customers:
    payment = payments[customer_id]
    customers[customer_id]["payment"] = payment
    if payment >= customers[customer_id]["due"]:
        status = "Paid"
        new_due = 0
        old_due = customers[customer_id]["due"]
        return_amount = payment - old_due
        customers[customer_id]["due"] = new_due
    else:
        status = "Due"
        customers[customer_id]["due"] -= payment
        return_amount = 0
    print("Customer ID:", customer_id, ",", "Name:", customers[customer_id]["name"], ",", "Payment:", payment, ",", "Status:", status, ",", "Return Amount:", return_amount, "New Due:", customers[customer_id]["due"])