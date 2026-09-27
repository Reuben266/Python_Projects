"""This code converts any integer value into binary"""
"""It does not accept floating point numbers and negative values"""

import sys

count = 0

while True: 
  #Alerting user on final trial
  if count == 2:
    print("=" * 48)
    print("The program will exit after an unsuccessful input")
    print("=" * 48)
    print("\n")

  #exiting the program on 3 trials
  if count == 3:
    print("=======Too many trial=======")
    input()
    sys.exit()
    
  #restricting user input to positive integers
  try:
    user_number = int(input("type in any positive integer: "))
    number = user_number
    if number < 0:
      print("Only accepts positive integers")
      count += 1
      continue
    break
  except ValueError: 
    print("This is not a value, type in a value next time")
    count += 1
    continue

number_of_times = []
number_of_times.append(number)

# The if statement ensure typing 0 does not crash the program
if number == 0:
  number_of_times.append(0)

while True:
  if 0 in number_of_times:
    break
  
  if number % 2 == 0:
    divide = number / 2
    number_of_times.append(divide)
    number = divide
    
  elif number % 2 != 0:
    divide = number // 2
    number_of_times.append(divide)
    number = divide

binary_list = []   
binarystring = ""

for numbers in number_of_times:
  binary = int(numbers % 2)
  binary_list.append(binary)

binary_list.reverse()

for bits in binary_list:
  bits = str(bits)
  binarystring += bits
  
binarystring = binarystring[1:]
print(f"the binary equivalen of {user_number} is: {binarystring}")