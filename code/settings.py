import pygame
from os.path import join 
from os import walk
from random import randint, choice

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': 'gray',
    'white': '#ffffff',
}

ENEMY_DATA = {
    'cultist': {'hp': randint(48,54),
                'moves': {'incantation': ('gain(3, ritual)'),
                           'dark Strike': ('deal(6)')}},
    'jaw_worm': {'hp': randint(40,44),
                 'moves': {'chomp': ('deal(11)'),
                           'thrash': ('deal(7)', 'gain(5, block)'),
                           'bellow': ('gain(3, strength)', 'gain(6, block)')}}
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