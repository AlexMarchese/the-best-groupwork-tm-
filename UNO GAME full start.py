import random

#CRATE DECK
def create_deck():
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
  for i in colors:
    deck.remove([i, '0'])

    #now let's add the wild cards

  wild_cards=[['black','+4'],['black','choose_color']]

  x = 0
  while x < 4:
    for a in range (2):
        deck.append(wild_cards[a])
    x += 1    
  #the deck is ready. Format: [[color,symbol],[color,symbol],[],...] --> all strings
 
  return deck





#SHUFFLE THE DECK
def shuffle(deck):
    shuffled_deck = random.shuffle(deck)
    return shuffled_deck



def lay_first_card(shuffled_deck):
  x = shuffled_deck[0]
  shuffled_deck.remove(x)
  return x


def distribute_cards(shuffled_deck):
#DISTRIBUTE CARDS FROM SHUFFELED DECK
  cards_comp = shuffled_deck[0:7]
  cards_ply = shuffled_deck[7:14]

#REMOVE THOSE 14 CARDS FROM THE DECK -->Comment Nico: sollte es nicht ab 15 sein?
  shuffled_deck = shuffled_deck[14:]
  return cards_comp, cards_ply

def choose_starter():
  i = random.randrange(2)
  if i == 0:
    starter = 'player'
  else:
    starter = 'computer'

  return starter



def display_player_cards(cards_ply):

  print('Your cards are: ')
  name_cards_ply = []
  for i in cards_ply:
      new = (i[1]+' of '+ i[0])
      name_cards_ply.append(new)

  for (i, item) in enumerate(name_cards_ply, start=0):
      print(str(i) +': '+ str(item))
    
      #OUTPUT:
      #Your cards are: 
      # 0: 3 of green
      # 1: switch of blue
      # 2: 9 of green
      # 3: +4 of black
      # 4: +2 of green
      # 5: choose_color of black
      # 6: switch of yellow

def comp_lays_card():
  #COMPUTER LAYS FIRST CARD
  first_card = shuffled_deck.pop(0)
  #print(first_card)
  print('The played card is ' + str(first_card[1]) + ' of ' + str(first_card[0]))
      
#PLAYER PLAYS FIRST CARD

def ply_lays_card():

  card_played = int(input('Insert the number of the card you want to play: '))
  print("You played " + str(name_cards_ply[card_played]))

#CAN YOU PLAY THAT? WRITE CODE FOR ERROR MESSAGE

#REMOVE THAT CARD FROM YOUR CARDS

########################################

## The actual game

deck = create_deck()

#WELCOME TO THE GAME
name_ply = str(input("Welcome to this extremely fun UNO game! Please insert your name: "))
welcome_message = "Hello {}! Thank you for playing with me. I swear I won't cheat :)".format(name_ply)
print(welcome_message)

#THE RULES
rules = """You will play against me, the computer. I changed some rules to make it easier for the both of us.
- Everyone starts with 7 cards.
- You can start with every card you want.
- We can not play double cards.
- We can not turn two +2 into a +4.
- We can play every card at the end.
- Me, the computer, will say UNO for you, because I can't hear you."""
print(rules)

#READY MESSAGE
Ready_message = str(input("{}, are you ready? ".format(name_ply)))
print("Great, let's go.")

shuffled_deck = shuffle(deck)

first_card = lay_first_card(shuffled_deck)
print('The first card is: ', first_card)

cards_comp, cards_ply = distribute_cards()

starter = choose_starter()
print('{}'.format(starter))
