# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from CONFIG_game import *
from CONFIG_fonts import *
from CONFIG_texts import *
from GAME_functions import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import pygame

pygame.init()

class EndScreen:
    def __init__(self, screen_w: int, screen_h: int, texts:list[str], lvl_img: str) -> None:
        # INICIAÇÃO
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.texts = texts
        self.lvl_img = lvl_img
        # PROPRIEDADES
        self.color = 'black'
        # CAIXA DE TEXTO
        self.text_box_size = (1250, 200)
        self.box_offset = (20, 20)
        self.text_box_pos = (self.screen_w / 2 - self.text_box_size[0] / 2, self.screen_h - self.text_box_size[1] - self.box_offset[1])
        self.text_box_img = convert_img('./resources/ilustrations/dialog_box.png', 0, 1)
        # ILUSTAÇÃO DO PERSONAGEM
        self.player_face_offset = (25,0)
        self.player_face_size = (250, 250)
        self.player_face_pos = (self.text_box_pos[0] + self.player_face_offset[0], self.text_box_pos[1] - self.player_face_size[1])
        self.player_face_img = convert_img('./resources/ilustrations/day_city_diolog_art.png', 0, 1)
        # ILUSTRACÃO DA FASE
        self.ilustration_offset = (0, 20)
        self.ilustration_size = (450, 300)
        self.ilustration_pos = (self.screen_w / 2 - self.ilustration_size[0] / 2, self.text_box_pos[1] - self.ilustration_size[1] - self.ilustration_offset[1])
        self.ilustration_img = convert_img(self.lvl_img, 0, 1)
        # TEXTOS
        self.text_offset = (20, 30)
        self.line_space = 10
        self.lines = []
        self.lines_pos = []
        space = 0
        for i,text in enumerate(self.texts):
            line = FONT_PS2P.render(f'{text}', False, 'white')
            pos = (self.text_offset[0], (line.get_height() + self.line_space) * i + self.text_offset[1])
            self.lines.append(line)
            self.lines_pos.append((self.text_box_pos[0] + pos[0],  self.text_box_pos[1] + pos[1]))
        # TEXTO DE VITÓRIA
        self.victory_txt = FONT_PS2P_STAGE_NAME.render(load_current_texts()['victory'], False, 'white')
        self.victory_pos = (self.screen_w / 2 - self.victory_txt.get_width() / 2, 50)

    def paint(self, screen):
        # BACKGROUND
        screen.fill(self.color)
        # ROSTO DO PERSONAGEM
        screen.blit(self.player_face_img, self.player_face_pos)
        # CAIXA DE TEXTO
        screen.blit(self.text_box_img, self.text_box_pos)
        # TEXTO
        for i,line in enumerate(self.lines):
            screen.blit(line, self.lines_pos[i])
        # ILUSTRAÇÃO DA FASE
        screen.blit(self.ilustration_img, self.ilustration_pos)
        # NOME DA FASE
        screen.blit(self.victory_txt, self.victory_pos)
        # INFORMAÇÕES DA FASE


