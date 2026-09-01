
class BankAcount:
  def __init__(self, name, phone_number, emial, balance=0):
    self.name = str(name)
    self.phone_number = str(phone_number)
    self.emial = str(emial)
    self.balance = float(balance)
    self.amount_owed = 0
    

  def deposit(self, amount):
    if amount < 0:
      return "Invalid input, the amount must be greater than 0.00"
    else:
      self.balance += amount
      return f"Deposited: ${amount:.2f}, current balance: ${self.balance:.2f}"

  
  def withdraw(self, amount):
    if amount > self.balance:
      return f"Cannot withdraw an amount greater than your balance. Current balance: ${self.balance:.2f}"
    else:
      if amount < 0:
        return "Cannot withdraw an amount less than $0.00"
      else:
        self.balance -= amount
        return f"Withdrew ${amount:.2f}, current balance ${self.balance:.2f}"

  
  def loan(self, amount, time):
    if self.balance == 0:
      return "you Cannot aquire a loan if your account balance is $0.00"
    else:
      SI = (amount * 25 * time)/100
      self.amount_owed = amount + SI
      self.balance += amount
      return f"Took a loan of ${amount:.2f}, interest on ${amount:.2f} is ${SI:.2f}, total amount_owed: ${self.amount_owed:.2f}, current balance: ${self.balance:.2f}"

  
  def pay_loan(self, amount):
    if self.amount_owed == 0:
      return f"Loan already paid, current balance: ${self.balance:.2f}"
      
    elif amount > self.amount_owed:
      amount -= self.amount_owed
      self.balance -= self.amount_owed
      change = amount
      self.amount_owed = 0
      return f"Amount left: ${self.amount_owed:.2f}. Change of ${change:.2f} was returned. Current account balance: ${self.balance}"
      
    elif amount <= 0:
      return "Amount must be greater than $0.00"
      
    else:
      self.amount_owed -= amount
      self.balance -= amount
      return f"paid an amount of: ${amount:.2f}. total amount left: ${self.amount_owed:.2f}. Current account balance: ${self.balance:.2f}"

  
  def __str__(self):
    return f"Acount name: {self.name} | Acount balance: ${self.balance:.2f}"


class SavingsAcount(BankAcount):
  def __init__(self, name, phone_number, emial, age, balance=0.00):
    super().__init__(name, phone_number, emial, balance)
    self.age = int(age)

  
  def apply_interest(self):
    interest = self.balance * 0.05
    old_balance = self.balance
    new_balance = interest + self.balance
    return f"0.05 interest was calculated on ${old_balance:.2f}. Total balance: ${new_balance:.2f}"

  
  def __str__(self):
    return f"Acount name: ${self.name} | Age: {self.age} | Balance: ${self.balance:.2f}"
      

ac2 = BankAcount("Bright", "006644366", "bright@gmail.com", 4000)
