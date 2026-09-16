import bank_account_class as ba
import json

ac1 = ba.BankAccount("reuben", "0534543355", "reu@gmail.com", 0)
ac2 = ba.SavingsAcount("bright", "0248547898", "bri@gmail.com", 17, 200)

account = {ac1, ac2}

