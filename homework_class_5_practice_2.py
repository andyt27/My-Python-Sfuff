Sum = 0
Count = 0
fname = input('Enter File Name:')
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:")
        continue
    if line.startswith('X-DSPAM-Confidence:')
         a = float(line[20:])
         Sum = Sum + a
         Count = Count + 1
print('Average spam confidence:', Sum/Count)