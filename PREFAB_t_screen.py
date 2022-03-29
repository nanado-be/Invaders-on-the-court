# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from CONFIG_game import *
from CONFIG_fonts import *
from CONFIG_texts import *
from GAME_functions import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import pygame

pygame.init()

class TutorialScreen:
    def __init__(self, screen_w: int, screen_h: int, number:int) -> None:
        # INICIAÇÃO
        self.screen_w = screen_w
        self.screen_h = screen_h
        # PROPRIEDADES
        self.color = 'black'
        # QUADRO DO TUTORIAL
        self.tutorial_img_size = (700, 600)
        self.tutorial_img = convert_img(f'./resources/ilustrations/tutorial/t{number}.png',0, 1)
        self.tutorial_img_pos = (self.screen_w / 2 - self.tutorial_img_size[0] / 2, self.screen_h / 2 - self.tutorial_img_size[1] / 2)

    def paint(self, screen):
        # BACKGROUND
        screen.fill(self.color)
        # QUADRO DO TUTORIAL
        screen.blit(self.tutorial_img, self.tutorial_img_pos)
        # TEXTO
        # for i,line in enumerate(self.lines):
        #     screen.blit(line, self.lines_pos[i])
