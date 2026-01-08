def display_menu():
    menu_dic = {
        1: "Add Contact",
        2: "View Contact",
        3: "Edit Contact",
        4: "Delete Contact",
        5: "List All Contacts",
        6: "Exit"
        }

    print("Contact Book Menu:")
    for key, value in menu_dic.items():
        print(f"{key}. {value}")

def add_contact(contact_book):
    
    name = input()
    phone = input()
    email = input()
    address = input()

    if name not in contact_book:
        contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
        }
        print("Contact added successfully!")
    
    else:
        print("Contact already exists!")

def view_contact(contact_book):
    name = input()

    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()

    if name not in contact_book:
        print("Contact not found!")
        return
    
    # New values
    new_phone = input()
    new_email = input()
    new_address = input()
        
    if new_phone == "":
        new_phone = contact_book[name]["phone"]
    if new_email == "":
        new_email = contact_book[name]["email"]
    if new_address == "":
        new_address = contact_book[name]["address"]
    
    contact_book[name] = {
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }

    print("Contact updated successfully!")

def delete_contact(contact_book):
    name = input()

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):

    if contact_book == {}:
        print("No contacts available.")
        return
    
    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print()
# Driver
contact_book = {}

while True:
    display_menu()
    choice = int(input())

    if choice == 6:
        break
    
    if choice == 1:
        add_contact(contact_book)
    elif choice == 2:
        view_contact(contact_book)
    elif choice == 3:
        edit_contact(contact_book)
    elif choice == 4:
        delete_contact(contact_book)
    elif choice == 5:
        list_all_contacts(contact_book)
    else:
        print("Invalid choice. Please try again")



