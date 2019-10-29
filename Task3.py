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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extractFixedAreaCode(number):
    if receiver.find('(') == 0 and receiver[1] == '0':
        return number[1:number.find(')')]


numbersCalledByBangalore = []
telemarketers = []
mobile = []
fixed = set()

mobilePrefixes = set()
fixedLinesAreaCodes = set()
telemarketersAreaCode = set()
fixedNumbersInBangaloreCalledByBangalore = set()

areaCodes = []

for call in calls:
    caller = call[0]
    receiver = call[1]
    if caller[0:5] == '(080)':
        numbersCalledByBangalore.append(receiver)
        if receiver[0:3] == '140':
            telemarketers.append(receiver)
            telemarketersAreaCode.add(receiver[0:3])
        if str.isspace(receiver[5:6]) and receiver[0:1] in ['7', '8', '9']:
            mobile.append(receiver)
            mobilePrefixes.add(receiver[0:4])
        if receiver.find('(') == 0 and receiver[1] == '0':
            fixed.add(receiver)
            fixedLinesAreaCodes.add(extractFixedAreaCode(receiver))
        if receiver[0:5] == '(080)':
            fixedNumbersInBangaloreCalledByBangalore.add(receiver)

areaCodes = list(mobilePrefixes) + list(fixedLinesAreaCodes) + list(telemarketersAreaCode)

print("The numbers called by people in Bangalore have codes:")
for code in sorted(areaCodes):
    print(code)

fixedLinesPercent = len(fixedNumbersInBangaloreCalledByBangalore) / len(fixed)  * 100
print("{:.1f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(fixedLinesPercent))