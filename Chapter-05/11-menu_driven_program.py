choice = ""

while choice != "6":
    print("\n ====Menu====")
    print("1. Burger")
    print("2. Pizza")
    print("3. Coffee")
    print("4. Pasta")
    print("5. Cold Drinks")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        print("Burger Ordered")

    elif choice == "2":
        print("Pizza Ordered")

    elif choice == "3":
        print("Coffee Ordered")

    elif choice == "4":
        print("Pasta Ordered")

    elif choice == "5":
        print("Cold Drinks")

    elif choice == "6":
        print("Thank You!")

    else:
        print("Invalid Choice. Please select a valid option.")    