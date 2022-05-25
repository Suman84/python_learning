skins=[[0]*5]*6
#for norse collection only



print(skins)
skins[2][2] = 0

choosen_skins_rarity = input('choose skins\nplease enter rarity(1-6) 1 being highest:')
choosen_skins_rank = input('please enter rank(1-3) 1 being highest:')
value1 = skins[int(choosen_skins_rarity)-1][int(choosen_skins_rank)-1]
value2 = skins[int(choosen_skins_rarity)-2][int(choosen_skins_rank)-1]
print('skins price is:' + str(value1))
print('output skin price:' + str(value2))
print(skins)