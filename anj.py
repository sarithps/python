import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


count = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

url = urllib.request.urlopen(address)
print('Retrieving', url)

data = url.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data.decode())
com = tree.findall('.//comment')

for item in com:
    c = item.find('count').text
    ic = int(c)
    count = count + ic


print('Count =',count )
