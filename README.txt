Group Project: UNO Card Game

For this group project we created a program that gives us the chance to play the famous card game UNO against the computer. The card game we programmed follows all the rules of a normal UNO card game. However, the number of players has been reduced to two: the computer and the person running the code.

Basics about UNO:

The UNO card deck consists of 108 cards: 76 number cards, 24 action cards and 8 wild cards. All cards and their meaning can be seen here: https://www.letsplayuno.com/news/guide/20181213/30092_732567.html

Rules:

Every player starts with seven cards from the card deck. The first card is taken from the deck. Based on randomness, the computer or the player can begins to lay down a card.

After a colored card (blue, yellow, red, or green) with a specific meaning or action (number, switch, wait_a_round or draw two) can be laid a card with the same color or the same meaning. For example, after a “7 of green” the player can lay down a “7 of red” or a “2 of green”.  

Wild cards (choose color and draw four) have the color black and can be laid after every card. The player who plays a wild card can choose a color. The other player has to lay down a card with that specific color.

When a player lays down a “switch” or a “wait_a_round” card, he can play another card.

When a player lays down a “draw” card, the other player has to draw the given amount (two or four). However, if he can put down another “draw” card, the first player has to draw the sum of the numbers given on of both cards.

If a player can´t lay down any card, he has to draw a new card from the remaining deck (in the game he needs to type “take” to do so). If the card can be played, he can lay it down. If not, he has to pass to the other person.

The player that remains with only one card left needs to say “UNO“. N.B. This has to be said whenever this conditions occurs, that means after he laid down the prelist card.

The winner is the player who finishes all his cards first.

Particularities:

Of course, the computer is not a person and can´t “think” for itself. However, we wrote a program that gives the computer the chance to play in a strategic way. This means that the cards played by the computer are not totally random. Firstly they follow certain strategic principles and after having considered them, randomness occurs. For example, when the human player lays down a “draw“ card the computer lays down a “draw“ card as well, if he has one.
When the computer chooses a color, he chooses the color that is most represented in his cards.

Functions:

This code is a sum of different functions. Some of them get called only once in the beginning (they have a game preparatory usage) and some of them are getting repeated until the game is finished. Because the code is quite long, we decided to give an overview and a quick explanation of the different functions used.

Singe-use functions:
- create_deck(): this function creates the 108 cards from scratch and returns them as deck
- shuffle(): this function takes the deck created, shuffles it and returns the shuffled deck (N.B. this functions is reused throughout the game when the deck gets reshuffled, once the remaining cards of the deck finish)
- lay_first_card(): this function takes the first card from the shuffled deck and returns it. This card is the starting card for the given game.
- distribute_cards(): this function gives each player 7 cards from the shuffled deck and removes them from the deck
- choose_starter(): this function chooses the starter of the game and returns it (player or computer)


Repeated-use functions:
- display_player_cards(): this function creates a dictionary and tells the player which cards he has
- display_addit_cards_received(): this function serves to print the cards, after they are taken from deck, in a nicer way (more user friendly). It is also used to display the first card that is laid (very first card to start the game)
- card_from_deck(): this function is used to take one or more cards from deck. Per default, only one card gets taken. If more cards are needed, it has to be specified when the function is called
- comp_lays_cards(): this function determines how the computer plays (what cards he lays down based on the previous card, when he has to draw a card, etc) 
- ply_lays_card(): this function gives the player the chance to decide which card to play by giving an input. This function also determines if that input it correct and if the card chosen can be played. It also determines whether or not the player can play and if he has to draw a new card from the remaining deck. The function also checks, whether the rules of the game are respected (the player says “UNO” once he remains with one card only and he doesn´t finish the game with a special card). If the rules are not respected, the player (as punishment) directly receives two more cards

Final game function:
- play_game(): this function is responsible for the actual mechanisms of the game. The game continues, until somebody (player or computer) remains with zero cards and therefore wins

All these functions are called from the final part of the code (more or less the last 100 lines of code). This part composes the actual game.
