hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hour)
fr = float(rate)
if fh <= 40:
    pay = fh * fr
    print("Pay:",pay)
else:
    pay = (40 * fr) + (fh-40) * (fr*1.5)
    print("Pay:",pay)

#Rewrite your pay computation to give the employee 1.5 times the hourly rate 
# for hours worked above 40 hours.