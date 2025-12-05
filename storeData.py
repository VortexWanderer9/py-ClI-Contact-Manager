def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    if contacts:
        for name, details in contacts.items():
            print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Found contact for {name}: Phone - {details['phone']}, Email - {details['email']}")
    else:
        print(f"No contact found for {name}.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print(f"No contact found for {name}.")

def main():
    contacts = {}
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()
