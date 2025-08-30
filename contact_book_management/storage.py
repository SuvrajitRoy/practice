import json
from contact import Contact

CONTACTS_FILE = "contacts.json"

#File read/write operations and store 

def load_contacts():  
    try:
        with open(CONTACTS_FILE, "r") as file:
            data = json.load(file)
            return [Contact.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=2) 