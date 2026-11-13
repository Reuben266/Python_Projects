import inventory_db as db
import inventory_class as ic

db.init_database()

def is_valid(prompt):
  while True:
    try:
     return int(input(prompt))
      
    except ValueError:
      print("Invalid input")
      continue

user_options = ["[1] Register Item","[2] Restock Item", "[3] Sell item", "[4] View Most Sold Item", "[5] View Least Sold Item", "[6] Exit Application"]

while True:
  print("=============================")
  for option in user_options:
    print(option)
  print("=============================\n")

  try:
    choice = int(input("What action do you want to perform(1-6)::  "))
  except ValueError:
    print("Invalid input, try again")
    continue

  if choice == 1:
    name = input("What is the name of thr item::  ").lower().strip()
    item_found = db.check_duplicate(name)
    if item_found:
      stock = is_valid("What is the quantity of the item::  ")
      db.restock(name, stock)
    else:
      price = is_valid("What is the price of the item::  ")
      stock = is_valid("What is the quantity of the item::  ")
      item = ic.Inventory(name, price, stock)
      db.insert_to_database(item.name, item.stock, item.price, item.quantity_sold)
    
    print("\n=======================================")
    print(f"{name} was added to stock successfully")
    print("=========================================\n")

  elif choice == 2:
    name = input("What is the name of the item you want to stock::  ")
    item_found = db.check_duplicate(name)
    if item_found:
      quantity = is_valid("Enter stock quantity:: ")
      db.restock(name, quantity)
    else:
      print("Item has not been registed yet")

  elif choice == 3:
    name = input("What is the name of the item you want to sell:: ")
    quantity_sold = input("How many items:: ")
    db.sell(name, quantity_sold)

  elif choice == 4:
    print(db.most_sold())

  elif choice == 5:
    print(db.least_sold())

  elif choice == 6:
    break