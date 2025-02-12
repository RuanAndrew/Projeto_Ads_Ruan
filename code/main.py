from settings import *
from support import *
from entities import *
from deck import *
from ui import UI
from powers import *

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
        self.cards_group = pygame.sprite.Group()


        # data
        self.all_cards = card_folder_importer('images', 'cards')
        self.card = [Card(card, self.all_cards[card], self.cards_group) for card in list(self.all_cards.keys())]
        self.deck = Deck(self.all_cards, self.cards_group)

        self.player = Player(pygame.image.load(join('images', 'entities', 'ironclad.webp')).convert_alpha(), self.all_sprites)

        monster_name = choice(list(ENEMY_DATA.keys()))
        self.enemies = Enemies(monster_name, pygame.image.load(join('images', 'entities', f'{monster_name}.webp')).convert_alpha(), self.all_sprites)

        # ui
        self.ui = UI(self.deck.hand_cards, self.apply_card_attack, self.player, self.enemies)

        # cards
        self.deck.start_deck()

    def apply_card_attack(self, card_name):
        card_data = CARDS_DATA[card_name]
        for effect, *args in card_data['description']:
            if effect == 'deal':
                deal(self.enemies, *args)
            elif effect == 'gain':
                gain(self.player, *args)
            elif effect == 'apply':
                apply(self.enemies, *args)
            else:
                print(f"Unknown effect: {effect}")

    def input(self):
        pass

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_collide = self.card.rect.collidepoint(pos)
                    
                    clicked_cards = [card for card in self.cards_group if card.rect.collidepoint(pos)]
                    print(clicked_cards)

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