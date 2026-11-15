class Inventory:
  def __init__(self, name: str, price: float, stock: int = 0, quantity_sold: int = 0):
    self.name = name
    self.__price = price
    self.__stock = stock
    self.__quantity_sold = quantity_sold

  @property
  def stock(self):
    return self.__stock

  @stock.setter
  def stock(self, quantity):
    if quantity < 0:
      raise ValueError("Cannot set quantity less than 0")
    else:
      self.__stock = quantity

  @property
  def price(self):
    return self.__price

  @price.setter
  def price(self, amount):
    if amount <= 0:
      raise ValueError("Invalid input. Expected a value greater than 0 in setting the price of stock")
    else:
      self.__price = amount

  @property
  def quantity_sold(self):
    return self.__quantity_sold