fname = input('Enter the file name: ') 
fhand = open(fname)

for line in fhand:
        line = line.rstrip()
        print(line.upper())

# Write a program to read through a file and print the 
# contents of the file (line by line) all in upper case. 