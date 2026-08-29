#Challenge 1 — Duplicate Data Cleaning
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com",
    "d@gmail.com"
]

unique_emails = set(emails)
print("Unique Emails:", unique_emails)
print("Total Unique Emails:", len(unique_emails))

#Comprehensive Practice — Challenge 2
set_a = {"Python", "Java", "C++", "JavaScript"}
set_b = {"Python", "JavaScript", "HTML", "CSS"}

common = set_a.intersection(set_b)
print("Common Topics:", common)
print("Total Common Topics:", len(common))

#Comprehensive Practice — Challenge 3
course_a = {"Python", "HTML", "CSS", "JavaScript"}
course_b = {"Python", "CSS", "React", "Node.js"}

result = course_a.difference(course_b)
results = course_b.difference(course_a)

print("Only in Course A:", result)
print("Only in Course B:", results)
print("Total Different Topics:", len(result) + len(results))

#Comprehensive Practice — Challenge 4
products = {"Laptop", "Phone", "Tablet"}
products.add("Watch")
products.discard("Tablet")
print(products)

#Comprehensive Practice — Challenge 5
students_a = {"Shahadat", "Rahim", "Karim", "Hasan"}
students_b = {"Karim", "Hasan", "Jamal", "Rafi"}
result = students_a.union(students_b)
results = students_a.intersection(students_b)
print("All Students:", result)
print("Common Students:", results)

#Comprehensive Practice — Challenge 6
registered_users = {
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com",
    "d@gmail.com"
}

newsletter_users = {
    "b@gmail.com",
    "c@gmail.com",
    "e@gmail.com"
}

common_user = registered_users.intersection(newsletter_users)
registered_only = registered_users.difference(newsletter_users)
newsletter_only = newsletter_users.difference(registered_users)

print("Common Users:", common_user)
print("Registered Only:", registered_only)
print("Newsletter Only:", newsletter_only)

#Comprehensive Practice — Challenge 7
students = {
    "Shahadat",
    "Rahim",
    "Karim",
    "Hasan"
}

previous_students = {
    "Shahadat",
    "Rahim",
    "Karim",
    "Hasan",
    "Jamal"
}

students.add("Jamal")
students.remove("Hasan")
students.discard("Rafi")

current_batch = previous_students.difference(students)

print("Removed Students:", current_batch)
print("Current Students:", students)

#Comprehensive Practice — Challenge 8
available_products = {
    "Laptop",
    "Phone",
    "Tablet",
    "Watch"
}

requested_products = {
    "Phone",
    "Watch",
    "Camera"
}

available = available_products.intersection(requested_products)
customer_request = requested_products.difference(available_products)

print("Available:", available)
print("Not Available:", customer_request)
print("Requested Count:", len(requested_products))

#Comprehensive Practice — Challenge 9
morning_attendees = {
    "Shahadat",
    "Rahim",
    "Karim"
}

evening_attendees = {
    "Karim",
    "Hasan",
    "Jamal"
}

print(morning_attendees.intersection(evening_attendees))

#Comprehensive Practice — Challenge 9 (repeat)
club_a = {"Shahadat", "Rahim", "Karim"}
club_b = {"Karim", "Hasan", "Jamal"}

before_update = club_a.intersection(club_b)

club_a.add("Hasan")
after_add = club_a.intersection(club_b)

club_b.discard("Karim")
after_disord = club_a.intersection(club_b)

print("Before Update:", before_update)
print("After Add:", after_add)
print("After Discard:", after_disord)

#Comprehensive Practice — Challenge 10
python_students = {
    "Shahadat",
    "Rahim",
    "Karim",
    "Hasan"
}

web_students = {
    "Karim",
    "Hasan",
    "Jamal",
    "Rafi"
}

all_students = python_students.union(web_students)
both_courses = python_students.intersection(web_students)
python_only = python_students.difference(web_students)
web_only = web_students.difference(python_students)

print("All Students:", all_students)
print("Both Courses:", both_courses)
print("Python Only:", python_only)
print("Web Only:", web_only)

#Comprehensive Practice — Challenge 11
usernames = [
    "shahadat",
    "rahim",
    "karim",
    "rahim",
    "hasan",
    "karim",
    "jamal"
]
unique_usernames = set(usernames)

