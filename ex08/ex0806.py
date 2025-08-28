num = list()
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        val = float(line)
        num.append(val)

    except: 
        print("Invald Input")
        continue

print('Maximum: ', max(num), 'Minimum: ', min(num)) 

# Rewrite the program that prompts the user for a list of numbers and prints 
# out the maximum and minimum of the numbers at the end when the user enters 
# "done”. Write the program to store the numbers the user enters in a list 
# and use the max() and min() functions to compute the maximum and minimum 
# numbers after the loop completes.