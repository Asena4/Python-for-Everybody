#Enter the desired file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('The file cannot be found in the present directory')
    quit()
#Initialise the total addition of spam confidence and the count
tfsc = 0
count = 0
#Loop into the string to find the spam confidence and the count
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    sppos = line.find(' ')
    sc = line[sppos:]
    fsc = float(sc)
    tfsc = tfsc + fsc
    count = count + 1
#Calculate the average of the spam count
avsc = (tfsc/count)
print('Average spam confidence:',avsc)
