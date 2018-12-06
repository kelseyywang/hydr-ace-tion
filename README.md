# Hydr-ace-tion

Hydr-ace-tion is a terminal-based card game that encourages you to drink more liquids. It’s a great addition to any party!

## Instructions for running code:
* Clone repo
* In the hydr-ace-tion directory, enter ```python run.py```
* To run tests, enter ```python test.py```
* If the block words are jumbled up, try making window bigger.


## Rules for game:
* This is a multiplayer game - you must have between 2-8 players but it’s probably most fun with 3-6 people.
* All players start with no cards. For every player’s turn, a random card will be drawn and added to their hand.
* The face card rule:
   * When a player gets a face card - J, Q, or K, the next player in line will get 2, 3, or 4 options respectively to choose from. That next player will enter a card from the options to take as their card.
* The drink rules:
   * When a player gets an Ace, they will be asked for who they want the drinker to be. The drinker will take 1 drink.
   * When a player gets a card that creates a rank pair (a.k.a a “pair” in poker), the next player in line will take a drink. When a player gets a card that creates a second rank pair (“4-of-a-kind” in poker), the next player in line will take 2 drinks
* How can I enter a card name?
   * When you’re given options by the face card rule, you must specify a card. Some examples of how to do this are:
      * Jack of hearts: “jack of hearts”, “J of H”, “J H”, “jh”
      * Two of diamonds: “two of diamonds”, “2 diamond”, “2 of d”, “2d”
