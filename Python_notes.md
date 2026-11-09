# print() Function
Used to display output on the screen.

Example:
print("Hello")

Output:
Hello

IMPORTANT:
print("name")-> prints text name
print(name)-> print value stored in variable

print("a+b")-> prints a+b
print(a+b)-> prints result of addition


# input() Function
Used to take input from the user

Example:
name = input("Enter your name:")
age = int(input("Enter you age:"))

IMPORTANT:
input gives data as text(string).
Use int() to convert number.


# Variables
Variable are used to store data.

Example:
name = "Sanidhya"
age = 18

print(name)
Output: Sanidhya
print(age)
Output: 18

Rules:
-Cannot start with number
-Cannot contain spaces
-Use meaningful names

Examples:
age = 18
student_name = "Rahul"

Wrong:
age = 18
student name = "Rahul"


# Data Types
Data types tell python what kind of data is being stored.

1. int(Integer)
Whole numbers

2. float
Decimal numbers

3. str(string)
Text data

4. bool(Boolean)
only two value(T/F)

IMPORTANT:
age = input("Enter age: ")

age becomes a string (str) by default.

To use it as a number:

age = int(input("Enter age: "))


int    -> Whole numbers
float  -> Decimal numbers
str    -> Text
bool   -> True or False



# Operators
Operators are used to perform calculations and comparison.

-Arithmatic Operators

+   Addition
-   Subtraction
*   Multiplication
/   Division(3.33333)
//  Floor Division(3)
%   Modulus (Remainder)

-Comparison Operators
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to

IMPORTANT:
age = 18

Here:
=
means assign a value.

But:
==
means compare two values.


=   Assign value
==  Compare values
+   Add
-   Subtract
*   Multiply
/   Divide
//  Floor Division
%   Remainder


# Loops
Used to repeat code.

for i in range(5):
    print(i)

    range(5)
→ 0,1,2,3,4

range(1,11)
→ 1 to 10

range(2,21,2)
→ Even numbers


# While Loops
A while loop is used to repeat code until a condition becomes false.

Example:
count = 1

while count <= 5:
    print(count)
    count = count + 1

Output:
1
2
3
4
5

IMPORTANT:
In a whileloop,we must update the variable inside the loop.

Example:
count = count + 1

If we do not update the variable, the loop may never stop.

This is called an infinite loop.

# for loop vs while loop

for loop:
Used when we know how many times we want to repeat.

Example:
for i in range(5):
    print(i)

while loop:
Used when we want to repeat until a condition becomes false.

Example:
password = ""

while password != "python":
    password = input("Enter password: ")

print("Access granted")

Here,the program keeps asking for password until the user enters python.


# While Loops With Chances
Example:
chances = 5

while chances > 0:
    guess = input("Enter your guess:")
    chances = chances - 1

print("Game over")

Here:
chances = 5 at start

Every time the loop runs:
chances = chances - 1
so chances reduce by one.

When chances become 0,the loop stops

IMPORTANT:
If a while loop never stops, press Ctrl + C in terminal to stop the program.


# Lists
A list is used to store multiple values in one variable.

Example:
expenses = []

items = ["Pen", "Book", "Bottle"]

IMPORTANT:
List indexing starts from 0.

items[0] -> Pen
items[-1] -> Bottle


# append() Function
append() is used to add a new item to the end of a list.

Example:
expenses = []

expenses.append("Snacks")

print(expenses)

Output:

["Snacks"]


# Dictionaries
A dictionary stores data using keys and values.

Example:
expense= {
"name":"Snacks",
"amount":50
}

Here:

"name" and "amount" are keys.

"Snacks" and 50 are values.


# Accessing Dictionary Values
Use the key inside square brackets to access a value.

Example:

expense = {
"name":"Snacks",
"amount":50
}

print(expense["name"])

Output:
Snacks

print(expense["amount"])

Output:
50


# List of Dictionaries
A list can store multiple dictionaries.

Example:
expenses = []

expenses.append({
"name":"Snacks",
"amount":50
})

