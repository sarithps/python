f = input('fname :')
if len(f)<1:
    f = 'mbox-short.txt'
c = 0
fh = open(f)
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        word = line.split()
        print(word[1])
        c = c + 1

print(c)
