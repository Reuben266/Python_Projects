import select
class Weapon:
  def __init__(self, name, damage, durability=35):
    self.name = str(name)
    self.damage = int(damage)
    self.durability = int(durability)

  def attack(self):
    if self.durability == 0:
      return f"{self.name} is broken, repair it first"

    else:
      self.durability = max(0, (self.durability - 10))
      return f"Attacked with {self.name} for {self.damage} damage, remaining durability: {self.durability}"

  def repair(self, amount):
    if self.durability == 100:
      return f"maximum durability reached. Durability: {self.durability}"
    else:
      self.durability = min(100, (self.durability + amount))
      return f"{self.name} was repaired. Remaining durability: {self.durability}"

  def __str__(self):
    return f"Weapon: {self.name} | Damage: {self.damage} | Durability: {self.durability}"

w1 = Weapon("M4", 45)

class RangedWeapon(Weapon):
  def __init__(self, name, damage, ammo_capacity, durability=100):
    super().__init__(name, damage, durability)
    self.ammo_capacity = int(ammo_capacity)

  def shooter(self):
    if self.durability == 0:
      return f"{self.name} is broken, repair it first"
    elif self.ammo_capacity == 0:
      return "Out of ammo. Reload first"

    else:
      self.ammo_capacity -= 1
      self.durability = max(0, (self.durability - 5))
      return f"Ammo capacity: {self.ammo_capacity}. Remaining durability: {self.durability}"

w2 = RangedWeapon("sniper", 45, 5)