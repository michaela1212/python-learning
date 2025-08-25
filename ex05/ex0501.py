count = 0 
total = 0

while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        val = float(line)
    except: 
        print("Invald Input")
        continue
    total = total + val
    count = count + 1
    average = total / count

print('Total: ',total, 'Count: ',count, 'Average: ',average) 

#Write a program which repeatedly reads integers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the integers. 
# If the user enters anything other than a integers, detect their mistake using try 
# and except and print an error message and skip to the next integers.


    
