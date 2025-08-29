fname = input('Enter file: ') 
fhand = open(fname)
words = {}

for line in fhand:
    if line.startswith("From "):
        word = line.split()[2] 
        words[word] = words.get(word,0) + 1

print(words)


# Write a program that categorizes each mail message by which day of the week 
# the commit was done. To do this look for lines that start with “From”, 
# then look for the third word and keep a running count of each of the days of the 
# week. At the end of the program print out the contents of your dictionary 
# (order does not matter).