expenses.append({
    "name":"Recharge",
    "amount":299
})
each dictionary represents one expense.


# Displaying Expenses
A for loop can be used to display every expense.

Example:

for expense in expenses:
print(expense["name"])
print(expense["amount"])

Here:
expense represent one dictionary from the expenses list during each loop.


# Checking an Empty List
len() gives the number of items stored in a list.

Example:

if len(expenses) == 0:
print("No expenses added yet")

If the list contains no items,its length is 0.


# Nested if-else
An if-else statement can be written inside another condition.

Example:

elif choice == "2":
if len(expenses) == 0:
print("No expenses added yet.")
else:
print("Your expenses are available.")

If inner if-else checks whether the expenses list is empty.


# Calculating Total
Start the total from 0.
Then add every expense amount using a for loop.

Example:
total = 0

for expense in expenses:
total += expense["amount"]

print(total)


# The += Operator
+= adds a value to the current value of a variable.

Example:

total = 10

total += 5

This means:

total = total + 5

Output:
15


# Formating decimal Numbers
.2f displays a number with exactly two digits after the decimal point.

Example:

amount = 50

print(f"Rs.{amount:.2f}")

Output:

Rs.50.00


# f-Strings
An f-strings is used to insert variables or expressions inside text.

Example:

name = "Snacks"
amount = 50

print(f"{name}: Rs.{amount:.2f}")

Output:

Snacks:Rs.50.00


# Indentation
Python uses indentation to show which lines belong inside a condition or loop.

Correct:

for expense in expenses:
    print(expense["name"])

Wrong:

for expense in expenses:
print(expense["name"])


# Common Mistakes:
-->Missing colon

Wrong:

if len(expenses) == 0

Correct:

if len(expenses) == 0:

-->Using == instead of =

total = 0

This assigns the value 0.

total == 0

This compares total with 0.

--> Incorrect indentation
Lines inside if,else,for and while must be indented correctly.

-->Incorrect decimal formatting

Better:

{amount:.2f}

Avoid:

{amount: .2f}


# Expense Tracker Structure

expenses[]

while True:
print("1. Add expense")
print("2. Show expenses")
print("3. Show total")
print("4. Exit")

choice = input("Choose an option: ")

The while True loop keeps showing the menu.

The break statement stops the program when the user chooses Exit.


# Functions
A function is a reusable block of code.

def is used to create a function.

Example:

def greet_user():
    print("Hello")

greet_user()

Here:
def -> creates the function
greet_user -> function name
()  -> used with the function
:  -> starts the function block
greet_user() -> calls/runs the function


# Before Functions vs After Functions

# Before using def:
We wrote the code directly and python ran it from top to bottom.

name = input("What is your name? ")
print("Hello", name)

--> if we wanted to do the same task again, we had to write the same code again.

# After using def:
We can put that code inside a function.

def greet_user():
    name = input("What is your name? ")
    print("Hello", name)

--> Defining the function does NOT run it immediately.
It only creates/stores the function.

To run it,we call:
greet_user()

**MAIN DIFFERENCE:
--> Before def:
code runs directly when python reaches it.

--> After def:
code can be grouped under a name and runs only when the function is called.

*Functions help:
-avoid repeating code
-organize progress
-reuse the same code
-make larger programs easier to understand


# Parameters
A parameter allows a function to receive a value.

EXAMPLE:

def show_square(number):
    print(number*number)

show_square(5)

Here:
number --> parameter
5 --> argument/value given to the function

Output:
25


# Multiple Parameters
A function can receive multiplce values.

EXAMPLE:
def add_numbers(a, b):
    print(a + b)

add_numbers(10, 5)

Output:
15


# Local Variables
A variable created inside a function normally belongs only to that function.

EXAMPLE:

def check_numbers():
    number = 10
    print(number)

The variable number is local to check_number().


# Return
return send a value back from a function so it can be stored or used later.

EXAMPLE:

def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(5, 4)

print(result)

Output:
20

