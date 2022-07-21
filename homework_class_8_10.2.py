name = input('Enter file:"')
if len(name) < 1
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        word = line.split
        time = word[5]
        hours = time[:2]
        counts[hours] = counts.get(hours,0) + 1

for a, b in sorted(counts.items()):
    print (a,b)
