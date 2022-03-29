# IMPORTA AS BIBLIOTECAS USADAS
import pygame
pygame.init()

# IMPORTA OS OUTROS ARQUIVOS USADOS
from GAME_functions import *
from ASSETS_others import *


# CLASSE DE OBJETO EM GERAL
class Object(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        # PROPRIEDADES
        self.render_distance = 2 * 64

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        self.image.fill('#812F33')
        self.rect = self.image.get_rect(topleft = self.pos)


    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


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
        
        self.rect = self.image.get_rect(bottomleft = self.rect.center)


    def update(self, player):
        # if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.animate()

# ******** TODOS ************
class Flag(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLAG, 0, self.width / 64)
        self.animation_speed = 0.1

class S_Flag(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_FLAG, 0, self.width / 64)
        self.animation_speed = 0.1

class N_Flag(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_N_FLAG, 0, self.width / 64)
        self.animation_speed = 0.1

# ******** CIDADE DE DIA ************

# POSTE DE LUZ NA CIDADE DE DIA (!)
class DayLightPost(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_LIGHT_POST, 0, self.width / 64)
        self.animation_speed = 0.1


# BANCO DA CIDADE DE DIA (#)
class DayBench(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BENCH, 0, self.width / 128)
        self.animation_speed = 0.1


# BANCO DA CIDADE DE DIA ($)
class DayHydrant(Object):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_HYDRANT, 0, self.width / 64)
        self.animation_speed = 0.1


# ******* ESGOTO *********
# TUBO DA PAREDE COM QUEDA DE ESGOTO (@)
class Waterfall(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_WATERFALL, 0, self.width / 64)
        self.animation_speed = 0.1

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
        
        self.rect = self.image.get_rect(topleft = self.rect.center)


# ESCADA DE PAREDE (#)
class Stair(Waterfall):
    def __init__(self, pos):
        super().__init__(pos)
        self.animation_frames = convert_animation_imgs(ANIMATION_STAIR, 0, self.width / 64)


# LAMPADA (º)
class Lamp(Object):
    def __init__(self, pos):
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.width = 64
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_LAMP, 0, self.width / 64)
        self.animation_speed = 0.1


# ******* NAVE ***********
# SETAS
# (>)
class SignL(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_L, 0, self.width / 64)
        self.animation_speed = 0.1
# (<)
class SignR(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_R, 0, self.width / 64)
        self.animation_speed = 0.1
# (^)
class SignU(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_U, 0, self.width / 64)
        self.animation_speed = 0.1
# (|)
class SignD(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_D, 0, self.width / 64)
        self.animation_speed = 0.1
# ("(")
class SignLU(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_LU, 0, self.width / 64)
        self.animation_speed = 0.1
# (")")
class SignLD(Object):
    def __init__(self, pos):
        super().__init__(pos)
    # PROPRIEDADES DE ANIMAÇÃO
        self.width = 128
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SIGN_LD, 0, self.width / 64)
        self.animation_speed = 0.1






