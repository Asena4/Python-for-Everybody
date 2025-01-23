import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Prompt for user inputs
url = input("Enter URL: ").strip()
count = int(input("Enter count: "))
position = int(input("Enter position: "))

print(f"Retrieving: {url}")

# Loop for the specified number of times
for _ in range(count):
    # Open the URL and read the HTML
    html = urllib.request.urlopen(url).read()
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    tags = soup('a')

    # Get the URL at the specified position (1-indexed)
    url = tags[position - 1].get('href', None)
    print(f"Retrieving: {url}")

# The final name is in the last retrieved URL
last_name = url.split('_')[-1].split('.')[0]
print(f"The answer to the assignment is: \"{last_name}\"")

