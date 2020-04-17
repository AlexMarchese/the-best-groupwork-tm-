#UNO card game

deck=[]

cardfaces = []
for i in range (0,10):
  cardfaces.append(str(i))

special_symbols=["wait_a_round","switch","+2"]

for j in range (3):
  cardfaces.append(special_symbols[j])

#print(cardfaces)

#now we have all the symbols together. let's pair them with the colors

colors=["red","blue","yellow","green"]

for k in range (4):
    for l in range (13):
        card = (cardfaces[l]+" of "+ colors[k])
        deck.append(card)

#print(deck)

#if you want to have all these cards double you just need to
#multiply the deck like this:

#deck=deck*2
#print(deck)

#so far so good, now I'm gonna add the black cards.
wild_cards = ["+4 of black","choose a color"]*2
#print(wild_cards)

#adding the wild_cards to the deck:

for a in range (4):
    deck.append(wild_cards[a])

print("Final Card Deck:")

for c in range(56):
    print(deck[c])


#import random
#random.shuffle(deck)
