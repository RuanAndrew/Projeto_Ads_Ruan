from settings import *
from powers import *

class UI:
    def __init__(self, hand_cards, aplay_card_attack, player, enemies):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 250 
        self.top = WINDOW_HEIGHT / 2 + 100
        self.active_card = None

        # self.card_obj = card_obj
        self.hand_cards = hand_cards
        self.aplay_card_attack = aplay_card_attack
        self.player = player
        self.enemies = enemies

    def input(self):
        pass
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_just_pressed()


    def card_area(self):
        # rect
        rect = pygame.FRect(self.left, self.top + 60 ,550, 200)
        pygame.draw.rect(self.display_surface, COLORS['gray'],rect, 4, 4)

        # hand cards
        displayed_cards = 0
        for card in self.hand_cards:
            x = rect.left + displayed_cards * 100
            y = rect.top + rect.height / 2

            card.rect.center = (x,y)
            self.display_surface.blit(card.image, card.rect)
            displayed_cards += 1
    
    def health_bar(self, target):
        health_rect = pygame.FRect(target.rect.left, target.rect.bottom, target.rect.width * 0.9, 8)
        pygame.draw.rect(self.display_surface, COLORS['gray'], health_rect)
        self.draw_bar(health_rect, target.hp, target.max_hp)

    def draw_bar(self, rect, value, max_value):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft, (value * ratio,rect.height))
        pygame.draw.rect(self.display_surface, COLORS['red'], progress_rect)

    def update(self):
        self.input()

    def draw(self):
        self.card_area()
        self.health_bar(self.player)
        self.health_bar(self.enemies)
