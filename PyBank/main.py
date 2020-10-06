from prettytable import PrettyTable
import os
import csv
pybank_csv = os.path.join('Resources','02-Homeworks_03-Python_Instructions_PyBank_Resources_budget_data.csv')
month_counter = 1
Total_profit = 0
greatest_inc = 0
great_i_mo = ""
greatest_dec = 0
great_d_mo = ""
month_list_change = []
with open(pybank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    Total_profit = int(first_row[1])
    prev_prof_value = int(first_row[1])
    # print(Total_profit,prev_prof_value)
    # first_row = next(csvreader)
    # print(header)
    for row in csvreader:
        month_counter += 1
        Total_profit = Total_profit + int(row[1])
        change = int(row[1]) - prev_prof_value
        prev_prof_value = int(row[1])
        month_list_change.append(change)
        if change > greatest_inc:
            greatest_inc = change
            great_i_mo = row[0]
        if change < greatest_dec:
            greatest_dec = change
            great_d_mo = row[0]
average_profit = sum(month_list_change)/len(month_list_change)
aver_prof = round(average_profit,2)
x=PrettyTable()
x.field_names = ["Variables", "Values", "Month"]
x.add_row(["Number of months:",month_counter,""])
x.add_row(["Total amount of P/L:",Total_profit,""])
x.add_row(["Average change:",aver_prof,""])
x.add_row(["Greatest increase in profits:",greatest_inc,great_i_mo])
x.add_row(["Greatest decreas in profits:",greatest_dec,great_d_mo])
print(x)
analysis_file=os.path.join("analysis","anlysis.txt")
with open(analysis_file,"w") as f:
    print(x,file=f)
# print(Total_profit,month_counter,greatest_dec,great_d_mo,greatest_inc,great_i_mo,average_profit)
# print("- - - - - - - - - - - - - - - - - - - - - - ")
# Print("!             Financial Analysis           !")
# Print("- - - - - - - - - - - - - - - - - - - - - - ")
# Print("Total Months =" month_counter)
# Print("Total =")

        # counter for months


        # print(', '.join(row))
        # CSV Reader works

 # len(csvreader)
    # print (len(csvfile))
    # # print(first_row)



# print(pybank_csv)
# def prof_loss (pybank_data):
#     month = str(pybank_data [0])
#     p_l_value = int(pybank_data[1])
#     print (p_l_value)
#     print (prof_loss)