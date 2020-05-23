import random



#CREATE DECK
def create_deck(): # this function creates the deck from scratch and returns it as deck
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

  cards_comp = shuffled_deck[0:7]  
  cards_ply = shuffled_deck[7:14]  
  shuffled_deck = shuffled_deck[14:]   
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

def display_addit_cards_received(new_cards): # this function serves to print the cards, after they are taken from deck, in a nicer way
                                             # it is also used to display the first card that is laid (very first card to start the game)
  show = []
  
  for i in new_cards:
    card = '{} of {}'.format(i[1], i[0])
    show.append(card)
  return show


def card_from_deck(shuffled_deck, card_laid, num = 1):  # this function is used to take one or more cards from deck
                                    # default: it gives out one. If more are needed it has to be specified with the input (the num)
  
 
  #print('the length of shuffled deck now is: ', len(shuffled_deck)) 
                             
  if len(shuffled_deck) == 0 or len(shuffled_deck) < num: 
                                    # this second condition is for the case that there are less cards remaining than 
             # the ones that need to be given out. If so the remaining cards get overwritten
    #print('length:', len(cards_ply), 'cards of ply: ', cards_ply)  -> to be removed
    #print('length:', len(cards_comp),'cards of comp: ', cards_comp)  -> to be removed
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

    print('The deck was reshuffled. Its length is: ', len(shuffled_deck)) #maybe to be kept like this
      
  
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
  #print('card laid is: ', card_laid)   # the shuffled deck, the color (it is 'none' by default and specified if the person before laid                     
                                        # a +4 black or a color change black) and the action (it is also by default 'none' and specified
  card = []                             # with the numbers of cards to be taken from deck if the player(s) before laid one / multiple +2 / +4)
                           
  error = 'No card can be played'  # this is the error message in case no card can be laid 


### checking whether the card plaid before is special. That means whether action is not 'none'. If so the special characteristics get executed

  if color != 'none':          # in case the color is not 'none' as by default, that means a black card was laid before (+4 or color change),
    card_laid = [color, ' ']   # the last card laid (this is taken as a reference for the card that can be laid on it) gets overwritten 
    color = 'none'             # with the previously selected color. After having done that the color = 'none' -> the player after has no restriction

  if type(action) == int:                               # this checks whether action is not 'none'. This is the case when the player before 
    cards_to_answer = []                                # laid a +2 / +4 
    for i in cards_comp:                                # The computer checks whether it can answer by also playing a +2 of the same (or the 
                                                        # deisred) color or a +4. If that is the case computer plays it (or randomly one 
                                                        # of the possible ones, in case of multiple possibilities)
      if i[1] == '+4' or (i[0] == card_laid[0] and i[1] == '+2') or (card_laid[1] == '+2' and i[1] == '+2'):
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
      #print('additional cards received are: ', new_cards)  # to 'none' again

    #print('different cards to answer: ', cards_to_answer)
    #print('card to answer is: ', card)


  elif action == 'switch':
    print('the playing direction has been switched, therefore you play again') # in case the card played before is a 'switch' or
    action = 'none'                                                                # 'wait a round', the computer passes the turn to 
    return cards_comp, card_laid, shuffled_deck, color, action          # the player, without laying any card

  elif action == 'wait_a_round':
    print('computer has been skipped, therefore you play again')
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
    #print('successfully entered this scenario') 
    
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
      print('The played card by computer is "' + str(card[1]) + ' of ' + str(card[0]) +'"')  # the desired color afterwards needs to be specified)
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
          n_green = n_red = n_yellow = n_blue = 0 # computer chooses the most useful color after he laid a black card
          for i in cards_comp:
            if i[0] == 'green':
              n_green += 1
            elif i[0] == 'blue':
              n_blue += 1
            elif i[0] == 'red':
              n_red += 1
            elif i[0] == 'yellow':
              n_yellow += 1
            
          nmax = max(n_green, n_red, n_yellow, n_blue)
          if nmax == n_green:
            color = 'green'
          elif nmax == n_yellow:
            color = 'yellow'
          elif nmax == n_blue:
            color = 'blue'
          else:
            color = 'red'
          
          
          
          print('The played card by computer is "' + str(card[1]) + ' of ' + str(card[0]) + '" with desired color "' + color + '"')
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
    
    #print('The card taken from deck is: ', card)
    

    if card[0] == card_laid[0] or card[1] == card_laid[1]:
        print('The played card by computer is "' + str(card[1]) + ' of ' + str(card[0]) + '"')
        card_laid = card

        if card[1] == '+2':
          action = 2

        elif card[1] == 'switch':
          action = 'switch'
      
        elif card[1] == 'wait_a_round':
          action = 'wait_a_round'
        


    elif card[0] == 'black':

          n_green = n_red = n_yellow = n_blue = 0 # computer chooses the most useful color after he laid a black card
          for i in cards_comp:
            if i[0] == 'green':
              n_green += 1
            elif i[0] == 'blue':
              n_blue += 1
            elif i[0] == 'red':
              n_red += 1
            elif i[0] == 'yellow':
              n_yellow += 1
            
          nmax = max(n_green, n_red, n_yellow, n_blue)
          if nmax == n_green:
            color = 'green'
          elif nmax == n_yellow:
            color = 'yellow'
          elif nmax == n_blue:
            color = 'blue'
          else:
            color = 'red'
        
          
          print('The played card by computer is "' + str(card[1]) + ' of ' + str(card[0]) + '" with desired color "' + color + '"')
          card_laid = card

          if card[1] == '+4':
            action = 4

    else:
        cards_comp.append(card)
        print('computer can´t play. PASS')

    return cards_comp, card_laid, shuffled_deck, color, action
      


def ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action, last):  # this function represents how the player plays at every turn


  if len(cards_ply) == 1:     # this is used to punish the player with +2 cards, if he forgot to say 'UNO' (check also further parts in this function)
    if last != 'UNO':
      print('You did not say UNO! As punishement you receive two additional cards')
      new_cards, shuffled_deck = card_from_deck(shuffled_deck, card_laid, 2)
      for i in new_cards:
        cards_ply.append(i)
      new_cards_pr = display_addit_cards_received(new_cards)
      print('additional cards received are: ', new_cards_pr)

    
  
  if color != 'none':                # these following actions are all as described in comp_lays_card function
    card_laid = [color, ' '] 
    color = 'none'

 
  if action == 'switch':
    print('the playing direction has been switched, therefore computer plays again')
    action = 'none'
    return cards_ply, card_laid, shuffled_deck, color, action, last

  elif action == 'wait_a_round':
    print('you have been skipped, therefore computer plays again')
    action = 'none'
    return cards_ply, card_laid, shuffled_deck, color, action, last 

  

  card = []

  last_maybe = ''

  if type(action) == int:   # this big part is entered if in the turn before one/multiple +2/+4 was/were laid. With this player has the 
                                    # possibility to also answer with such a card
    cards_to_answer = []
    for i in cards_ply:
      if i[1] == '+4' or (i[0] == card_laid[0] and i[1] == '+2') or (card_laid[1] == '+2' and i[1] == '+2'):  # control this
        cards_to_answer.append(i)
    #print('Checking possible cards to answer:', cards_to_answer) ### just for debugging


    while True:   # the whole loop can be exited either when chooses to play a +2/+4 to answer (if he has one) or he writes 'take cards' and
                                                                  # collects the cards
      print(display_player_cards(cards_ply))
      print('The last laid card is: ', display_addit_cards_received([card_laid]) if card_laid[1].strip() else card_laid[0])
      x = input('\nInsert the number of the card you want to play, "take" if you can´t play and need a new card from deck,\n\
or "take cards" if you have to take multiple cards from the deck (in case one/multiple +2/+4 was/were laid before): ')
      
      if len(cards_ply) == 2 and not x in ['take cards', 'take']  and not x.isdigit():   # this is used to give player the possibility to say UNO
        y = x.split(' ')
        if len(y) == 2 and y[0].isdigit() and y[1] == 'UNO':
          last_maybe = 'UNO'
          x = y[0]
        else:
          print('This input is not valid. Try again.')
          continue


      if x.isdigit():                   # if he entered a correct number corresponding to a card of the dictionary displayed, this gets checked
        x = int(x)                      # if this card can be played, it gets assigned to card and removed
        if 0 <= x < len(cards_ply): 
          card = cards_ply[x]
          print('Your chosen card is "' + str(card[1]) + ' of ' + str(card[0]) + '"')
          if card[0] == card_laid[0] or card[1] == card_laid[1] or card[0] == 'black':

            if card in cards_to_answer:
              cards_ply.remove(card)   #  removes played card 
              break

            else:
              print('You first have to take the cards from deck!! Type "take cards".') 
              card = []
              continue
            
            
          else:
            print('This card can´t be played')
            continue

        else:
          print('This input is not valid. Try again.')
          continue
      else:
        
        if x == 'take':
          print('You can either play or still need to take cards from deck.')
          continue

        elif x == 'take cards':   # when take cards is typed the cards are taken from deck
          
          print('you receive +{} additional cards'.format(action))
          new_cards, shuffled_deck = card_from_deck(shuffled_deck, card_laid, action)
          for i in new_cards:
            cards_ply.append(i)
          action = 'none'
          new_cards_pr = display_addit_cards_received(new_cards)
          print('additional cards received are: ', new_cards_pr)
          break

        else:
          print('This input is not valid. Try again.')
          continue


  

  error = 'No card can be played'
  #print(display_player_cards(cards_ply))

  if card == []: # this part with its True loop gets entered if computer had no +2/+4 to answer or no such card was laid before

    while True:  # the loop ends after computer plaid a card successfully or had to pass
      
      print(display_player_cards(cards_ply))
      print('The last laid card is: ', display_addit_cards_received([card_laid]) if card_laid[1].strip() else card_laid[0])
      x = input('\nInsert the number of the card you want to play, "take" if you can´t play and need a new card from deck,\n\
or "take cards" if you have to take multiple cards from the deck (in case one/multiple +2/+4 was/were laid before): ')
      
      if len(cards_ply) == 2 and not x in ['take cards', 'take']  and not x.isdigit():
        y = x.split(' ')
        if len(y) == 2 and y[0].isdigit() and y[1] == 'UNO':
          last_maybe = 'UNO'
          x = y[0]
        else:
          print('This input is not valid. Try again.')
          continue
      if x.isdigit():

        x = int(x)
        if 0 <= x < len(cards_ply): 
          card = cards_ply[x]
          print('Your chosen card is "' + str(card[1]) + ' of ' + str(card[0]) + '"')
          if card[0] == card_laid[0] or card[1] == card_laid[1] or card[0] == 'black':
            
            cards_ply.remove(card)   #  removes played card 
            #print(cards_ply)
            break
          else:
            print('This card can´t be played')
            continue

        else:
          print('This input is not valid. Try again.')
          continue
      else:
        if x == 'take':
          card, shuffled_deck = card_from_deck(shuffled_deck, card_laid)
          card_pr = display_addit_cards_received([card])
          print('The card taken from deck is: ', card_pr)
          if card[0] == card_laid[0] or card[1] == card_laid[1] or card[0] == 'black':
            print('The taken card could be laid successfully.')
            if len(cards_ply) == 1:
              last_maybe = 'UNO'

          else:
            print('Also the new card could not be played, therefore you have to pass')
            cards_ply.append(card)
            card = error
          break

        elif x == 'take cards':
          print('This input does not make sense here, as no +2/+4 has/have been played before or the cards have already been collected!')
          continue

        else:
          print('This input is not valid. Try again.')
          continue
    
  if card == error:                                                      # for information about this part check the function comp_lays_card
    return cards_ply, card_laid, shuffled_deck, color, action, last

  if card[0] != 'black':

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

    while True:
      color = input(str('What color do you choose? [type: "green", "yellow", "blue" or "red"]\nYour choice: '))
                  
      if color == "green" or color == "yellow" or color == "blue" or color == "red":
        #print('color seems correct')   # color input check 
        break
      else:
        print("That's not a valid color!")
        continue
    
    if card[1] == '+4':
            if type(action) == int:
              action += 4
            else:  
              action = 4

  if len(cards_ply) == 0:

    if card[1] == 'wait_a_round' or card[1] == 'switch' or card[1] == '+2' or card[0] == 'black':
      print('You are not allowed to end the game with a special card! \nThis cards gets played as wanted, however \
as punishement you get two additional cards!')
      
      new_cards, shuffled_deck = card_from_deck(shuffled_deck, card_laid, 2)
      for i in new_cards:
        cards_ply.append(i)
      new_cards_pr = display_addit_cards_received(new_cards)
      print('additional cards received are: ', new_cards_pr)

    else: # just for debugging!!!!!!!
      print('Last card rule correctly respected')
      


  
  card_laid = card

  last = 'none'

  if last_maybe == 'UNO':
    if len(cards_ply) == 1:
      last = last_maybe
    else:
      print('You wrote UNO, however you have more than one card left!!')

  return cards_ply, card_laid, shuffled_deck, color, action, last
  



      
                                                                             
