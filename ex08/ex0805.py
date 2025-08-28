fname = input('Enter file: ') 
fhand = open(fname)
count = 0 
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '): 
        words = line.split()
        count = count + 1
        print(words[1])

print('There were', count, 'lines in the file with From as the first word.')

# Write a program to read through the mail box data and when you 
# find line that starts with “From”, you will split the line 
# into words using the split function. We are interested in 
# who sent the message, which is the second word on the From line.
