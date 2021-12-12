import pydealer
import os

def initialize(deal_deck, player_pile):
    for pile in player_pile:
        pile.add(deal_deck.deal(4))

def see2cards(player):
    print("Pick 2: \n 1 2 3 4")
    for i in range(2):
        n= input()
        n1=int(n)
        print(player[n1-1])

    print("Remember these 2 cards and their positions. Press any key to continue")
    n = input()

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

def main():
    # Deal deck. Main deck to draw cards from
    deal_deck = pydealer.Deck()
    deal_deck.shuffle()

    # Discard deck
    discard_deck = pydealer.Deck()
    discard_deck.empty()

    player_pile = []
    # 4 player piles. TODO: Change this to n
    for i in range(4):
        deck = pydealer.Deck()
        deck.empty()
        player_pile.append(deck)

    initialize(deal_deck, player_pile)
    
    # Now each player can see 2 of their cards
    for player in player_pile:    
        see2cards(player)
        clear()

if __name__ == "__main__":
    main()


