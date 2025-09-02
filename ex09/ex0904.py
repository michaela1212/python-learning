fname = input('Enter file: ') 
fhand = open(fname)
emails = {}
maxs = 0
mins = 1
maxes = None
minus = None

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1] 
        emails[email] = emails.get(email,0) + 1

for c in emails:       
    if emails[c] > maxs:    
        maxes = c
        maxs = emails[c]
    if emails[c] <= mins:    
        minus = c
        mins = emails[c]

print('Maximum: ', maxes,maxs, 'Minimum: ', minus, mins) 
  


# Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through 
# the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to 
# find who has the most messages and print how many messages the person has.