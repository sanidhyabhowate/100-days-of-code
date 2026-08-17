import csv

orders = [
    {
        "name": "A",
        "amount":500,
        "status": "paid"
    },
    {
        "name": "H",
        "amount": 10000,
        "status": "paid"
    },
    {
        "name": "K",
        "amount": 65000,
        "status": "pending"
        
    }
]

def save_orders_to_csv(orders, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "amount", "status"]
        )
 
        writer.writeheader()
        writer.writerows(orders)

save_orders_to_csv(orders, 'day21_orders.csv')
        

for order in orders:
    print(order)

def load_orders_from_csv(filename):
    loaded_orders = []

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["amount"] = int(row["amount"])
                loaded_orders.append(row)

    except FileNotFoundError:
            print("File not found.")
            return []

    return loaded_orders

loaded_orders = load_orders_from_csv("day21_orders.csv")
print(loaded_orders)


def calculate_total(orders):
    total = 0

    for order in orders:
        total += order["amount"]

    return total
total_amount = calculate_total(loaded_orders)
print("Total:", total_amount)


def get_pending_orders(orders):
    pending_orders = []

    for order in orders:
        if order["status"] == "pending":
            pending_orders.append(order)

    return pending_orders

pending_orders = get_pending_orders(loaded_orders)
print("Pending Orders:", pending_orders)

save_orders_to_csv(pending_orders, "pending_orders.csv")





    