IMPORTANT:
If return is placedinside a loop, the function may stop after the first item.
Code written after return inside a function will not run.

* print() --> displays a value.
* return --> gives the value back to the program.

->Why return is useful

EXAMPLE:

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(200, 3)

if total >= 500:
     print("Free delivery")

    Here calculate_total() returns 600.

The value is stored in total and can then be used in another condition.


# Function with if-else
A function with if-else is used when the function needs to make a decision based on a condition.

If the condition is True, one block of code runs.
If the condition is False, the else block runs.

def calculate_discount(price):
    if price >= 1000:
       return price * 0.90
    else:
        return price

final_price = calculate_discount(1500)

print(final_price)

Output:
1350.0


# Function with Loop
A function can be called inside a loop so the same function can work multiple times with different values.

def check_even_odd(number):
    if number % 2 == 0:
       return "Even"
    else:
        return "Odd"

for i in range(3):
    number = int(input("Choose a number:"))
    result = check_even_odd(number)
    print(result)

IMPORTANT:
-> The loop repeats the code.
-> Each value is passed to the function.
-> the function returns a result each time.


# Running Total
We can keep adding values to one variable.

grand_total = 0

for i in range(3):
    amount = int(input("Amount:"))
    grand_total += amount

print("Grand Total:", grand_total)

IMPORTANT:
grand_total += amount
Means,
grand_total = grand_total + amount


# Input Cleaning
Used to make user input consistent before checking or storing it.

EXAMPLE:
status = input("Status:").strip().lower()

.strip() -> removes extra speces
.lower() -> converts text to lowercase

Ex- "PAID" -> "paid"


# try-except
Used to handle errors without crashing the program.

while True:
   try:
       amount = int(input("Order Amount:"))
       break
   except ValueError:
       print("Please enter a valid number.")
Here:
* try -> runs code that may cause an error
* except -> runs if that error happens
* ValueError -> can happen when python expects a  number but receives text.
* break -> stops the loop when valid input is entered


# Function Name vs Function Call
Writing only the function name does not run the function.

EXAMPLE:
get_pending_orders
* This refers to the function itself.
BUT
get_pending_orders(orders)
* This calls/runs the function.

IMPORTANT:
function_name -> function itself
function_name(...) -> runs the function


# Filtering Data
USed to keep only the data that matches a condition.

EXAMPLE:
def get_pending_orders(orders):
    pending_orders = []

    for order in orders:
        if order["status"] == "pending":
            pending_orders.append(order)

    return pending_orders
HERE:
* orders -> complete list
* order -> one dictionary from the list
* pending_orders -> stores only pending orders

IMPORTANT:
pending_orders.append(order)
adds the current matching order.


# Finding Largest Order
Used to find the order with the highest amount.

def find_largest_order(orders):
    largest_order = orders[0]

    for order in orders:
        if order["amount"] > largest_order["amount"]:
        largest_order = order
    return largest_order
HERE:
orders[0] means the first order in the list.

The program compares each order with the largest order found so far.

IMPORTANT:
largest_order
stoes the whole order dictionary.


# CSV
CSV means Comma-separated Values.
A CSV file stores data in rows and columns and can be opened in Excel.

EXAMPLE:
name,amount,status
A,500,paid
B,800,pending

To use CSV  tools in python:
import csv


# Writing data to CSV
Used to save python data into a CSV file.

def save_orders_to_csv(orders, filename):
    with open(filename, "w", newline="") as files:
        write = csv.DictWriter(
            files,
            fieldnames = ["name", "amount", "status"]
        )

        write.writeheader()
        write.writerows(orders)
HERE:
* 'w' -> write mode
*DictWriter -> writes dictionary data into CSV
* fieldnames -> column names
* writeheader() -> writes column headings
* writerows() -> writes multiple rows
To run:
save_orders_to_csv(orders, "orders.csv")


# Reading Data from CSV
Used to load CSv data back into python.

def load_orders_from_csv(filename):
    loaded_orders = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            loaded_orders.append(row)

    return loaded_orders
