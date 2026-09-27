import json
import bank_account_class as ba

 
def convert_to_class_instance(file_name):
    account_list = []
    try:
      with open(file_name, 'r') as file:
        accounts = json.load(file)
        for account in accounts:
          if account['account_type'] == "BankAccount":
            banking = ba.BankAccount(account['name'], account['phone_number'], account['email'], account['balance'])
            banking._amount_owed = account['amount_owed']
            banking.transaction = account['transaction history']
            account_list.append(banking)
          elif account['account_type'] == "SavingsAccount":
            saving = ba.SavingsAccount(account['name'], account['phone_number'], account['email'], account['age'], account['balance'])
            saving._amount_owed = account['amount_owed']
            saving.transaction = account['transaction history']
            account_list.append(saving)
    except FileNotFoundError:
      account_list = []
      
    return account_list


def save_to_json(file_name, reference):
  saved_account = []
  for account in reference:
    finished = account.convert_to_class_instance_to_dic()
    saved_account.append(finished)

  with open(file_name, 'w') as file:
    json.dump(saved_account, file, indent = 5)