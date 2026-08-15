import sys
import json

try:
  with open("contacts.json", "r") as my_contacts:
    contacts = json.load(my_contacts)
except FileNotFoundError:
  contacts = {}

user_options = ["[1] Add Contact", "[2] View All Contacts", "[3] Delete Contact", "[4] Save & Exit"]

while True:
  print("="*48)
  for options in user_options:
    print(options)
  print("="*48)
  

  try:
    user_choice = int(input("What would you like to do:: "))
    
  except ValueError:
    print("="*48)
    print("Invalid input")
    print("="*48)
    print("\n")
    continue

  if user_choice == 1:
    print("="*48)
    name = input("Enter name:: ").lower()
    number = input("Enter number:: ")
    print("="*48)
    contacts[name] = number

  elif user_choice == 2:
    if len(contacts) == 0:
      print("="*48)
      print("No saved contact")
      print("="*48)
      print("\n")
    else:
      
      print("="*48)
      for people in contacts:
        print(people, ":", contacts.get(people))
      print("="*48)
      
  elif user_choice == 3:
    if len(contacts) == 0:
      print("="*48)
      print("No saved contacts")
      print("="*48)
      print("\n")
    else:
      name_contact = input("Name the contact you want to Delete:: ").lower()
      if name_contact in contacts:
        print("="*48)
        print("found")
        print("="*48)
        del contacts[name_contact]
      else:
        print(f"{name_contact} do not exist")

  elif user_choice == 4:
      with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

      sys.exit()