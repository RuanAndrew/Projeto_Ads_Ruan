from settings import *
from entities import *
# from main import function

# ui temporaria copiada da internet para testar os efeitos das cartas e ataques

class UI:
    def __init__(self, hand_cards, aplay_card_attack):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 250 
        self.top = WINDOW_HEIGHT / 2 + 100
        self.hand_cards = hand_cards
        self.aplay_card_attack = aplay_card_attack
        # self.player = Player()

        # control 
        self.general_options = ['Bash', 'Defend', 'Strike', 'None']
        self.general_index = {'col': 0, 'row': 0}
        self.state = 'general'
        self.rows, self.cols = 2,2

    def input(self):
        keys = pygame.key.get_just_pressed()
        if self.state == 'general':
            self.general_index['row'] = (self.general_index['row'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.rows
            self.general_index['col'] =  (self.general_index['col'] + int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])) % self.cols
            if keys[pygame.K_SPACE]:
                if self.general_index['row'] == 0 and self.general_index['col'] == 0:
                    # name = self.hand_cards[0]
                    # self.aplay_card_attack(name)
                    # function.deal()
                    pass

                

    def quad_select(self, index, options):
        # bg
        rect = pygame.FRect(self.left + 40, self.top + 60 ,400, 200)
        pygame.draw.rect(self.display_surface, COLORS['white'],rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'],rect, 4, 4)

        # menu 
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + rect.width / (self.cols * 2) + (rect.width / self.cols) * col
                y = rect.top + rect.height / (self.rows * 2) + (rect.height / self.rows) * row
                i = col + 2 * row
                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']

                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center = (x,y))
                self.display_surface.blit(text_surf, text_rect)
    
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
        match self.state:
            case 'general': self.quad_select(self.general_index, self.general_options)
