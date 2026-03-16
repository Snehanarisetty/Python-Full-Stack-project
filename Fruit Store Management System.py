cart = []
fruits = ['apple', 'orange', 'mango', 'banana']

while True:
    print("\nMANAGEMENT")
    print("1. Owner")
    print("2. User")
    print("3. Exit")

    role = int(input("Select role: "))
    if role == 1:
        while True:
            print("\n--- OWNER SECTION ---")
            print("1. Add Fruit")
            print("2. Remove Fruit")
            print("3. View Inventory")
            print("4. Exit Owner")

            ch = int(input("Choose option: "))

            if ch == 1:
                fruit = input("Enter fruit name: ")
                if fruit not in fruits:
                    fruits.append(fruit)
                    print(fruit, "added to inventory")
                else:
                    print("Fruit already exists")

            elif ch == 2:
                fruit = input("Enter fruit name: ")
                if fruit in fruits:
                    fruits.remove(fruit)
                    print(fruit, "removed from inventory")
                else:
                    print("Fruit not found")

            elif ch == 3:
                print("\n--- INVENTORY ---")
                for f in fruits:
                    print(f)

            elif ch == 4:
                break

            else:
                print("Choose correct option")
    elif role == 2:
        while True:
            print("\nAvailable Fruits:")
            for f in fruits:
                print(f)

            print("*" * 30)
            print("1. Add")
            print("2. Remove")
            print("3. View Cart")
            print("4. Checkout")

            ch = int(input("Choose one option: "))

            if ch == 1:
                fruit = input("Which fruit: ")
                if fruit in fruits:
                    if fruit in cart:
                        print(fruit, "is already in cart")
                    else:
                        cart.append(fruit)
                        print(fruit, "is added successfully")
                else:
                    print(fruit, "is not available")

            elif ch == 2:
                fruit = input("Which fruit: ")
                if fruit in cart:
                    cart.remove(fruit)
                    print(fruit, "has been removed from cart")
                else:
                    print(fruit, "is not there in cart")

            elif ch == 3:
                print("\n********** CART **********")
                if cart:
                    for f in cart:
                        print(f, end=" ")
                    print()
                else:
                    print("Cart is empty")
                print("*" * 26)

            elif ch == 4:
                print("Done!!!!")
                cart.clear()
                break

            else:
                print("Choose correct option")
    elif role == 3:
        print("Thank you!")
        break

    else:
        print("Invalid selection")
