import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter file name: ')

response = urllib.request.urlopen(url)
data = response.read().decode()

print(f"Retrieved {len(data)} characters")

info = json.loads(data)

comments = info.get("comments", [])
count = len(comments)
#total_sum = 

print(f"Count: {count}")
#for item in info:
#    print('Name', item['name'])
#    print('Attribute', item['count'])
