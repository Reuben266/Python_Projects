import sqlite3
import inventory_class as ic
import os


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


def restock(item_name, quantity):
  cursor.execute("""UPDATE inventory
                    SET quantity = quantity + (?)
                    WHERE name = (?)""",(quantity, item_name))
  conn.commit()

def sell(item_name, quantity):
  cursor.execute("""UPDATE inventory
                    SET quantity_sold = quantity_sold + (?) 
                    WHERE name = (?)""", (quantity, item_name))
  
  cursor.execute("""UPDATE inventory
                    SET quantity = quantity - (?)
                    WHERE name = (?)""", (quantity, item_name))
  conn.commit()

def most_sold():
  cursor.execute("""
                  SELECT name, MAX(quantity_sold)
                  FROM inventory
  """)
  return cursor.fetchone()

def least_sold():
  cursor.execute("""
                  SELECT name, MIN(quantity_sold)
                  FROM inventory
  """)
  return cursor.fetchone()
  
def check_duplicate(item_name):
  item_found = False
  duplicate = cursor.execute("""SELECT name FROM inventory 
                       WHERE name = (?)""",(item_name,))
  retrieve_duplicate = cursor.fetchone()
  
  if retrieve_duplicate == None:
    item_found = False
  else:
    if item_name in retrieve_duplicate:
      item_found = True
      

  return item_found