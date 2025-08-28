fname = input('Enter file: ') 
fhand = open(fname)
words = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 
        'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 
        'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 
        'with', 'yonder']

for x in fhand:
    x = x.split()
    x.sort()

for x in words:
    if x not in words:
        words.extend(x)
    words.sort()    
    words = x.split()
    print(x)

#Write a program to open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split function. 
# or each word, check to see if the word is already in the list of unique words.
#If the word is not in the list of unique words, add it to the list. 
#When the program completes, sort and print the list of unique words in 
#alphabetical order.
