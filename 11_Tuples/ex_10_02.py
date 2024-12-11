#Set default file name or enter unique file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)

#Declare wds as list and hrs as a dictionary
wds = []
hrs = {}

#Loop into file handle
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    #Loop then split into the line and words to get the hours 
    for words in line:
        wds = line.split()
        wds = wds[5]
        wds = wds.split(':')
        wds = wds[0]
    #Enter the hours and their respective count into hrs
    hrs[wds] = hrs.get(wds, 0) + 1

#Sort hrs in ascending order    
sorted(hrs.items())
for kifunguu, thamani in sorted(hrs.items()):
    print(kifunguu, thamani)
