from bs4 import BeautifulSoup
import requests
import time     #5-number of skins, 6-rarity, 5-wear
skins_price = [[[0.09, 0.04, 0.03, 0.03, 0.03], [0.08, 0.03, 0.03, 0.03, 0.03], [0.06, 0.03, 0.03, 0.03, 0.03], [0.1, 0.03, 0.03, 0.03, 0.03], [0.16, 0.03, 0.03, 0.03, 0.03], [0, 0, 0, 0, 0]],
               [[0.6, 0.12, 0.09, 0.12, 0.09], [0.2, 0.41, 0.09, 0.09, 0.09], [0.16, 0.12, 0.09, 0, 0], [0.42, 0.11, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[1.16, 0.95, 0.82, 1.4, 0], [1.1, 1.1, 0.79, 0.89, 0], [1.72, 0.96, 0.77, 1.04, 0], [1.85, 0.9, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[10.7, 6.16, 3.68, 2.55, 5.11], [10.0, 6.94, 11.2, 6.3, 2.13], [10.2, 7.4, 5.58, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[12.8, 8.25, 34.8, 14.1, 9.75], [0, 61.1, 5.91, 3.25, 3.03], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
set_name = ['inferno','inferno_2']
wear_category = [0,1,2,3,4]
exterior = 'normal'
rarity = ['Common','Uncommon', 'Rare', 'Mythical', 'Legendary', 'Ancient' ]

def extract_values():
    for j in range(0, 5):
        for i in range(0, 6):
            print('waiting for 10 sec so that steam wont ban')
            time.sleep(10)
            link = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=' \
                   'tag_set_norse&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=' \
                   'tag_WearCategory' + str(wear_category[j]) + '&category_730_Quality%5B%5D=' \
                                                                'tag_normal&category_730_Rarity%5B%5D=' \
                                                                'tag_Rarity_' + rarity[i] + '_Weapon&appid=730'
            html_text = requests.get(link).text
            soup = BeautifulSoup(html_text, 'html.parser')
            items = soup.find_all('div',class_="market_listing_row market_recent_listing_row market_listing_searchresult")
            counter = -1
            for item in items:
                item_name = item.find('span', class_='market_listing_item_name').text.replace(" ", "_")
                item_price = item.find('span', class_='sale_price').text
                counter = counter + 1
                item_priceinfloat = item_price[1:5]
                print(item_name + ' = ' + item_price)
                if float(item_priceinfloat) < 10:
                    item_priceinfloat = item_price[1:5]
                elif float(item_priceinfloat) < 100:
                    item_priceinfloat = item_price[1:6]
                elif float(item_priceinfloat) < 1000:
                    item_priceinfloat = item_price[1:7]
                else:
                    item_priceinfloat = item_price[1:8]
                skins_price[i][counter][j] = float(item_priceinfloat)
                # skins_price[1][1] = 1.11
                print('counter=' + str(counter) + 'and i=' + str(i))
                print(skins_price)
                print(item_priceinfloat)


extract_values()
print("final value =")
print(skins_price)
file = open('files\skin_prices.txt', 'a+')
file.write(str(skins_price))