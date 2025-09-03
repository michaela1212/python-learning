fname = input('Enter file: ') 
fhand = open(fname)
emails = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1] 
        emails[email] = emails.get(email,0) + 1

l = list()
for key, val in list(emails.items()):
    l.append((val, key))

l.sort(reverse=True)

for key, val in l[:1]:
    print(val, key)

#Revise a previous program as follows: Read and parse the “From” lines and pull out 
# the addresses from the line. Count the number of messages from each person using a 
# dictionary.

#After all the data has been read, print the person with the most commits by creating 
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse 
# order and print out the person who has the most commits.    
