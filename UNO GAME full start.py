import random

#CREATE DECK
def create_deck():
  deck = []

  colors = ['red', 'green', 'yellow', 'blue', 'black']
  symbols = ['wait_a_round', 'switch', '+2', '+4', 'choose_color']

  for i in colors:
    if i != 'black':
      
      card = [i, str(0)]
      deck.append(card)
      y = 0
      while y < 2:
        for k in range(1, 10):
          card = [i, str(k)]
          deck.append(card)
        for k in range(3):
          card = [i, symbols[k]]
          deck.append(card)
        y += 1
    
    else:
      y = 0
      while y < 4:
        card = [i, symbols[3]]
        deck.append(card)
        card = [i, symbols[4]]
        deck.append(card)
        y += 1

  return deck



def shuffle(deck):          
    deck_to_sfuffle = deck.copy()  ### VERY IMPORTANT TO EXPLAIN THIS A MISTAKE HERE COSTED ME 6h OF WORK HAHAHA
    random.shuffle(deck_to_sfuffle)
    shuffled_deck = deck_to_sfuffle
    return shuffled_deck



def lay_first_card(shuffled_deck): #check if card is effetively removed from deck
  x = shuffled_deck[0]
  y = 0
  while x[0] == 'black' or x[1] == '+2': # this part makes sure that the first card laid is not
    y += 1                               # a +4 black, a color change black or any +2 
    x = shuffled_deck[y]                 # -> we avoid it also when playing with physical cards

  shuffled_deck.remove(x)
  return x

'''
def card_laid(card_laid = first_card, first_card): #this serves to retreive the card which is currently laid down
  if card_laid == first_card:
    return first_card
  else:                                       #Maybe not needed
    return card_laid
'''

def distribute_cards(shuffled_deck):
#DISTRIBUTE CARDS FROM SHUFFELED DECK
  cards_comp = shuffled_deck[0:7]   #change this -> use a for loop. The cards should be distributed as one each
  cards_ply = shuffled_deck[7:14]   # this makes the game more realistic
  shuffled_deck = shuffled_deck[14:]
  return cards_comp, cards_ply, shuffled_deck

def choose_starter():
  i = random.randrange(2)
  if i == 0:
    starter = 'player' #instead of player personalize it with the name
  else:                # need to input the name in function
    starter = 'computer'

  return starter

##### Till here the functions were used for the preparation of the game -> each is used once EXCEPTION: shuffle is used
                                                      # for whenever cards of the shuffled deck are finished

 

def display_player_cards(cards_ply):  #for now it is fine, let us improve it later

  print('Your cards are: ') #add also name as input, in order to personalize this
  name_cards_ply = []
  for i in cards_ply:
      new = (i[1]+' of '+ i[0])
      name_cards_ply.append(new)

  cards = {}
  
  for (i, item) in enumerate(name_cards_ply, start=0):
      cards[i] = item
  return cards

def card_from_deck(shuffled_deck, num = 1):  #this function is used to take one or more cards from deck
  
  print('connection to function successful')
  print('the lenght of shuffled deck now is: ', len(shuffled_deck))
                             # default: it gives out one. If more are needed it has to be specified with the input
  if len(shuffled_deck) == 0: # to check whether cards are effectively removed from shuffled deck
      
    shuffled_deck = shuffle(deck) 
    print('The deck was reshuffled. Its lenght is: ', len(shuffled_deck)) #maybe to be kept like this
    #print(shuffled_deck)  
  
  if num == 1:
    
    x = shuffled_deck[0]
    shuffled_deck.remove(x)
    
    return x, shuffled_deck

  elif num == '+2':

    x = shuffled_deck[0]
    shuffled_deck.remove(x)
    y = shuffled_deck[0]
    shuffled_deck.remove(y)

    return x, y, shuffled_deck

  elif num == '+4':

    x = shuffled_deck[0]
    shuffled_deck.remove(x)
    y = shuffled_deck[0]
    shuffled_deck.remove(y)
    a = shuffled_deck[0]
    shuffled_deck.remove(a)
    b = shuffled_deck[0]
    shuffled_deck.remove(b)
  
    return x, y, a, b, shuffled_deck 


  else: #here actions for +2/+4 follow
    pass #remember to put break / y += 1 also after this
    
  



def comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action):  

  print('card laid is: ', card_laid)
  
  if color != 'none':
    card_laid = [color, ' ']
    color = 'none'

  if action == '+2':
    print('computer receives +2 additional cards')
    card1, card2, shuffled_deck = card_from_deck(shuffled_deck, action)
    cards_ply.append(card1) #check if possible to make append card1,card2 in the same 
    cards_ply.append(card2)
    action = 'none'
    print('additional cards received are: ', card1, card2)

  if action == '+4':
    print('computer receives +4 additional cards')
    card1, card2, card3, card4, shuffled_deck = card_from_deck(shuffled_deck, action)
    cards_ply.append(card1) #check if possible to make append card1,card2 in the same 
    cards_ply.append(card2)
    cards_ply.append(card3) 
    cards_ply.append(card4)      
    
    action = 'none'
    print('additional cards received are: ', card1, card2, card3, card4)

  if action == 'switch':
    print('the playing direction has been switched, therefore player plays again')
    action = 'none'
    return cards_comp, card_laid, shuffled_deck, color, action 

  if action == 'wait_a_round':
    print('computer has been skipped, therefore player plays again')
    action = 'none'
    return cards_comp, card_laid, shuffled_deck, color, action 



    #print('color gets considered')
  #print('card laid is: ', card_laid)
  cards_comp_temp = cards_comp.copy()
  #print(len(cards_comp_temp))  # has to be removed after!!
  error = 'No card can be played'
  x = random.randrange(len(cards_comp_temp))
  
  card = cards_comp_temp[x]
  while card[0] != card_laid[0] and card[1] != card_laid[1] and card[0] != 'black': 

    if len(cards_comp_temp) == 0:
      card = error
      break

    #elif card[0] == 'black':
     # break

    else:
      x = random.randrange(len(cards_comp_temp))
      card = cards_comp_temp[x]   
      cards_comp_temp.remove(card)
      #print('to check 1: ', card)
      #print('to check remaining cards: ', cards_comp_temp)

  #print('to check 2: ', card)

  if card is not error:
    cards_comp.remove(card)
    
    if card[0] != 'black':
      print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]))
      card_laid = card

      if card[1] == '+2':
        action = '+2'

      if card[1] == 'switch':
        action = 'switch'
      
      if card[1] == 'wait_a_round':
        action = 'wait_a_round'
      
    
    else:
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]) + ' with color ' + color)
          card_laid = card

          if card[1] == '+4':
            action = '+4'
      
    return cards_comp, card_laid, shuffled_deck, color, action

  else:
    print(card)
    print('computer is taking a new card from deck')
    
        
    card, shuffled_deck = card_from_deck(shuffled_deck)
    
    print('The card taken from deck is: ', card)
    #print(card[0])
    #print(card_laid[0])
    #print(card_laid[1])

    if card[0] == card_laid[0] or card[1] == card_laid[1]:
        print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]))
        card_laid = card

        if card[1] == '+2':
          action = '+2'

        if card[1] == 'switch':
          action = 'switch'
      
        if card[1] == 'wait_a_round':
          action = 'wait_a_round'
        


    elif card[0] == 'black':
        
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]) + ' with color ' + color)
          card_laid = card

          if card[1] == '+4':
            action = '+4'

    else:
        cards_comp.append(card)
        print('computer can´t play. PASS')

    return cards_comp, card_laid, shuffled_deck, color, action
      


def ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action):  ### method is good, however it should do smth if it is not possible to lay down anything!!
  
 # card_played = int(input('Insert the number of the card you want to play: '))
# print("You played " + str(name_cards_ply[card_played]))
  # card_played = int(input('Insert the number of the card you want to play: '))
