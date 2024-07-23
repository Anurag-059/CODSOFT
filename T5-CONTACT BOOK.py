# Contact Management System

class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone]
        if not results:
            print("No matching contacts found!")
        else:
            print("Search Results:")
            for i, contact in enumerate(results, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name == name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                print(f"Contact '{name}' updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print("Contact not found!")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number (optional): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            manager.update_contact(name, phone, email, address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            manager.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "_main_":
    main()