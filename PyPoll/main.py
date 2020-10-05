import os
import csv
pypoll_csv = os.path.join('Resources','02-Homeworks_03-Python_Instructions_PyPoll_Resources_election_data.csv')
vote_count = 0
winning_candidate = ""
vote_counter_Khan = 0
vote_counter_Li = 0
vote_counter_Correy = 0
vote_counter_Tooley = 0
with open(pypoll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        vote_count += 1
        if row[2] == "Khan":
            vote_counter_Khan +=1
        if row[2] == "Correy":
            vote_counter_Correy +=1
        if row[2] == "Li":
            vote_counter_Li += 1
        if row[2] == "O'Tooley":
            vote_counter_Tooley +=1
    print(vote_count,vote_counter_Khan,vote_counter_Correy,vote_counter_Li,vote_counter_Tooley)

        
