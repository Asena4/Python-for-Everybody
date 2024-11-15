# Create a file handle and initialise a list
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

# Loop into the file handle
for line in fh:
    # Convert string to list elements
    sentence = line.split()
    for word in sentence:
        # Exclude recurring words from the list
        if word in lst:
            continue
        # Append unique words to the list
        lst.append(word)
# Sort in ascending order
lst.sort()
print(lst)
