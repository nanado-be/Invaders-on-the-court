# IMPORTA AS BIBLIOTECAS USADAS
import pygame
pygame.init()
import math
import random

# IMPORTA OS OUTROS ARQUIVOS USADOS
from GAME_functions import *
from ASSETS_enemys import *


# CLASSE DE INIMIGO EM GERAL
class Enemy(pygame.sprite.Sprite): 
    def __init__(self, pos, tiles = [], born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.born_bg_pan = born_bg_pan
        self.hp = self.max_hp
        self.type = 'minion'

        # PROPRIEDADES
        self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        self.death_sound = random.choice(SFX_E_DEATH)
        self.fragile_head = True
        self.spike_head = False
        self.bounce_protected = False
        self.front_protected = False
        self.explosion_protected = False
        self.laser_protected = False
        self.harmless = False
        self.inert = False
        self.render_distance = 8 * 64
        self.shoot_distance = 4 * 64
        self.living = True

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(topleft = self.pos)

        self.near_tiles = []
        self.get_near_tiles(tiles)


        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')


    # VERIFICA SE O PERSONAGEM VAI BATER EM UM TILE NA DIREITA (SYSTEM)
    def hit_right_tile(self, distance, tiles):
        # VERIFICA SE AO MOVIMENTAR NÃO BATERÁ EM UMA PAREDE
        distance *= 2
        for tile in self.near_tiles:
            if tile.rect.centerx > self.rect.centerx - 10 * self.size and tile.rect.centerx < self.rect.centerx + 10 * self.size:
                if tile.rect.collidepoint((self.rect.bottomright[0] + distance, self.rect.bottomright[1] -10)) or tile.rect.collidepoint((self.rect.midright[0] + distance, self.rect.midright[1])) or tile.rect.collidepoint((self.rect.topright[0] + distance, self.rect.topright[1])):
                    self.rect.right = tile.rect.left - 1
                    return True
        return False
    
    # VERIFICA SE O PERSONAGEM VAI BATER EM UM TILE NA ESQUERDA (SYSTEM)
    def hit_left_tile(self, distance, tiles):
        distance *= 2
        for tile in self.near_tiles:
            if tile.rect.centerx > self.rect.centerx - 10 * self.size and tile.rect.centerx < self.rect.centerx + 10 * self.size:
                if tile.rect.collidepoint((self.rect.bottomleft[0] - distance, self.rect.bottomleft[1] -10)) or tile.rect.collidepoint((self.rect.midleft[0] - distance, self.rect.midright[1])) or tile.rect.collidepoint((self.rect.topleft[0] - distance, self.rect.topleft[1])):
                    self.rect.left = tile.rect.right + 1
                    return True
        return False

    # MOVE O PERSONAGEM VAI CAIR NA DIREITA (SYSTEM)
    def fall_right(self, distance, tiles):
        for tile in self.near_tiles:
            if self.rect.right + distance >= tile.rect.left and self.rect.right + distance < tile.rect.right and self.rect.bottom >= tile.rect.top and self.rect.bottom < tile.rect.top + 5:
                return False
        return True
 
    # MOVE O PERSONAGEM VAI CAIR NA ESQUERDA (SYSTEM)
    def fall_left(self, distance, tiles):
        for tile in self.near_tiles:
            if self.rect.left + distance >= tile.rect.left and self.rect.left + distance < tile.rect.right and self.rect.bottom >= tile.rect.top and self.rect.bottom < tile.rect.top + 5:
                return False
        return True
 
    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # APLICA UMA CERTA QUANTIDADE DE DANO AO PERSONAGEM
    def get_hit(self, damage, player, particles_group, pop = True, n_particles = 25):
        self.hp -= damage
        self.life_bar.update_pos(self.rect.bottomleft)
        self.life_bar.update_life(self.hp)
        if self.hp <= 0 and self.living:
            player.score += 5
            self.living = False
        if not pop: return
        for i in range (n_particles):
            particles_group.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))
            # particles_group.add(Particle([self.rect.center[0], self.rect.center[1]], 2, 4, 15, 20, 64, 'white'))

    # VERIFICA SE O PERSONAGEM DEVE SER APAGADO
    def life_check(self, player):
        if self.hp <= 0:
            self.death_sound.play()   
            player.particles.add(DeathExplosion([self.pos[0] + self.size/2 , self.pos[1] - self.size/2], self.size))
            self.kill()

    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True

    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE atirar
    def in_shoot_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.shoot_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.shoot_distance + player.screen_w: return False
        return True

    def get_near_tiles(self, tiles):
        for tile in tiles:
            if tile.rect.bottom < self.rect.top - self.size - 10: continue
            if tile.rect.top > self.rect.bottom + self.size: continue
            if tile.rect.left < self.rect.left - 3000 + self.born_bg_pan[0]: continue
            if tile.rect.right > self.rect.right + 3000 - self.born_bg_pan[0]: continue
            self.near_tiles.append(tile)
    
    def get_hit_tiles(self, tiles):
        self.hit_tiles = pygame.sprite.Group()
        self.hit_tiles.add(tiles.sprites()[0])
        
        for tile in tiles.sprites():
            if tile.rect.left - self.rect.left >= 20 * 64: continue
            if self.rect.right - self.rect.right >= 20 * 64: continue
            if tile.rect.bottom < self.rect.top: continue
            if tile.rect.top > self.rect.bottom: continue
            self.hit_tiles.add(tile)

    def get_tank_hit_tiles(self, tiles):
        self.hit_tiles = pygame.sprite.Group()
        self.hit_tiles.add(tiles.sprites()[0])
        
        for tile in tiles.sprites():
            if tile.rect.left - self.rect.left >= 20 * 64: continue
            if self.rect.right - self.rect.right >= 20 * 64: continue
            if tile.rect.bottom < self.rect.top - 64: continue
            if tile.rect.top > self.rect.bottom - 64: continue
            self.hit_tiles.add(tile)

    def get_bomb_hit_tiles(self, tiles):
        self.hit_tiles = pygame.sprite.Group()
        self.hit_tiles.add(tiles.sprites()[0])
        
        for tile in tiles.sprites():
            if tile.rect.right - self.rect.right > 12 * 64: continue
            if self.rect.left  - tile.rect.left  > 12 * 64: continue
            self.hit_tiles.add(tile)

    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(bottomleft = self.rect.center)



