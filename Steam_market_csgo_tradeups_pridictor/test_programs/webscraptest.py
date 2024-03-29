from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://steamcommunity.com/market/search?appid=730').text
soup = BeautifulSoup(html_text, 'html.parser')
items = soup.find_all('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult")
for item in items:
    item_name = item.find('span', class_='market_listing_item_name').text.replace(" ", "_")
    item_price = item.find('span', class_='sale_price').text
    file = open('files\data.txt', 'a+')
    file.write(item_name + ' = ' + item_price)
    file.write("\n")
    print(item_name + ' = ' + item_price)
