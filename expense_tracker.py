expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: Rs."))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour expenses:")

            for expense in expenses:
                print(f"{expense['name']}: Rs.{expense['amount']:.2f}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total expenses: Rs.{total:.2f}")

    elif choice == "4":
        print("Closing Expense Tracker.")
        break

    else:
        print("Invalid option. Choose 1, 2, 3 or 4.")