# CLASSE DA BARRA QUE MOSTRA A VIDA DE UM PERSONAGEM
class LifeBar(pygame.sprite.Sprite):
    def __init__(self, size, pos, max_hp, bg_color, fg_color):
        # INICIALIZAÇÂO
        super().__init__()
        self.size = size
        self.max_hp = max_hp
        self.pos = pos
        self.bg_color = bg_color
        self.fg_color = fg_color

        # PROPRIEDADES
        self.current_hp = self.max_hp
        self.current_hp_bar_size = [self.size[0], self.size[1] * self.current_hp / self.max_hp]
        self.y_offset = 5

        # SPRITES
        # -- BARRA DE FUNDO
        self.bg_bar = pygame.sprite.Sprite()
        self.bg_bar.image = pygame.Surface(self.size)
        self.bg_bar.image.fill(self.bg_color)
        self.bg_bar.rect = self.bg_bar.image.get_rect(topleft = self.pos)
        # -- BARRA DA FRENTE
        self.fg_bar = pygame.sprite.Sprite()
        self.fg_bar.image = pygame.Surface(self.size)
        self.fg_bar.image.fill(self.fg_color)
        self.fg_bar.rect = self.fg_bar.image.get_rect(topleft = self.pos)
        self.group = pygame.sprite.Group()
        self.group.add(self.bg_bar)
        self.group.add(self.fg_bar)


    def update_life(self, new_hp):
        self.current_hp = new_hp
        self.current_hp_bar_size = self.size[0] * self.current_hp / self.max_hp
        if self.current_hp_bar_size < 0: self.current_hp_bar_size = 0
        self.fg_bar.image = pygame.Surface([self.current_hp_bar_size, self.size[1]])
        self.fg_bar.image.fill(self.fg_color)
        # self.fg_bar.rect = self.fg_bar.image.get_rect(topleft = self.pos)


    def update_pos(self, pos):
        self.bg_bar.rect.topleft = pos
        self.fg_bar.rect.topleft = pos   


    def move(self, dist):
        self.bg_bar.rect.x += dist[0]
        self.bg_bar.rect.y += dist[0]
        self.fg_bar.rect.x += dist[1]
        self.fg_bar.rect.y += dist[1]


    def paint(self, screen):
        self.group.draw(screen)
        

    def update(self):
        self.group.empty()
        self.group.add(self.bg_bar)
        self.group.add(self.fg_bar)        



# CLASSE DE PARTICULAS GENÉRICAS
class ExplosionParticle(pygame.sprite.Sprite):
    def __init__(self, pos, min_size, max_size, min_speed, max_speed, life_radius, color):
        # INICIALIZAÇÃO
        super().__init__()
        self.size = random.randint(min_size, max_size)
        self.pos = pos
        self.origin = (pos[0], pos[1])
        self.p_speed = random.randint(min_speed, max_speed)
        self.p_angle = random.randint(0, 360)
        self.p_angle = self.p_angle * math.pi / 180
        self.x_speed = self.p_speed * math.cos(self.p_angle)
        self.y_speed = self.p_speed * math.sin(self.p_angle)
        self.v = [self.x_speed, self.y_speed]
        self.life_radius = life_radius

        # PROPRIEDADES DO SPRITE
        self.color = random.choice(color)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)

    # MOVE O SPRITE
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


    
    # AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


    # VERIFICA SE A SPRITE DEVE CONTINUAR EXISTINDO
    def check_life(self):
        if math.sqrt((self.pos[0] - self.origin[0]) ** 2 + (self.pos[1] - self.origin[1]) ** 2) > self.life_radius: self.kill()


    # ATUALIZA A SPRITE
    def update(self, bg_pan):
        self.move()
        self.pan_ajust(bg_pan)
        self.check_life()



# CLASSE DO PROJETIL BASICO DO INIMIGO
class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, pos, v, damage, tiles):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.v = v
        self.damage = damage
        self.type = 'basic'
        self.size = 16
        self.render_distance = 64
        self.life_distance = 20 * 64 
        self.born_pos = (pos[0], pos[1])
        self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']

        # PROPRIEDADES DO SPRITE
        self.image = convert_img(E_PROJECTILE, 0, self.size / 8)
        self.rect = self.image.get_rect(center = pos)

        self.hit_tile = tiles

    # MOVE O SPRITE
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

# AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # VERIFICA SE O PROJETIL DEVER SUMIR
    def life_check(self, player):
        # VERIFICA SE O PEOJETIL SAIU DA TELA
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance and self.v[0] <= 0: self.kill()
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w  and self.v[0] >= 0: self.kill()
        
        # VERIFICA SE O PROJETIL ATINGIU UM TERRENO
        collinding_tile = pygame.sprite.spritecollide(self, self.hit_tile, False)
        if collinding_tile:
            for i in range (10):
                player.particles.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))
            self.kill()
        # VERIFICA SE PASSOU O LIMITE DA EXISTENCIA
        if self.pos[0] - self.born_pos[0] > 20 * 64 or self.born_pos[0] - self.pos[0] > 20 * 64:
            for i in range (10):
                player.particles.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))
            self.kill()


    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True

    def update(self, player):
        # if not self.in_render_distance(player): return
        self.move()
        self.pan_ajust(player.bg_pan)
        self.life_check(player)



# CLASSE DA FUMAÇA VENENOSA
class Smoke(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = 512
        self.render_distance = 512

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(center = self.pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SMOKE, 0, self.size / 512)
        self.animation_speed = 0.1

    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True
    
    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    def check_life(self, dad):
        try:
            if dad.living: pass
            else: self.kill()
        except: self.kill()

    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, player, dad):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.check_life(dad)
        self.animate()



# CLASSE DA FUMAÇA DE SURGIMENTO DE INIMIGOS
class BornSmoke(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = 128

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(center = self.pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BORN_SMOKE, 0, self.size / 128)
        self.animation_speed = 0.25
 
    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames):
                self.current_animation_frame = 0
                self.kill()

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, bg_pan):
        self.pan_ajust(bg_pan)
        self.animate()



# CLASSE DA FUMAÇA DE SURGIMENTO DE INIMIGOS
class DeathExplosion(pygame.sprite.Sprite):
    def __init__(self, pos, dad_size):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = 128 * dad_size/64

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(center = self.pos)

        self.animation_types = [
            ANIMATION_E_DEATH_1,
            ANIMATION_E_DEATH_2,
            ANIMATION_E_DEATH_3,
            ANIMATION_E_DEATH_4
        ]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(random.choice(self.animation_types), 0, self.size / 128)
        self.animation_speed = 0.5
 
    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames):
                self.current_animation_frame = 0
                self.kill()

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, bg_pan):
        self.pan_ajust(bg_pan)
        self.animate()



