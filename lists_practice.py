tasks = ["PYthon", "Typing", "Exercise", "Anime"]

print("Today's tasks:")
for task in tasks:
    print("-", task)

print("\nFirst task:", tasks[0])
print("Last task:", tasks[-1])

tasks.append("Cooking")
print("\nUpdated tasks:")
for task in tasks:
    print("-", task)

    tasks[1] = "Typing Practice"
tasks.remove("Anime")

print("\nFinal tasks:")
for task in tasks:
    print("-", task)