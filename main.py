import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://www.noticiasdeaveiro.pt/aveiro-arcos-voltar-a-ter-quiosque-de-engraxador/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
# Send a GET request to fetch the webpage
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Find all links on the webpage
    links = soup.find_all('p')
    
    # Print each link with its text and URL
    for link in links:
        # Extract the text and href attribute of each link
        link_text = link.get_text().strip()
        #link_url = link.get('href')
        
        # Print the link information
        print(f"Link Text: {link_text}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")