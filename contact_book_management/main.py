from contact_manager import ContactManager
from menu import print_menu

def get_int_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("~~The phone number must be an integer.")
        return None

def main():
    manager = ContactManager()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            # Add Contact
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            phone = get_int_input("Enter Phone Number: ")
            if phone is None:
                continue
            address = input("Enter Address: ").strip()
            try:
                manager.add_contact(name, email, phone, address)
                print("Contact added successfully!")
            except ValueError as ve:
                print(f"~~{ve}")
        elif choice == '2':
            # View Contacts
            contacts = manager.get_all_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- All Contacts ---")
                for c in contacts:
                    print(c)
                    print("-" * 30)
        elif choice == '3':
            # Remove Contact
            phone = get_int_input("Enter phone number of contact to remove: ")
            if phone is None:
                continue
            removed = manager.remove_contact(phone)
            if removed:
                print("Contact deleted successfully!")
            else:
                print("No contact found with that phone number.")
        elif choice == '4':
            # Search Contacts
            keyword = input("Enter keyword to search: ").strip()
            results = manager.search_contacts(keyword)
            if not results:
                print("No matching contacts found.")
            else:
                print("\n--- Search Results ---")
                for c in results:
                    print(c)
                    print("-" * 30)
        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")

if __name__ == "__main__":
    main() 