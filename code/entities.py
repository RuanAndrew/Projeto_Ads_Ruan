from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale_by(surf, 0.7)
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2 + 150))
        
        self.hp = self.max_hp = 80
        self.energy = self.max_energy = 3
        self.gold = 99
        self.relics = ['burning blood']
        
class Enemies(pygame.sprite.Sprite):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale_by(surf, 0.35)
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH / 4 + WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 150))
        self.get_data(name)
        
    def get_data(self, name):
        self.hp = self.max_hp = ENEMY_DATA[name]['hp']
        self.moves = ENEMY_DATA[name]['moves']