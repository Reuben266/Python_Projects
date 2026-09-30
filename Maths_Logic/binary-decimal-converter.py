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

max_pow = (len(bin_list) - 1)
result_list = []

for bit in bin_list:
  result = bit * (2**max_pow)
  result_list.append(result)
  max_pow -= 1

result = sum(result_list)

print(f"The decimal value of {binary_str} is:: {result}")