# CLASSE DA FUMAÇA DE SURGIMENTO DE INIMIGOS
class PlayerHurt(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = 64

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(center = self.pos)


        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_P_HURT, 0, self.size / 32)
        self.animation_speed = 0.5
 
    # AJUSTA A POSIÇÃO DO PERSONAGEM NA TELA, DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames):
                self.current_animation_frame = 0
                self.kill()

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.size, self.size))
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self, bg_pan):
        self.pan_ajust(bg_pan)
        self.animate()



# CLASSE DO CIRCULO MAGNETICO
class MagCircle(Smoke):
    def __init__(self, pos):
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_M_CIRCLE, 0, self.size / 512)
        self.animation_speed = 0.2



# CLASSE DO PROJETIL BASICO DO INIMIGO
class EnemyBomb(pygame.sprite.Sprite):
    def __init__(self, pos, v, damage, tiles):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.v = v
        self.g = 1
        self.damage = damage
        self.hit_tile = tiles
        self.type = 'basic'
        self.size = 32
        self.render_distance = 64
        self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']

        # PROPRIEDADES DO SPRITE
        self.image = convert_img(E_BOMB, 0, self.size / 16)
        self.rect = self.image.get_rect(center = pos)

    # MOVE O SPRITE
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.v[1] += self.g


    # AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    # VERIFICA SE O PROJETIL DEVER SUMIR
    def life_check(self, player):
        # VERIFICA SE O PEOJETIL SAIU DA TELA
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance and self.v[0] <= 0: self.kill()
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w and self.v[0] >= 0: self.kill()

        # VERIFICA SE O PROJETIL ATINGIU UM TERRENO
        collinding_tile = pygame.sprite.spritecollide(self, self.hit_tile, False)
        if collinding_tile:
            for i in range (10):
                player.particles.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))
            self.kill()


    # VERIFICA SE O PERSONAGEM ESTÁ NA DISTANCIA DE RENDERIZAÇÃO
    def in_render_distance(self, player):
        if self.pos[0] <= - player.bg_pan[0] - self.render_distance: return False
        if self.pos[0] >= - player.bg_pan[0] + self.render_distance + player.screen_w: return False
        return True

    def update(self, player):
        # if not self.in_render_distance(player): return
        self.move()
        self.pan_ajust(player.bg_pan)
        self.life_check(player)


# CLASSE DOS PROJETEIS DE EXPLOSÃO da BombSpikeBall
class E_ExplosionProjectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÃO
        super().__init__()
        self.size = random.randint(2,4)
        self.pos = pos
        self.origin = (pos[0], pos[1])
        self.p_speed = random.randint(2, 10)
        self.p_angle = random.randint(0, 360)
        self.p_angle = self.p_angle * math.pi / 180
        self.x_speed = self.p_speed * math.cos(self.p_angle)
        self.y_speed = self.p_speed * math.sin(self.p_angle)
        self.v = [self.x_speed, self.y_speed]
        self.life_radius = 64 * 3
        self.type = 'bomb projectile'

        # PROPRIEDADES DO SPRITE
        if self.p_speed < 3: self.color = 'black'
        elif self.p_speed < 7: self.color = 'red'
        else: self.color = 'yellow'
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = pos)

    # MOVE O SPRITE
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


    
    # AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


    # VERIFICA SE A SPRITE DEVE CONTINUAR EXISTINDO
    def check_life(self):
        # if self.pos[0] - self.origin[0] > 64: self.kill()
        # if self.pos[0] - self.origin[0] < -64: self.kill()
        if math.sqrt((self.pos[0] - self.origin[0]) ** 2 + (self.pos[1] - self.origin[1]) ** 2) > self.life_radius: self.kill()


    # ATUALIZA A SPRITE
    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        self.check_life()

 

# **********************************
# **********************************
#            INIMIGOS
# **********************************
# **********************************

