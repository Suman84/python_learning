#skins=[[0]*3]*6
#for norse collection only
skins = [[10000, 10000, 10000],[2000, 2000, 2000], [600, 500, 300], [250, 100, 100], [30, 20, 15],  [4, 4, 4]]
print(skins)
choosen_skins_rarity = input('choose skins\nplease enter rarity(1-6) 1 being highest:')
choosen_skins_rank = input('please enter rank(1-3) 1 being highest:')
value1 = skins[int(choosen_skins_rarity)-1][int(choosen_skins_rank)-1]
value2 = skins[int(choosen_skins_rarity)-2][int(choosen_skins_rank)-1]
print('skins price is:' + str(value1))
print('output skin price:' + str(value2))