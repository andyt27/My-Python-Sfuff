a = imput('Enter a file name:')
text = open(a)
for i in text:
    print(i.upper().rstrip())
