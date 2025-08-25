def computepay(hours, rates):
    print("In computepay", hours, rates)
    if hours <= 40:
        pay = hours * rates
    else:
        pay = (40 * rates) + (hours-40) * (rates*1.5)
    print("Returning:",pay)
    return pay
 
hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hour)
fr = float(rate)
pay = computepay(fh, fr) 

print("Pay:",pay)

#Rewrite your pay computation with time-and-a-half for overtime and create a 
# function called computepay which takes two parameters (hours and rate).