import pygame
from os.path import join 
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

ENEMY_DATA = {
    'cultist': {'hp': 51,
                'moves': ('incantation', 'dark Strike')}
}

CARDS_DATA = {
    'bash': {'rarity': 'starter',
              'type': 'attack',
              'energy': 2,
              'description': ('deal(8)','apply(2, vulnerable)'),
              'is_upgrade': ('deal(10)','apply(3, vulnerable)')},
    'defend': {'rarity': 'starter',
              'type': 'skill',
              'energy': 1,
              'description': ('gain(5, block)'),
              'is_upgrade': ('gain(8, block)')},
    'strike': {'rarity': 'starter',
              'type': 'attack',
              'energy': 1,
              'description': ('deal(6)'),
              'is_upgrade': ('deal(9)')}
}