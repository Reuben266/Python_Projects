class BankAcount:
  def __init__(self, name, phone_number, emial, balance=0):
    self.name = str(name)
    self.phone_number = str(phone_number)
    self.emial = str(emial)
    self.balance = float(balance)

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
    SI = (amount * 25 * time)/100
    amount_owed = amount + SI
    self.balance += amount
    return f"Took a loan of ${amount:.2f}, interest on ${amount:.2f} is ${SI:.2f}, total amount_owed: ${amount_owed:.2f}, current balance: ${self.balance:.2f}"

  def __str__(self):
    return f"Acount name: {self.name} | Acount balance: {self.balance}"

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
      
    
ac1 = SavingsAcount("Reuben", "055555", "ben@gmial.com", 28, 400)
print(ac1.apply_interest())
print(ac1.deposit(200))
print(ac1.withdraw(130))
print(ac1.loan(200, 2))
