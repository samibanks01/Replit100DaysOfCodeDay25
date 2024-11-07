
print("⚔️ Character Stats Generator ⚔️")

print()

def rollDice(sides):
  import random
  roll = random.randint(1,sides)
  return roll

def rollDice2():
  import random
  roll = random.randint(1,6)
  roll2 = random.randint(1,8)
  health = roll * roll2
  return health

while True:
  name = input("Name your warrior: ")
  health = rollDice2()
  print("Their health is:", health, "hp")
  print()
  again = input("Do you want to create another character? ")
  if again == "yes":
    continue

  else:
    break

  
