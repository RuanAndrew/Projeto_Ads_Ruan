from settings import *
from powers import *

class UI:
    def __init__(self, hand_cards, all_cards, aplay_card_attack, player, enemies):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 250 
        self.top = WINDOW_HEIGHT / 2 + 100
        self.active_card = None

        # self.card_obj = card_obj
        self.hand_cards = hand_cards
        self.all_cards = all_cards
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
        # pygame.draw.rect(self.display_surface, COLORS['gray'],rect, 4, 4)

        # hand cards
        displayed_cards = 0
        for card in self.hand_cards:
            for cards in self.all_cards:
                if card == cards:
                    x = rect.left + displayed_cards * 100
                    y = rect.top + rect.height / 2

                    card_surf = self.all_cards[card]
                    card_surf = pygame.transform.scale_by(card_surf, 0.25)
                    card_rect = card_surf.get_frect(center = (x,y))
                    self.display_surface.blit(card_surf, card_rect)
                    displayed_cards += 1
    
    # health
        # health_rect = pygame.FRect(self.player.rect.y + 100, self.player.rect.y + 50, self.rect.width * 0.9, 20)
        # pygame.draw.rect(self.display_surface, COLORS['gray'], health_rect)
        # self.draw_bar(health_rect, self.hp, self.max_hp)

    def draw_bar(self, rect, value, max_value):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft, (value * ratio,rect.height))
        pygame.draw.rect(self.display_surface, COLORS['red'], progress_rect)

    def update(self):
        self.input()

    def draw(self):
        self.card_area()
