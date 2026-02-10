contacts ={}
def addcontact():
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact details with user name {name} is available in contacts.")
        return
    else:
        mobile = input("Enter your mobile number: ")
        email = input("Enter your email id: ")
        contacts[name] = {'mobile': mobile, 'email': email}

def viewvalue():
    for k,v in contacts.items():
        print(f"{k}\t{v['mobile']}\t{v['email']}")

while True:
    print("Enter your choice:")
    print("1. Add Contact\n2. View all Contacts\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addcontact()
    elif choice == 2:
        viewvalue()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")