duplicate_usernames = set()

print(unique_usernames)
print("Total Unique Usernames:", len(unique_usernames))

for duplicate in usernames:
    if usernames.count(duplicate) > 1:
        duplicate_usernames.add(duplicate)
print("Duplicate Usernames:", duplicate_usernames)

#Comprehensive Practice — Challenge 12
shahadat_foods = [
    "pizza",
    "burger",
    "pasta",
    "biryani",
    "chicken"
]

rahim_foods = [
    "burger",
    "biryani",
    "sandwich",
    "pizza",
    "rice"
]

shahadat_food = set(shahadat_foods)
rahim_food = set(rahim_foods)

common = shahadat_food.intersection(rahim_food)
print("Common Foods:", common)

print("Total Common Foods:", len(common))

#Comprehensive Set Challenge — 13
python_club = {
    "shahadat",
    "rahim",
    "karim",
    "hasan",
    "jamal"
}

web_club = {
    "rahim",
    "karim",
    "sakib",
    "tanvir",
    "hasan"
}

ai_club = {
    "karim",
    "hasan",
    "sakib",
    "nayeem"
}

python_club.add("fahim")
web_club.remove("tanvir")
ai_club.discard("rahim")

unique_member = python_club.union(web_club)
common_member = python_club.intersection(web_club)
only_python_members = python_club.difference(web_club)
common_three_clubs = python_club.intersection(web_club, ai_club)

print("Python + Web Members:", unique_member)
print("Common Python & Web Members:", common_member)
print("Only Python Members:", only_python_members)
print("Common in All Three Clubs:", common_three_clubs)

print("Python Club Members:",len(python_club))
print("Web Club Members:", len(web_club))
print("AI Club Members:", len(ai_club))

#Comprehensive Challenge 14
day_1 = [
    "shahadat",
    "rahim",
    "karim",
    "hasan",
    "rahim",
    "sakib"
]

day_2 = [
    "karim",
    "tanvir",
    "rahim",
    "sakib",
    "nayeem",
    "karim"
]

day_3 = [
    "hasan",
    "sakib",
    "fahim",
    "rahim",
    "tanvir",
    "fahim"
]

seen_1 = set()
duplicate_1 = set()

seen_2 = set()
duplicate_2 = set()

seen_3 = set()
duplicate_3 = set()


for num_1 in day_1:
    if num_1 in seen_1:
        duplicate_1.add(num_1)
    else:
        seen_1.add(num_1)


for num_2 in day_2:
    if num_2 in seen_2:
        duplicate_2.add(num_2)
    else:
        seen_2.add(num_2)

for num_3 in day_3:
    if num_3 in seen_3:
        duplicate_3.add(num_3)
    else:
        seen_3.add(num_3)

day_1_unique_students = set(day_1)
day_2_unique_students = set(day_2)
day_3_unique_students = set(day_3)


total_unique_students = day_1_unique_students.union(day_2_unique_students, day_3_unique_students)
total_common_students = day_1_unique_students.intersection(day_2_unique_students, day_3_unique_students)
only_day_1_students = day_1_unique_students.difference(day_2_unique_students, day_3_unique_students)
day_1_or_day_2_but_not_day_3 = day_1_unique_students.union(day_2_unique_students).difference(day_3_unique_students)

print("===== Registration Report =====")
print()
print("Day 1 Duplicates:", list(duplicate_1)) 
print("Day 2 Duplicates:", list(duplicate_2)) 
print("Day 3 Duplicates:", list(duplicate_3)) 
print()
print("Total Unique Students:", total_unique_students)
print("Students Registered All 3 Days:", total_common_students)
print("Only Day 1 Students:", only_day_1_students)
print("Day 1/Day 2 but NOT Day 3:", day_1_or_day_2_but_not_day_3)

#Comprehensive Challenge 15
day_1_sales = [
    "laptop",
    "mouse",
    "keyboard",
    "laptop",
    "headphone",
    "mouse"
]

day_2_sales = [
    "keyboard",
    "mouse",
    "monitor",
    "laptop",
    "monitor",
    "webcam"
]

seen_1 = set()
duplicate_1 = set()

seen_2 = set()
duplicate_2 = set()

