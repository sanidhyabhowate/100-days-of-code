#print() Function
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


#input() Function
Used to take input from the user

Example:
name = input("Enter your name:")
age = int(input("Enter you age:"))

IMPORTANT:
input gives data as text(string).
Use int() to convert number.


#Variables
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
1age = 18
student name = "Rahul"


#Data Types
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



#Operators
Operators are used to perform calculations and comparison.

-Arithmatic Operators

+   Addition
-   Subtraction
*   Multiplication
/   Division(3)
//  Floor Division(3.3333333)
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


#Loops
Used to repeat code.

for i in range(5):
    print(i)

    range(5)
→ 0,1,2,3,4

range(1,11)
→ 1 to 10

range(2,21,2)
→ Even numbers


#While Loops
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

If we di not update the variable, the loop may never stop.

This is called an infinite loop.

#for loop vs while loop

for loop:
Used when we know how many times we want to repeat.

Example:
fir i in range(5):
    print(i)

while loop:
Used when we want to repeat until a condition becomes false.

Example:
password = ""

While password != "python":
    password = input("Enter password: ")

print("Access granted")

Here,the program keeps asking for password until the user enters python.


#While Loops With Chances
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

