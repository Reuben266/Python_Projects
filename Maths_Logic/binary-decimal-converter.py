import sys

"""this program converts binary input from the user into decimal values"""

#checking user input
count = 0
binary_list = {"0", "1"}
bin_list = []

while True:
  if count == 3:
    print("====Too many trials====")
    input()
    break

  binary_str = input("type in a string of binary digits:: ")
  
  if len(binary_str) != 0:
    break
  else:
    print("Invalid input")
    break
  
  for bits in binary_str:
    if bits in binary_list:
      is_true = True
    else:
      is_true = False
      break
  
  if is_true:
    break
  
  else:
    print("that is not a string of binary digits")
    print("please type in a string of binary digits")
    count += 1
    continue
      
for bits in binary_str:
  int_bit = int(bits)
  bin_list.append(int_bit)

len_of_bits = (len(bin_list) - 1)

dec_list = []

for bit in bin_list:
  dec_value = bit * 2**(len_of_bits)
  dec_list.append(dec_value)
  len_of_bits -= 1

decimal_value = sum(dec_list)
print(decimal_value)
input()