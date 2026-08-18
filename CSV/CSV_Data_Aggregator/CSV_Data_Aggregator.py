import csv

with open('sales_data.csv', 'r') as file, open("sales_summary.txt", "w") as output_file:
  csv_reader = csv.DictReader(file)
  total = 0
  total_electronics = 0
  total_gloceries = 0
  total_clothing = 0
  
  for rows in csv_reader:
    
    quantity, price_per_unit = int(rows["quantity"]), float(rows["price_per_unit"])
    revenue = quantity * price_per_unit
    total += revenue
    
    if rows["category"] == "Electronics":
      total_electronics += revenue
      
    if rows["category"] == "Groceries":
      total_gloceries += revenue

    if rows["category"] == "Clothing":
      total_clothing += revenue

  total = round(total, 2)
  total_electronics = round(total_electronics, 2)
  total_gloceries = round(total_gloceries, 2)
  total_clothing = round(total_clothing, 2)
  
  print(f"Total revenue:: ${total}")
  print(f"Total revenue for Electronics:: ${total_electronics}")
  print(f"Total revenue for Groceries:: ${total_gloceries}")
  print(f"Total revenue for Clothing:: ${total_clothing}")

  output_file.write(f"Total revenue:: ${total} \nTotal revenue for Electronics:: ${total_electronics} \nTotal revenue for Groceries:: ${total_gloceries} \nTotal revenue for Clothing:: ${total_clothing}")

  