fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)
many = {}

for line in fhand :
    line = line.rstrip()
    wds = line.split()

    for w in wds :
        many[w] = many.get(w, 0) + 1

# Find the word with the largest count

largest = None
bigword = None

for kifunguu, thamani in many.items() :
    print(kifunguu, thamani)
    if largest is None or thamani > largest :
        largest = thamani
        bigword = kifunguu

print(bigword, largest)
