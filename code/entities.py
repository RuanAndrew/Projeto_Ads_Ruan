from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale_by(surf, 0.6)
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2 + 150))
        
        self.hp = self.max_hp = 80
        self.energy = self.max_energy = 3
        self.block = 0
        self.strength = 0
        self.vulnerable = 0

    def gain_block(self, amount):
        self.block += amount

    def take_damage(self, damage):
        if self.block > 0:
            absorbed = min(self.block, damage)
            self.block -= absorbed
            damage -= absorbed
        
        if damage > 0:
            self.hp -= damage
        
class Enemies(pygame.sprite.Sprite):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale_by(surf, 0.4)
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH / 4 + WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 150))

        self.name = name
        self.hp = self.max_hp = ENEMY_DATA[name]['hp']
        self.block = 0
        self.vulnerable = 0
        self.weak = 0