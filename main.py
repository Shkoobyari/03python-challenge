import os
import csv

csv_file_path = os.path.join('./', 'Resources', 'election_data.csv')
final_txt_file_path = os.path.join('./', 'Analysis', 'pypoll.txt')

total_votes = 0
candidates = []
vote_talley = {}

with open(csv_file_path) as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=',')

  header = next(csv_reader)

  for row in csv_reader:
    total_votes += 1
    candidate = row[-1]
    if candidate not in candidates:
      candidates.append(candidate)
      vote_talley[candidate] = 1
    else:
      vote_talley[candidate] += 1
print(vote_talley)
# Analyze data

final_vote = {}
for key, val in vote_talley.items():
  final_vote[key] = {
    'vote_number': val,
    'vote_percentage': (val / total_votes) * 100
  }
winner = ''
dummy_counter = 0
for key, val in final_vote.items():
  if val['vote_number'] > dummy_counter:
    dummy_counter = val['vote_number']
    winner = key

print(f"""Election Results \n-------------------- \nTotal Votes: {total_votes} \n-------------------- \nKhan: {final_vote['Khan']['vote_percentage']} ({final_vote['Khan']['vote_number']})\nCorrey: {final_vote['Correy']['vote_percentage']} ({final_vote['Correy']['vote_number']}) \nLi: {final_vote['Li']['vote_percentage']} ({final_vote['Li']['vote_number']}) \nO'Tooley: {final_vote["O'Tooley"]['vote_percentage']} ({final_vote["O'Tooley"]['vote_number']}) \n -------------------- \nWinner: {winner} \n--------------------""")

with open(final_txt_file_path, "w") as txtfile:
  txtfile.write(f"""Election Results \n-------------------- \nTotal Votes: {total_votes} \n-------------------- \nKhan: {final_vote['Khan']['vote_percentage']} ({final_vote['Khan']['vote_number']})\nCorrey: {final_vote['Correy']['vote_percentage']} ({final_vote['Correy']['vote_number']}) \nLi: {final_vote['Li']['vote_percentage']} ({final_vote['Li']['vote_number']}) \nO'Tooley: {final_vote["O'Tooley"]['vote_percentage']} ({final_vote["O'Tooley"]['vote_number']}) \n -------------------- \nWinner: {winner} \n--------------------""")