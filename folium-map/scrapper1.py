import requests
import json
from bs4 import BeautifulSoup
headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138  Safari/537.36'}
# Make an initial request to get the page HTML
news_list=[]
for page in range(1, 11):  # Scrape pages 1 to 10
    endpoint = "https://www.indiatoday.in/api/ajax/loadmorecontent?page={page}&pagepath=/crime&pagetype=story/photo_gallery/video/breaking_news"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    data = json.loads(soup)
    for item in data:
        news_list.append(item)

print(news_list)