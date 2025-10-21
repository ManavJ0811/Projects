import requests
from bs4 import BeautifulSoup

# Define a User-Agent header to mimic a regular web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 1. Identify the URL of the page to scrape
url = input("URL OF THE WEBSITE YOU WANNA SCRAPE")

# 2. Fetch the page content (HTTP Request) - NOW PASSING THE HEADERS
try:
    # Notice the added 'headers=headers' argument
    response = requests.get(url, headers=headers) 
    response.raise_for_status() # Check for bad status codes
except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    exit()

# 3. Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# 4. Extract specific data
# We're targeting the main title of the Wikipedia page, which is usually in an <h1> tag
# with the ID 'firstHeading'.
title_tag = soup.find('h1', {'id': 'firstHeading'})

# 5. Output the result
if title_tag:
    page_title = title_tag.text
    print(f"Successfully scraped the page title: \n\n'{page_title}'")
else:
    print("Could not find the page title.")