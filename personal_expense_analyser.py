expenses = []

name = input("What do you want to add:")

amount = int(input("What is the price:"))

expense = {
    "name": name ,
    "amount": amount 
}
expenses.append(expense)

print(expenses)

