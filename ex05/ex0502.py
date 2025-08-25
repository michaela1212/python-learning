count = 0 
total = 0
mx = None
mn =  None

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
    if mx is None or val > mx: 
        mx = val
    if mn is None or val < mn: 
        mn = val
print('Total: ',total, 'Count: ',count, 'Max: ',mx, 'Min: ',mn) 

#Write another program that prompts for a list of numbers as above and at the end 
# prints out both the maximum and minimum of the numbers instead of the average.