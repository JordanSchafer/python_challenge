#Create a Python script that analyzes the PyBank records and calculate
#The total number of months
#the net total amount of "Profit/Losses"
#the average of the changes in "Profit/Losses"
#the greatest increase in profits(date and amount)
#the greatest decrease in losses(date and amount)
#Print the analysis to the terminal and export to a text file

#import dependencies'
import os
import csv

#create variables
month=[]
pl_changes=[]

mcount=0
net_pl=0
prev_month=0
cur_month=0
pl_change=0

#Set path to csv file budget_data.csv
csvpath=os.path.join("Resources","budget_data.csv")


with open(csvpath) as csvfile:
    
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next (csvfile)
    
    #print(f"Header: {csv_header}")
    for row in csv_reader:
        
        #counts number of months
        mcount+=1
        
        month.append(row[0])
        
        #Net total amount of Profit/Losses
        cur_month=int(row[1])
        net_pl+= cur_month
        if mcount==1:
            prev_month=cur_month
            
        else:
            pl_change=cur_month-prev_month
        
            pl_changes.append(pl_change)
        
            prev_month=cur_month
        
   #find the average changes
    sum_pl=sum(pl_changes)
    avg_pl=sum_pl/(len(pl_changes))

    #find the highest profit and lowest lose
    high_pl=max(pl_changes)
    low_pl=min(pl_changes)
    
    #find the index and add one since the first month was skipped inthe profit/losses array
    high_index=pl_changes.index(high_pl)+1
    low_index=pl_changes.index(low_pl)+1
    
    #save which months are the best and worst
    best_month=month[high_index]
    worst_month = month[low_index]
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {mcount}")
print(f"Total:  ${net_pl}")
print(f"Average Change:  ${avg_pl:.2f}")
print(f"Greatest Increase in Profits:  {best_month} (${high_pl})")
print(f"Greatest Decrease in Losses:  {worst_month} (${low_pl})")