for sale_1 in day_1_sales:
    if sale_1 in seen_1:
        duplicate_1.add(sale_1)
    else:
        seen_1.add(sale_1)  

for sale_2 in day_2_sales:
    if sale_2 in seen_2:
        duplicate_2.add(sale_2)
    else:
        seen_2.add(sale_2)       

day_1_sale = set(day_1_sales)
day_2_sale = set(day_2_sales)

total_unique_products = day_1_sale.union(day_2_sale)
products_sold_both_days = day_1_sale.intersection(day_2_sale)
only_day_1_products = day_1_sale.difference(day_2_sale)
only_day_2_products = day_2_sale.difference(day_1_sale)

print("===== Sales Report =====")
print()
print("Day 1 Duplicates:", duplicate_1)
print("Day 2 Duplicates:", duplicate_2)
print()
print("Total Unique Products:",total_unique_products)
print("Products Sold Both Days:", products_sold_both_days)
print("Only Day 1 Products:", only_day_1_products)
print("Only Day 2 Products:", only_day_2_products)

#Comprehensive Challenge 16
day_1 = [
    "python",
    "java",
    "html",
    "python",
    "css",
    "javascript"
]

day_2 = [
    "python",
    "css",
    "react",
    "java",
    "react",
    "sql"
]

day_3 = [
    "html",
    "python",
    "sql",
    "react",
    "css",
    "html"
]

day_1_unique_books = set(day_1)
day_2_unique_books = set(day_2)
day_3_unique_books = set(day_3)

seen_1 =set()
duplicate_1 =set()

seen_2 =set()
duplicate_2 =set()

seen_3 =set()
duplicate_3 =set()

for borrow_1 in day_1:
    if borrow_1 in seen_1:
        duplicate_1.add(borrow_1)
    else:
        seen_1.add(borrow_1)    

for borrow_2 in day_2:
    if borrow_2 in seen_2:
        duplicate_2.add(borrow_2)
    else:
        seen_2.add(borrow_2)  

for borrow_3 in day_3:
    if borrow_3 in seen_3:
        duplicate_3.add(borrow_3)
    else:
        seen_3.add(borrow_3) 

total_unique_books = day_1_unique_books.union(day_2_unique_books, day_3_unique_books) 
books_borrowed_all_3_days = day_1_unique_books.intersection(day_2_unique_books, day_3_unique_books)
only_day_1_books = day_1_unique_books.difference(day_2_unique_books, day_3_unique_books)
day_1_or_day_2_but_not_day_3 = day_1_unique_books.union(day_2_unique_books).difference(day_3_unique_books)
day_1_and_day_3_but_not_day_2 = day_1_unique_books.intersection(day_3_unique_books).difference(day_2_unique_books)

print("===== Library Borrowing Report =====")
print("Day 1 Duplicates:", duplicate_1)
print("Day 2 Duplicates:", duplicate_2)
print("Day 3 Duplicates:", duplicate_3)
print()
print("Total Unique Books:", total_unique_books)
print("Books Borrowed All 3 Days:", books_borrowed_all_3_days)
print("Only Day 1 Books:", only_day_1_books)
print("Day 1/Day 2 but NOT Day 3:", day_1_or_day_2_but_not_day_3)
print("Day 1 & Day 3 but NOT Day 2:", day_1_and_day_3_but_not_day_2)

#Comprehensive Challenge 17
shahadat_movies = [
    "inception",
    "interstellar",
    "avatar",
    "titanic",
    "inception",
    "joker"
]

rahim_movies = [
    "avatar",
    "joker",
    "tenet",
    "inception",
    "joker",
    "matrix"
]

karim_movies = [
    "interstellar",
    "avatar",
    "matrix",
    "tenet",
    "interstellar",
    "gladiator"
]

shahadat = set(shahadat_movies)
rahim = set(rahim_movies)
karim = set(karim_movies)

seen_1 = set()
duplicate_1 = set()

seen_2 = set()
duplicate_2 = set()

seen_3 = set()
duplicate_3 = set()

for Movies_1 in shahadat_movies:
    if Movies_1 in seen_1:
        duplicate_1.add(Movies_1)
    else:
        seen_1.add(Movies_1)  

for Movies_2 in rahim_movies:
    if Movies_2 in seen_2:
        duplicate_2.add(Movies_2)
    else:
        seen_2.add(Movies_2) 