# CLASSE (a) - PLANADOR <<- ->>
class Fly1(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [2, 0]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 50
        self.atk = 20
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLY, 0, self.size / 64)
        self.animation_b2 = convert_animation_imgs(ANIMATION_FLY_B2, 0, self.size / 64)
        self.animation_b1 = convert_animation_imgs(ANIMATION_FLY_B1, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.timer >= self.time_moving:
            self.timer = 0
            self.v[0] = -self.v[0]
        self.timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

    def life_state(self):
        if self.hp <= self.max_hp / 3: self.animation_frames = self.animation_b2
        elif self.hp <= 2 * self.max_hp / 3: self.animation_frames = self.animation_b1

    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_state()
        self.life_check(player)
        self.animate()



# CLASSE (b) - PLANADOR ^^- -\/\/
class Fly2(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 2]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 50
        self.atk = 20
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLY, 0, self.size / 64)
        self.animation_b2 = convert_animation_imgs(ANIMATION_FLY_B2, 0, self.size / 64)
        self.animation_b1 = convert_animation_imgs(ANIMATION_FLY_B1, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.timer >= self.time_moving:
            self.timer = 0
            self.v[1] = -self.v[1]
        self.timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


    def life_state(self):
        if self.hp <= self.max_hp / 3: self.animation_frames = self.animation_b2
        elif self.hp <= 2 * self.max_hp / 3: self.animation_frames = self.animation_b1


    def update(self,player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_state()
        self.life_check(player)
        self.animate()



# CLASSE (c) - PLANADOR \
class Fly3(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [-2, -2]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 50
        self.atk = 20
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLY, 0, self.size / 64)
        self.animation_b2 = convert_animation_imgs(ANIMATION_FLY_B2, 0, self.size / 64)
        self.animation_b1 = convert_animation_imgs(ANIMATION_FLY_B1, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.timer >= self.time_moving:
            self.timer = 0
            self.v[0] = -self.v[0]
            self.v[1] = -self.v[1]
        self.timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


    def life_state(self):
        if self.hp <= self.max_hp / 3: self.animation_frames = self.animation_b2
        elif self.hp <= 2 * self.max_hp / 3: self.animation_frames = self.animation_b1


    def update(self,player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_state()
        self.life_check(player)
        self.animate()



# CLASSE (d) - PLANADOR /
class Fly4(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [2, -2]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 50
        self.atk = 20
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLY, 0, self.size / 64)
        self.animation_b2 = convert_animation_imgs(ANIMATION_FLY_B2, 0, self.size / 64)
        self.animation_b1 = convert_animation_imgs(ANIMATION_FLY_B1, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.timer >= self.time_moving:
            self.timer = 0
            self.v[0] = -self.v[0]
            self.v[1] = -self.v[1]
        self.timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

    def life_state(self):
        if self.hp <= self.max_hp / 3: self.animation_frames = self.animation_b2
        elif self.hp <= 2 * self.max_hp / 3: self.animation_frames = self.animation_b1

    def update(self,player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_state()
        self.life_check(player)
        self.animate()



# CLASSE (e) - PLANADOR [] 
class Fly5(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [2, 0]
        self.timer = 0
        self.move_state = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 50
        self.atk = 20
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_FLY, 0, self.size / 64)
        self.animation_b2 = convert_animation_imgs(ANIMATION_FLY_B2, 0, self.size / 64)
        self.animation_b1 = convert_animation_imgs(ANIMATION_FLY_B1, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.timer >= self.time_moving:
            self.timer = 0
            if self.move_state == 0:
                if self.v[0] == 0:
                    self.v[0] = - self.v[1]
                    self.v[1] = 0
                else:
                    self.v[1] = - self.v[0]
                    self.v[0] = 0
                self.move_state += 1
            else:
                if self.v[0] == 0:
                    self.v[0] = self.v[1]
                    self.v[1] = 0
                else:
                    self.v[1] = self.v[0]
                    self.v[0] = 0
                self.move_state -= 1

        self.timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

    def life_state(self):
        if self.hp <= self.max_hp / 3: self.animation_frames = self.animation_b2
        elif self.hp <= 2 * self.max_hp / 3: self.animation_frames = self.animation_b1

    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_state()
        self.life_check(player)
        self.animate()



# CLASSE (f) - OCUPUS <<- ->>
class Octopus(Enemy):
    def __init__(self, pos, tiles, born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        self.v = [1.75, 0]
        self.size = 64
        self.max_hp = 20
        self.atk = 25
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles, born_bg_pan)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_OCTOPUS, 0, self.size / 64)
        self.animation_speed = 0.3


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]



    def update(self,player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (g) - ELETRIC OCUPUS <<- ->>
class EletricOctopus(Enemy):
    def __init__(self, pos, tiles, born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        self.v = [2.5, 0]
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles, born_bg_pan)

        self.spike_head = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_ELETRIC_OCTOPUS, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]


    def update(self,player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (h) - TANK <<- ->>
class Tank(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.v = [1.5, 0]
        self.size = 96
        self.max_hp = 100
        self.atk = 40
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles)
        self.fragile_head = False
        self.bounce_protected = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_TANK, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]


    def update(self, player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (i) - SPIKE <<- ->>
class Spike(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.v = [1.5, 0]
        self.size = 96
        self.max_hp = 100
        self.atk = 20
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles)
        self.fragile_head = False
        self.spike_head = True
        self.bounce_protected = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SPIKE, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]


    def update(self, player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (j) - BOLA X
class Ball1(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE (k) - BOLA - SENTINELA1 antihorário
class Ball2(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [2, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = -math.pi / (128)
        self.angle = 0
        self.r = 2
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (l) - BOLA - SENTINELA1 horário
class Ball3(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [-2, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = math.pi / (128)
        self.angle = 0
        self.r = 2
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (m) - BOLA - GRANDE ARCO ANTIORÀRIO
class Ball4(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = -2 * math.pi / (128)
        self.angle = 0
        self.r = 6
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (n) - BOLA - PEQUENO ARCO ANTIORÀRIO
class Ball5(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = -2 * math.pi / (128)
        self.angle = 0
        self.r = 3
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (o) - BOLA - GRANDE ARCO HORÀRIO
class Ball6(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = 2 * math.pi / (128)
        self.angle = 0
        self.r = 6
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (p) - BOLA - PEQUENO ARCO HORÀRIO
class Ball7(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.time_moving = 64
        self.timer = 0
        self.angular_speed = 2 * math.pi / (128)
        self.angle = 0
        self.r = 3
        self.size = 64
        self.max_hp = 20
        self.atk = 50
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)
        self.linear_pos = self.pos
        self.c_pos = [0,0]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        self.c_pos[0] = self.r  * math.cos(self.angle)
        self.c_pos[1] = self.r  * math.sin(self.angle)
        self.angle += self.angular_speed

        self.linear_pos[0] += self.v[0]
        self.linear_pos[1] += self.v[1]
        self.timer += 1
        if self.timer > self.time_moving:
            self.timer = 0
            self.v[0] = - self.v[0]
            self.v[1] = - self.v[1]
        
        self.pos[0] = self.linear_pos[0] + self.c_pos[0]
        self.pos[1] = self.linear_pos[1] + self.c_pos[1]


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (q) - TORRETA X
class BigShooter(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.timer = 1
        self.atkspd = 1 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.size = 96
        self.max_hp = 20
        self.atk = 30
        self.p_speed = 10
        super().__init__(pos)

        self.get_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SHOOTER, 0, self.size / 64)
        self.animation_speed = 0.1

    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.25], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.25], [self.p_speed,0],  self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (r) - TORRETA X
class SmallShooter(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.timer = 1
        self.atkspd = 1 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.size = 64
        self.max_hp = 20
        self.atk = 45
        self.p_speed = 10
        super().__init__(pos)

        self.get_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SHOOTER, 0, self.size / 64)
        self.animation_speed = 0.1


    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_SHOOT.play()

    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.25], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.25], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (s) - TORRETA X
class CrazyShooter(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.timer = 1
        self.atkspd = 1.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.size = 64
        self.max_hp = 20
        self.atk = 10
        self.p_speed = 10
        super().__init__(pos)

        self.get_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_C_SHOOTER, 0, self.size / 64)
        self.animation_speed = 0.1

    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.25], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.25], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (t) - TORRETA X
class BombShooter(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.timer = 1
        self.atkspd = 1.1 #atk por segundo
        self.recover_time = int(60 / self.atkspd)
        self.size = 96
        self.max_hp = 20
        self.atk = 50
        self.p_speed = 15
        self.p_up_speed = -8
        super().__init__(pos)
        self.front_protected = True

        self.get_bomb_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_B_SHOOTER, 0, self.size / 64)
        self.animation_speed = 0.1

    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyBomb([self.pos[0], self.pos[1] - self.size * 0.25], [-self.p_speed,self.p_up_speed], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyBomb([self.pos[0] + self.size, self.pos[1] - self.size * 0.25], [self.p_speed,self.p_up_speed], self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (u) - TORRETA X
class BombShooter2(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.timer = 1
        self.atkspd = 1.1 #atk por segundo
        self.recover_time = int(60 / self.atkspd)
        self.size = 128
        self.max_hp = 20
        self.atk = 50
        self.p_speed = 15
        self.p_up_speed = -20
        super().__init__(pos)
        self.front_protected = True

        self.get_bomb_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_B_SHOOTER2, 0, self.size / 64)
        self.animation_speed = 0.1


    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyBomb([self.pos[0], self.pos[1] - self.size * 0.25], [-self.p_speed,self.p_up_speed], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyBomb([self.pos[0] + self.size, self.pos[1] - self.size * 0.25], [self.p_speed,self.p_up_speed], self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (v) - SHOTER TANK <<- ->>
class Shootank(Enemy):
    def __init__(self, pos, tiles, born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        self.atkspd = 0.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.timer = random.randint(0, self.recover_time)
        self.v = [2.5, 0]
        self.size = 96
        self.max_hp = 100
        self.atk = 35
        self.p_speed = 15
        self.p_up_speed = 0

        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles, born_bg_pan)
        self.fragile_head = False
        self.bounce_protected = True

        self.get_tank_hit_tiles(tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_TANK, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]


    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        SFX_E_B_SHOOT.play()
    
        self.get_tank_hit_tiles(player.level.tiles_group)


        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.9], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.9], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (w) - SHOTER TANK VOADOR BASICO <<- ->>
class Shootank2(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.atkspd = 0.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.timer = random.randint(1, self.recover_time)
        self.v = [2, 0]
        self.move_timer = 0
        self.time_moving = 64 * 4
        self.size = 96
        self.max_hp = 100
        self.atk = 35
        self.p_speed = 15
        self.p_up_speed = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles)
        self.fragile_head = False
        self.bounce_protected = True

        # self.get_tank_hit_tiles(tiles)


        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_TANK_FLY_GREEN, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.move_timer >= self.time_moving:
            self.move_timer = 0
            self.v[0] = -self.v[0]
        self.move_timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        self.get_tank_hit_tiles(player.level.tiles_group)

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.9], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.9], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return "FIZ ISSO PRA NÃO DESINCRONIZAR OS INIMIGOS"
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (ŵ) - SHOTER TANK VOADOR BASICO <<- ->>
class Shootank2b(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.atkspd = 0.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.timer = random.randint(1, self.recover_time)
        self.v = [-2, 0]
        self.move_timer = 0
        self.time_moving = 64 * 4
        self.size = 96
        self.max_hp = 100
        self.atk = 35
        self.p_speed = 15
        self.p_up_speed = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles)
        self.fragile_head = False
        self.bounce_protected = True

        # self.get_tank_hit_tiles(tiles)


        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_TANK_FLY_GREEN, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self):
        if self.move_timer >= self.time_moving:
            self.move_timer = 0
            self.v[0] = -self.v[0]
        self.move_timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        self.get_tank_hit_tiles(player.level.tiles_group)

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.9], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.9], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        self.move()
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return "FIZ ISSO PRA NÃO DESINCRONIZAR OS INIMIGOS"
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (x) - SHOTER TANK VOADOR AVANÇADO <<- ->>
class Shootank3(Enemy):
    def __init__(self, pos, tiles, born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        self.atkspd = 0.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.timer = random.randint(1, self.recover_time)
        self.v = [2, 1]
        self.move_timer = 0
        self.time_moving = 64 * 1
        self.size = 96
        self.max_hp = 100
        self.atk = 35
        self.p_speed = 15
        self.p_up_speed = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles, born_bg_pan)
        self.fragile_head = False
        self.bounce_protected = True

        self.get_tank_hit_tiles(tiles)


        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_TANK_FLY_BLUE, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles, player):
        if self.v[0] >= 0:
            if self.rect.right + self.v[0] > player.screen_w: self.v[0] = - self.v[0]
            elif self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            else:
                self.pos[0] += self.v[0]

        else:
            if self.rect.left + self.v[0] < 0: self.v[0] = - self.v[0]
            elif self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            else:
                self.pos[0] += self.v[0]

        if self.move_timer >= self.time_moving:
            self.move_timer = 0
            self.v[1] = -self.v[1]
        self.move_timer += 1
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        self.get_tank_hit_tiles(player.level.tiles_group)

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.9], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.9], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        self.move(1, player)
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (y) - SHOTER TANK VOADOR AVANÇADO QUE PERCEGUE <<- ->>
class Shootank4(Enemy):
    def __init__(self, pos, tiles, born_bg_pan = [0,0]):
        # INICIALIZAÇÂO
        self.atkspd = 0.5 #atk por segundo
        self.recover_time = 60 / self.atkspd
        self.timer = random.randint(1, self.recover_time)
        self.v = [1, 1]
        self.vx = 1
        self.vy = 1
        self.move_timer = 0
        self.time_moving = 64 * 4
        self.size = 96
        self.max_hp = 100
        self.atk = 35
        self.p_speed = 15
        self.p_up_speed = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles, born_bg_pan)
        self.y_limit = self.pos[1]
        self.originalx = self.pos[0]
        self.x_limit = 1000

        self.fragile_head = False
        self.bounce_protected = True

        self.get_tank_hit_tiles(tiles)


        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_S_TANK_FLY, 0, self.size / 64)
        self.animation_speed = 0.1


    def move(self, tiles, player):
        if   player.rect.centerx > self.rect.centerx: self.v[0] =   self.vx
        elif player.rect.centerx < self.rect.centerx: self.v[0] = - self.vx
        else: self.v[0] = 0 
        if   player.rect.centery > self.rect.centery: self.v[1] =   self.vy
        elif player.rect.centery < self.rect.centery: self.v[1] = - self.vy
        else: self.v[1] = 0 

        if self.pos[0] + self.v[0] > self.originalx + self.x_limit: self.v[0] = 0
        if self.pos[0] + self.v[0] < self.originalx - self.x_limit: self.v[0] = 0
        if self.rect.top + self.v[1] < 128: self.v[1] = 0

        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

        # SE FOR USAR ISSO DAQUI, TEM QUE TRAZER A DEFINIÇÃO DA POSIÇÃO PRA BAIXO DESSE BLOCO DE CÓDIGO
        # if self.v[0] >= 0:
        #     if self.hit_right_tile(self.v[0], tiles):
        #         self.v[0] = - self.v[0]
        #         self.pos[0] += self.v[0] 
        #     else:
        #         self.pos[0] += self.v[0]

        # else:
        #     if self.hit_left_tile(self.v[0], tiles):
        #         self.v[0] = - self.v[0]
        #         self.pos[0] += self.v[0] 
        #     else:
        #         self.pos[0] += self.v[0]

        




    def atack(self, player):
        self.timer -= 1
        if self.timer < 0: self.timer = self.recover_time
        if self.timer != 0: return
        if not self.in_shoot_distance(player): return

        self.get_tank_hit_tiles(player.level.tiles_group)

        SFX_E_B_SHOOT.play()
    
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False

        if player_in_left: player.enemy_particles.add(EnemyProjectile([self.pos[0], self.pos[1] - self.size * 0.9], [-self.p_speed,0], self.atk, self.hit_tiles))
        else: player.enemy_particles.add(EnemyProjectile([self.pos[0] + self.size, self.pos[1] - self.size * 0.9], [self.p_speed,0], self.atk, self.hit_tiles))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.move('nanado', player)
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()



