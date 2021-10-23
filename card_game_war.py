"""
Simple card game(war), typically played by two players using a standard playing card deck.
"""
# card,suit,rank,value
import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


player_one = Player('One')
player_two = Player('Two')

# new deck
new_deck = Deck()
new_deck.shuffle()

# split the deck between the players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# set a variable just to have the game continue
# check to see if anyone is losing
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards. Player Two Wins!')
        game_one = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards. Player One Wins!')
        game_one = False
        break

# new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        else:
            print('WAR ! ')

            if len(player_one.all_cards) <5:
                print('Player One unable to declare war.')
                print('PlAYER TWO WINS')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war.')
                print('PlAYER One WINS')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())







# two_hearts = Card(suits[0], ranks[0])
# mydeck = Deck()
# print(len(mydeck.all_cards))
# print(mydeck.all_cards[0])
# mydeck.shuffle()
# print(mydeck.all_cards[0])
# my_card = mydeck.deal_one()
#
# Karolina = Player('Karolina')
# print(Karolina)
# Karolina.add_cards([my_card])
# print(Karolina)
# Karolina.add_cards([my_card, my_card])
# print(Karolina)
# Karolina.remove_one()
# print(Karolina)
#


# for card_object in new_deck.all_cards:
#     print(card_object)
#
# bottom = new_deck.all_cards[-1]
# print(bottom)
# new_deck.shuffle()
# print(new_deck.all_cards[-1])
#
# two_hearts = Card('Hearts', 'Two')
# three_of_clubs = Card('Clubs', 'Three')
#
# print(values[two_hearts.rank])
# print(three_of_clubs.value)
#
# mycard = new_deck.all_cards
# new_player = Player('Karolina')
