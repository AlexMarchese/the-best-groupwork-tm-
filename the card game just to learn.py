
import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# This method creates the initial card deck as a list with all possible combinations of suits and ranks.
# In contrast to the example on the lecture slides generating first all suits for a rank and continuing this for \
# the next rank,
# start with generating first all ranks for a suit and continue with the next suit. We will test this order.
# You can represent each card as a list with three elements (strings) in the form [rank of suit,suit,rank]
# e.g. ['2 of Clubs', 'Clubs', '2'] and ['Jack of Diamonds', 'Diamonds', 'Jack']. Add each card to the deck list,
# as a result the deck becomes a two-dimensional list with the cards being elements of the "outer" list and the
# attributes of an individual card being elements of the "inner" list.

def generate_deck(deck):
    # your code here
    
    for i in SUITS:
        for k in RANKS:
            card = ['{} of {}'.format(k,i), i, k]
            deck += [card]

    return deck 

# This method is used to calculate the score of a card. The score is calculated based on the card's suit (2nd element
# of the list) and it's rank (3rd element of the list). The score is the sum of the points for the suit and the rank.
# For the suits the following points should be assumed: Clubs = 1, Diamonds = 2, Hearts = 3, Spades = 4.
# For the ranks the following points should be assumed: 1 = 1, 2 = 2, ..., Jack = 11, Queen = 12, King = 13, Ace = 14.
# Hint: Use the int() method to convert the string representing a numerical rank of a card directly into an integer,
# e.g., int('2') = 2

def calculate_score(card):
    # your code here
    for i in range(len(card) - 1):
        i += 1
        if i == 1:
            if card[i] == 'Clubs':
                suit_score = 1
            elif card[i] == 'Diamonds':
                suit_score = 2
            elif card[i] == 'Hearts':
                suit_score = 3
            elif card[i] == 'Spades':
                suit_score = 4
            continue

        
        if card[i] == 'Jack':
            rank_score = 11
        elif card[i] == 'Queen':
            rank_score = 12
        elif card[i] == 'King':
            rank_score = 13
        elif card[i] == 'Ace':
            rank_score = 14
        else:
            rank_score = int(card[i])

    return rank_score + suit_score

# This method is used to store the score assigned with each card in a dictionary. We will call the \
# calculate_score(card)
# method from here for each card of the deck and store the card as key and its associated score as value\
#  in the dictionary.
# Use the first element of the "card" list as key for the dictionary. Dictionary entries will look \
# like this: '2 of Clubs': 3
# and 'Jack of Diamonds': 13.

def store_score(deck):
    # your code here
    score_dict = {}
    for i in deck:
        score_dict[i[0]] = calculate_score(i)

    return score_dict

# This method is used for shuffling a copy of the initial deck using the random.randrange() function (see lecture slides).

def shuffle(deck):
    # your code here
    n = len(deck)
    for i in range(n):
        r = random.randrange(i, n)
        temp = deck[r]
        deck[r] = deck[i]
        deck[i] = temp

    return deck

# This method is used for distributing the cards of the shuffled deck to player1 and player2. \
# Hand out the first ten cards
# in an alternating way to the decks of the players, i.e. player1 gets the cards with indices 0,2,4,6,8 and player2
# gets the cards with indices 1,3,5,7,9.
# Hint: use the modulus function '%' to determine whether the current list index is odd or even.

def distribute_cards(deck):

    deck_player1 = []
    deck_player2 = []

    for i in range(10):
        if i % 2 == 0:
            new_card = deck[i]
            deck_player1.append(new_card)
        else:
            new_card = deck[i]
            deck_player2.append(new_card)

    # your code here
    return deck_player1, deck_player2

# This method is used for playing one round comparing two cards with each other based on their calculated score.
# Use the dictionary to look up the score for each card. Compare scores, if player1's score is larger than player \
#  2's then
# he/she wins, analogous for player2, or there is a tie if both scores are equal. Return the result as an Integer with:
# 1 means player 1 won, 2 means player 2, 0 means tie. Also, print the result of a round on the console in the form:
# Player 1: 5 of Clubs, score=6
# Player 2: Jack of Hearts, score=14
# Hint: use the format() function for strings to create the output strings.

