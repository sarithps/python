fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for any in words:
        if any not in lst:
            lst.append(any)
print (lst)
