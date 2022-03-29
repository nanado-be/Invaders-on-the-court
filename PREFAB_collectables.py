# IMPORTA AS BIBLIOTECAS USADAS
import pygame
pygame.init()
import math
import random

# IMPORTA OS OUTROS ARQUIVOS USADOS
from GAME_functions import *
from ASSETS_enemys import *
from ASSETS_others import *

# CLASSE DE INIMIGO EM GERAL
class Collectable(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = [pos[0] + 32, pos[1] + 32]
        self.size = 32

        # PROPRIEDADES
        self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        self.pop_sound = random.choice(SFX_E_DEATH)
        self.render_distance = 8 * 64

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        self.image.fill('#812F33')
        self.rect = self.image.get_rect(center = self.pos)
 

    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


    # VERIFICA SE O PERSONAGEM DEVE SER APAGADO
    def pop(self):
        self.pop_sound.play()           
        self.kill()


    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True


    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.animate()
 
class C_Bomb(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'bomb'

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_BOMB, 0, self.size / 32)
        self.animation_speed = 0.1

class C_Heart(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'heart'

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_HEART, 0, self.size / 32)
        self.animation_speed = 0.1

class C_Cristal(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'cristal'

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_CRISTAL, 0, self.size / 32)
        self.animation_speed = 0.1

class C_Syringe(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'syringe'

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_SYRINGE, 0, self.size / 32)
        self.animation_speed = 0.1

class C_Pills(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'pills'

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_PILLS, 0, self.size / 32)
        self.animation_speed = 0.1

class C_Coin(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'coin'
        self.size = 32



        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_COIN, 0, self.size / 64)
        self.animation_speed = 0.1

class C_MegaCoin(Collectable):
    def __init__(self, pos):
        super().__init__(pos)
        self.type = 'mega coin'
        self.size = 64
        self.place = 0
        self.id = None

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_MEGA_COIN, 0, self.size / 128)
        self.animation_speed = 0.1