# CLASSE (z) - OCUPUS ENORME<<- ->>
class MegaOctopus(Enemy):
    def __init__(self, pos, tiles):
        # INICIALIZAÇÂO
        self.v = [2, 0]
        self.size = 96
        self.max_hp = 20
        self.atk = 35
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos, tiles)

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_OCTOPUS, 0, self.size / 64)
        self.animation_speed = 0.3


    def move(self, tiles):
        if self.v[0] >= 0:
            if self.hit_right_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_right(self.v[0], tiles):
                    self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]

        else:
            if self.hit_left_tile(self.v[0], tiles):
                self.v[0] = - self.v[0]
                self.pos[0] += self.v[0] 
            elif self.fall_left(self.v[0], tiles):
                self.v[0] = - self.v[0]
                # self.pos[0] += self.v[0]
            else:
                self.pos[0] += self.v[0]
 

    # VERIFICA SE O PERSONAGEM DEVE SER APAGADO
    def life_check(self, player):
        if self.hp <= 0:
            for i in range(2):
                if i==0:
                    player.particles.add(BornSmoke([self.pos[0] + 0 + 64/2, self.pos[1] - 64/2]))
                    player.level.enemys_group.add(Octopus(self.pos, player.level.tiles_group, born_bg_pan = player.bg_pan))
                else:
                    player.particles.add(BornSmoke([self.pos[0] + 64 + 64/2, self.pos[1] - 64/2]))
                    player.level.enemys_group.add(Octopus([self.pos[0] + 64, self.pos[1]], player.level.tiles_group, born_bg_pan = player.bg_pan))
            # player.level.enemys_group.update(player)
            self.death_sound.play()           
            self.kill()


    def update(self,player):
        self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        if not self.in_render_distance(player): return
        self.life_check(player)
        self.animate()



