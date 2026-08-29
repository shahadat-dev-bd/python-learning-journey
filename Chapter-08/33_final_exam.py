numbers = {10, 20, 30, 40}
print(type(numbers))

fruits = {"apple", "banana", "orange"}
fruits.add("mango")
fruits.discard("banana")
print(fruits)

usernames = [
    "shahadat",
    "rahim",
    "karim",
    "rahim",
    "hasan",
    "karim",
    "jamal"
]

seen = set()
duplicate = set()

for username in usernames:
    if username in seen:
        duplicate.add(username)
    else:
        seen.add(username)

print(duplicate)

python_team = {"A", "B", "C", "D"}
web_team = {"C", "D", "E", "F"}
ai_team = {"D", "F", "G"}

unique_employee = python_team.union(web_team, ai_team)
same_employee_all_departments = python_team.intersection(web_team, ai_team)
python_and_Web_not_ai_department = python_team.intersection(web_team).difference(ai_team)
only_python_department = python_team.difference(web_team, ai_team)

print(unique_employee)
print(same_employee_all_departments.count())
print(python_and_Web_not_ai_department)
print(only_python_department)

customer_ids = [
    "C101",
    "C102",
    "C103",
    "C101",
    "C104",
    "C105",
    "C103",
    "C106",
    "C102"
]

seen = set()
duplicate = set()

for username in customer_ids:
    if username in seen:
        duplicate.add(username)
    else:
        seen.add(username)

seen = set()
duplicate = set()

for username in customer_ids:
    if username in seen:
        duplicate.add(username)
    else:
        seen.add(username)

print("ALL Unique Customer ID:",seen)
print("Duplicate Customer ID:",duplicate)
print("Total Unique Customer:",len(seen))
print("Total Duplicate Customer ID:", len(duplicate))



