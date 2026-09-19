import json

class BankAccount:
  def __init__(self, name, phone_number, email, balance=0):
    self.name = str(name)
    self.phone_number = str(phone_number)
    self.email = str(email)
    self._balance = float(balance)
    self._amount_owed = 0
    self.transaction = []

  def deposit(self, amount):
    if amount < 0 or amount == 0:
      result = "Invalid input, the amount must be greater than 0.00"
      print(result)
    else:
      self._balance += amount
      self.transaction.append(f"Deposited: ${amount:.2f}")
      result = f"Deposited: ${amount:.2f}, current balance: ${self._balance:.2f}"
      print(result)
      
  
  def withdraw(self, amount):
    if amount > self._balance:
      return f"Cannot withdraw an amount greater than your balance. Current balance: ${self._balance:.2f}"
    
    elif amount < 0 or amount == 0:
      result = "Cannot withdraw an amount less than or equal to $0.00"
      print(result)
      return result
    
    else:
      self._balance -= amount
      self.transaction.append(f"Withdrew ${amount:.2f}")
      result = f"Withdrew ${amount:.2f}, current balance ${self._balance:.2f}"
      print(result)
      return result
  
  def loan(self, amount, time):
    if self._balance == 0:
      result = "you Cannot acquire a loan if your account balance is $0.00"
      print(result)
      
    elif time <= 0:
      result = "Invalid input, negative time"
      print(result)
  
    elif amount < 0 or amount == 0:
      result = "Invalid input, cannot take a loan less than or equal to $0.00"
      print(result)
      
    else:
      SI = (amount * 25 * time)/100
      self._amount_owed += (amount + SI)
      self._balance += amount
      self.transaction.append(f"Took a loan of ${amount:.2f} for a time of {time} year(s)")
      result = f"Took a loan of ${amount:.2f}, interest on ${amount:.2f} is ${SI:.2f}, total _amount_owed: ${self._amount_owed:.2f}, current balance: ${self._balance:.2f}"
      print(result)
  
  def pay_loan(self, amount):
    if self._amount_owed == 0:
      result = f"Loan already paid, current balance: ${self._balance:.2f}"
      print(result)
    elif amount > self._balance:
      result = "Insufficient balance"
      print(result)
      
    elif amount > self._amount_owed:
      self.transaction.append(f"Paid ${self._amount_owed:.2f}")
      amount -= self._amount_owed
      self._balance -= self._amount_owed
      change = amount
      self._amount_owed = 0
      result = f"Amount left: ${self._amount_owed:.2f}. Change of ${change:.2f} was returned. Current account balance: ${self._balance:.2f}"
      print(result)
      
    elif amount <= 0:
      result="Amount must be greater than $0.00"
      print(result)
      
    else:
      self._amount_owed -= amount
      self._balance -= amount
      self.transaction.append(f"Paid ${amount:.2f}")
      result=f"paid an amount of: ${amount:.2f}. total amount left: ${self._amount_owed:.2f}. Current account balance: ${self._balance:.2f}"
      print(result)

  
  def transfer(self, target_account, amount):
    if self._balance <= 0:
      return f"Transfer failed, account balance: ${self._balance:.2f}"
      
    elif self._balance < amount:
      return f"Cannot send an amount greater than your account balance, current account balance: ${self._balance:.2f}"
      
    
    elif amount <= 0:
      return "Invalid transfer, cannot send an amount less than or equal to $0.00"
        
      
    elif target_account is self:
      return "Cannot transfer money to yourself"
          
    else:
      self._balance -= amount
      target_account._balance += amount
      target_account.transaction.append(f"Received ${amount:.2f} from {self.name}")
      self.transaction.append(f"Transferred ${amount:.2f} to {target_account.name}")
      return f"Sent ${amount:.2f} to {target_account.name} current balance ${self._balance:.2f}"

    
  def convert_to_class_instance_to_dic(self):
    account = {
      "account_type": "BankAccount",
      "name": self.name,
      "phone_number": self.phone_number,
      "email": self.email,
      "balance": self._balance,
      "amount_owed": self._amount_owed,
      "transaction history": self.transaction
    }

    return account
    
  def __str__(self):
    return f"Account name: {self.name} | Account balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
  def __init__(self, name, phone_number, email, age, balance=0.00):
    super().__init__(name, phone_number, email, balance)
    self.age = int(age)

  
  def apply_interest(self):
    old_balance = self._balance
    interest = self._balance * 0.05
    self._balance += interest
    new_balance = self._balance
    self.transaction.append(f"Interest of ${interest:.2f} calculated and added to savings account current balance: ${self._balance:.2f}")
    return f"0.05 interest was calculated on ${old_balance:.2f}. Total balance: ${new_balance:.2f}"

  def convert_to_class_instance_to_dic(self):
    account = super().convert_to_class_instance_to_dic()
    account['account_type'] = "SavingsAccount"
    account['age'] = self.age

    return account
  

  
  def __str__(self):
    return f"Account name: {self.name} | Age: {self.age} | Balance: ${self._balance:.2f}"

ac1 = BankAccount("Reuben", "00777", "ben.com", 1000)
print(ac1.loan(200, 2))
print(ac1._amount_owed)