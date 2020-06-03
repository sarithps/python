name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    print (line)
