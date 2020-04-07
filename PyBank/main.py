# Modules
import csv
import os

#Get the data from the source
budget_data_csv = os.path.join("budget_data.csv")
#Read the csv file
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    #print(csv_header)
    
    #Assign variables    
    profit_loss=[]
    pl_summary={}    
    total=0
    past=0
    total1=0
    average=0
    total_months=0

    # Convert budget_reader string to a list profit_loss
    for row in csv_reader:
        profit_loss.append(row)
        # The total net amount of "Profit/Losses" over the entire period
        total+=int(row[1])
        # The total number of months included in the dataset
        total_months+=1
        
        #print(total)

    
    # Initialize max increase and max decrease values with latest increase/decrease value
    max_dec=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_inc=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    
    # Compute the change in "Profit/Losses" between months over the entire period
    # by iterating (backwards) from latest month-year to the earliest
    for i in range(total_months,1,-1): # stops when i is 2
        past=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])
        
        # Find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if past < max_dec:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=past
        elif past > max_inc:
            max_increase=past
            max_month_yr=profit_loss[i-1][0]
        
        # Total amount change in "Profit/Losses" between months over the entire period
        total1=total1+past
    
    #The average change in "Profit/Losses" between months over the entire period    
    average=total1/(total_months-1)
    
print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(total_months))
print('Total: $'+str(total))
print('Average  Change: $'+str(round(average,2)))
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_inc)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_dec)+')')

inputfile='\\Desktop\\Data Analytics\\python-challenge\\PyBank\\Resources\\budget_data.csv'
outputfile='\\Desktop\\Data Analytics\\python-challenge\\PyBank\\budget_output.txt'

# Output to text file and console
text_file=open(outputfile,"x")
text_file.write('Financial Analysis')
text_file.write('\n----------------------------')
text_file.write('\nTotal Months: '+str(total_months))
text_file.write('\nTotal: $'+str(total))
text_file.write('\nAverage  Change: $'+str(round(average,2)))
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
text_file.close()