HERE:
* 'r' -> read mode
* DictReader -> reads each CSV row as a dictionary
* row -> one row from the CSv file


# CSV Numbers Become Strings
When data is read from CSV, numbers may come back as strings.

EXAMPLE:
CSV contains:
500
Python may read it as:
"500"
To convert it back to an integer:
row["amount"] = int(row["amount"])

IMPORTANT:
CSV data may need type conversion before calculations.


# Reusable Filename Parameter
A filename can be passed into a function as a parameter.

def save_orders_to_csv(orders, filename):
Then:
save_orders_to_csv(orders, "day21_orders.csv")

the same function can also create another file:
save_orders_to_csv(pending_orders, "pending_orders.csv")

IMPORTANT:
* open(filename, ...)
uses the value stored in filename.
BUT:
* open("filename",...)
means a file literally named filename.


# FileNotFoundError
FileNotFoundError happens when Python tries to open a file that does not exist.

try:
   with open(filename, "r", newline="") as file:
       reader= csv.DictReader(file)

except FileNotFoundError:
     print("File not found.")
     return []

This prevents the program from crashing if the file is missing.

IMPORTANT:
* try-> runs the code that may fail
* except FileNotFoundError -> handles the missing-file error
* return[] -> returns an empty list if the file is not found


# Handling Invalid CSV Data
CSV values are read as strings.
INvalid numeric values can cause ValueError.

try:
    row["amount"] = int(row["amount"])

except ValueError:
    print("Invalid Amount")
    continue

IMPORTANT:
* try attempts conversion.
* except handles an invalid value.
* continue skips the invalid row.
* Valid rows can still be processed.


# CSV Flow
Python Data
    ↓
Write CSV
    ↓
Open in Excel
    ↓
Read CSV into Python
    ↓
Convert Data Types
    ↓
Analyze / Filter Data
    ↓
Save Useful Results

IMPORTANT:
* DictWriter -> Python data to CSV

* DictReader -> CSV data to Python


# Python Modules
A module is a Python file containing reusable functions, variables or classes.
Modules help  organize code and avoid repetition.


EXAMPLE:
import math

print(math.sqrt(225))   --> 15.0
print(math.pow(5, 3))   --> 125.0
print(math.factorial(5)) --> 120


IMPORTANT:
* import allows us to use code from another module.
* math.sqrt() calculates a square root.
* math.pow(a, b) calculates a raise to power b.
* math.factorial() calculates the factorial of an integer.


# Different Import Methods
import math
from math import sqrt
from math import sqrt as square_root

-> Difference:
* import math -> use math.sqrt(25)
* from math import sqrt -> use sqrt(25)
* as -> creates an alternative name(alias)


# Creating Our Own Module
A Python file can contain functions that are imported into another Python file.

->calculations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

-->main.py
import calculations

print(calculations.add(10, 5))
print(calculations.subtract(25, 0))

Output:
15
17

IMPORTANT:
The functions are written in calculation.py, but called from main.py.
This helps separate reusable logic from the main program.


# Python Packages
A package organizes related Python modules inside a folder.

EXAMPLE STRUCTURE:

project/
├── main.py
└── helpers/
    ├── __init__.py
    └── text_tools.py

->text_tools.py
def make_uppercase(text):
    return text.upper().strip()

->main.py
from helpers.text_tools import make_uppercase

