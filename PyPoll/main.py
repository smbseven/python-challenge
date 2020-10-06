import os
import csv
from prettytable import PrettyTable
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
    # print(vote_count,vote_counter_Khan,vote_counter_Correy,vote_counter_Li,vote_counter_Tooley)
    vc = vote_count
vote_pctg_khan = (vote_counter_Khan / vote_count) * 100
vpk = round(vote_pctg_khan,2)
vote_pctg_correy = (vote_counter_Correy / vote_count) * 100
vpc = round(vote_pctg_correy)
vote_pctg_li = (vote_counter_Li / vote_count) * 100
vpl = round(vote_pctg_li,2)
vote_pctg_tooley = (vote_counter_Tooley / vote_count) * 100
vpo = round(vote_pctg_tooley,2)
if vote_pctg_khan > vote_pctg_correy and vote_pctg_khan > vote_pctg_li and vote_pctg_khan > vote_pctg_tooley:
    winner = "Khan"
    # print ("Khan wins")
if vote_pctg_correy > vote_pctg_khan and vote_pctg_correy > vote_pctg_li and vote_pctg_correy > vote_pctg_tooley:
    winner = "Correy"
    # print ("Correy wins")
if vote_pctg_li > vote_pctg_khan and vote_pctg_li > vote_pctg_correy and vote_pctg_li > vote_pctg_tooley:
    winner = "Li"
    # print ("Li wins")
if vote_pctg_tooley > vote_pctg_khan and vote_pctg_tooley > vote_pctg_correy and vote_pctg_tooley > vote_pctg_li:
    winner = "O'Tooley"
    # print ("O'Tooley wins")
v = "Election Results"
w = "Total votes: " + str(vote_count)
y = "The winner is: " + str(winner)
x=PrettyTable()
# http://zetcode.com/python/prettytable/
x.field_names = ["Candidate", "Percentage", "Number of Votes"]
x.add_row(["Khan",vpk,vote_counter_Khan])
x.add_row(["Correy",vpc,vote_counter_Correy])
x.add_row(["Li",vpl,vote_counter_Li])
x.add_row(["O'Tooley",vpo,vote_counter_Tooley])
print (v)
print(w)
print(x)
print(y)
analysis_file=os.path.join("analysis","anlysis.txt")
with open(analysis_file,"w") as f:
     print(v,file=f)
     print(w,file=f)
     print(x,file=f)
     print(y,file=f)
#  print(Total_profit,month_counter,greatest_dec,great_d_mo,greatest_inc,great_i_mo,average_profit)



# print(vote_count)
# x = PrettyTable()
# # http://zetcode.com/python/prettytable/
# x.field_names = ["Election Results"]
# x.add_row = ["Total Votes = " + str(vc)]
# print(x)

# print(vote_pctg_khan,vote_pctg_correy,vote_pctg_li,vote_pctg_tooley)
# print (winner)
# print(vote_count)
# win_percent = (wins / total_matches) * 100

        
