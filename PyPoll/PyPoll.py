
#import dependencies'
import os
import csv


csvpath=os.path.join("Resources","election_data.csv")

#vote counter
total_votes=0

#track candidates and their votes
candidate_choices=[]
candidate_votes={}

#winning candidate and their votes
winning_candidate=""
winning_count=0

with open(csvpath) as election_data:
    reader=csv.reader(election_data)
    
    header=next(reader)
    
    for row in reader:
        total_votes+=1
        
        candidate_name=row[2]
        
        if candidate_name not in candidate_choices:
            #add ne candidates as they're read and set vote count to 0 
            candidate_choices.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        #add another count for each vote
        candidate_votes[candidate_name]+=1
        

outpath=os.path.join("Output","Results.txt")

open with(outpath,"w") as out_file:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    

    for candidate in candidate_votes:

            # gets the number of votes for every candidate and finde percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100

            # finds winning vote count and candidate
            if (votes > winning_count):
                winning_count = votes
                winning_candidate = candidate

            # Prints each candidate, count and percentage
            print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
            outfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winning_candidate}\n")
    outfile.write("-------------------------\n")