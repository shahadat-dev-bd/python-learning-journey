name="Shahadat Hossain"
age=35
height=5.8
is_learning_python=True

first_name="Shahadat"
last_name="Hossain"


print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_python))


print()
print(33+33)
print("33"+"33")
print("Shahadat"+"Hossain")
print()
print(first_name + " " + last_name)

print()
print("10" + "20")
print(10 + 10)
print ("Python" + " Developer")    

age = "33"
age = int(age)
print (age)

print(type(age))

print(age + 7)

age = 33
age = str(age)
print(type(age))
print("My age is " + age + " Years")


price = "99.90"
price = float(price)
print(type(price))
print(price)


print(int("100") + float("50.0"))

name = input("Enter your name: ")
print("Hello", name)

try:
    age = input("Please Enter your age: ")
    age = int(age)
    print("Your age is ", age, "Years Old")
    print("After 10 years, your age will be ", age + 10, "Years Old")

except ValueError:
    print("Invalid input! Please enter a valid input for age.")

