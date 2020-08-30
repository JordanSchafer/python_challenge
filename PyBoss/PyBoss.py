#import dependencies
import csv
import os

#list of state abbrevations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath = os.path.join("employee_data.csv")
outpath = os.path.join("Results","formated_data.csv")

with open(csvpath)as csvfile:
    #set up csvreader and store header
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    #print(header)
    with open(outpath,'w',newline='')as outfile:
        #set up csvwriter and write header
        writer= csv.writer(outfile)
        writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
        for row in reader:
            
            #store csv file information
            empID=row[0]
            empName=row[1]
            empDOB=row[2]
            empSSN=row[3]
            empState=row[4]
            
            #split names into first and last name
            splitname=empName.split()
            empFname=splitname[0]
            empLname=splitname[1]
            
            #split date into year month and day
            splitDOB=empDOB.split("-")
            dobYear=splitDOB[0]
            dobMonth=splitDOB[1]
            dobDay=splitDOB[2]
            
            #create formatted strings
            formattedDOB=dobMonth+"/"+dobDay+"/"+dobYear
            formattedSSN="***-**-"+empSSN.split("-")[2]
            abbrState=us_state_abbrev.get(empState)
            
            #write formatted strings to file and terminals
            writer.writerow([empID,empFname,empLname,formattedDOB,formattedSSN,abbrState])
            print(str([empID,empFname,empLname,formattedDOB,formattedSSN,abbrState]))
            
        