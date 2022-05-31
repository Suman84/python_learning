from bs4 import BeautifulSoup
import requests
import time     #5-number of skins, 6-rarity, 5-wear
skins_price = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
set_name = ['inferno','inferno_2']
wear_category = [0,1,2,3,4]
exterior = 'normal'
rarity = ['Common','Uncommon', 'Rare', 'Mythical', 'Legendary', 'Ancient' ]
for j in range (0,5):
    for i in range(0,6):
        print('waiting for 1 sec')
        time.sleep(2)
        link = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=' \
               'tag_set_inferno_2&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=' \
               'tag_WearCategory' + str(wear_category[j]) + '&category_730_Quality%5B%5D=' \
                'tag_normal&category_730_Rarity%5B%5D=' \
                'tag_Rarity_' + rarity[i] + '_Weapon&appid=730'
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'html.parser')
        items = soup.find_all('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult")
        counter = -1
        for item in items:
            item_name = item.find('span', class_='market_listing_item_name').text.replace(" ", "_")
            item_price = item.find('span', class_='sale_price').text
            item_priceinfloat = item_price[1:5]
            counter = counter + 1

            print(item_name + ' = ' + item_price)
            if (float(item_priceinfloat) < 100):
                skins_price[i][counter][j] = float(item_priceinfloat)
                # skins_price[1][1] = 1.11
                print('counter=' + str(counter) + 'and i=' + str(i))
                print(skins_price)

            print(item_priceinfloat)

print("final value =")
print(skins_price)
file = open('skin_prices.txt', 'a+')
file.write(skins_price)