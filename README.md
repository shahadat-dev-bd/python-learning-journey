# python-learning-journey
My-python-learning-journey

Variable শুধু Value রাখার জন্য নয়, প্রথম Condition Check করার আগেই Variable-এর অস্তিত্ব থাকা দরকার।

========================

+ Additional Operator (মানে যোগ করা)
- subtraction Operator (মানে বিয়োগ করা)
* Multiplication Operator (মানে গুন করা)
/ Division Operator (মানে ভাগ করা) - Division Operator সবসময় float Return করে
// Floor Division Operator -  Floor Division শুধু পূর্ণ অংশ রাখে।
% Modulus Operator ( মানে ভাগশেষ) - Modulus Operator শুধু ভাগশেষ প্রকাশ করে
** Power Operator (Square করা)

৩*৩*৩*৩
২৭*৩
৮১


Dividend = (Divisor × Quotient) + Remainder এই সমিকরন এর মানে কি
এর অর্থ হলো, যে সংখ্যাকে ভাগ করা হয় (Dividend), সেটি পাওয়া যায় ভাগকারী (Divisor) ও ভাগফল (Quotient)-এর গুণফলের সঙ্গে ভাগশেষ (Remainder) যোগ করলে।

এখানে প্রতিটি অংশের অর্থ:

Dividend = যে সংখ্যাকে ভাগ করা হয় (ভাজ্য)
Divisor = যে সংখ্যা দিয়ে ভাগ করা হয় (ভাজক)
Quotient = ভাগফল
Remainder = ভাগশেষ


কেন এই সমীকরণটি গুরুত্বপূর্ণ?

এটি দিয়ে সহজেই ভাগের উত্তর যাচাই করা যায়। যদি

(ভাজক × ভাগফল) + ভাগশেষ = ভাজ্য

হয়, তাহলে ভাগটি সঠিক হয়েছে।

মনে রাখার সহজ সূত্র:

ভাজ্য = (ভাজক × ভাগফল) + ভাগশেষ


/ → যখন সঠিক গাণিতিক ফলাফল (দশমিকসহ) দরকার।
// → যখন শুধু পূর্ণ সংখ্যা দরকার।
% → যখন ভাগশেষ দরকার।


আজ আমরা ৬টি Comparison Operator শিখব
Operator	নাম	অর্থ
==	Equal To	সমান কি?
!=	Not Equal To	সমান নয় কি?
>	Greater Than	বড় কি?
<	Less Than	ছোট কি?
>=	Greater Than or Equal To	বড় অথবা সমান কি?
<=	Less Than or Equal To	ছোট অথবা সমান কি?




: (Colon) কেন লাগে?

if-এর নিচের লাইন কেন একটু ভেতরে (Indentation) লেখা হয়?
যদি Indentation না দিই তাহলে কী হবে?
if-এর ভিতরের Code কখন Run হবে?



উদাহরণ হিসেবে হতে পারে— গেম রান্না ইন্টারনেট লিফট — অথবা তোমার নিজের চিন্তা।

============================================
🎯 আজকের Lesson-এর Golden Rule

Python if...elif...else-এ উপরে থেকে নিচে Condition Check করে।

যেই প্রথম True Condition পায়, সেই Block Run করে এবং নিচের সব elif ও else Skip করে দেয়।

এটাই elif-এর সবচেয়ে গুরুত্বপূর্ণ নিয়ম।
============================================


এটা তোমার নোটে লিখে রাখো।

and ব্যবহার করা হয় যখন একাধিক Condition একসাথে পরীক্ষা করতে হয়।

Nested if ব্যবহার করা হয় যখন দ্বিতীয় Condition পরীক্ষা করার আগে প্রথম Condition অবশ্যই True হতে হবে।
===========================

🌟 আজকের Golden Rule

Nested if-এ বাইরের if হলো দরজা।

দরজা খুললে (True হলে) তবেই ভিতরের if-এ যাওয়া যাবে।

দরজা না খুললে (False হলে) ভিতরের if কখনোই Check হবে না।
==========================

🎯 আজকের Golden Rule

Nested if-এ ভিতরের Condition-এর Result গুরুত্বপূর্ণ নয়, যদি বাইরের Condition False হয়।

কারণ বাইরের if False হলে Python ভিতরের if-এ প্রবেশই করে না।
====================

এরপরের Lessons
এরপর সাধারণত এই বিষয়গুলো আসে:

📘 Chapter 5 – Loops (for ও while)
📘 Chapter 6 – Functions
📘 Chapter 7 – Lists
📘 Chapter 8 – Tuples
📘 Chapter 9 – Dictionaries
📘 Chapter 10 – File Handling
📘 Chapter 11 – Object-Oriented Programming (OOP)

