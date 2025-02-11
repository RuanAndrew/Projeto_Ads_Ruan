from settings import *
from support import *
from entities import *
from deck import *
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('slay the spire')
        self.clock = pygame.time.Clock()
        self.running = True
        self.active_box = None

        # groups 
        self.all_sprites = pygame.sprite.Group()
        self.cards_groups = pygame.sprite.Group()

        # data
        self.all_cards = card_folder_importer('images', 'cards')
        # self.card = [Card(card, self.all_cards[card], (self.all_sprites, self.cards_groups)) for card in list(self.all_cards.keys())]
        self.deck = Deck(self.all_cards)

        self.player = Player(pygame.image.load(join('images', 'entities', 'ironclad.webp')).convert_alpha(), self.all_sprites)

        monster_name = choice(list(ENEMY_DATA.keys()))
        self.enemies = Enemies(monster_name, pygame.image.load(join('images', 'entities', f'{monster_name}.webp')).convert_alpha(), self.all_sprites)

        # ui
        self.ui = UI(self.deck.hand_cards, self.all_cards, self.apply_card_attack, self.player, self.enemies)

        # cards
        self.deck.start_deck()

    def apply_card_attack(self, name):
        card_attack = CARDS_DATA[name]['description']
        card_attack = str(card_attack).split(",")
        for func in card_attack:
            func

    def input(self):
        pass

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)
            self.ui.update()

            # draw
            self.display_surface.blit(pygame.transform.scale(pygame.image.load(join('images', 'other', 'background.webp')).convert_alpha(),(WINDOW_WIDTH, WINDOW_HEIGHT)))
            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()