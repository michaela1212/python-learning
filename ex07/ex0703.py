
fname = input('Enter the file name: ') 
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try:
    fhand = open(fname)  
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print(count)      

#Sometimes when programmers get bored or want to have a bit of fun, they add a 
# harmless Easter Egg to their program. Modify the program that prompts the user 
# for the file name so that it prints a funny message when the user types in the 
# exact file name “na na boo boo”. The program should behave normally for all other 
# files which exist and don’t exist. 