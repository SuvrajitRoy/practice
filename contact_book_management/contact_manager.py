from contact import Contact
import storage

#Core logic for managing contacts

class ContactManager:
    def __init__(self):
        self.contacts = storage.load_contacts()

    def add_contact(self, name, email, phone, address):
        # Prevent duplicate phone numbers
        for c in self.contacts:
            if c.phone == phone:
                raise ValueError("Phone number already exists for another contact.")
        contact = Contact(name, email, phone, address)
        self.contacts.append(contact)
        storage.save_contacts(self.contacts)

    def remove_contact(self, phone):
        for i, c in enumerate(self.contacts):
            if c.phone == phone:
                del self.contacts[i]
                storage.save_contacts(self.contacts)
                return True
        return False

    def get_all_contacts(self):
        return self.contacts

    def search_contacts(self, keyword):
        keyword = str(keyword).lower()
        results = []
        for c in self.contacts:
            if (keyword in c.name.lower() or
                keyword in c.email.lower() or
                keyword in str(c.phone) or
                keyword in c.address.lower()):
                results.append(c)
        return results