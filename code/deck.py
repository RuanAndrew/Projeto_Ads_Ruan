from settings import *
import pygame
from random import shuffle

class Deck:
    def __init__(self, all_cards, card_group):
        self.all_cards = all_cards
        self.draw_pile = []
        self.discard_pile = []
        self.hand_cards = []
        self.card_group = card_group

    def shuffle(self):
        shuffle(self.draw_pile)

    def draw(self, amount=5):
        for _ in range(amount):
            if not self.draw_pile:
                if self.discard_pile:
                    self.shuffle_discard_pile()
                else:
                    print("Não há cartas na pilha de descarte para reciclar!")
                    break
            if self.draw_pile:
                card = self.draw_pile.pop(0)
                card.reset_state()
                self.hand_cards.append(card)
                self.card_group.add(card)

    def add_cards(self, name, amount):
        for _ in range(amount):
            card = Card(name, self.all_cards[name], self.card_group)
            self.draw_pile.append(card)

    def start_deck(self):
        self.add_cards('Anger', 1)
        self.add_cards('Bash', 1)
        self.add_cards('BattleTrance', 1)
        self.add_cards('BodySlam', 3)
        # self.add_cards('Clothesline', 1)
        self.add_cards('Defend', 4)
        # self.add_cards('Entrench', 1)
        self.add_cards('Impervious', 1)
        self.add_cards('Inflame', 1)
        self.add_cards('IronWave', 2)
        self.add_cards('Juggernaut', 1)
        self.add_cards('Strike', 5)
        self.shuffle()
        self.draw(5)

    def shuffle_discard_pile(self):
        if self.discard_pile:
            self.draw_pile.extend(self.discard_pile)
            self.shuffle()
            self.discard_pile.clear()
            for card in self.draw_pile:
                card.reset_state()
                self.card_group.add(card)
        else:
            print("Pilha de descarte está vazia. Não é possível embaralhar.")

class Card(pygame.sprite.Sprite):
    def __init__(self, name, surf, card_group):
        super().__init__(card_group)
        self.name = name
        self.image = pygame.transform.scale_by(surf, 0.25)
        self.rect = self.image.get_rect()
        self.original_y = self.rect.y
        self.original_x = self.rect.x
        self.selected = False
        self.interactable = True

    def reset_state(self):
        self.selected = False
        self.interactable = True
