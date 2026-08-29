class Player:
  def __init__(self, username, health=100, score=0):
    self.username = username
    self.health = health
    self.score = score

  def take_damage(self, amount):
    self.health -= amount
    return f"{self.username} took damage of {amount}HP. Health status: {self.health}"

  def add_score(self, point):
    self.score += point
    return f"score of {point} rewarded to {self.username}. Score status: {self.score}"


p1 = Player("BrightBen")

print(p1.take_damage(40))
print(p1.add_score(50))