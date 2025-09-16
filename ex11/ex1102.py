import re
hand = open('mbox.txt')
count = 0
number = list()

for line in hand:
    line = line.rstrip()
    x = re.findall('^New\sRevision:\s(\d+)', line)
    if len(x) > 0:
        for numbers in x:
            numbers = int(numbers)
            number.append(numbers)

print(sum(number)/len(number))

#  Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the 
# findall() method. Compute the average of the numbers and print out the average as 
# an integer.
