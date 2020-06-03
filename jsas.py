import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter url : ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)

total = 0

for u in js['comments']:
    tot = int(u['count'])
    total = total + tot

print('Total count : ',total)
