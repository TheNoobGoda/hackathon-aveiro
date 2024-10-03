import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.noticiasdeaveiro.pt/category/regiao/aveiro/"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all 'a' tags with class 'td-image-wrap' or 'td-module-thumb'
    titles = soup.find_all('a', class_='td-image-wrap')

    # Loop through and print out each title (from the 'title' attribute or text)
    for title in titles:
        print(title['title'])  # The title is inside the 'title' attribute of the 'a' tag
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
