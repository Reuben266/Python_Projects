"""this program converts binary input from the user into decimal values"""

count = 0
valid_binary = {"0", "1"}
bin_list = []
run = True

while True:
  binary_str = input("type in a string of binary digits:: ")

  is_valid = True
  
  for bit in binary_str:
    if bit not in valid_binary:
      is_valid = False
    else:
      bit = int(bit)
      bin_list.append(bit)
      
  if is_valid:
    break
  else:
    print("Invalid Input")
    bin_list.clear()
    continue
