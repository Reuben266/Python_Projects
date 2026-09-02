
class BankAcount:
  def __init__(self, name, phone_number, emial, balance=0):
    self.name = str(name)
    self.phone_number = str(phone_number)
    self.emial = str(emial)
    self.__balance = float(balance)
    self.amount_owed = 0
    self.transaction = []
    

  def deposit(self, amount):
    if amount < 0:
      return "Invalid input, the amount must be greater than 0.00"
    else:
      self.__balance += amount
      self.transaction.append(f"Deposited: ${amount:.2f}")
      return f"Deposited: ${amount:.2f}, current balance: ${self.__balance:.2f}"

  
  def withdraw(self, amount):
    if amount > self.__balance:
      return f"Cannot withdraw an amount greater than your balance. Current balance: ${self.__balance:.2f}"
    else:
      if amount < 0:
        return "Cannot withdraw an amount less than $0.00"
      else:
        self.__balance -= amount
        self.transaction.append(f"Withdrew ${amount:.2f}")
        return f"Withdrew ${amount:.2f}, current balance ${self.__balance:.2f}"
  
  
  def loan(self, amount, time):
    if self.__balance == 0:
      return "you Cannot aquire a loan if your account balance is $0.00"
    else:
      SI = (amount * 25 * time)/100
      self.amount_owed = amount + SI
      self.__balance += amount
      self.transaction.append(f"Took a loan of ${amount:.2f} for a time of {time} year(s)")
      return f"Took a loan of ${amount:.2f}, interest on ${amount:.2f} is ${SI:.2f}, total amount_owed: ${self.amount_owed:.2f}, current balance: ${self.__balance:.2f}"

  
  def pay_loan(self, amount):
    if self.amount_owed == 0:
      return f"Loan already paid, current balance: ${self.__balance:.2f}"
      
    elif amount > self.amount_owed:
      amount -= self.amount_owed
      self.__balance -= self.amount_owed
      change = amount
      self.amount_owed = 0
      return f"Amount left: ${self.amount_owed:.2f}. Change of ${change:.2f} was returned. Current account balance: ${self.__balance}"
      
    elif amount <= 0:
      return "Amount must be greater than $0.00"
      
    else:
      self.amount_owed -= amount
      self.__balance -= amount
      return f"paid an amount of: ${amount:.2f}. total amount left: ${self.amount_owed:.2f}. Current account balance: ${self.__balance:.2f}"

  
  def transfer(self, target_account, amount):
    if self.__balance <= 0:
      return f"Transfer failed, account balance: ${self.__balance:.2f}"
      
    elif self.__balance < amount:
      return f"Cannot send an amount greater than your account balance, current account balance: ${self.__balance:.2f}"
      
    else:
      if amount <= 0:
        return "Invalid transfer, cannot send an amount less than or equal to $0.00"
        
      else:
        if target_account.name == self.name:
          return "Cannot transfer money to yourself"
          
        else:
          self.__balance -= amount
          target_account.balance += amount
          return f"Sent ${amount:.2f} to {target_account.name}"
      
  
  def __str__(self):
    return f"Acount name: {self.name} | Acount balance: ${self.__balance:.2f}"


class SavingsAcount(BankAcount):
  def __init__(self, name, phone_number, emial, age, balance=0.00):
    super().__init__(name, phone_number, emial, balance)
    self.age = int(age)

  
  def apply_interest(self):
    interest = self.__balance * 0.05
    old_balance = self.__balance
    new_balance = interest + self.__balance
    return f"0.05 interest was calculated on ${old_balance:.2f}. Total balance: ${new_balance:.2f}"

  
  def __str__(self):
    return f"Acount name: ${self.name} | Age: {self.age} | Balance: ${self.__balance:.2f}"
      

ac1 = SavingsAcount("Sonic", "03424", "sonic@gmail.com", 0)
ac1.__balance = 10000
print(ac1.withdraw(200))
print(ac1.deposit(2900))
print(ac1.loan(400, 2))


print("="*20, "History", "="*20)
for history in ac1.transaction:
  print(history)