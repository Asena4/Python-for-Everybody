# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print(f"Retrieving: {url}")

def html_it(url, count, position):
    for i in range(count):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        pst = 0
        tags = soup('a')
        for tag in tags:
            pst = pst + 1
            if pst == position:
                url = tag.get('href', None)
                print(f"Retrieving: {url}")
    return ('\0')

cnt = 0

if cnt < count:
    print(html_it(url, count, position))
    cnt = cnt + 1
