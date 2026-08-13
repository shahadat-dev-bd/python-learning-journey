# students = ["Shahadat", "Rahim", "Karim", "Hasan"]

# for index, student in enumerate(students, start=5):
#     print(index, student)


# print("========")    

# students = ["Shahadat", "Rahim", "Karim", "Hasan"]
# marks = [85, 45, 72, 90]

# for number, student in enumerate(students, start=1):
#     if marks [number - 1] >= 50:
#         print(number,".", student, "→", marks [number - 1], "→", "Pass")
#     else:
#         print(number,".", student,"→",marks [number - 1], "→", "Fail")  


# print("========")       
# # 
# 

# products = ["Shirt", "Pants", "Jacket", "Shoes", "Watch"] 
# search = ""

# search = input("Enter Product: ")

# for product in products:
#      print("Checking:", product)
#      if search == product:
#         print("Product Found!")
#         break
# else:
#     print("Product Not Found")
     
# print("========")       

pins = ["123456", "111111", "636363", "555555", "999999"]
correct_pin = ""

correct_pin = input("Enter Your PIN: ")

for pin in pins:
    print("Checking PIN:", pin)
    if correct_pin == pin:
        print("Access Granted")
        break
else:
    print("Access Denied")   
