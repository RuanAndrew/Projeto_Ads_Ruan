import pygame
from os.path import join 
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

ENEMY_DATA = {
    'Cultist': {'hp': 51,
                'moves': ('Incantation', 'Dark Strike')}
}

CARDS_DATA = {
    'Bash': {'rarity': 'starter',
              'type': 'attack',
              'energy': 2,
              'description': ('deal(8)','apply(2, vulnerable)')},
    'Defend': {'rarity': 'starter',
              'type': 'skill',
              'energy': 1,
              'description': ('gain(5, block)')},
    'Strike': {'rarity': 'starter',
              'type': 'attack',
              'energy': 1,
              'description': ('deal(6)')}
}