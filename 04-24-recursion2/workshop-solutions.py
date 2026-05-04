import json

def menu():

  while True:
    print("\nMenu Options:")
    print("(1) List Contacts")
    print("(2) Add Contact")
    print("(3) Exit")
    choice = input("\nChoose option: ")

    if choice == "1":
      list_contacts()

    elif choice == "2":
      add_contact()

    elif choice == "3":
      print("Goodbye.")
      exit()

    else:
      print("Invalid option, try again.")

def list_contacts():
  contacts = load_contacts()

  if len(contacts) > 0:
    # list contacts in table format
    print(f"{"NAME":<20} | {"PHONE":<20}")
    for contact in contacts:
      print(f"{contact["name"]:<20} | {contact["phone"]:<20}")
  else:
    print("Address book is empty. Add a contact first.")

def add_contact():
  name = input("Name: ")
  phone = input("Phone: ")

  contacts = load_contacts()
  contacts.append({"name": name, "phone": phone})

  # sorts contacts by name in ascending order
  contacts.sort(key=sort)

  # prepare json string for file
  contacts = json.dumps(contacts, indent=2)

  f = open("data.json", "w")
  f.write(contacts)
  f.close()

  print(f"{name} was added.")

def sort(person):
  # we want to sort by name
  return person["name"]

def load_contacts():
  try:
    # load contacts from data.json file if it exists.
    f = open("data.json")
    contacts = f.read()
    f.close()

    # convert json string to a python list of dicts
    return json.loads(contacts)

  # in case there is no database yet return an empty list.
  except FileNotFoundError:
    return []

def main():
  menu()

main()