====================================================

Start + Condition + Update

এই তিনটা ছাড়া while Loop বেশিরভাগ সময় ঠিকমতো কাজ করবে না।

======================

git status
git add .
git commit -m "Add Chapter 5 Lesson 5.2 while loop examples"
git push

==========================
একটা ছোট Diagram

Start

pin = ""

        │
        ▼

Condition Check (১)
"" != "1234"

        │
      True
        │
        ▼

Loop Body (১)
Input → 1234

        │
        ▼

Condition Check (২)
1234 != 1234

        │
     False
        │
        ▼

ATM Unlocked

====================

while বলে "আবার করো", আর if বলে "কী করবো?"

========================

\n একটা নতুন লাইন বা ফাঁকা লাইন দিয়ে Output-কে সুন্দর করে।

==============


আজকের Lesson-এর সবচেয়ে গুরুত্বপূর্ণ Concept

আমি চাই তুমি এই নিয়মটা সব সময় মনে রাখো:

while Loop

প্রথমে Condition Check

↓

True হলে Loop Body Execute

↓

Variable Update

↓

আবার Condition Check

↓

False হলে Loop Stop

Loop Body কখনো Condition Check না করে Run হয় না।

===================================
📌 আমার একটা পরামর্শ

আমি চাই Chapter 5 শুরু করার আগে আমরা Git & GitHub-এর জন্য ১টা ছোট Bonus Chapter করি।

সেখানে আমি একদম শুরু থেকে শেখাবো:

Git কী?
GitHub কী?
Repository কী?
Clone কী?
Commit কী?
Push কী?
Pull কী?
Branch কী?
Tag কী?
Release কী?
.gitignore কী?
README.md কীভাবে লিখতে হয়?

এতে করে তুমি শুধু Python শিখবে না, Professional Developer Workflow-ও শিখে ফেলবে। আমার মতে, এটা Chapter 5 শুরু করার আগে শেখা তোমার জন্য খুবই উপকারী হবে।

আগে Status দেখো
git status

সব File Stage করো
git add .

Commit করো
git commit -m "Add Chapter 5 atm_system program using while loop"

GitHub-এ Push করো
git push

===========================

Phase -১
Python Roadmap (আমাদের Course)
✅ Chapter 1: Variables
Lessons
1.1 Variables কী?
1.2 Variable Naming Rules
1.3 Print Function
1.4 Mini Practice
1.5 Exam

✅ Chapter 2: Data Types
Lessons
2.1 String
2.2 Integer
2.3 Float
2.4 Boolean
2.5 input()
2.6 Type Conversion
2.7 Error Handling (try/except)
2.8 Exam

✅ Chapter 3: Operators
Lessons
3.1 Arithmetic Operators
3.2 Assignment Operators
3.3 Comparison Operators
3.4 Logical Operators
3.5 Mini Projects
3.6 Exam

✅ Chapter 4: Conditional Statements
Lessons
4.1 if
4.2 if...else
4.3 if...elif...else
4.4 Nested if
4.5 Real Life Examples
4.6 Exam

🔄 Chapter 5: Loops (বর্তমানে)
Lessons
✅ 5.1 Loop কী?
✅ 5.2 Basic while Loop
✅ 5.3 Password Verification System
🔄 5.4 Menu Driven Program
5.5 Number Guessing Game
5.6 Infinite Loop
5.7 Nested while
5.8 Loop Debugging
5.9 Chapter Exam

Chapter 6: for Loop
Lessons
for Loop কী?
range()
Start, Stop, Step
String Loop
List Loop
Nested for
Pattern Printing
Real Projects
Exam

Chapter 7: Functions
Lessons
Function কী?
কেন Function ব্যবহার করি?
def
Parameters
Arguments
Return
Local Variable
Global Variable
Real Projects
Exam

Chapter 8: Lists
Lessons
List কী?
Index
Slicing
Add
Remove
Update
Loop with List
Mini Projects
Exam

Chapter 9: Tuples
Lessons
Tuple কী?
Difference between List and Tuple
Methods
Practice
Exam

Chapter 10: Dictionaries
Lessons
Dictionary কী?
Keys
Values
Update
Loop
Nested Dictionary
Exam

Chapter 11: Sets
Lessons
Set কী?
Unique Value
Methods
Union
Intersection
Exam

Chapter 12: Strings (Advanced)
Lessons
String Methods
replace()
split()
join()
strip()
find()
Practice
Exam

Chapter 13: File Handling
Lessons
Open File
Read File
Write File
Append
with Statement
Real Project
Exam

Chapter 14: Exception Handling
Lessons
try
except
else
finally
raise
Custom Exception
Exam

