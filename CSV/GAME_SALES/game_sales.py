import csv

with open("game_sales.csv", "r") as file, open("game_summary.txt", "w") as output_file:
  csv_reader = csv.DictReader(file)
  
  total = 0
  total_North_America = 0
  total_revenue_Erope = 0
  total_revenue_Asia = 0
  items_quantity = {}
  
  for rows in csv_reader:
    quantity, price = int(rows["quantity"]), float(rows["unit_price"])
    revenue = quantity * price
    total += revenue
    items_quantity[rows["item"]] = items_quantity.get(rows["item"], 0) + quantity

    if rows["region"] == "North America":
      total_North_America += revenue
    elif rows["region"] == "Europe":
      total_revenue_Erope += revenue
    elif rows["region"] == "Asia":
      total_revenue_Asia += revenue

  top_item = max(items_quantity, key=items_quantity.get)
  top_quantity = items_quantity[top_item]
  total_revenue_Asia = round(total_revenue_Asia, 2)
  total_revenue_Erope = round(total_revenue_Erope, 2)
  total_North_America = round(total_North_America, 2)

  summery = (
      f"Total revenue:: ${total}\n",
      f"The total revenue for North America is:: ${total_North_America}\n",
      f"The total revenue for Europe is:: ${total_revenue_Erope}\n",
      f"The total revenue for Asia is:: ${total_revenue_Asia}\n",
      f"The top item sold is {top_item}. {top_quantity} items sold"
      )

  

  for notes in summery:
    output_file.write(notes)
    print(notes)