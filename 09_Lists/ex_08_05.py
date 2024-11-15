#Create file handle and initialize count for lines
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File does not exist in this directory")
    exit()
count = 0

#Loop into file handle
for line in fh:
    #Parse into lines that starts with 'From '
    if line.startswith('From '):
        #Split the line to remove whitespaces
        sl = line.split()
        #Print the second character
        print(sl[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
