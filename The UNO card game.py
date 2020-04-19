import random


def create_deck(): # Julia  input: none
    color = ['green', 'blue', 'red', 'yellow', 'black']
    value = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, '+2', 'switch', 'skip', '+4', '', 'color_change']
   
    return deck # output: [['color','value/number'], [card]]   i.e. [['green', '7'], []]
    pass [color, value]

    

def shuffle_deck(deck): # Flurin 
    pass # output shuffled deck

""""

def distribute_cards(shuffled_deck):  # Nicola
    pass  # output: 2 list comp = [[],[]] and ply = [[],[]] !Warning please remove akso the 14 cards
            # shuffled_deck also to be returned 

# .pop formula removes and returns specified seven cards_ply and cards_comp from shuffled_deck
cards_ply = shuffled_deck.pop(0, 1, 2, 3, 4, 5, 6)
cards_comp = shuffled_deck.pop(7, 8, 9, 10, 11, 12, 13)
return shuffled_deck


def lay_first_card(): # Nicola
    pass # Rule: first card cannot be +2, +4 or color change
#.pop formula will remove and return a random first_card defined with random.choice from shuffled_deck
first_card = shuffled_deck.pop(random.choice(shuffled_deck))
#If first_card is +2, +4 or color_change, the function lay_first_card is to be repeated -->question: do I need to break the function when repeating?
if str(first_card == "+2" or "+4" or "color_change"):
    repeat(lay_first_card, 1)
print(first_card)
return shuffled_deck


"""
def sequence_of_players(): #this function serves to determine the beginner/starter of the game and the order
    pass    # output is: seq_of_ply (a list)
"""

def display_deck(ply): #this allows players to see what cards they have  # Julia
    pass #print() output: ['green of 2', 'black of +4']


def play_card():  # Alex
    pass # rule: +2, +4, color change cannot played as last
         # rule: if last card is played and before player did not say uno \
         # (typed uno before pass) player cannot lay and gets 2 extra cards

def take_card(): # Flurin
    pass 

def receive_card():
    pass  # either trough +2, +4 or punishement

def determine_punishement(): # this function is used to punish for making errors/cheating
    pass 

def pass_turn():
    pass

def input_error():
    pass    # this functions warns the user when he entered an unappropriate/wrong input

def play_the_game():
    pass    #this function serves to allow both types of players (normal user and computer) to play
"""
    seq_of_type_ply = [] # this list creates a sequence with all players per type (i.e. ['computer', 'ply'])
    for i in range(len(seq_of_ply)):
        if seq_of_ply[i] == 'computer':
            seq_of_type_ply.append('computer')
        else:
            seq_of_type_ply.append('ply')
"""
    

def display_the_winner():
    pass    # this function displays the winner once the game is over






def main():

    deck = create_deck()

    print('Welcome to the UNO card game. Select the players to play.\nJust put the names of the players.\
\nIn case you are playing alone you can choose "computer" as second player.\nSo you can play against\
 the machine.\nThis option is alo available if you are multiple players already and\
 you wish having the machine as an additional player.\nHAVE FUN!!!')
    
    ply = input('Write you name: ')
    """
    ply1 = input('player 1: ')
    ply2 = input('player 2: ')
    """
    """
    if ply1 or ply2 not type == str:
        raise input_error

    """

    ply1 = ply1.lower() # this serves to convert the name into lowercase latters (in case it was entered \
    ply2 = ply2.lower() # in a messy way)

    players = [ply1, ply2]

    one_more_game = 'yes'
    while one_more_game == 'yes':

        shuffled_deck = shuffle_deck()

        distribute_cards()

        lay_first_card()

        sequence_of_players()

        play_the_game()

        display_the_winner()

        one_more_game = input('This was the game. Do you want to play again? If so type "yes", otherwise \
press any other key to quit.\nYour answer: ')


if __name__ == "__main__": main()
 