# CLASSE (á) - BOLA X
class SpikeBall(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 35
        self.atk = 100
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        self.fragile_head = False
        self.spike_head = True
        self.bounce_protected = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SPIKE_BALL, 0, self.size / 64)
        self.animation_speed = 0.1


    def update(self, player):
        if not self.in_render_distance(player): return
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE (é) - BOMBA BOLA X
class BombSpikeBall30(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 30  # segundos que fica vivo
        self.fire_dmg = 1 / 50
        self.atk = 100
        self.loaded = False
        self.wick_SFX_timer = 10
        self.last_ignited = False
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        self.fragile_head = False
        self.spike_head = True
        self.bounce_protected = True
        self.explosion_protected = True
        self.laser_protected = True
        self.render_distance = 8 * 64

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 2], self.rect.bottomleft, self.max_hp, 'brown', 'black')

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BOMB_SPIKE_BALL, 0, self.size / 64)
        self.animation_speed = 0.1

    def ignite(self):
        if self.wick_SFX_timer == 10: SFX_E_WICK.play()  
        self.wick_SFX_timer -= self.fire_dmg
        if self.wick_SFX_timer < 0: self.wick_SFX_timer = 10
        if self.hp <= 3 and self.hp >= 2.9 and not self.last_ignited:
            SFX_E_LAST_WICK.play()
            self.last_ignited = True
        self.hp -= self.fire_dmg
        self.life_bar.update_pos(self.rect.bottomleft)
        self.life_bar.update_life(self.hp)


    def load(self):
        if self.loaded: return
        self.loaded = True
        SFX_E_WICK.set_volume(1)
        


    # VERIFICA SE O PERSONAGEM DEVE SER APAGADO
    def life_check(self, player):
        if self.hp <= 0:
            SFX_E_WICK.set_volume(0)
            SFX_E_EXPLOSION.play()           
            for i in range(200):
                player.enemy_particles.add(E_ExplosionProjectile([self.rect.centerx + 32 - player.bg_pan[0], self.rect.centery - 32 - player.bg_pan[1]]))
            self.kill()

            # enemy_particles

    def update(self, player):
        if self.loaded:
            self.ignite()
            self.life_check(player)
        if not self.in_render_distance(player): return
        self.load()
        self.pan_ajust(player.bg_pan)
        self.animate()



