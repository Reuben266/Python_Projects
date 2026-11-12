import sqlite3
import inventory_class as ic


conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

item1 = ic.Inventory("Frying Pan", 20, 500)

def init_database():
  cursor.execute("""
          CREATE TABLE IF NOT EXISTS inventory
          (
          stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          price REAL,
          quantity INTEGER,
          quantity_sold INTEGER
          )
                """)
  conn.commit()

def insert_to_database(x, y, z, w):
  cursor.execute("""INSERT INTO inventory(name, quantity, price, quantity_sold)
                  VALUES (?,?,?,?)""",(x, y, z, w)
                )
  conn.commit()

def check_duplicate(item_name):
  duplicate = cursor.execute("""SELECT name FROM inventory 
                       WHERE name = (?)""",(item_name,))
  retrieve_duplicate = cursor.fetchone()
  try:
    if item_name in retrieve_duplicate:
      duplicate_found = True
  except TypeError:
    duplicate_found = False
      
  if duplicate_found:
    item_price = cursor.execute("""SELECT quantity FROM inventory
                      WHERE name = (?)""",(item_name,))
    
    return duplicate_found, item_price

def restock(item_name, quantity):
  cursor.execute("""UPDATE inventory
                    SET quantity = quantity + 10
                    WHERE name = (?)""",(item_name,))