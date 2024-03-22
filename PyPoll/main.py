# csv is needed to start so we import it.
import csv
import os

election_data_path = os.path.join('/Users/diego/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

with open(election_data_path, 'r') as csvfile:

    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

# This is how we are able to go down the row in the candidates column.
    candidates = [row[2] for row in csv_reader]

# Once we get the last code we need the names.
name = list(set(candidates))

#Variables to get the end result/names of candidates.
can_1 = name[0]
can_2 = name[1]
can_3 = name[2]

# Allows us to grab/count the votes for each can(candidate).
can_1_vote = candidates.count(can_1)
can_2_vote = candidates.count(can_2)
can_3_vote = candidates.count(can_3)

# To get the total amount of all the votes between each can(candidate).
tot_votes = len(candidates)

# Here we create a dict(dictionary) and inside the dict is the name
# of the can(candidate) along with their votes.
can_votes = {can_1: [can_1_vote],
             can_2: [can_2_vote],
             can_3: [can_3_vote]
             }

# Percentage of votes each can(candidate) won. 
# Formula is simple: we get the votes from each can(candidate)
# from the can_votes_summary above, then divide their individual
# votes by the total amount of votes and multpily by 100.
can_1_perc = (can_1_vote / tot_votes) * 100
can_2_perc = (can_2_vote / tot_votes) * 100
can_3_perc = (can_3_vote / tot_votes) * 100
# Time to reveal the the winner of the election
winner = max(can_votes, key= can_votes.get)

# Election results in Terminal
print_results = (
    "Election Results\n"
    "------------------------\n"
    f"Total Votes: {tot_votes}\n"
    f"------------------------\n"
    f"{can_1}: {can_1_perc}% ({can_1_vote})\n"
    f"{can_2}: {can_2_perc}% ({can_2_vote})\n"
    f"{can_3}: {can_3_perc}% ({can_3_vote})\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
)
print(print_results)
# Text file
with open('/Users/diego/Desktop/python-challenge/PyPoll/Analysis/Results', 'w') as elec_res:
    elec_res.write("Election Results\n")
    elec_res.write("------------------------\n")
    elec_res.write(f"Total Votes: {tot_votes}\n")
    elec_res.write(f"------------------------\n")
    elec_res.write(f"{can_1}: {can_1_perc}% ({can_1_vote})\n")
    elec_res.write(f"{can_2}: {can_2_perc}% ({can_2_vote})\n")
    elec_res.write(f"{can_3}: {can_3_perc}% ({can_3_vote})\n")
    elec_res.write("-------------------------\n")
    elec_res.write(f"Winner: {winner}\n")