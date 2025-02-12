from settings import *

class Deck():
    def __init__(self, all_cards, card_group):
        super().__init__()
        self.all_cards = all_cards
        self.draw_pile = []
        self.discard_pile = []
        self.hand_cards = []
        self.card_group = card_group
        
    def shuffle(self):
        shuffle(self.draw_pile)

    def draw(self, amount = 1):
        for _ in range(amount):
            if not self.draw_pile:
                self.shuffle_discard_pile()
                if not self.draw_pile:
                    break
            self.hand_cards.append(self.draw_pile.pop(0))

    def add_cards(self, name, amount):
        for _ in range(amount):
            self.draw_pile.append(Card(name, self.all_cards[name], self.card_group))

    def start_deck(self):
        self.add_cards('Strike', 5)
        self.add_cards('Defend', 4)
        self.add_cards('Bash', 1)
        self.shuffle()
        self.draw(5)

    def shuffle_discard_pile(self):
        if self.discard_pile:
            self.draw_pile = self.discard_pile[:]
            self.shuffle()
            self.discard_pile = []

class Card(pygame.sprite.Sprite):
    def __init__(self, name, surf, card_group):
        super().__init__(card_group)
        self.name = name
        self.surf = surf
        self.data = CARDS_DATA[name]
        self.image = pygame.transform.scale_by(surf, 0.25)
        self.rect = self.image.get_frect()