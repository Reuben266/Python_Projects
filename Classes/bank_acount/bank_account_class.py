class BankAccount:
  def __init__(self, name, phone_number, email, balance=0):
    self.name = str(name)
    self.phone_number = str(phone_number)
    self.email = str(email)
    self._balance = float(balance)
    self._amount_owed = 0
    self.transaction = []
    
    

  def deposit(self, amount):
    if amount < 0:
      return "Invalid input, the amount must be greater than 0.00"
    else:
      self._balance += amount
      self.transaction.append(f"Deposited: ${amount:.2f}")
      return f"Deposited: ${amount:.2f}, current balance: ${self._balance:.2f}"

  
  def withdraw(self, amount):
    if amount > self._balance:
      return f"Cannot withdraw an amount greater than your balance. Current balance: ${self._balance:.2f}"
    else:
      if amount < 0:
        return "Cannot withdraw an amount less than $0.00"
      else:
        self._balance -= amount
        self.transaction.append(f"Withdrew ${amount:.2f}")
        return f"Withdrew ${amount:.2f}, current balance ${self._balance:.2f}"
  
  
  def loan(self, amount, time):
    if self._balance == 0:
      return "you Cannot aquire a loan if your account balance is $0.00"
      
    elif time <= 0:
      return "Invalid input, negative time"
    
    else:
      SI = (amount * 25 * time)/100
      self._amount_owed = amount + SI
      self._balance += amount
      self.transaction.append(f"Took a loan of ${amount:.2f} for a time of {time} year(s)")
      return f"Took a loan of ${amount:.2f}, interest on ${amount:.2f} is ${SI:.2f}, total _amount_owed: ${self._amount_owed:.2f}, current balance: ${self._balance:.2f}"

  
  def pay_loan(self, amount):
    if self._amount_owed == 0:
      return f"Loan already paid, current balance: ${self._balance:.2f}"
      
    elif amount > self._amount_owed:
      amount -= self._amount_owed
      self._balance -= self._amount_owed
      change = amount
      self._amount_owed = 0
      return f"Amount left: ${self._amount_owed:.2f}. Change of ${change:.2f} was returned. Current account balance: ${self._balance}"
      
    elif amount <= 0:
      return "Amount must be greater than $0.00"
      
    else:
      self._amount_owed -= amount
      self._balance -= amount
      return f"paid an amount of: ${amount:.2f}. total amount left: ${self._amount_owed:.2f}. Current account balance: ${self._balance:.2f}"

  
  def transfer(self, target_account, amount):
    if self._balance <= 0:
      return f"Transfer failed, account balance: ${self._balance:.2f}"
      
    elif self._balance < amount:
      return f"Cannot send an amount greater than your account balance, current account balance: ${self._balance:.2f}"
      
    else:
      if amount <= 0:
        return "Invalid transfer, cannot send an amount less than or equal to $0.00"
        
      else:
        if target_account.name == self.name:
          return "Cannot transfer money to yourself"
          
        else:
          self._balance -= amount
          target_account.deposit(amount)
          return f"Sent ${amount:.2f} to {target_account.name}"
      
  def convert_to_class_instance_to_dic(self):
    ...

  def convert_to_class_instance(self):
    ...
    
  def __str__(self):
    return f"Acount name: {self.name} | Acount balance: ${self._balance:.2f}"


class SavingsAcount(BankAccount):
  def __init__(self, name, phone_number, email, age, balance=0.00):
    super().__init__(name, phone_number, email, balance)
    self.age = int(age)

  
  def apply_interest(self):
    old_balance = self._balance
    interest = self._balance * 0.05
    self._balance += interest
    new_balance = self._balance
    return f"0.05 interest was calculated on ${old_balance:.2f}. Total balance: ${new_balance:.2f}"

  
  def __str__(self):
    return f"Acount name: {self.name} | Age: {self.age} | Balance: ${self._balance:.2f}"
      

ac1 = BankAccount("Reuben", "08888", "reu@ben.com", 1000)
ac2 = SavingsAcount("Bright", "066666", "bri@gmail.com", "20", 200)
print(ac1.loan(200,-6))