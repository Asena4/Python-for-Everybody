# Set default file name or type unique file name 
name = input('Enter file name: ')
if len(name) < 1:
    name = 'mbox-short.txt'
    
fh = open(name) # Open a file handle
wds = dict() # Initialise dictionary

# Loop into file handle
for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split() # Split lines into a list of words
    email = words[1] # Select the postion email address
    # Add the email address with its count to the wds dictionary
    wds[email] = wds.get(email, 0) + 1

# Initialise variables
bigcount = None
bigword = None
# Loop into dictionary
for kifunguu, thamani in wds.items() :
    if bigcount is None or thamani > bigcount :
        bigword = kifunguu
        bigcount = thamani
print(bigword, bigcount)