def play_round(card1,card2,score_dict):
    # your code here

    card1 = card1[0]
    card2 = card2[0]

    score_1 = score_dict[card1]
    score_2 = score_dict[card2]
    
    print('Player 1: {}, score={}'.format(card1,score_1))
    print('Player 2: {}, score={}'.format(card2,score_2))

    if score_1 == score_2:
        res = 0
    elif score_1 > score_2:
        res = 1
    else:
        res = 2

    return res

# This method is used for simulating a complete game consisting of playing all the cards on player1 and player2's decks,
# i.e. 1 card each in 5 rounds. Call the play_round() function for each round with card1, card2 and the score dictionary
# as input. Use the returned value of th play_round() function to evaluate the result of one round. Print if Player 1 \
# or Player 2
# won the round or there was a Tie on the console.
# Also, keep track of the number of of wins for player 1, player 2 and ties. Similarly to playing one round, return
# the total result of the game, with total=1 meaning that player 1 has won, total=2 meaning that player 2 has won,
# and total=0 meaning nobody has won.
# Print the result of a complete game on the console in the form:
# The total score is: Player 1: 2, Player 2: 3, Ties: 0
# Player 2 wins the game.
# Hint: use the format() function to create the output strings.te the output strings.

def play_game(deck1,deck2,score_dict):
    wins1=0 # the number of wins of player 1
    wins2=0 # the number of wins of player 2
    ties=0 # the number of ties
    
    # Implement the loop here to play all the cards from players 1 and 2's decks in individual rounds by calling the play_round() function. 
    # Count the number of wins or ties based on the return value of the play_round() function.
    
    # your code here

    for i, k in zip(deck1, deck2):
        res = play_round(i,k,score_dict)
        if res == 0:
            print('Tie')
            ties += 1

        elif res == 1:
            print('Player 1 wins')
            wins1 += 1

        else:
            print('Player 2 wins')
            wins2 += 1

    print('The total score is: Player 1: {}, Player 2: {}, Ties: {}'.format(wins1, wins2, ties))
    
    # Implement the functionality here to determine the winner of the game based on the total number of wins of the individual rounds.

    # your code here

    if wins1 > wins2:
        total = print('Player 1 wins the game')
    
    elif wins1 == wins2:
        total = print('Nobody wins')

    else:
        total = print('Player 2 wins the game')
      
    return total   

def main():
    #The main method to be executed.

    #1. We generate a new card deck with all cards.
    card_deck = generate_deck([])

    #2. We calculate the individual scores of each card and store them in a dictionary.
    score_dict = store_score(card_deck)

    cont='y'
    while(cont=='y'):

        #3. We create a copy of the original card deck.
        shuffle_deck = card_deck.copy()

        #4. We shuffle the copied deck.
        shuffled_deck = shuffle(shuffle_deck)

        #5. We distribute cards from the shuffled deck to player 1 and player 2.
        deck_player1,deck_player2 = distribute_cards(shuffled_deck)

        #6. We play a game of cards.
        play_game(deck_player1,deck_player2,score_dict)

        cont = input('Play again? Enter "y" to play another round. Press any other key to quit.')

if __name__ == '__main__': main()


# The complete output on the console for one exemplary game would look like this:
# Player 1: 10 of Diamonds, score=12
# Player 2: 8 of Diamonds, score=10
# Player 1 wins
# Player 1: 7 of Hearts, score=10
# Player 2: 3 of Diamonds, score=5
# Player 1 wins
# Player 1: 2 of Hearts, score=5
# Player 2: 8 of Spades, score=12
# Player 2 wins
# Player 1: King of Spades, score=17
# Player 2: Jack of Clubs, score=12
# Player 1 wins
# Player 1: 3 of Spades, score=7
# Player 2: Ace of Clubs, score=15
# Player 2 wins
# The total score is: Player 1: 3, Player 2: 2, Ties: 0
# Player 1 wins the game.



