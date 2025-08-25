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