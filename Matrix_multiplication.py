import time

"""this program shows the mechanism behind the multiplication of a two by two matrix"""
def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Invalid Input, try again")

print("======FIRST MATRIX======")
place_a = get_int(("first place:: "))
place_b = get_int(("second place:: "))
place_c = get_int(("third place:: "))
place_d = get_int(("forth place:: "))
print("======SECOND MATRIX======")
place_1 = get_int(("first place:: "))
place_2 = get_int(("second place:: "))
place_3 = get_int(("third place:: "))
place_4 = get_int(("forth place:: "))

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

result1 = first_num * matrix_2[0][0]
result2 = second_num * matrix_2[1][0]
sum1 = result1 + result2

result1 = first_num * matrix_2[0][1]
result2 = second_num * matrix_2[1][1]
sum2 = result1 + result2

result1 = third_num * matrix_2[0][0]
result2 = forth_num * matrix_2[1][0]
sum3 = result1 + result2

result1 = third_num * matrix_2[0][1]
result2 = forth_num * matrix_2[1][1]
sum4 = result1 + result2

pos_1 = [sum1, sum2]
pos_2 = [sum3, sum4]

print(pos_1)
print(pos_2)