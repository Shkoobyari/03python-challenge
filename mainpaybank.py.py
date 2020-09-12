import csv
import os
csv_path = os.path.join('.', 'Resources', 'budget_data.csv')
final_txt_file_path = os.path.join('.', 'Analysis', 'pybank.txt')

n_months = 0
net_profit = 0
greatest_increase_amount = 0
greatest_increase_month_year = ''
greatest_decrease_amount = 0
greatest_decrease_month_year = ''
average_change = 0

with open(csv_path) as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=',')

  header = next(csv_reader)

  first_row = next(csv_reader)

  previous_month_net = int(first_row[1])
  monthly_change = 0

  for row in csv_reader:
    current_month_net = int(row[1])

    n_months += 1
    net_profit += current_month_net

    # Conditional statements for dealing with negative number
    if current_month_net > 0:
      monthly_change = previous_month_net - current_month_net
    elif current_month_net < 0:
      monthly_change = previous_month_net + current_month_net
      
    if monthly_change > 0:
      if monthly_change > greatest_increase_amount:
        greatest_increase_amount = monthly_change
        greatest_increase_month_year = row[0]
    elif monthly_change < 0:
      if monthly_change < greatest_decrease_amount:
        greatest_decrease_amount = monthly_change
        greatest_decrease_month_year = row[0]
  average_change = net_profit / n_months
  print(f"Financial Analysis \n-------------------------- \nTotal Months: {n_months} \nTotal: ${net_profit}\nAverage Change: ${average_change} \nGreatest Increase in Profits: {greatest_increase_month_year} (${greatest_increase_amount}) \nGreatest Decrease in Profits: {greatest_decrease_month_year} (${greatest_decrease_amount})")

with open(final_txt_file_path, "w") as txtfile:
  txtfile.write(f"Financial Analysis \n-------------------------- \nTotal Months: {n_months} \nTotal: ${net_profit}\nAverage Change: ${average_change} \nGreatest Increase in Profits: {greatest_increase_month_year} (${greatest_increase_amount}) \nGreatest Decrease in Profits: {greatest_decrease_month_year} (${greatest_decrease_amount})")