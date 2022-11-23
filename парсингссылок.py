
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')
count = int(input("Enter count"))
position = int(input("Enter position"))


counthide = 0
positionhide = 0

while positionhide != position:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        print(counthide)
        if counthide == count:
            positionhide += 1
            counthide = 0
            url = a
            break
        else:
            counthide += 1
            a = tag.get('href', None)
            print(tag.contents[0])

print(positionhide)
