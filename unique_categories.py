expenses = [

    {"name": "Lunch", "category": "Food"},
    {"name": "Bus", "category": "Travel"},
    {"name": "Dinner", "category": "Food"},
    {"name": "Notebook", "category": "Education"},
    {"name": "Train", "category": "Travel"}

]

categories = set()

for expense in expenses:
    categories.add(expense["category"])

print("Unique Categories:")

    #for category in categories:
        #print(category)


if "Food" in categories:
    print("Food Category Exists")


categories.discard("Travel")
print(categories)
    
                                                   
    
    
    

