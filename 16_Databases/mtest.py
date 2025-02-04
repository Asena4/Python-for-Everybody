#Set default file name or enter unique file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)

#Declare wds as list and hrs as a dictionary
wds = []
email = {}

#Loop into file handle
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    #Loop then split into the line and words to get the hours 
    for words in line:
        wds = line.split()
        wds = wds[1]
        wds = wds.split('@')
        wds = wds[1]
        #print(wds)
    #Enter the hours and their respective count into hrs
    email[wds] = email.get(wds, 0) + 1

#Sort hrs in ascending order    
#sorted(hrs.items())
#for kifunguu, thamani in sorted(hrs.items()):
#    print(kifunguu, thamani)
print(email)
#bigcount = None
#bigword = None

#for key, val in email.items() :
#    if bigcount is None or val > bigcount :
#        bigword = key
#        bigcount = val
#print(bigword, bigcount)
