students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

print(students[1]) #Positive Index

print(students[-5]) #Negative Index

#List-এর Item পরিবর্তন করা
students = ["Shahadat", "Rahim", "Karim"]
students[1] = "Hasan"
print(students[1])

students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]

students[1] = "Rafi"
students[4] = "Sakib"
students[2] = "Arif"
print(students)
# print(students[0], students[1], students[2], students[3], students[4])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])

#List-এর মধ্যে Item যোগ করা
#append()
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits.append("Grapes")
print(fruits)

#insert()
fruits = ["Apple", "Banana", "Mango", "Grapes"]
fruits.insert(2, "Orange")
print(fruits)

#extend()
students = ["Shahadat", "Rahim"]
new_students = ["Karim", "Hasan", "Jamal"]
students.extend(new_students)
print(students)

#remove()
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
fruits.remove("Mango")
fruits.remove("Grapes")
print(fruits)

#pop()
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
removed_student = students.pop(2)
print("Removed:", removed_student)
print("Updated List:", students)

#del
students = ["Shahadat", "Rahim", "Karim", "Hasan", "Jamal"]
del students[2]
del students[3]
print(students)