for Movies_3 in karim_movies:
    if Movies_3 in seen_3:
        duplicate_3.add(Movies_3)
    else:
        seen_3.add(Movies_3) 

total_unique_movies = shahadat.union(rahim, karim)
movies_in_all_3_watchlists = shahadat.intersection(rahim, karim)
only_shahadat_movies = shahadat.difference(rahim, karim)
shahadat_or_Rahim_but_not_karim = shahadat.union(rahim).difference(karim)
shahadat_and_rahim_but_not_karim = shahadat.intersection(rahim).difference(karim)
karim_and_rahim_but_not_shahadat = rahim.intersection(karim).difference(shahadat)
shahadat_and_karim_but_not_rahim = shahadat.intersection(karim).difference(rahim)
exactly_2_people_watched = shahadat_and_rahim_but_not_karim.union(karim_and_rahim_but_not_shahadat).union(shahadat_and_karim_but_not_rahim)

print("===== Movie Watchlist Report =====")
print()
print("Shahadat Duplicates:", duplicate_1)
print("Rahim Duplicates:", duplicate_2)
print("Karim Duplicates:", duplicate_3)
print()
print("Total Unique Movies:", total_unique_movies)
print("Movies in All 3 Watchlists:", movies_in_all_3_watchlists)
print("Only Shahadat Movies:", only_shahadat_movies)
print("Shahadat/Rahim but NOT Karim:", shahadat_or_Rahim_but_not_karim)
print()
print("Shahadat & Rahim but NOT Karim:", shahadat_and_rahim_but_not_karim)
print("Rahim & Karim but NOT Shahadat:", karim_and_rahim_but_not_shahadat)
print("Shahadat & Karim but NOT Rahim:", shahadat_and_karim_but_not_rahim)
print()
print("Exactly 2 People Watched:", exactly_2_people_watched)

#Comprehensive Challenge 18
python_workshop = [
    "shahadat",
    "rahim",
    "karim",
    "hasan",
    "shahadat",
    "sakib"
]

web_workshop = [
    "rahim",
    "karim",
    "sakib",
    "tanvir",
    "nayeem",
    "rahim"
]

ai_workshop = [
    "karim",
    "hasan",
    "sakib",
    "nayeem",
    "fahim",
    "karim"
]

python = set(python_workshop)
web = set(web_workshop)
ai = set(ai_workshop)

seen_1 = set()
duplicate_1 = set()

seen_2 = set()
duplicate_2 = set()

seen_3 = set()
duplicate_3 = set()

for python_1 in python_workshop:
    if python_1 in seen_1:
        duplicate_1.add(python_1)
    else:
        seen_1.add(python_1)  

for web_2 in web_workshop:
    if web_2 in seen_2:
        duplicate_2.add(web_2)
    else:
        seen_2.add(web_2) 

for ai_3 in ai_workshop:
    if ai_3 in seen_3:
        duplicate_3.add(ai_3)
    else:
        seen_3.add(ai_3) 

total_unique_participants = python.union(web, ai)
registered_in_all_3_workshops = python.intersection(web, ai)
only_python_workshop = python.difference(web, ai)
python_or_web_but_not_ai = python.union(web).difference(ai)

python_and_ai_but_not_web = python.intersection(ai).difference(web)
ai_and_web_but_not_python = ai.intersection(web).difference(python)
python_and_web_but_not_ai = python.intersection(web).difference(ai)

registered_in_exactly_2_workshops = python_and_ai_but_not_web.union(ai_and_web_but_not_python).union(python_and_web_but_not_ai)
special_session_participants = python.union(ai).difference(web)

print("===== Event Registration Report =====")
print()
print("Python Workshop Duplicates:", duplicate_1)
print("Web Workshop Duplicates:", duplicate_2)
print("AI Workshop Duplicates:", duplicate_3)
print()
print("Total Unique Participants:", total_unique_participants)
print("Registered in All 3 Workshops:", registered_in_all_3_workshops)
print("Only Python Workshop:", only_python_workshop)
print("Python/Web but NOT AI:", python_or_web_but_not_ai)
print("Registered in Exactly 2 Workshops:", registered_in_exactly_2_workshops)
print("Special Session Participants:", special_session_participants)

