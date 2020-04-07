# Modules
import csv
import os

# Create empty list for csv file
polls=[]
# Create empty dictionary to record only candidate names
dict_polls={}
# Create empty dictionaty to summarize the total number votes per candidate name
dict_summary={}


#Get the data from the source
election_data_csv = os.path.join("election_data.csv")
#Read the csv file
with open(election_data_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #print(csv_reader)
# Convert pollreader string to list 
for row in csv_reader:
    polls.append(row)
       
    # Convert polls list into dictionary for counting and grouping candidate names
for row in polls:
    name_key=row[1]
    if name_key not in dict_polls:
        # insert name_key into dictionary and initialize to 0
        dict_polls[name_key]=0
        # count the name key inside dictionary
        dict_polls[name_key]+=1
    
    # Compute the percentages of each name key of dict_polls and insert into dict_summary
total_polls=len(polls)
for name in dict_polls:
    dict_summary[name]=round((dict_polls[name]/total_polls)*100)
        
        
    # Initialize the highest value to comapre
highest=0
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
for name in dict_summary:
    if highest < dict_summary[name]:
        highest=dict_summary[name]
        winner=name
            
    
# Output to console
print("Election Results")
print("-------------------------") 
print("Total Votes: "+str(len(polls)))
print("-------------------------")
print(str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
print("-------------------------")
print("Winner: "+winner)
print("-------------------------")

#Output file
election_outputfile = os.path.join("Pypoll", "election_output.txt")
# Output to text file
text_file=open(election_outputfile,"x")
text_file.write("Election Results")
text_file.write("\n-------------------------")
text_file.write("\nTotal Votes: "+str(len(polls)))
text_file.write("\n-------------------------")
text_file.write("\n"+str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
text_file.write("\n-------------------------")
text_file.write("\nWinner: "+winner)
text_file.write("\n-------------------------")
    
# Close text file
text_file.close()