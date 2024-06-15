contacts = {}

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact():
    search = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

/*OUTPUT


Contact Management System
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1
Enter the contact name: SHRUTHI
Enter the phone number: 65578900532
Enter the email address: SHRUTHI123@gmail.com
Enter the address: madurai
Contact added successfully.

Contact Management System
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice:*/
