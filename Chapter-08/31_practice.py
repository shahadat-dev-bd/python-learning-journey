#Practice 1
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]
result = set(emails)
print(result)
print(len(result))

#Practice 2
club_a = {"Rahim", "Karim", "Hasan", "Jamal"}
club_b = {"Karim", "Jamal", "Rafi", "Sakib"}

result = club_a.intersection(club_b)
print(result)

#Practice 3
course_a = {"Python", "HTML", "CSS", "JavaScript"}
course_b = {"Python", "CSS", "React", "Node.js"}

print(course_b - course_a)
