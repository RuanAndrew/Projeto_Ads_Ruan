from settings import *
from support import *
from random import shuffle
from time import sleep

class Deck:
    def __init__(self):
        self.all_cards = folder_importer('images', 'cards')
        self.draw_pile = []
        self.discard_pile = []
        self.hand_cards = []
        
    def shuffle(self):
        shuffle(self.draw_pile)

    def draw(self, amount = 5):
        c = 0
        while c < amount:
            self.hand_cards.append(self.draw_pile.pop(0))
            c += 1

    def add_cards(self, name, amount):
        cont = 0
        while cont < amount:
            for cards in self.all_cards:
                if name == str(cards):
                    cont += 1
                    self.draw_pile.append(cards)

    def start_deck(self):
        self.deck = Deck()
        self.deck.add_cards('Strike.webp', 5)
        self.deck.add_cards('Defend.webp', 4)
        self.deck.add_cards('Bash.webp', 1)
        self.deck.shuffle()
        self.deck.draw(5)

    def get_data_cards(self, name):
        self.name = name
        self.rarity = CARDS_DATA[name]['rarity']
        self.type = CARDS_DATA[name]['type']
        self.energy = CARDS_DATA[name]['energy']
        self.descripition = CARDS_DATA[name]['description']

    def shuffle_discard_pile(self):
        if len(self.draw_pile) == 0:
            self.draw_pile.copy(self.discard_pile)
            self.deck.shuffle()
            self.discard_pile.clear()

    # card powers

    def deal(self, damage, target, times = 0):
        self.damage = damage
        self.target = target