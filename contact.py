# Step 1: Create an empty dictionary (Address Book)
contacts = {}

print("--- Smart Contact Book ---")

while True:
    # Step 2: Show a menu
    print("\nOptions: 1. Add  2. Search  3. Exit")
    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        # Step 3: Add a new contact
        name = input("Enter friend's name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact saved!")

    elif choice == '2':
        # Step 4: Search for a contact
        search_name = input("Enter name to search: ")
        
        if search_name in contacts:
            print(search_name + "'s number is: " + contacts[search_name])
        else:
            print("Sorry, contact not found!")

    elif choice == '3':
        # Step 5: Exit the app
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")