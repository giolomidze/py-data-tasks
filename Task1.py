"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phoneNumbers = []

for text in texts:
    caller = text[0]
    receiver = text[1]
    phoneNumbers.append(caller)
    phoneNumbers.append(receiver)


for call in calls:
    caller = call[0]
    receiver = call[1]
    phoneNumbers.append(caller)
    phoneNumbers.append(receiver)

totalPhoneNumbers = str(len(list(set(phoneNumbers))))

print("There are "+totalPhoneNumbers +
      " different telephone numbers in the records.")
