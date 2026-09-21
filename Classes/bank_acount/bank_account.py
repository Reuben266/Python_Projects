import bank_account_class as ba
import json

account_list = []
def convert_to_class_instance():
    try:
      with open('account.json', 'r') as file:
        accounts = json.load(file)
        for account in accounts:
          if account['account_type'] == "BankAccount":
            banking = ba.BankAccount(account['name'], account['phone_number'], account['email'], account['balance'])
            banking._amount_owed = account['amount_owed']
            banking.transaction = account['transaction history']
            account_list.append(banking)
          if account['account_type'] == "SavingsAccount":
            saving = ba.SavingsAccount(account['name'], account['phone_number'], account['email'], account['age'], account['balance'])
            saving._amount_owed = account['amount_owed']
            saving.transaction = account['transaction history']
            account_list.append(saving)
        return account_list
    except FileNotFoundError:
      print("File Not Found")
convert_to_class_instance()

def value(prompt):
  while True:
    try:
     return float(input(prompt))
    except ValueError:
      print("Invalid Input")
      

user_options = ["[1] Add Bank Account 🏛️➕", "[2] Add Savings Account 🐷➕", "[3] Deposit 💵📥", "[4] Withdraw 💵📤", "[5] Take loan 🤝💵", "[6] Pay loan 💳✅", "[7] Save and Exit 💾🚪"]

while True:
  print("=" * 20, "USER OPTIONS", "=" * 20)
  for option in user_options:
    print(option)
  print("=" * 54)

  try:
    choice = int(input("\nWhat would you like to do:  "))
  except ValueError:
    print("Invalid input")
    continue

  print("\n")
  if choice == 1:
    account_type = "BankAccount"
    name = input("Enter account name::  ")
    phone_number = input("What is your phone number::  ")
    email = input("Enter your email:: ")
    print("\n")

    Bank = ba.BankAccount(name, phone_number, email)
    account_list.append(Bank)

  elif choice == 2:
    name = input("Enter account name::  ")
    phone_number = input("What is your phone number::  ")
    email = input("Enter your email:: ")
    age = value(("What is you age::  "))
    print("\n")

    Save = ba.SavingsAccount(name, phone_number, email, age)
    account_list.append(Save)

  elif choice == 3:
    phone = input("Enter your phone number::  ")
    
    found = False
    for account in account_list:
      if account.phone_number == phone:
        account_name = account.name
        found = True
        break
          
    if found:
      print("=" * 20, "ACCOUNT NAME", "=" * 20)
      print(account_name)
      print("=" * 54)
      print("\n")

      verification = input("Verify the name of the account (yes/no):  ").lower().strip()
      print("\n")
        
      if verification == "no":
        print("=" * 54)
        print("Account not found")
        print("=" * 54)
        print("\n")
      elif verification == "yes":
        amount = value(("How much do you want to deposit::  "))
        print("\n")
        print("=" * 54)
        account.deposit(amount)
        print("=" * 54)
        print("\n")
      else:
        print("=" * 54)
        print("Invalid Input")
        print("=" * 54)
        print("\n")
    else:
      print("=" * 54)
      print("Account not found")
      print("=" * 54)
      print("\n")

  elif choice == 4:
    phone = input("Enter your phone number::  ")
    
    found = False
    for account in account_list:
      if account.phone_number == phone:
        found = True
        break
          
    if found:
      print("=" * 20, "ACCOUNT NAME", "=" * 20)
      account_name = account.name
      print(account_name)
      print("=" * 54)
      print("\n")

      verification = input("Verify the name of the account (yes/no):  ").lower().strip()
      print("\n")

      if verification == "no":
        print("=" * 54)
        print("Account not found")
        print("=" * 54)
        print("\n")
      elif verification == "yes":
        amount = value(("How much do you want to Withdraw::  "))
        print("\n")
        print("=" * 54)
        account.withdraw(amount)
        print("=" * 54)
        print("\n")
      else:
        print("=" * 54)
        print("Invalid Input")
        print("=" * 54)
        print("\n")
          
    else:
      print("=" * 54)
      print("Account not found")
      print("=" * 54)
      print("\n")

  elif choice == 5:
    phone = input("Enter your phone number::  ")
    
    found = False
    for account in account_list:
      if account.phone_number == phone:
        found = True
        break
          
    if found:
      print("=" * 20, "ACCOUNT NAME", "=" * 20)
      account_name = account.name
      print(account_name)
      print("=" * 54)
        
      print("\n")
      verification = input("Verify the name of the account (yes/no):  ").lower().strip()
      print("\n")

      if verification == "no":
        print("=" * 54)
        print("Account not found")
        print("=" * 54)
        print("\n")
      elif verification == "yes":
        amount = value(("Enter loan amount::  "))
        duration = value(("Enter the duration of the loan::  "))
        print("\n")
        print("=" * 54)
        account.loan(amount, duration)
        print("=" * 54)
        print("\n")
      else:
        print("=" * 54)
        print("Invalid Input")
        print("=" * 54)
        print("\n")
          
    else:
      print("=" * 54)
      print("Account not found")
      print("=" * 54)
      print("\n")

  elif choice == 6:
    phone = input("Enter your phone number::  ")
    
    found = False
    for account in account_list:
      if account.phone_number == phone:
        found = True
        break
          
    if found:
      print("=" * 20, "ACCOUNT NAME", "=" * 20)
      account_name = account.name
      print(account_name)
      print("=" * 54)
      print("\n")

      verification = input("Verify the name of the account (yes/no):  ").lower().strip()
      print("\n")

      if verification == "no":
        print("=" * 54)
        print("Account not found")
        print("=" * 54)
        print("\n")
      elif verification == "yes":
        amount = value("Enter amount::  ")
        print("=" * 54)
        account.pay_loan(amount)
        print("=" * 54)
        print("\n")
      else:
        print("=" * 54)
        print("Invalid Input")
        print("=" * 54)
        print("\n")
    else:
      print("=" * 54)
      print("Account not found")
      print("=" * 54)
      print("\n")

  elif choice == 7:
    saved_account = []
    for account in account_list:
      finished = account.convert_to_class_instance_to_dic()
      saved_account.append(finished)

    with open('account.json', 'w') as file:
      json.dump(saved_account, file, indent = 5)

    break
 
  else:
    print("\n")
    print("=" * 54)
    print("Invalid Input!, Try again")
    print("=" * 54)
    print("\n")
    continue