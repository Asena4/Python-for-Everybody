fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)
many = {}

for line in fhand :
    line = line.rstrip()
    wds = line.split()

    for w in wds :
        many[w] = many.get(w, 0) + 1

# Find the top 5 words by frequency

tmp ={}
newlist = []
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)

for v,k in cool[:5]:
    print(k,v)
