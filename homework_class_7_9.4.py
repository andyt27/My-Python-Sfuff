name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
for line in handle:
    if not line.startswith("From "): continue
    line = line.split()
    st.append(line[1])
 counts = dict()
 for word in lst:
    counts[word] = counts.get(word,0) + 1

bcount = None
bword = None
for word,count in counts.items():
    if bcount is None or count > bcount:
    bcount = count
    bword = word