from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://steamcommunity.com/market/').text
soup = BeautifulSoup(html_text, 'html.parser')
item = soup.find('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult")
item_name = item.find('span', class_ = 'market_listing_item_name').text.replace(" ","_")
print(item_name)
#print(html_text)