print(make_uppercase("hello python))

OUTPUT:
HELLO PYTHON

IMPORTANT:
* Module -> A Pythone file.
* Package -> A collection of related modules.
* _init_.py is commonly used in regular Python packages.
* helpers.text_tools refers to the module inside the package.


# pycache
Python may automatically create a folder named _pycache_ when importing modules.
It contains compiled Python bytecode(.pyc) files.

IMPORTANT:
* Python manages these files automatically.
* Deleting them does not delete the original .py source code.
* They normally should not be uploaded to GitHub.

.gitignore:
__pycache__/
*.pyc


# UTF-8 Encoding
UTF-8(Unicode Transformation Format - 8-bit) is a character encoding used to store and read text correctly.
It supports English, Hindi, Marathi, Japanese, emojis and many other characters.

EXAMPLE:
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello नमस्ते")

HERE:
* encoding="utf-8" -> Specifices how text is converted into bytes.
* "w" -> Opens the file in write mode.
* file.write() -> Writes text into the file.

IMPORTANT:
* UTF-8 helpsprevent text encoding problems.
* It is useful when files contain different languages or symbols.
* Use encoding="UTF-8" when working with text files.
* UTF-8 is an encoding, not encryption.


# File Paths (pathlib)
pathlib is a build-in Python module used to work with files and folder paths.

EXAMPLE:
from pathlib import Path

base = Path(_file_).resolve().parent

folder = base / "python_records"

folder,mkdir(exist_ok=True)

file = folder / "progress.txt"

file.write_text("Python Day 1 completed-8/11/26, encoding="utf-8)

print(file.read_text(encoding="utf-8))
print(file.exists())

OUTPUT:
Python Day 1 completed-8/11/26
True

HERE:
* Path() -> Creates a path object.
* _file_ -> Represents the current python script's path.
* .resolve() -> Resolves a path to an absolute path.
* .parent -> gets the parent folder.
* / -> Joins paths.
* .mkdir() -> Creates a folder.
* exist_ok=True -> Avoids an error if the folder already exists.
* .write_text() -> Writes text into a file.
* .read-text() -> reads text from a file.
* .exists() -> Checks whether a file or folder exists.

IMPORTANT:
* _file_ has two underscores on each side.
* .write_text() overwrites existing file contents.
* pathlib helps manage paths across operating systems.


# JSON
JavaScript Object Notation.
It is a text-based format used to store and exchange structured data.
* JSON is commonly used in websites, APIs and AI applications.

EXAMPLE:
{
    "name": "notebook",
    :price": 50,
    "available": true
}

IMPORTANT:
JSON is similar to a python dictionary, but it has some differences.

* Python                            JSON
  True                               true
  False                              false
  None                               null
  Dictionary                         object
  List                               Array

* FOUR JSON Functions
Python provides a built-in module called json.

1. json.dump() --> Python data to JSON file.
2. json.load() --> JSON file to Python data.
3. json.dumps() --> Python data to JSON string.
4. json.loads() --> JSON string to Python data.

IMPORTANT:
The extra s stands for string.

# Writing Data to a JSON File
json.dump() saves Python data into JSON file.

EXAMPLE:
import json

product = {
    "name": "Notebook",
    "price": 50,
    "quantity": 3,
    "available": True
}
with open("product.json", "w", encoding="utf-8") as file:
     json.dump(product, file, indent=4)

HERE:
* json.dump() -> Writes Python data as JSON.
* "w" -> Write mode.
* indent=4 -> Makes JSON easier to read.
* with open() -> Automatically closes the file.


# Reading Data from a JSON FIle
json.load() reads JSON data from a file and converts it into Python data.

EXAMPLE:
with open("product.json", "r", encoding="utf-8") as file:
     loaded_product = json.load(file)

print(loaded_product["name"])
print(loaded_product["price"] * loaded_product["quantity"])
print(loaded_product["available"])

OUTPUT:
Notebook
150
True

IMPORTANT:
* dump() -> Writes JSON to a file.
* load() -> reads JSON from a file.
* "r" -> Read mode.
* Loaded JSON objects can be accessed using dictionary keys.


# JSON Strings - dumps() and loads()
* json.dumps() converts Python data into a JSON
string.
* json.loads() converts JSON text back into Python data.

EXAMPLE:
import json

student = {
    "name": "Amit",
    "age": 20,
    "course": "Engineering"
}
json_text = json.dumps(student)

print(type(json_text))

converted = json.loads(json_text)

print(converted["course"])
print(type(converted))

OUTPUT:
<class 'str'>
Engineering
<class 'dict'>

HERE:
* dumps() -> Converts a Python dictionary into JSON text.
* loads() -> Converts JSOn text back into a dictionary.
* type() -> Checks the type of data.

IMPORTANT:
* dump() and load() work with files.
* dumps() and loads() work with strings.
* JSON is useful for transferring data between applications.


# OOP (Object-Oriented Programming)
OOP is a programming approach that organizes related data and functions into objects.
OOP helps organize programs, reuse code and manage larger applications.

IMPORTANT:
* OOP -> Objects-Oriented Programming.
* OOPS -> Another commonly used term for the same concept.
* Class -> Blueprint for creating objects.
* Object -> An instance created from a class.


# Classes and Objects
A class defines the structure of an object.
An object is created using that class.

EXAMPLE:
class Student:
    pass

student1 = Student()

student1.name = "Rahul"
student1.age = 19

print(student1.name)
print(student1.age)

OUTPUT:
Rahul
19

HERE:
* class -> Defines a class.
* student -> Class name.
* pass -> Placeholder for an empty class.
* Student() -> Creates an object.
* student1.name -> Attribute blonging to the object.


# Attriubutes and self
Attributes are variable that belong to an object or class.
self refers to the current object inside an instance method.

EXAMPLE:
class Student:
    def _init_(self,name,age):
       self.name = name
       self.age = age

student1 = Student("Rahul", 19)
student2 = Student("Amit", 20)

print(student1.name)
print(student2.name)

OUTPUT:
Rahul
Amit

IMPORTANT:
* self.name stores the name of a particular object.
* Different objects can contain different values.
* self is conventionally the first parameter of an instance method.
* When calling student1.name, we access an attribute.


# init() Method
_init_() is a special method to initialize an object's attributes.
It runs automatically during normal object creation.

EXAMPLE:
class Product:
    def _init_(self, name, price):
       self.name = name
       self.price = price

product1 = Product("Notebook", 50)

HERE:
* _init_() -> initializes object attributes.
* self -> Refers to the current object.
* name, price -> Parameters.
* self.name = name -> Stores the name in the object.

IMPORTANT:
_init_ has two underscores, before and after init.


# Methods in OOP
A method  is a function defined inside a class.
Methods allow objects to perform actions and calculations.

EXAMPLE:
class Product:
    def _init_(self, name, price, quantity):
       self.name = name
       self.price = price
       self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

product1 = Product("Notebook", 50, 3)

print(product1.calculate_total())

OUTPUT:
150

HERE:
* calculate_total() -> Method.
* self.price -> Accesses the object's price.
* self.quantity -> Accesses its quantity.
* product1.calculate_total() -> Calls the method.


# Calling One Method from Another
A method can call another method belonging to the same object.

EXAMPLE:
def discounted_price(self):
    total = self.calculate_total()
    discount = total * 10 / 100
    return total - discount

HERE:
* self.calculate_total() -> Calls another method of the object.
* total -> local variable.

IMPORTANT:
* self.discounted_total would be an instance attribute.
* % in Python means remainder, not percentage.


# Inheritance
INheritance allows a child class to reuse or extend the attributes and methods of a parent class.

EXAMPLE:
class Product:
    def _init_(self, name, price):
       self.name = name
       self.price = price

    def show_details(self):
        print(self.name, self.price)

class DigitalProduct(Product):
    pass

product1 = DigitalProduct("Python Ebook", 200)

product1.show_details()

OUTPUT:
Python Ebook 200

HERE:
* Product -> Parent class.
* DigitalProduct -> Child class.
* DigitalProduct(Product) -> Establishes inheritance.
* pass -> no additional code in the child class.
* The child class inherits the parent's functionality.


# Child Class Methods
A child class can also contain its own methods.

EXAMPLE:
A child class can also contain its own methods.

EXAMPLE:
class DigitalProduct(Product):
    def download(self):
        print("Downloading", self.name)

    def file_info(self):
        print(self.name, "is available as a digital file.")

IMPORTANT:
A child class can use both inherited methods and its own methods.


# super() in Python
super() allows a child class to access methods from its parent class according to Python's inheritance order.
It is commonly used to call the parent's _init_() method.

EXAMPLE:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size


product1 = DigitalProduct("Python Course", 500, 250)

print(product1.name)
print(product1.price)
print(product1.file_size)

OUTPUT:
Python Course
500
250

HERE:
* super()._init_(name, price) -> Calls the parent initialization method.
* self.file.size -> New attribute belonging to the child object.
* The child reuses the parent's initialization code.


# Four MAin OOP Priniciples
1. Encapsulation --> Grouping related data and methods together, with access control when needed.
2. Inheritance --> Reusing and extending functionality from another class.
3. Polymorphism --> Different objects can respond differently to the same method or interface.
4. Abstraction --> Hiding implementation details and exposing essential functionality.

These are introductory definitions.
Classes, methods and inheritance are practised.


# Common OOP Mistakes
* Writing self outside an instance method.
* Incorrect indentation inside classes and methods.
* Forgetting to call a method using ()
* Confusing local variables with self attributes.
* Misspelling _init_ .
* Forgetting super()._init_() when parent initialization is required.


# pip (Python Package Installer)
pip is used to install and manage external Python packages.

EXAMPLE:
python -m pip install requests
python -m pip list
python -m pip show requests

IMPORTANT:
* Python's standard library includes modules such as math, json and pathlib.
* External packages such as requests may need installation.
* PyPI is a public repository of Python packages.


# Virtual Environments (venv)
A virtual environment provides an isolated Python environment for a project.

EXAMPLE (Windows PowerShell):

python -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install requests

IMPORTANT:
* Different projects can have different packages.
* .venv stores the local Python environment.
* Add .venv/ to .gitignore.
* Do not upload virtual environments to Github.


# Useful Standard Libraries
- datetime is used for dates and times.

from datetime import datetime

print(datetime.now())

- random is used to generate random values.

import random

print(random.randint(1, 10))


# API (Application Programming Interface)
An API allows software applications to communicate through defined interfaces.
A web API can receive HTTP requests and return structured information, commonly JSON.

EXAMPLE URL:

https://jsonplaceholder.typicode.com/posts/1

HERE:
* https:// -> Protocol.
* jsonplaceholder.typicode.com -> Domain.
* /posts -> Resource path.
* /1 -> Resource ID.

An API endpoint identifies a resource or operation exposed by an API.


# HTTP Request Methods
* GET -> Retrieve information.
* POST -> Submit or create information.
* PUT -> Replace a resource.
* PATCH -> Partially update a resource.
* DELETE -> request resource deletion.

EXAMPLE:

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

print(data["title"])

HERE:
* requests.get() -> Sends a GET request,
* timeout=10 -> Limits how long an API request waits for connection or response activity, measured in seconds. It does not control the website's refresh rate.
* raise_for_status() -> Raises an exception for unsuccessful HTTP status codes.
* response.json() -> Parses JSON into Python data.


# Sending JSON Data
EXAMPLE:

new_post = {
    "title": "My Python Journey",
    "body": "Learning APIs",
    "userId": 5
}

response = requests.post(url, json=new_post, timeout=10)

json=new_post sends the dictionary as JSON.

PUT and PATCH use similar syntax with requests.put() and requests.patch().


# HTTP Status Codes
* 200 -> Successful request.
* 201 -> Resource created.
* 204 -> Successful request with no response body.
* 400 -> Bad request.
* 401 -> Authentication required or invalid.
* 403 -> Forbidden.
* 404 -> Resource not found.
* 500 -> Server error.


# API Error Handling
EXAMPLE:

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("HTTP request failed.")

except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Connection failed.")

IMPORTANT:
API requests may fail due to network problems, servor errors or invalid requests.
Use timeouts and exception handling.


# requirements.txt
A requirements.txt file records the external packages required by a Python project.

EXAMPLE:
request==2.34.2

Install packages using:
python -m pip install -r requirements.txt

IMPORTANT:
* == specifies an exact package version.
* pip freeze lists installed package versions.
* Upload requirement.txt not .venv.
* Never publish API keys or passwords in project files.


