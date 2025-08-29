fname = input('Enter file: ') 
fhand = open(fname)

words = dict()
for line in fhand:
    count = line.split()
    for word in count:
#        words[word] = words.get(word,0) + 1
#        print(word, words[word])
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

print(words)

#Write a program that reads the words in words.txt and stores them as keys in a 
# dictionary. It doesn’t matter what the values are. Then you can use the in operator 
# as a fast way to check whether a string is in the dictionary.
