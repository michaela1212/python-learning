hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    fh = int(hour)
    fr = int(rate)
    pay = fh * fr
except:
    hour = -1
    rate = -1
    pay = hour * rate
    
if pay > 1:
        print("Pay:",pay)
else:
        print("Please enter numeric input")

#Rewrite your pay program using try and except so that your program handles 
# non-numeric input gracefully by printing a message and exiting the program.