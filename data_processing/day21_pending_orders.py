import csv

pending_orders = []
total = 0

try:
    with open("day21_orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                row["amount"] = int(row["amount"])

            except ValueError:
                print("Invalid amount for:", row["name"])
                continue

            if row["status"] == "pending":
              pending_orders.append(row)
              total += row["amount"]
              print(row["name"], row["amount"])


except FileNotFoundError:
    print("Error: Input CSV file not found.")
    raise SystemExit(1)

print("Total Pending Amount:", total)

with open("pending_orders.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name","amount", "status"]
    )

    writer.writeheader()
    writer.writerows(pending_orders)

print("Pending Orders saved successfully.")

print("\nReading Saved Pending Orders:")

with open("pending_orders.csv","r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