Chapter 15: Modules & Packages
Lessons
import
from ... import
Built-in Modules
Random
Math
Datetime
pip
Exam

Chapter 16: Object-Oriented Programming (OOP)
Lessons
Class
Object
Constructor
Methods
Inheritance
Polymorphism
Encapsulation
Practice
Exam

Chapter 17: Mini Projects

এখানে আমরা বাস্তব Project বানাব।

যেমন:

Calculator
ATM Machine
Student Management System
Quiz App
Password Generator
Contact Book
To-Do List
Banking System
Chapter 18: Git & GitHub (Professional Workflow)

এটা আমরা শেখা শুরু করে দিয়েছি।

এখানে আরও শিখব:

Branch
Merge
Pull Request
Release
Tags
Issues
README Professional করা
Open Source Contribution

Chapter 19: Python Interview Preparation
Common Questions
Coding Problems
Debugging
Logic Building
Mock Interview

Chapter 20: Final Project
=======================================

শেষ Chapter-এ আমরা একটি বড় Project বানাব, যেখানে আগের সব Chapter-এর Concept ব্যবহার হবে।

Phase 2 — Problem Solving (নতুন)
Chapter 17: Problem Solving

এখানে শুধু Problem থাকবে।

কোন নতুন Syntax থাকবে না।

শুধু Logic।

Level 1 — Easy (২৫টি)

যেমন:

Hello 10 বার Print করো
1–10 পর্যন্ত সংখ্যা Print করো
Even Number বের করো
Odd Number বের করো
1–100 এর Sum
Multiplication Table
Largest Number
Smallest Number
Password Check
Count Digits
Level 2 — Medium (২৫টি)

যেমন:

Prime Number
Palindrome
Reverse Number
Fibonacci
Factorial
Armstrong Number
Menu Program
Simple Calculator
Student Result System
ATM Simulation
Level 3 — Hard (২৫টি)

যেমন:

Pattern Printing
Nested Loop Logic
Number Guessing Game
Tic Tac Toe Logic
Word Counter
Login System
Quiz System
Inventory System
Contact Book
Expense Tracker
Level 4 — Super Hard (২৫টি)

যেমন:

Sudoku Validator
Mini Banking System
Library Management
Hospital Queue
Restaurant Billing
Parking Management
Bus Ticket Booking
Student Database
Payroll System
Mini E-commerce Logic

===========================

| Difference from `secret_number` | Output           |
| ------------------------------- | ---------------- |
| `0`                             | ✅ Correct Answer |
| `+1` থেকে `+4`                  | 🙂 Slightly High |
| `+5` বা তার বেশি                         | 🚀 Way Too High  |
| `-1` থেকে `-4`                  | 🙂 Slightly Low  |
| `-5` বা তার বেশি কম                    | ❄️ Way Too Low   |

================================

break হলো এমন একটি Loop Control Statement, যা execute হলে Loop-কে সঙ্গে সঙ্গে সম্পূর্ণভাবে বন্ধ করে দেয়।

=======================

Loop ভুল দেখলে আগে এই ৩টা জিনিস check করবে:

① Condition কী?
        ↓
② Variable কোথা থেকে শুরু করছে?
        ↓
③ Loop-এর ভিতরে Variable কোন দিকে পরিবর্তন হচ্ছে?

এই তিনটা মিলিয়ে দেখলেই অনেক Loop-এর bug ধরা যায়।

============================

Positive Index হলো শুরু থেকে শুরু হয় এবং Index ০ থেকে শুরু হয় আর Negative Index হলো শেষ থেকে শুরু হয় এবং Index - ১ থেকে শুরু হয়

=============================

append() হচ্ছে List-এর একদম শেষে একটি নতুন Item যোগ করে।

========================

List-এর নির্দিষ্ট একটি Position/Index-এ নতুন Item যোগ করতে insert() ব্যবহার
Syntax list_name.insert(index, value)
insert() পুরনো Item-কে Replace করে না।
=====================

একসাথে একাধিক Item যোগ করতে extend() ব্যবহার হয়

=========================

List থেকে নির্দিষ্ট একটি Item-এর Value মুছে ফেলা জন্য remove() ব্যবহার করা হয়।
remove()-এ Index নয়, Value দিতে হয়
remove() একই Value-এর সবগুলো মুছে ফেলে না— শুধু প্রথম matching Item-টি মুছে ফেলে।
=======================

pop() দিয়ে যে আইটেম মুছে ফেলা হলো সেটা একটা নতুন ভ্যারিয়েবল এর মধ্যে সেভ হয়ে থাকলো। পরে যদি সেই আইটেম এর দরকার হয় তাহলে সেটা আমরা অই নতুন ভ্যারিয়েবল কে প্রিন্ট এ কল করে আউটপুট দেখাতে পারবো

