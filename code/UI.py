from settings import *
from powers import *
from timers import Timer

class UI:
    def __init__(self, hand_cards, player, enemies, card_group, draw_pile, discard_pile, timers, apply_attack_card, apply_power_card, apply_skill_card):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 250 
        self.top = WINDOW_HEIGHT / 2 + 100
        self.active_card = None
        self.cards_group = card_group
        self.timers = timers

        self.hand_cards = hand_cards
        self.draw_pile = draw_pile
        self.discard_pile = discard_pile
        self.player = player
        self.enemies = enemies

        self.apply_attack_card = apply_attack_card
        self.apply_power_card = apply_power_card
        self.apply_skill_card = apply_skill_card

        self.card_cooldown = Timer(500)

    def input(self):
        self.card_cooldown.update()
        if self.card_cooldown.active:
            return

        mouse_pos = pygame.mouse.get_pos()
        mouse_collide = [card for card in self.cards_group if card.rect.collidepoint(mouse_pos)]

        for card in self.cards_group:
            card.rect.y = card.original_y

        for card in mouse_collide:
            card.rect.y -= 20

            if pygame.mouse.get_pressed()[0] and mouse_collide:
                self.active_card = card
                card_type = CARDS_DATA[self.active_card.name]['type']

                if card_type == 'attack':
                    self.apply_attack_card(self.player, self.enemies, card.name)
                elif card_type == 'skill':
                    self.apply_skill_card(self.player, self.enemies, card.name)
                elif card_type == 'power':
                    self.apply_power_card(self.player, self.enemies, card.name)
                
                if card in self.hand_cards:
                    self.hand_cards.remove(card)
                card.kill()

                self.card_cooldown.activate()

    def card_area(self):
        # rect
        rect = pygame.FRect(self.left, self.top + 60 ,550, 250)

        # hand cards
        displayed_cards = 0
        for card in self.hand_cards:
            x = rect.left + displayed_cards * 130
            y = rect.top + rect.height / 2

            card.rect.center = (x,y)
            self.display_surface.blit(card.image, card.rect)
            displayed_cards += 1

    def piles(self):
        self.base = pygame.image.load(join('images/other/Base.webp')).convert_alpha()
        self.base = pygame.transform.scale_by(self.base, 0.8)
        self.base_discard = pygame.image.load(join('images/other/BaseDiscard.webp')).convert_alpha()
        self.base_discard = pygame.transform.scale_by(self.base_discard, 0.8)

        self.base_rect = self.base.get_frect(center = (50, WINDOW_HEIGHT- 50))
        self.base_discard_rect = self.base_discard.get_frect(center = (WINDOW_WIDTH-50, WINDOW_HEIGHT- 50))

        self.display_surface.blit(self.base, self.base_rect)
        self.display_surface.blit(self.base_discard, self.base_discard_rect)

        base_text = self.font.render(f"{len(self.draw_pile)}", True, COLORS['black'])
        text_rect = base_text.get_rect(center=self.base_rect.center)
        self.display_surface.blit(base_text, text_rect)

        base_discrd_text = self.font.render(f"{len(self.discard_pile)}", True, COLORS['black'])
        text_rect = base_text.get_rect(center=self.base_discard_rect.center)
        self.display_surface.blit(base_discrd_text, text_rect)

    def health_bar(self, target):
        # HP
        health_rect = pygame.FRect(target.rect.left, target.rect.bottom + 10, target.rect.width * 0.9, 8)
        pygame.draw.rect(self.display_surface, COLORS['gray'], health_rect)
        self.draw_bar(health_rect, target.hp, target.max_hp, COLORS['red'])
        # Block
        if target.block > 0:
            block_rect = pygame.FRect(health_rect.left, health_rect.top - 10, health_rect.width, 5)
            self.draw_bar(block_rect, target.block, target.max_hp, COLORS['blue'])

        health_text = self.font.render(f"{target.hp}/{target.max_hp} (Block: {target.block})", True, COLORS['white'])
        text_rect = health_text.get_rect(center=health_rect.center)
        self.display_surface.blit(health_text, text_rect)

    def draw_bar(self, rect, value, max_value, color):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft, (value * ratio, rect.height))
        pygame.draw.rect(self.display_surface, color, progress_rect)

    def update(self):
        self.input()

    def draw(self):
        self.card_area()
        self.health_bar(self.player)
        self.health_bar(self.enemies)
        self.piles()