# print("You played " + str(name_cards_ply[card_played]))

  print('card laid is: ', card_laid)
  
  if color != 'none':
    card_laid = [color, ' ']
    color = 'none'

  if action == '+2':
    print('player receives +2 additional cards')
    card1, card2, shuffled_deck = card_from_deck(shuffled_deck, action)
    cards_ply.append(card1) #check if possible to make append card1,card2 in the same 
    cards_ply.append(card2)
    action = 'none'
    print('additional cards received are: ', card1, card2)

  if action == '+4':
    print('player receives +4 additional cards')
    card1, card2, card3, card4, shuffled_deck = card_from_deck(shuffled_deck, action)
    cards_ply.append(card1) #check if possible to make append card1,card2 in the same 
    cards_ply.append(card2)
    cards_ply.append(card3) 
    cards_ply.append(card4)      

    action = 'none'
    print('additional cards received are: ', card1, card2, card3, card4)

  if action == 'switch':
    print('the playing direction has been switched, therefore computer plays again')
    action = 'none'
    return cards_ply, card_laid, shuffled_deck, color, action 

  if action == 'wait_a_round':
    print('player has been skipped, therefore computer plays again')
    action = 'none'
    return cards_ply, card_laid, shuffled_deck, color, action 



  cards_ply_temp = cards_ply.copy()
  
  error = 'No card can be played'
  x = random.randrange(len(cards_ply_temp))
  
  card = cards_ply_temp[x]
  while card[0] != card_laid[0] and card[1] != card_laid[1] and card[0] != 'black': 

    if len(cards_ply_temp) == 0:
      card = error
      break

    #elif card[0] == 'black':
     # break

    else:
      x = random.randrange(len(cards_ply_temp))
      card = cards_ply_temp[x]   
      cards_ply_temp.remove(card)
      #print('to check 1: ', card)
      #print('to check remaining cards: ', cards_ply_temp)

  #print('to check 2: ', card)

  if card is not error:
    cards_ply.remove(card)
    
    if card[0] != 'black':
      print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]))
      card_laid = card
      if card[1] == '+2':
        action = '+2'
      
      if card[1] == 'switch':
          action = 'switch'
      
      if card[1] == 'wait_a_round':
        action = 'wait_a_round'

    else:
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]) + ' with color ' + color)
          card_laid = card

          if card[1] == '+4':
            action = '+4'

    return cards_ply, card_laid, shuffled_deck, color, action

  else:
    print(card)
    print('player is taking a new card from deck')
    
        
    card, shuffled_deck = card_from_deck(shuffled_deck)
    
    print('The card taken from deck is: ', card)
    

    if card[0] == card_laid[0] or card[1] == card_laid[1]:
        print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]))
        card_laid = card

        if card[1] == '+2':
          action = '+2'

        if card[1] == 'switch':
          action = 'switch'
      
        if card[1] == 'wait_a_round':
          action = 'wait_a_round'

    elif card[0] == 'black':
        
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]) + ' with color ' + color)
          card_laid = card

          if card[1] == '+4':
            action = '+4'

    else:
        cards_ply.append(card)
        print('player can´t play. PASS')

    return cards_ply, card_laid, shuffled_deck, color, action
      

def play_game(starter, shuffled_deck, first_card, cards_ply, cards_comp): #to personalize with player name 

  
  if starter == 'player': 
    print('###################################################')
    cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, first_card, shuffled_deck, color='none', action='none')
    print('--------------------------------------------------')
    cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
    mode = 1 #this says how the playing sequence is
    print('###################################################')
  else:
    print('###################################################')
    cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, first_card, shuffled_deck, color='none', action='none')
    print('--------------------------------------------------')
    cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action)
    mode = 2
    print('###################################################')

  while True: #len(cards_comp) > 0 and len(cards_ply) > 0: # or whatever i.e. while True

    if mode == 1:
      if len(cards_ply) != 0:
        cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action)
      else:
        print('player won!')
        break

      print('--------------------------------------------------')

      if len(cards_comp) != 0:
        cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      else:
        print('computer won!') ##to add name -> personalize it
        break
      print('###################################################')
    
    else:
      if len(cards_comp) != 0:
        cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      else:
        print('computer won!')
        break
      
      print('--------------------------------------------------')

      if len(cards_ply) != 0:
        cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action)
      else:
        print('player won!')
        break
      print('###################################################')







########################################

## The actual game

deck = create_deck()

'''
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
print("Great, let's go.")   ### GAME HAS TO START JUST IF PLAYER TYPES YES !!!
'''

shuffled_deck = shuffle(deck)


first_card = lay_first_card(shuffled_deck)
print('The first card is: ', first_card)


cards_comp, cards_ply, shuffled_deck = distribute_cards(shuffled_deck)
display_cards = display_player_cards(cards_ply)
print(display_cards)

starter = choose_starter()
print('{} starts'.format(starter))


play_game(starter, shuffled_deck, first_card, cards_ply, cards_comp)