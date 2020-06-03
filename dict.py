name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    if line.startswith('From: '):
        line = line.rstrip()
        word = line.split()
        email = word[1]
        if email in di:
            di[email] = di[email] + 1
        else:
            di[email]=1

bigword = None
bigcount = 0
for word,count in di.items():
    if count > bigcount :
        bigcount = count
        bigword = word

print (bigword,bigcount)
