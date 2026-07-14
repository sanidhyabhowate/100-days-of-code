expense_name = input("Enter expense name: ")
category = input("Enter category: ")

try:
    amount = float(input("Enter amount: Rs."))

    print("\nExpense Details")
    print("Expense name:", expense_name)
    print("Amount:Rs.", amount)
    print("category:", category)

except ValueError:
    print("Invalid amount. Please enter a number.")