# CLASSE (í) - BOLHA DE DANO <<- ->>
class DamageBubble(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.timer = 0
        self.hit_animation_time = 32
        self.size = 64
        self.max_hp = 5
        self.atk = 2
        self.critical_atk = 5
        self.influence_radius = 232
        self.critical_radius = 128
        super().__init__(pos)
        # self.fragile_head = False
        # self.bounce_protected = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_D_BUBBLE, 0, self.size / 64)
        self.animation_speed = 0.1

        # INICIA A FUMAÇAMA
        self.smoke_on = False
        self.smoke = Smoke([self.pos[0] + self.size/2, self.pos[1] - self.size/2 ])


    def atack(self, player):
        player_distance = math.sqrt((player.rect.centerx  - self.smoke.rect.centerx)**2 + (player.rect.centery - self.smoke.rect.centery)**2)
        if player_distance <= self.critical_radius:
            if self.timer == 0 : player.get_hit(self.critical_atk)
            else: player.get_hit(self.atk, pop = False, ouch = False)
            self.timer += 1
            if self.timer >= self.hit_animation_time: self.timer = 0
        elif player_distance <= self.influence_radius:
            if self.timer == 0 : player.get_hit(self.atk)
            else: player.get_hit(self.atk, pop = False, ouch = False)
            self.timer += 1
            if self.timer >= self.hit_animation_time: self.timer = 0
        else: self.timer = 0

    def update(self, player):
        if not self.in_render_distance(player): return
        if not self.smoke_on:
            player.enemy_smoke.add(self.smoke)
            self.smoke_on = True
        # self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()
        self.smoke.update(player, self)



# CLASSE (ó) - BOLHA DE IMÃ <<- ->>
class MagnBubble(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.timer = 0
        self.hit_animation_time = 32
        self.size = 64  
        self.max_hp = 5
        self.atk = 20
        self.influence_radius = 256
        self.force = 10
        super().__init__(pos)
        self.fragile_head = False
        self.spike_head = True
        # self.bounce_protected = True

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_M_BUBBLE, 0, self.size / 64)
        self.animation_speed = 0.1

        # INICIA A FUMAÇAMA 
        self.smoke_on = False
        self.smoke = MagCircle([self.pos[0] + self.size/2, self.pos[1] - self.size/2 ])



    def atack(self, player):
        player_in_left = True
        if player.rect.centerx > self.rect.centerx: player_in_left = False
        player_distance = math.sqrt((player.rect.centerx  - self.smoke.rect.centerx)**2 + (player.rect.centery - self.smoke.rect.centery)**2)
        if player_distance <= self.influence_radius:
            if player_in_left: player.move_right(self.force, player.level.tiles_group.sprites())
            else: player.move_left(self.force, player.level.tiles_group.sprites())
            

    def update(self, player):
        if not self.in_render_distance(player): return
        if not self.smoke_on:
            player.enemy_smoke.add(self.smoke)
            self.smoke_on = True
        # self.move(player.level.tiles_group.sprites())
        self.pan_ajust(player.bg_pan)
        self.atack(player)
        self.life_check(player)
        self.animate()
        self.smoke.update(player, self)



# CLASSE (ú) - BOMBA BOLA X
class BombSpikeBall60(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 0
        self.time_moving = 64
        self.size = 64
        self.max_hp = 60  # segundos que fica vivo
        self.fire_dmg = 1 / 50
        self.atk = 100
        self.loaded = False
        self.wick_SFX_timer = 10
        self.last_ignited = False
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        self.fragile_head = False
        self.spike_head = True
        self.bounce_protected = True
        self.explosion_protected = True
        self.laser_protected = True
        self.render_distance = 0 * 64

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 2], self.rect.bottomleft, self.max_hp, 'brown', 'black')

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BOMB_SPIKE_BALL, 0, self.size / 64)
        self.animation_speed = 0.1

    def ignite(self):
        if self.wick_SFX_timer == 10: SFX_E_WICK.play()  
        self.wick_SFX_timer -= self.fire_dmg
        if self.wick_SFX_timer < 0: self.wick_SFX_timer = 10
        if self.hp <= 3 and self.hp >= 2.9 and not self.last_ignited:
            SFX_E_LAST_WICK.play()
            self.last_ignited = True
        self.hp -= self.fire_dmg
        self.life_bar.update_pos(self.rect.bottomleft)
        self.life_bar.update_life(self.hp)


    def load(self):
        if self.loaded: return
        self.loaded = True
        SFX_E_WICK.set_volume(1)
        


    # VERIFICA SE O PERSONAGEM DEVE SER APAGADO
    def life_check(self, player):
        if self.hp <= 0:
            SFX_E_WICK.set_volume(0)
            SFX_E_EXPLOSION.play()           
            for i in range(200):
                player.enemy_particles.add(E_ExplosionProjectile([self.rect.centerx + 32 - player.bg_pan[0], self.rect.centery - 32 - player.bg_pan[1]]))
            self.kill()

            # enemy_particles

    def update(self, player):
        if self.loaded:
            self.ignite()
            self.life_check(player)
        if not self.in_render_distance(player): return
        self.load()
        self.pan_ajust(player.bg_pan)
        self.animate()



