import os
import csv
import Counter

poll_df = os.path.join('Resources’, ‘election_data.csv’)

total_candidate = []
votes_count = []

with open(poll_df) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=“,”)
    csv_header = next (csvreader)

    total_votes = (len(list(csvreader))

    for row in csvreader:
        total_candidate.append(str(row[2]))

    total_candidate_count = {}
    for candidate in total_candidate:
    if candidate in total_candidate_count:
        total_candidate_count[candidate] += 1
    else:
        total_candidate_count[candidate] = 1

    votes_str = []
    names = []
    for key in total_candidate_count.keys():
    votes_str.append(total_candidate_count[key])
    names.append(str(key))

    votes = []
    votes_percent = []
    for vote in votes:
    votes_percent.append(round(vote / total_votes * 100, 3))
    max_percent = max(votes_percent)
    min_percent = min(votes_percent)

    for i in range(len(votes_percent)):
    if votes_percent[i] == max_percent:
        winner = names[i]
        winner_votes = int(votes[i])
    # if votes_percent[i] == min_percent:
    #     looser = names[i]
    #     looser_votes = int(votes[i])


print(“Election Results”)
print(f'------------------')
print(“Total Votes: ” , total_votes)
print(f'------------------')
for i in range(len(names)):
    print(f”{names[i]}: {votes_percent[i]}%  ({votes[i]})“)
print(f'------------------')
print(“Winner: “, winner)
print(f'------------------')

# Print csv_header
print(f'Financial Analysis')

print(f'Total Months: {totalMonths}')
print(f'Total:{netTotal}')

# Write results to CSV output file
output_path = os.path.join(‘..‘, ‘/Users/grinn/UCBWork/Python_Work/python_challenge/PayPoll/output’, ‘output_election_data.csv’)
with open(output_path, ‘w’) as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =“,”)
    csvwriter.writerow([‘Election Results’])
    csvwriter.writerow([‘Total Votes:‘, total_votes])
    csvwriter.writerow([])
    for i in range(len(names)):
        csvwriter.writerow([names[i], str(votes_percent[i])+‘%’, votes[i]])
    csvwriter.writerow([“Winner: “, winner])