
contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to search: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                break
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to update: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contact["phone"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found!")

    elif choice == 5:
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n===== SAVED CONTACTS =====")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("----------------------")

    elif choice == 6:
        print("Exiting Contact Book. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
