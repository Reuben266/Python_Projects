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
          if account['account_type'] == "Savings Account":
            saving = ba.SavingsAccount(account['name'], account['phone_number'], account['email'], account['age'], account['balance'])
            account_list.append(saving)

        return account_list
    except FileNotFoundError:
      accounts = []
convert_to_class_instance()

user_options = ["[1] Add Bank Account", "[2] Add Savings Account", "[3] Deposit", "[4] Withdraw", "[5] Take loan", "[6] Pay loan", "[7] Save and Exit"]

while True:
  for option in user_options:
    print(option)

  try:
    choice = int(input("What would you like to do:  "))
  except ValueError:
    print("Invalid input")
    continue

  if choice == 1:
    account_type = "BankAccount"
    name = input("Enter account name::  ")
    phone_number = input("What is your phone number::  ")
    email = input("Enter your email:: ")

    Bank = ba.BankAccount(name, phone_number, email)
    account_list.append(Bank)

  elif choice == 2:
    account_type = "BankAccount"
    name = input("Enter account name::  ")
    phone_number = input("What is your phone number::  ")
    email = input("Enter your email:: ")
    age = int(input("What is you age::  "))

    Save = ba.SavingsAccount(name, phone_number, email, age)
    account_list.append(Save)

  elif choice == 3:
    phone = input("Enter your phone number::  ")
    verification = input("Enter your phone number again::  ")

    if phone != verification:
      print("Phone number mismatch!")
      continue
    else:
      found = False
      for account in account_list:
        if account.phone_number == phone:
          found = True
          break
          
      if found:
        amount = int(input("How much do you want to deposit::  "))
        account.deposit(amount)
      else:
        print("Account not found")

  elif choice == 4:
    phone = input("Enter your phone number::  ")
    verification = input("Enter your phone number again::  ")

    if phone != verification:
      print("Phone number mismatch!")
      continue
    else:
      found = False
      for account in account_list:
        if account.phone_number == phone:
          found = True
          break
          
      if found:
        amount = int(input("How much do you want to Withdraw::  "))
        account.withdraw(amount)
      else:
        print("Account not found")

  elif choice == 5:
    phone = input("Enter your phone number::  ")
    verification = input("Enter your phone number again::  ")

    if phone != verification:
      print("Phone number mismatch!")
      continue
    else:
      found = False
      for account in account_list:
        if account.phone_number == phone:
          found = True
          break
          
      if found:
        amount = int(input("Enter loan amount::  "))
        duration = int(input("Enter the duration of the loan"))
        account.loan(amount, duration)
      else:
        print("Account not found")

  elif choice == 6:
    phone = input("Enter your phone number::  ")
    verification = input("Enter your phone number again::  ")

    if phone != verification:
      print("Phone number mismatch!")
      continue
    else:
      found = False
      for account in account_list:
        if account.phone_number == phone:
          found = True
          break
          
      if found:
        amount = int(input("Enter amount::  "))
        account.pay_loan(amount)
      else:
        print("Account not found")

  elif choice == 7:
    saved_account = []
    for account in account_list:
      finished = account.convert_to_class_instance_to_dic()
      saved_account.append(finished)

    with open('account.json', 'w') as file:
      json.dump(saved_account, file, indent = 5)

    break