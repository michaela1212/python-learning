fname = input('Enter file: ') 
fhand = open(fname)
hour = {}

for line in fhand:
    if line.startswith("From "):
        time = line.split()[5]
        hours = time.split(":")[0]
        hour[hours] = hour.get(hours,0) + 1

l = list(hour.items())
#l = []
#for key, val in hour.items():
 #   l.append((key, val))

l.sort()

for key, val in l[:]:
    print(key, val)

#This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then 
# splitting that string into parts using the colon character. Once you have 
# accumulated the counts for each hour, print out the counts, one per line, sorted by 
# hour as shown below.