# CLASSE (â) - Spawner de shootank
class ShootankSpawner(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 50 * 3
        self.loaded = False
        self.spawn_time = 50 * 10
        self.near_enemys_limit = 4
        self.enemys_per_spawn = 1
        self.spawn_influence = 64 * 8
        self.size = 128 * 2
        self.max_hp = 500
        self.atk = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')

        self.render_distance = 8 * 64
        self.harmless = True
        self.inert = True
        self.fragile_head = False
        # self.bounce_protected = True

        self.near_enemys = []

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_SPAWNER, 0, self.size / 128)
        self.animation_speed = 0.1

    def get_near_enemys(self, player):
        self.near_enemys = []
        for e in player.level.enemys_group:
            if self.pos[0] - e.pos[0] < self.spawn_influence and e.pos[0] - self.pos[0] < self.spawn_influence:
                self.near_enemys.append(e)


    def spawn(self, player):
        if self.timer < 0: self.timer = self.spawn_time
        else: self.timer -= 1

        if self.timer == 0 or self.timer == 50 * 2:
            self.get_near_enemys(player)
            if len(self.near_enemys) >= self.near_enemys_limit: return
            for i in range(self.enemys_per_spawn):
                SFX_E_BORN.play()
                player.particles.add(BornSmoke([self.pos[0] + 64 + 96/2, self.pos[1] - 96/2]))
                if i == 0: player.level.enemys_group.add(Shootank([self.pos[0] + 64, self.pos[1]], player.level.tiles_group, born_bg_pan = player.bg_pan))
                # else: player.level.enemys_group.add(Shootank([self.pos[0] + 128, self.pos[1]], player.level.tiles_group))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.spawn(player)
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE ("î") - Spawner de shootank avançado
class ShootankSpawnerBlue(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 50 * 5
        self.loaded = False
        self.spawn_time = 50 * 3
        self.near_enemys_limit = 3
        self.enemys_per_spawn = 1
        self.spawn_influence = 64 * 8
        self.size = 128 * 2
        self.max_hp = 500
        self.atk = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')

        self.render_distance = 5 * 64
        self.harmless = True
        self.inert = True
        self.fragile_head = False
        # self.bounce_protected = True

        self.near_enemys = []

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_BLUE_SPAWNER, 0, self.size / 128)
        self.animation_speed = 0.1

    def get_near_enemys(self, player):
        self.near_enemys = []
        for e in player.level.enemys_group:
            if self.pos[0] - e.pos[0] < self.spawn_influence and e.pos[0] - self.pos[0] < self.spawn_influence:
                self.near_enemys.append(e)


    def spawn(self, player):
        if self.timer < 0: self.timer = self.spawn_time
        else: self.timer -= 1

        if self.timer == 0:
            self.get_near_enemys(player)
            if len(self.near_enemys) >= self.near_enemys_limit: return
            for i in range(self.enemys_per_spawn):
                SFX_E_BORN.play()
                player.particles.add(BornSmoke([self.pos[0] + 64 + 96/2, self.pos[1] - 96/2 - 64]))
                if i == 0: player.level.enemys_group.add(Shootank3([self.pos[0] + 64, self.pos[1] - 64], player.level.tiles_group, born_bg_pan = player.bg_pan))
                # else: player.level.enemys_group.add(Shootank([self.pos[0] + 128, self.pos[1]], player.level.tiles_group))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.spawn(player)
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE (ê) - Spawner de octopus elétricos
class EletricOctopusSpawner(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 1
        self.loaded = False
        self.spawn_time = 50 * 4
        self.near_enemys_limit = 10
        self.enemys_per_spawn = 1
        self.spawn_influence = 64 * 8
        self.size = 128 * 1
        self.max_hp = 500
        self.atk = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')


        self.harmless = True
        self.inert = True
        self.fragile_head = False
        # self.bounce_protected = True

        self.near_enemys = []

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_GREEN_SPAWNER, 0, self.size / 128)
        self.animation_speed = 0.1

    def get_near_enemys(self, player):
        self.near_enemys = []
        for e in player.level.enemys_group:
            if self.pos[0] - e.pos[0] < self.spawn_influence and e.pos[0] - self.pos[0] < self.spawn_influence:
                self.near_enemys.append(e)


    def spawn(self, player):
        if self.timer < 0: self.timer = self.spawn_time
        else: self.timer -= 1

        if self.timer == 0:
            self.get_near_enemys(player)
            if len(self.near_enemys) >= self.near_enemys_limit: return
            for i in range(self.enemys_per_spawn):
                SFX_E_BORN.play()
                player.particles.add(BornSmoke([self.pos[0] + 32 + 64/2, self.pos[1] - 64/2]))
                player.level.enemys_group.add(EletricOctopus([self.pos[0] + 32 , self.pos[1]], player.level.tiles_group, born_bg_pan = player.bg_pan))
            player.level.enemys_group.update(player)


    def update(self, player):
        if not self.in_render_distance(player): return
        self.spawn(player)
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE (ô) - Spawner de octopus
class OctopusSpawner(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 1
        self.loaded = False
        self.spawn_time = 50 * 4
        self.near_enemys_limit = 7
        self.enemys_per_spawn = 2
        self.spawn_influence = 64 * 8
        self.size = 128 * 1.5
        self.max_hp = 500
        self.atk = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')

        self.harmless = True
        self.inert = True
        self.fragile_head = False
        # self.bounce_protected = True

        self.near_enemys = []

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_PURPLE_SPAWNER, 0, self.size / 128)
        self.animation_speed = 0.1

    def get_near_enemys(self, player):
        self.near_enemys = []
        for e in player.level.enemys_group:
            if self.pos[0] - e.pos[0] < self.spawn_influence and e.pos[0] - self.pos[0] < self.spawn_influence:
                self.near_enemys.append(e)


    def spawn(self, player):
        if self.timer < 0: self.timer = self.spawn_time
        else: self.timer -= 1

        if self.timer == 0 or self.timer == 50 * 1:
            self.get_near_enemys(player)
            if len(self.near_enemys) >= self.near_enemys_limit: return
            for i in range(self.enemys_per_spawn):
                SFX_E_BORN.play()
                player.particles.add(BornSmoke([self.pos[0] + 32 + 64/2, self.pos[1] - 64/2]))
                # player.level.enemys_group.add(Octopus(0, 0], tiles = self.tiles_group))
                if i == 0:player.level.enemys_group.add(Octopus([self.pos[0] + 32, self.pos[1]], tiles = player.level.tiles_group, born_bg_pan = player.bg_pan))
                # else: player.level.enemys_group.add(Octopus([self.pos[0] + 96 , self.pos[1]], player.level.tiles_group))
            player.level.enemys_group.update(player)


    def update(self, player):
        if not self.in_render_distance(player): return
        self.spawn(player)
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()



# CLASSE ("û") - Spawner de shootank avançado
class ShootankSpawnerRed(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.v = [0, 0]
        self.timer = 50 * 3
        self.loaded = False
        self.spawn_time = 50 * 3
        self.near_enemys_limit = 6
        self.enemys_per_spawn = 1
        self.spawn_influence = 64 * 8
        self.size = 128 * 2
        self.max_hp = 500
        self.atk = 0
        # self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']
        # self.colors = ['blue', 'red', 'black']
        super().__init__(pos)

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([self.size, 0], self.rect.bottomleft, self.max_hp, 'brown', 'green')

        self.render_distance = 5 * 64
        self.harmless = True
        self.inert = True
        self.fragile_head = False
        # self.bounce_protected = True

        self.near_enemys = []

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_RED_SPAWNER, 0, self.size / 128)
        self.animation_speed = 0.1

    def get_near_enemys(self, player):
        self.near_enemys = []
        for e in player.level.enemys_group:
            if self.pos[0] - e.pos[0] < self.spawn_influence and e.pos[0] - self.pos[0] < self.spawn_influence:
                self.near_enemys.append(e)


    def spawn(self, player):
        if self.timer < 0: self.timer = self.spawn_time
        else: self.timer -= 1

        if self.timer == 0:
            self.get_near_enemys(player)
            if len(self.near_enemys) >= self.near_enemys_limit: return
            for i in range(self.enemys_per_spawn):
                SFX_E_BORN.play()
                player.particles.add(BornSmoke([self.pos[0] + 64 + 96/2, self.pos[1] - 96/2]))
                if i == 0: player.level.enemys_group.add(Shootank4([self.pos[0] + 64, self.pos[1]], player.level.tiles_group, born_bg_pan = player.bg_pan))
                # else: player.level.enemys_group.add(Shootank([self.pos[0] + 128, self.pos[1]], player.level.tiles_group))


    def update(self, player):
        if not self.in_render_distance(player): return
        self.spawn(player)
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()