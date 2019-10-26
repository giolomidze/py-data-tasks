"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

callResults = {}

for call in calls:

    caller = call[0]
    receiver = call[1]
    callDuration = call[3]
    
    if caller not in callResults:
        callResults.update({caller: int(callDuration)})
    else:
        callResults.update({caller: int(callResults[caller]) + int(callDuration)})

    if receiver not in callResults:
        callResults.update({receiver: int(callDuration)})
    else:
        callResults.update({receiver: int(callResults[receiver]) + int(callDuration)})

numberWithlongestTimeSpent = sorted(callResults, key=callResults.__getitem__, reverse=True)[0]

print(numberWithlongestTimeSpent + " spent the longest time, "+str(callResults[numberWithlongestTimeSpent])+" seconds, on the phone during September 2016.")