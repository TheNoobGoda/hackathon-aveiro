######################### API STUFF

import requests

# Replace this with your API token
API_TOKEN = 'apify_api_Hui1YjAM1cjLRzmYJ9F65IXyoulxUi4GDNGu'

# Corrected Actor ID for the Facebook Page Scraper
ACTOR_ID = 'apify~facebook-posts-scraper'

# The Facebook page you want to scrape
START_URL = 'https://www.facebook.com/noticiasdeaveiro/?locale=pt_PT'

# API endpoint to trigger the scraper
url = f'https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={API_TOKEN}'

# Headers
headers = {'Content-Type': 'application/json'}

# Body (scraper configuration)
payload = {
    "startUrls": [
        { "url": START_URL }
    ],
    "maxPosts": 10,       # Max posts to scrape
    "includeComments": False   # Set to True if you want comments
}

# Make the request to start the scraper
response = requests.post(url, headers=headers, json=payload)

# Get the run ID from the response
data = response.json()

# print(type(data))
# print("")
# print(data)


DATASET_ID = 'HZ2Pb7WSKtphMNyKX'
API_TOKEN = 'apify_api_Hui1YjAM1cjLRzmYJ9F65IXyoulxUi4GDNGu'

# API endpoint to get dataset results
url = f'https://api.apify.com/v2/datasets/{DATASET_ID}/items?token={API_TOKEN}'

# Make the request to fetch the results
response = requests.get(url)

# Get the data in JSON format
data = response.json()

# Print the titles of the posts
for post in data:
    # print(post.get('postText', 'No title available'))
    print("-------------------------------------------------------------------------------------------")
    try:
        print('text:'+ post['text'])
    except:
        print('noText')
    
    try:
        print('previewTitle: '+post['previewTitle'])
    except:
        print('noPreviewTitle')

    try:
        print('previewDescription: '+post['previewDescription'])
    except:
        print('noPreviewDescription')