def play_game(starter, shuffled_deck, first_card, cards_ply, cards_comp):  
                                                # this function is responsible for the actual mechanisms of the game
                                                # depending on the starter chosen randomly in the beginning, there is one or the other sequence
                                                # this sequence remains the same troughout the game. The game continues, until somebody
  if starter == 'player':                       # (player or computer) causes the loop to be interrupted. That is the case when he remains 
                                                # with 0 cards -> he won
    #print('###################################################')
    print('\n')
    cards_ply, card_laid, shuffled_deck, color, action, last = ply_lays_card(cards_ply, first_card, shuffled_deck, color='none', action='none', last='none')
    print('\n')
    #print('--------------------------------------------------')
    #print('\n')
    cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
    mode = 1 #this says how the playing sequence is
    #print('###################################################')
    print('\n')
  else:
    #print('###################################################')
    print('\n')
    cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, first_card, shuffled_deck, color='none', action='none')
    print('\n')
    #print('--------------------------------------------------')
    #print('\n')
    cards_ply, card_laid, shuffled_deck, color, action, last = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action, last='none')
    mode = 2
    #print('###################################################')
    print('\n')

  while True: #len(cards_comp) > 0 and len(cards_ply) > 0: # or whatever i.e. while True

    if mode == 1:
      
      cards_ply, card_laid, shuffled_deck, color, action, last = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action, last)  
      if len(cards_ply) == 0:
        winner = 'ply'
        print('\nCongratulations ' + str(player_name) + '! You have won!')
        return winner  
       
      print('\n')
      #print('--------------------------------------------------')
      #print('\n')

      cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      if len(cards_comp) == 0:
        winner = 'comp'
        print('\ncomputer won!')
        return winner
      elif len(cards_comp) == 1:
        print('\nUNO, computer has just one card left!\n') # this automatically prints UNO when the computer has just one card left
      #print('###################################################')
      print('\n')
    
    else:
      cards_comp, card_laid, shuffled_deck, color, action = comp_lays_card(cards_comp, card_laid, shuffled_deck, color, action)
      if len(cards_comp) == 0:
        winner = 'comp'
        print('\ncomputer won!')
        return winner
      elif len(cards_comp) == 1:
        print('\nUNO, computer has just one card left!\n') # this automatically prints UNO when the computer has just one card left
      
      print('\n')
      #print('--------------------------------------------------')
      #print('\n')

      cards_ply, card_laid, shuffled_deck, color, action, last = ply_lays_card(cards_ply, card_laid, shuffled_deck, color, action, last)
      if len(cards_ply) == 0:
        winner = 'ply'
        print('\nCongratulations ' + str(player_name) + '! You have won!')
        return winner
        
      #print('###################################################')
      print('\n')






