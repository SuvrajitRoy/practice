class Contact:
    def __init__(self, name, email, phone, address):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("The contact’s name must be a string.")
        if not isinstance(phone, int):
            raise ValueError("The phone number must be an integer.")
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone
        self.address = address.strip()

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            data["name"],
            data["email"],
            int(data["phone"]),
            data["address"]
        )

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}"
