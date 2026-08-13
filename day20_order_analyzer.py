import csv

def save_orders_to_csv(orders):
    with open("orders.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ["name", "amount", "status"]
        )

        writer.writeheader()
        writer.writerows(orders)

orders = []

for i in range(3):
    name = input("Customer name:")
    status = input("Status:").strip().lower()
    while True:
        try:
            amount = int(input("Order Amount:"))
            break
        except ValueError:
            print("Please enter Valid Number.")

    order = {
        "name": name,
        "amount": amount,
        "status": status
    }

    orders.append(order)

save_orders_to_csv(orders)

for order in orders:
    print(order)

def calculate_total(orders):
    total = 0

    for order in orders:
        total += order["amount"]

    return total

total_amount = calculate_total(orders)
print("Total Order Value:", total_amount)


def count_status(orders):
    paid = 0
    pending = 0

    for order in orders:
        if order["status"] == "paid":
            paid += 1
        elif order["status"] == "pending":
            pending += 1

    return paid, pending

paid_count, pending_count = count_status(orders)

print("Paid Orders:", paid_count)
print("Pending Orders:", pending_count)

def calculate_revenue_by_status(orders):
    paid_revenue = 0
    pending_revenue = 0

    for order in orders:
        if order["status"] == "paid":
            paid_revenue += order["amount"]
        elif order["status"] == "pending":
            pending_revenue += order["amount"]

    return paid_revenue, pending_revenue 

paid_revenue, pending_revenue = calculate_revenue_by_status(orders)

print("paid Revenue:", paid_revenue)
print("pending Revenue:", pending_revenue)

def find_largest_order(orders):
    largest_order = orders[0]

    for order in orders:
        if largest_order["amount"] < order["amount"]:
            largest_order = order

    return largest_order

Highest_Amount = find_largest_order(orders)

print("Largest Order:",Highest_Amount)

def load_orders_from_csv():
    orders = []
