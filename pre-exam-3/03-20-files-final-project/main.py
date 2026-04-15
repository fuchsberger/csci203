f = open("test.txt", "r")
text = f.read()
f.close()

print(text)


f = open("test.txt", "w")
f.write("Hello Class")
f.close()


def menu():
    print("(1) Add Contact")
    print("(2) List Contacts")
    print("(3) Exit")


def main():

    while(True):
        menu()
        choice = input("Press a key: ")

        if choice == "1":
            handle_add()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            print("Goodbye.")
            return

        else:
            print("Invalid Option. Try again.")

def handle_add():
    name = input("Name: ")
    number = input("Phone number:")

    # TODO: add it to file

    f = open("database.csv", "a")

    f.write(f"{name},{number}")
    f.close()

    print(name, " has been added to the contacts.")

def show_contacts():
    f = open("database.csv")
    print(f.read())
    f.close()

main()
