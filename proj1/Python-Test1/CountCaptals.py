filename = '/users/mrajagopal/WaitTypes.sql'
fh = open(filename,'r')
count=0
## you can iterate through multiple lines
for l in fh:
    for c in l:
        count +=(1 if c.isupper() else 0)

print (count)