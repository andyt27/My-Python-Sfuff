fname = input("Enter file name: ")
fh = open(fname)
for i in fh.readlines():
    print(i.upper().rstrip())