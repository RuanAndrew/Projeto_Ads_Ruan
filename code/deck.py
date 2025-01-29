from settings import *
from support import *
from random import shuffle

class Deck:
    def __init__(self):
        self.all_cards = folder_importer('images', 'cards')
        self.player_cards = []
        self.hand_cards = []

    def shuffle(self):
        shuffle(self.player_cards)

    def draw(self, amount):
        c = 0
        while c < amount:
            self.hand_cards.append(self.player_cards.pop(0))
            c += 1

    def add_cards(self, name, amount):
        cont = 0
        while cont < amount:
            for cards in self.all_cards:
                if name == str(cards):
                    cont += 1
                    self.player_cards.append(cards)

    def start_deck(self):
        self.deck = Deck()
        self.deck.add_cards('Strike.webp', 5)
        self.deck.add_cards('Defend.webp', 4)
        self.deck.add_cards('Bash.webp', 1)
        self.deck.shuffle()
        self.deck.draw(5)

    def get_data_cards(self, name):
        pass

class Hand_Cards(Deck):
    pass