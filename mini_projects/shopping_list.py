shopping_list = []

while True:
    print("\nShopping List Menu")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item= input("Enter item name: ")
            shopping_list.append(item)
            print("Item added!")

        elif choice == 2:
            if len(shopping_list) == 0:
                print("Your shopping list is empty")
            else:
                print("\nYour Shopping List:")
                for item in shopping_list:
                    print("-", item)
                       
        elif choice == 3:
            # remove item here
            pass

        elif choice ==4:
            print("Existing program...")
            break

        else:
            print("Invalid choice. Choose 1 to 4.")

    except ValueError:
        print("PLease enter a valid number")