====================

del ব্যবহার করে List-এর কোনো নির্দিষ্ট Index-এর Item মুছে ফেলা যায়।
=======================

🔑 del বনাম remove() বনাম pop()
remove(value)
      ↓
Value দিয়ে Item মুছে ফেলে

pop(index)
      ↓
Index দিয়ে Item মুছে ফেলে
      ↓
মুছে ফেলা Item return করে

del list[index]
      ↓
Index দিয়ে Item মুছে ফেলে
      ↓
Item return করে না

============================

clear() ব্যবহার করে একটি List-এর সবগুলো Item একসাথে মুছে ফেলা যায়।
list_name.clear()

=======================

len() ব্যবহার করে কোনো List-এর মধ্যে মোট কতগুলো Item আছে সেটা জানা যায়।
len(list_name)
len() List পরিবর্তন হওয়ার সাথে সাথে নতুন Length দেয়

========================================

কোনো নির্দিষ্ট Item List-এর মধ্যে আছে কি না তা জানার জন্য।  
in (Operator) এবং not in (Operator) ব্যবহার করা হয়।
in এবং not in-কে if Condition-এর সাথেও ব্যবহার করা যায়।

if search in students:
ইন দিয়ে লিস্ট এর মধ্যে আইটেম আছে কিনা সেটা সার্স করছে আর ইফ সিদ্ধান্ত নেওয়ার জন্য ব্যবহার করা হয়েছে

==========================
count() Method
একটি নির্দিষ্ট Item List-এর মধ্যে কতবার আছে।
list_name.count(value)
========================
count() বনাম len()
len(fruits) দিয়ে পরো List-এ মোট কতটি Item আছে
আর 
fruits.count("Apple") দিয়ে "Apple" কতবার আছে
====================

index()
index() ব্যবহার করে List-এর মধ্যে কোনো নির্দিষ্ট Value প্রথম কোন Index-এ আছে সেটা বের করা যায়।
list_name.index(value)
-==================
enumerate() Index এবং Value দুটোই দরকার হয় তখন enumerate() ব্যবহার হয়।।
========================
List-এর Copy
List-এর একটি আলাদা Copy বানাতে চাই, তাহলে ব্যবহার করতে পারি copy()
new_students = students.copy()
=================================
students = students বনাম students.copy()
new_students = students
        ↓
একই List

new_students = students.copy()
        ↓
আলাদা Copy

=============================
List Sorting
sort()
sort() List-এর Number-গুলোকে ছোট থেকে বড় সাজিয়েছে:এটাকে বলে Ascending Order।

বড় থেকে ছোট সাজিয়েছে:এটাকে বলে Descending Order

sort() = Ascending
sort(reverse=True) = Descending

========================
sorted()
দুটোর কাজ দেখতে একই রকম মনে হতে পারে, কিন্তু একটা গুরুত্বপূর্ণ পার্থক্য আছে।
sorted() একটি List-এর Item-গুলোকে ক্রমানুসারে সাজিয়ে একটি নতুন List return করে।

sort()
↓
মূল List সাজিয়ে দেয়

sorted()
↓
নতুন সাজানো List দেয়
মূল List আগের মতো থাকে

=========================
🧠 দ্রুত মনে রাখার টেবিল
Method	কাজ
append()	শেষে ১টি Item যোগ করে 
insert()	নির্দিষ্ট Position-এ ১টি Item যোগ করে
extend()	একাধিক Item যোগ করে
remove()	Value দিয়ে Item মুছে ফেলে
pop()	Index দিয়ে Item মুছে + Item return করে
clear()	সব Item মুছে ফেলে
sort()	মূল List Sort করে
copy()	আলাদা List Copy তৈরি করে 
=========================
যেসব Method মূল List পরিবর্তন করে:
append()
insert()
extend()
remove()
pop()
clear()
sort()

=======================

যেটা আলাদা List তৈরি করে:
copy()
আর:
sorted()

➡️ নতুন sorted List return করে, মূল List পরিবর্তন করে না।

============================
Nested Lists - একটি List-এর ভিতরে আরেকটি List

🧠 সহজ নিয়ম
students[Outer Index][Inner Index]
=========================

🧠 Debugging-এর সময় প্রথম প্রশ্ন:

"আমি যে Index ব্যবহার করেছি, সেটা কি List-এর মধ্যে আছে?"
=======================
sort()
→ মূল List পরিবর্তন করে
→ নতুন List return করে না
→ None return করে

sorted()
→ মূল List পরিবর্তন করে না
→ নতুন Sorted List return করে

================
copy() List-কে আলাদা করে। sorted() শুধু নতুন sorted List তৈরি করে।