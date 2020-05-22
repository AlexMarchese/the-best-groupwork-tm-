import random

#CREATE DECK
def create_deck(): # this function creates the deck from scratch and returns itv as deck
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



def shuffle(deck):  # this function takes the deck created and shuffles it. Output: the shuffled deck   
    deck_to_sfuffle = deck.copy()  
    random.shuffle(deck_to_sfuffle)
    shuffled_deck = deck_to_sfuffle
    return shuffled_deck



def lay_first_card(shuffled_deck): # this function takes the first card from the shuffled deck and returns it. This is going to be
  x = shuffled_deck[0]             # the card on which the starter plays his first card
  y = 0
  while x[0] == 'black' or x[1] == '+2' or x[1] == 'switch' or x[1] == 'wait_a_round': # this part makes sure that the first card laid is not
    y += 1                               # a +4 black, a color change black or any +2 
    x = shuffled_deck[y]                 # -> we avoid it also when playing with physical cards

  shuffled_deck.remove(x) # this card 
  return x


def distribute_cards(shuffled_deck): # this function gives each player 7 cards from the shuffled deck

  cards_comp = shuffled_deck[0:7]   #change this -> use a for loop. The cards should be distributed as one each
  cards_ply = shuffled_deck[7:14]   # this makes the game more realistic
  shuffled_deck = shuffled_deck[14:]   # NB here optimize
  return cards_comp, cards_ply, shuffled_deck

def choose_starter(): # this function chooses the starter of the game and returns it: either player or computer
  i = random.randrange(2)
  if i == 0:
    starter = 'player' #instead of player personalize it with the name
  else:                # need to input the name in function
    starter = 'computer'

  return starter

##### Till here the functions were used for the preparation of the game -> each is used once EXCEPTION: shuffle is used
                                                      # for whenever cards of the shuffled deck are finished

 

def display_player_cards(cards_ply):  # this function serves to tell the player what card he has and displays a list of them

  print('Your cards are: ') #add also name as input, in order to personalize this
  name_cards_ply = []
  for i in cards_ply:
      new = (i[1]+' of '+ i[0])
      name_cards_ply.append(new)

  cards = {}
  
  for (i, item) in enumerate(name_cards_ply, start=0):
      cards[i] = item
  return cards


def card_from_deck(shuffled_deck, card_laid, num = 1):  # this function is used to take one or more cards from deck
                                    # default: it gives out one. If more are needed it has to be specified with the input (the num)
  
 
  print('the lenght of shuffled deck now is: ', len(shuffled_deck)) 
                             
  if len(shuffled_deck) == 0 or len(shuffled_deck) < num: 
                                    # this second condition is for the case that there are less cards remaining than 
             # the ones that need to be given out. If so the remaining cards get overwritten
    #print('lenght:', len(cards_ply), 'cards of ply: ', cards_ply)  -> to be removed
    #print('lenght:', len(cards_comp),'cards of comp: ', cards_comp)  -> to be removed
    shuffled_deck = shuffle(deck) 
    
    for i in cards_comp:             # this and the following serve to remove from the new shuffled deck 
      shuffled_deck.remove(i)        # the cards, which are already given out in the game (computer´s and player´s 
    for i in cards_ply:              # deck and the last card laid) 
      shuffled_deck.remove(i)        # otherwise there would be too many cards in the game 
    try:                             # --> more than their total 108
      shuffled_deck.remove(card_laid)
    except:                                 # this is to remove the laid card
      card_laid = ['black', '+4']         # n.b. in case the laid card was a +4 black, as card_laid was already overwritten
      shuffled_deck.remove(card_laid)     # by the desired color, it has to be rewritten as ['black', '+4']

    print('The deck was reshuffled. Its lenght is: ', len(shuffled_deck)) #maybe to be kept like this
      
  
  if num == 1: # this is the default input value (this means when num is not specified)
                            # in this case player / computer needs to take a new card from deck, because he is not able to play
    x = shuffled_deck[0]
    shuffled_deck.remove(x)
    
    return x, shuffled_deck

  else:       # this is the case when the player(s) before laid a / multiple +2 and / or +4 
    new_cards = []            # the cards that need to be taken from the deck are returned
    for i in range(num):
      x = shuffled_deck[0]
      new_cards.append(x)
      shuffled_deck.remove(x)
    return new_cards, shuffled_deck
   


def comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action):  # this function determines how the computer plays at every turn
                                        # input parameters are respectively: the cards of the computer, the last card laid,
  print('card laid is: ', card_laid)    # the shuffled deck, the color (it is 'none' by default and specified if the person before laid                     
                                        # a +4 black or a color change black) and the action (it is also by default 'none' and specified
  card = []                             # with the numbers of cards to be taken from deck if the player(s) before laid one / multiple +2 / +4)
                           # WRITE ADDITIONAL OUTPUT !!!!!!!!!
  error = 'No card can be played'  # this is the error message in case no card can be laid 


### checking whether the card plaid before is special. That means whether action is not 'none'. If so the special characteristics get executed

  if color != 'none':          # in case the color is not 'none' as by default, that means a black card was laid before (+4 or color change),
    card_laid = [color, ' ']   # the last card laid (this is taken as a reference for the card that can be laid on it) gets overwritten 
    color = 'none'             # with the previously selected color. After having done that the color = 'none' -> the player after has no restriction

  if type(action) == int:                               # this checks whether action is not 'none'. This is the case when the player before 
    print('The cards of the computer: ', cards_comp)    # laid a +2 / +4 
    cards_to_answer = []
    for i in cards_comp:                                # the computer checks whether it can answer by also playing a +2 of the same (or the 
                                                        # deisred) color or a +4. If that is the case computer plays it (or randomly one 
      if i[0] == card_laid[0] and i[1] == '+2' or i[1] == '+4':   # of the possible ones, in case of multiple possibilities)
        cards_to_answer.append(i)
    if len(cards_to_answer) != 0:
      x = random.randrange(len(cards_to_answer))
      card = cards_to_answer[x]
    

    else:  
      print('computer receives +{} additional cards'.format(action))            # if this is not the case the computer takes from deck the cards
      new_cards, shuffled_deck = card_from_deck(shuffled_deck, card_laid, action)   # he has to take
      for i in new_cards:
        cards_comp.append(i)
      action = 'none'                                      # also here, after the specified action parameter did his function, it gets changed
      print('additional cards received are: ', new_cards)  # to 'none' again

    #print('different cards to answer: ', cards_to_answer)
    #print('card to answer is: ', card)


  elif action == 'switch':
    print('the playing direction has been switched, therefore player plays again') # in case the card played before is a 'switch' or
    action = 'none'                                                                # 'wait a round', the computer passes the turn to 
    return cards_comp, card_laid, shuffled_deck, color, action          # the player, without laying any card

  elif action == 'wait_a_round':
    print('computer has been skipped, therefore player plays again')
    action = 'none'
    return cards_comp, card_laid, shuffled_deck, color, action