########################################

## The actual game    # this part is responsible for connecting all the functions and allows the UNO game to take place

deck = create_deck()


#WELCOME TO THE GAME
player_name = str(input("\nWelcome to this extremely fun UNO game! Please insert your name: "))
welcome_message = "Hello {}! Thank you for playing with me. I swear I won't cheat :)\n".format(player_name)
print(welcome_message)

print("""
You will play against me, the computer. Before starting to play, please make yourself familiar with the rules of this game.

THE RULES:

- Everyone starts with 7 cards
- You can lay down a card if it has the same sign or the same color as the card laid before.
- Black cards (‘+4’ and ‘choose color’) can be played after every card
- After playing a ‘wait a round’ and ‘switch’ card you can lay down another card.
- If you have two cards with the same number AND the same color, you can lay them down at the same time.
- If one player lays down a ‘draw’ card (e.g. ‘+2’), the other player can answer by also laying down a ‘draw’ card (e.g. ‘+4). In this case the first player has to take the sum of the ‘draw’ cards (e.g. ‘+6’).
- If you have one card left you have to say UNO. If you don’t say UNO you get 2 more cards.
- The last card played can NOT be a ‘switch’, ‘wait a round’, ‘+2’, ‘+4’, or ‘choose color’. If you try to play one of these cards at the end you get 2 more cards.

HOW TO PLAY:

- To play a card, enter the number of the card you want to play (e.g. if you want to play 1: ‘5 of yellow’ enter ‘1’)
- If you can’t play any of your cards, take a card from the deck by entering ‘take’
- If you have to take cards because of a +2 or a +4, enter ‘take cards’
- If you have two cards left and you want to put down one card you have to enter the number of the card and the word ‘UNO’ with a space in between (e.g. ‘1 UNO’)
""")

wins_ply = 0
wins_comp = 0


play = 'yes' 
while play == 'yes':

  shuffled_deck = shuffle(deck)


  first_card = lay_first_card(shuffled_deck)

  #print('The first card is: ', first_card)

  first_card_pr = display_addit_cards_received([first_card])
  print('\nThe first card is: ', first_card_pr)


  cards_comp, cards_ply, shuffled_deck = distribute_cards(shuffled_deck)
  display_cards = display_player_cards(cards_ply)
  print(display_cards)

  starter = choose_starter()
  print('\n{} starts'.format(starter))


  winner = play_game(starter, shuffled_deck, first_card, cards_ply, cards_comp)
  
  if winner == 'ply':
    wins_ply += 1
  else:
    wins_comp += 1
  

  play = input('\nGame has ended. Do you want to play again?\nIf so just type "yes".\nYour choice: ')
  

print('That does not seem to be the case')
print('\nThese are the results:\n-> {} won {} time(s)\n-> computer won {} time(s)'.format(player_name, wins_ply, wins_comp))
print('\nHave a nice day and see you soon!')