# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from GAME_functions import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import pygame
pygame.init()


# CLASSE DE UMA UNIDADE DE PLATAFORMA
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, family, placement, rotation):
        super().__init__()
        # INICIALIZAÇÃO
        self.original_pos = pos
        self.size = size
        self.family = family
        self.placement = placement
        self.rotation = rotation


        # PROPRIEDADES BÁSICAS
        self.image_size = 64
        self. color = TUNA
        self.render_distance = 8 * self.size 

        # PROPRIEDADES DO SPRITE
        self.image = convert_img(f'./resources/map/tiles/{self.family}/{self.placement}.png', self.rotation, self.size / self.image_size)
        self.rect = self.image.get_rect(topleft = self.original_pos)

    # ALTERA A POSIÇÃO DO SPRITE DE ACORDO COM O OFFSET DA CÂMERA
    def h_shift(self, cam_shift):
        self.rect.x = self.original_pos[0] + cam_shift[0]

    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.original_pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.original_pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True

    def update(self, cam_shift):
        if not self.in_render_distance: return
        self.h_shift(cam_shift)




