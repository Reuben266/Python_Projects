import time

"""this program shows the mechanism behind the multiplication of a two by two matrix"""

print("======FIRST MATRIX======")
while True:
  try:
    place_a = int(input("first place:: "))
    place_b = int(input("second place:: "))
    place_c = int(input("third place:: "))
    place_d = int(input("forth place:: "))
    break
  except ValueError:
    print("Invalid input")
    continue

print("======SECOND MATRIX======")
place_1 = int(input("first place:: "))
place_2 = int(input("second place:: "))
place_3 = int(input("third place:: "))
place_4 = int(input("forth place:: "))


matrix_1 = [
    [place_a, place_b],
    [place_c, place_d]
]

matrix_2 = [
    [place_1, place_2],
    [place_3, place_4]
]

first_num = matrix_1[0][0]
second_num = matrix_1[0][1]


third_num = matrix_1[1][0]
forth_num = matrix_1[1][1]

pos_1 = []
pos_2 = []
pos_3 = []
pos_4 = []

first_cord = []
second_cord = []


for i in matrix_2:
    multiplier = i[0]
    result = multiplier * first_num
    pos_1.append(result)
    first_num = second_num

first_num = matrix_1[0][0]
second_num = matrix_1[0][1]

for x in matrix_2:
    multiplier = x[1]
    result = multiplier * first_num
    pos_2.append(result)
    first_num = second_num

sum_pos_1 = sum(pos_1)
sum_pos_2 = sum(pos_2)

first_cord.append(sum_pos_1)
second_cord.append(sum_pos_2)

for numbers in matrix_2:
    multiplier = numbers[0]
    result = multiplier * third_num
    pos_3.append(result)
    third_num = forth_num

third_num = matrix_1[1][0]
forth_num = matrix_1[1][1]

for numbers in matrix_2:
    multiplier = numbers[1]
    result = multiplier * third_num
    pos_4.append(result)
    third_num = forth_num
    
sum_pos_3 = sum(pos_3)
sum_pos_4 = sum(pos_4)

result_matrix_1 = [sum_pos_1, sum_pos_2]
result_matrix_2 = [sum_pos_3, sum_pos_4]

print(result_matrix_1)
print(result_matrix_2)