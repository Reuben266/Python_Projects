import json

try:
  with open("grades.json", "r") as file:
    student_info = json.load(file)
except FileNotFoundError:
  student_info = {}
  

name = input("Enter a new student's name:: ").lower()
while  True:
  try:
    grade = int(input(f"What is the grade of {name}::  "))
    break
  except ValueError:
    print("Invalid Input")
    
student_info[name] = grade
with open("grades.json", "w") as updated_file:
  json.dump(student_info, updated_file, indent=4)
    
print("done")