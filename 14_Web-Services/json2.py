# Import libraries
import urllib.request, urllib.parse, urllib.error
import json

# Prompt for the URL
url = input('Enter file name: ')

# Read JSON data from URL
data = urllib.request.urlopen(url).read().decode()

print(f"Retrieved {len(data)} characters")

# Parse the JSON data
try:
    info = json.loads(data)
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)
    exit()

# Extract the comment counts and compute the sum
comments = info.get("comments", [])
count = len(comments)
total_sum = 0
for comment in comments:
    total_sum = total_sum + comment["count"]

# Print the results
print(f"Count: {count}")
print(f"Sum: {total_sum}")
