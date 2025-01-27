import pygame
from os.path import join 
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

ENEMY_DATA = {
    'Cultist': {'hp': 51, 'moves': ('Incantation', 'Dark Strike')}
}