from settings import *
from support import *
from entities import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('slay the spire')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        self.player = Player(pygame.image.load(join('images', 'entities', 'ironclad.webp')).convert_alpha(), self.all_sprites)
        self.enemies = Enemies('cultist', pygame.image.load(join('images', 'entities', 'cultist.webp')).convert_alpha(), self.all_sprites)

    def import_assetes(self):
        pass

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.blit(pygame.transform.scale(pygame.image.load(join('images', 'other', 'background.webp')).convert_alpha(),(WINDOW_WIDTH, WINDOW_HEIGHT)))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()