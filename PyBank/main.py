# Modules
import os
import csv

budget_data_csv = os.path.join('Resources','budget_data.csv')

pl_change = 0
pl_change_list = []
month_year = []
Total_profit_loss = 0
months=0

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    totalMonths = len(list(csvreader))

    profit_loss = int(row[1])
    netTotal = budget_data_csv[profit_loss].sum()
    
    
     for row in csvreader
        pl_change_list.append(profit_loss - pl_change)
        pl_change = int(row[1])
        month_year.append(row[0])
        
    for i in range(1, totalMonths):
        Total_profit_loss = Total_profit_loss +  pl_change_list[i]
        
   

# Print csv_header
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {totalMonths}')
print(f'Total:{netTotal}')