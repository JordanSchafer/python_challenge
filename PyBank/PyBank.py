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
num_month=0
change_list=[]
months=[]
greatest_increase=["",0]
greatest_decrease=["",999999]
total_net=0
#Set path to csv file budget_data.csv
csvpath=os.path.join("Resources","budget_data.csv")


with open(csvpath) as csvfile:
    
    csv_reader=csv.reader(csvfile,delimiter=",")
    csv_header=next (csv_reader)
    #print(f"Header: {csv_header}")
    
    #read first row to leave out of net_change
    first_row=next(csv_reader)
    num_month+=1
    
    total_net+=int(first_row[1])
    prev_net=int(first_row[1])
    
    
    for row in csv_reader:
        
        #track totals
        num_month+=1
        total_net+=int(row[1])
        
        #track changes
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        change_list.append(net_change)
        months.append(row[0])
        
        #find greatest increase
        if net_change>greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        
        #find greatest decrease
        if net_change<greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change
            
#calculate average net change
change_avg=sum(change_list)/len(change_list)
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {num_month}")
print(f"Total:  ${total_net}")
print(f"Average Change:  ${change_avg:.2f}")
print(f"Greatest Increase in Profits:  {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Losses:  {greatest_decrease[0]} (${greatest_decrease[1]})")


outputfile = os.path.join("Output","Analysis.txt")
with open(outputfile,"w")as outfile:
    
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {num_month}\n")
    outfile.write(f"Total:  ${total_net}\n")
    outfile.write(f"Average Change:  ${change_avg:.2f}\n")
    outfile.write(f"Greatest Increase in Profits:   {greatest_increase[0]} (${greatest_increase[1]})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_decrease[0]} (${greatest_decrease[1]})\n")