## Choosing a card to lay down (if not already chosen before, i.e. a +2 of same color or a +4)

                              # as in the real game, when we play for instance with our friends, we (our group) agree on the fact that
  special_cards = []          # it is not allowed to enter the game by a special card. That means the last card played cannot be
  for i in cards_comp:        # 'switch', 'wait_a_round', '+2' or a black card. Therefore, this part here serves to make sure computer 
    if i[1] == 'wait_a_round' or i[1] == 'switch' or i[1] == '+2' or i[0] == 'black':   # plays (in case he has one or more of them) the
      special_cards.append(i)                                         # last of his special cards at latest in the potential prelast round
  #print('checked how many special cards are left.') ##               # to make sure that, in case he gets to remain with just one card left,
  #print('number of sp cards: ', len(special_cards)) ##               # that card is not a special one
  #print('number of comp cards: ', len(cards_comp)) ##


  if len(special_cards) == len(cards_comp) - 1 and len(special_cards) != 0:  
    x = random.randrange(len(special_cards))
    card = special_cards[x]
    while card[0] != card_laid[0] and card[1] != card_laid[1] and card[0] != 'black':
      if len(special_cards) == 0:
        card = error
        break
      else:
        x = random.randrange(len(special_cards)) 
        card = special_cards[x]   
        special_cards.remove(card)
    print('successfully entered this scenario')
    
  elif len(special_cards) == len(cards_comp):
    card = error


  elif card == []:           # this serves to check, whether computer has already a card it can lay down (either a +2 or a +4 he lays
                                              # down in response to a previous +2 or +4 or he needs to get rid of a special card)
                                              # if this is not the case, computer randomly chooses a card of his and checks if this can be
                                              # played. If it this is not the case, it tries to pick another one
    cards_comp_temp = cards_comp.copy()
    x = random.randrange(len(cards_comp_temp))
    
    card = cards_comp_temp[x]
    while card[0] != card_laid[0] and card[1] != card_laid[1] and card[0] != 'black': # the process is looped until either computer finds 
                                                                              # a card to be laid or he tried out all of them
      if len(cards_comp_temp) == 0: # this breaks the loop, after having tried out all cards
        card = error
        break

      else:
        x = random.randrange(len(cards_comp_temp)) # this chooses randomly a card to check whether it can be played
        card = cards_comp_temp[x]   
        cards_comp_temp.remove(card)  # card gets removed from the list of cards computer can still try
 
  if card is not error:         # if a playable card was found, computer prints it, 
    cards_comp.remove(card)     # after having removed it from the cards of the computer

    if card[0] != 'black':    # it is important to distinguish between black cards and all other colors (as in case a black card is played
      print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]))  # the desired color afterwards needs to be specified)
      card_laid = card

      if card[1] == '+2':           # if card is a +2 the action (which is transmitted to the following player) becomes 2
        if type(action) == int:     # N.B. If player before laid a +4 / +2 this +2 gets added on to it
          action += 2
        else:  
          action = 2

      elif card[1] == 'switch':  # very similar case also for 'switch' and 'wait_a_round' cards: the action for the following player
        action = 'switch'        # gets sepcified with 'switch' or 'wait_a_round'
      
      elif card[1] == 'wait_a_round':   ### N.B. to better understand how the action gets played from one player to the other
        action = 'wait_a_round'         # (in this case from computer to player), have a look at the last function 'play_game'
      
    
    else:
          x = random.randrange(4)   # computer randomly chooses a color after he laid a black card
          if x == 0:
            color = 'green'
          elif x == 1:
            color = 'yellow'
          elif x == 2:
            color = 'blue'
          else:
            color = 'red'
          
          print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]) + ' with desired color ' + color)
          card_laid = card

          
          if card[1] == '+4':
            if type(action) == int:
              action += 4
            else:  
              action = 4
      
    return cards_comp, card_laid, shuffled_deck, color, action

## error handling -> when the computer has no card it can lay

  else:
    print(card)
    print('computer is taking a new card from deck')    # if computer has to card he can play he picks one from deck by using the function
      	                                                # 'card_from_deck'. If the taken card can be played (the testing process is done as 
                                                        # before), the computer lays it or declares 'PASS' and the turn gets passed over
    card, shuffled_deck = card_from_deck(shuffled_deck, card_laid)
    
    print('The card taken from deck is: ', card)
    

    if card[0] == card_laid[0] or card[1] == card_laid[1]:
        print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]))
        card_laid = card

        if card[1] == '+2':
          action = 2

        elif card[1] == 'switch':
          action = 'switch'
      
        elif card[1] == 'wait_a_round':
          action = 'wait_a_round'
        


    elif card[0] == 'black':

          x = random.randrange(4)
          if x == 0:
            color = 'green'
          elif x == 1:
            color = 'yellow'
          elif x == 2:
            color = 'blue'
          else:
            color = 'red'
        
          
          print('The played card by computer is ' + str(card[1]) + ' of ' + str(card[0]) + ' with desired color ' + color)
          card_laid = card

          if card[1] == '+4':
            action = 4

    else:
        cards_comp.append(card)
        print('computer can´t play. PASS')

    return cards_comp, card_laid, shuffled_deck, color, action
      


def ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action):  
  
 # card_played = int(input('Insert the number of the card you want to play: '))
# print("You played " + str(name_cards_ply[card_played]))
  # card_played = int(input('Insert the number of the card you want to play: '))
# print("You played " + str(name_cards_ply[card_played]))

  print('card laid is: ', card_laid)
  
  if color != 'none':
    card_laid = [color, ' '] # ' ' to be removed?
    color = 'none'

  if type(action) == int:
    print('player receives +{} additional cards'.format(action))
    new_cards, shuffled_deck = card_from_deck(shuffled_deck, card_laid, action)
    for i in new_cards:
      cards_ply.append(i)
    action = 'none'
    print('additional cards received are: ', new_cards)
 
  elif action == 'switch':
    print('the playing direction has been switched, therefore computer plays again')
    action = 'none'
    return cards_ply, card_laid, shuffled_deck, color, action 

  elif action == 'wait_a_round':
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
        if type(action) == int:
          action += 2
        else:  
          action = 2
      
      elif card[1] == 'switch':
          action = 'switch'
      
      elif card[1] == 'wait_a_round':
        action = 'wait_a_round'

    else:
        print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]))
        while True:
          
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          card_laid = card
          
          if color != "green" and color != "yellow" and color != "blue" and color != "red":
            print("That's not a valid color!")
            continue
          else:
            break

        if card[1] == '+4':
            if type(action) == int:
              action += 4
            else:  
              action = 4

    return cards_ply, card_laid, shuffled_deck, color, action 

  else:
    print(card)
    print('player is taking a new card from deck')
    
        
    card, shuffled_deck = card_from_deck(shuffled_deck, card_laid)
    
    print('The card taken from deck is: ', card)
    

    if card[0] == card_laid[0] or card[1] == card_laid[1]:
        print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]))
        card_laid = card

        if card[1] == '+2':
          action = 2

        elif card[1] == 'switch':
          action = 'switch'
      
        elif card[1] == 'wait_a_round':
          action = 'wait_a_round'

    elif card[0] == 'black':
        
        print('The played card by player is ' + str(card[1]) + ' of ' + str(card[0]))
        while True:
          
          color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
          card_laid = card
          
          if color != "green" and color != "yellow" and color != "blue" and color != "red":
            print("That's not a valid color!")
            continue
          else:
            break

        if card[1] == '+4':
            action = 4

    else:
        cards_ply.append(card)
        print('player can´t play. PASS')

    return cards_ply, card_laid, shuffled_deck, color, action
      
                                                                              #to personalize with player name
def play_game(starter, shuffled_deck, first_card, cards_ply, cards_comp):  # this function is responsible for the actual mechanisms of the game
                                                # depending on the starter chosen randomly in the beginning, there is one or the other sequence
                                                # this sequence remains the same troughout the game. The game continues, until somebody
  if starter == 'player':                       # (player or computer) causes the loop to be interrupted. That is the case when he remains 
                                                # with 0 cards -> he won
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
      
      cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action)  
      if len(cards_ply) == 0:
        return print('\nplayer won!')  
       
      print('--------------------------------------------------')

      cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      if len(cards_comp) == 0:
        return print('\ncomputer won!')
      elif len(cards_comp) == 1:
        print('\nUNO, computer has just one card left!\n') # this automatically prints UNO when the computer has just one card left
      print('###################################################')
    
    else:
      cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      if len(cards_comp) == 0:
        return print('\ncomputer won!')
      elif len(cards_comp) == 1:
        print('\nUNO, computer has just one card left!\n') # this automatically prints UNO when the computer has just one card left
      
      print('--------------------------------------------------')

      cards_ply, card_laid, shuffled_deck, color, action = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action)
      if len(cards_ply) == 0:
        return print('\nplayer won!')
        
      print('###################################################')







########################################

## The actual game    # this part is responsible for connecting all the functions and allows the UNO game to take place

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
