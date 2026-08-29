colors = {"Red", "Green", "Blue"}
colors.add("Yellow")
print(colors)

fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Orange") #KeyError

fruits = {"Apple", "Banana", "Mango", "Orange"}
fruits.remove("Mango")
# print(fruits)
fruits.remove("Grapes")

fruits = {"Apple", "Banana", "Mango"}
fruits.discard("Banana")
print(fruits)

set_a = {"Apple", "Banana", "Mango"}
set_b = {"Mango", "Orange", "Grapes"}
result = set_a.union(set_b)
print(result)

set_a = {"Apple", "Banana", "Mango", "Orange"}
set_b = {"Mango", "Orange", "Grapes", "Banana"}
result = set_a.intersection(set_b)
print(result)

set_a = {"Apple", "Banana", "Mango", "Orange"}
set_b = {"Banana", "Mango", "Grapes"}

result = set_a - set_b
print(result)