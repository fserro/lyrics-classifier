
import requests
import sys
import re

# 1. Download the web page https://en.wikipedia.org/wiki/Berlin
url = 'https://en.wikipedia.org/wiki/Berlin'
response = requests.get(url)

# 2. Print the status code of the request
print(response.status_code)

# 3. Print the size of the HTML document in characters
html = response.text

print(len(html))            # size in characters
print(sys.getsizeof(html))  # memory size in bytes

# 4. Extract all hyperlinks (<a href="...">)
links = re.findall('''<a href="([^"]*)"[^>]*>[^<]*<\/a>''', html)

# 5. Remove all HTML tags
notags = re.sub('<[^>]*>', ' ', html)

# 6. Count how many times the word 'Berlin' occurs
print(notags.count('Berlin'))
# or
print(len(re.findall('Berlin', notags)))

# 7. Count the total number of words on the page
print(len(re.findall('\w+', notags)))

# very similar
# len(re.findall(r'[a-zA-Z]+', s))
# len(re.findall(r'[a-zA-Z0-9]+', s))
