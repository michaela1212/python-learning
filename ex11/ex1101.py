import re
hand = open('mbox.txt')
searching = input("Enter a regular expression: ")
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(searching, line):
        count += 1

print(count)

# Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched 
# the regular expression
