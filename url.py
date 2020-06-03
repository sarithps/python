from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
total = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    num = tag.contents[0]
    inum = int(num)
    total = total + inum

print ('Sum is :',total)
