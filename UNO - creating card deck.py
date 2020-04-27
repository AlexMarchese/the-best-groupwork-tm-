deck=[]

cardfaces = []
for i in range (0,10):
  cardfaces.append(str(i))

special_symbols=["wait_a_round","switch","+2"]

for j in range (3):
  cardfaces.append(special_symbols[j])

#now we have all the symbols together. let's pair them with the colors

colors=["red","blue","yellow","green"]

for k in range (4):
    for l in range (13):
        card=[colors[k],cardfaces[l]]
        deck.append(card)

deck=deck*2

#now let's add the wild cards

wild_cards=[['black','+4'],['black','choose_color']]*2

#print(wild_cards)

for a in range (4):
    deck.append(wild_cards[a])

print("Final Card Deck:")
print(deck)

#for visualizing all cards in one row:
#for c in range(108):
#    print(deck[c])
