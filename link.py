from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
cnt = int(input('Enter the count: '))
position = int (input('Enter position: '))
lst = []
for any in range(cnt):
    link = tags[position].get('href', None)
    print('Link : ', link)
    lst.append(tags[position].contents[0])
    html = urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(lst[-1])
