hour = input("Enter hours: ")
rate = input("Enter rate: ")
fh = float(hour)
fr = float(rate)
if fh <= 40:
    pay = fh * fr
    print("Pay:", pay)
else:
    pay = (40 * fr) + ((fh - 40) * fr * 1.5)
    print("Pay:", pay)