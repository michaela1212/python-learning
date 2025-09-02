fname = input('Enter file: ') 
fhand = open(fname)
domain = {}

for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        domains = email.split("@")[1]
        domain[domains] = domain.get(domains,0) + 1
print(domain)

#This program records the domain name (instead of the address) where the message was 
# sent from instead of who the mail came from (i.e., the whole email address). At the 
# end of the program, print out the contents of your dictionary.