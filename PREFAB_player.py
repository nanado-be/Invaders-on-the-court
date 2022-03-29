# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from CONFIG_game import *
from GAME_functions import *
from PREFAB_enemy import *
from ASSETS_player import *
from ASSETS_others import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import math
import random
import pygame
pygame.init()


# CLASSE DO PERSONAGEM DO JOGADOR
class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        # INICIALIZAÇÂO
        self.level = level

        # CAMERA
        self.screen_w = GAME_SCREEN_W
        self.screen_h = GAME_SCREEN_H
        self.bg_pan = [0,0]
        self.screen_treshold = 64 * 8

        # BASICO
        self.origin = (self.screen_treshold, 32)
        self.width = 64
        self.height = 128
        self.game_on = True
        self.stage_clear = False
        self.score = 0
        self.time = 0
        self.edit_mode = False
        self.won = False
        self.victory_count = 25


        self.coins_collecteds = 0
        # APARENCIA
        self.color = SALMON
        self.colors = ['yellow', 'red', 'brown']

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.width, self.height))
        # self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft = self.origin)
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)     

        self.import_images()
        
        # PROPRIEDADES DE MOVIMENTAÇÃO
        self.duck_speed = 2
        self.ground_speed = 5 
        self.air_speed = 6
        self.vy = 0 
        self.g = 1 
        self.impulse = -18
        self.second_impulse = -15
        self.enemy_bounce = -15

        # ESTADO DE MOVIMENTAÇÃO
        self.move_state = 'falling'
        self.facing_right = True
        self.walk_locked = False
        self.on_air = True
        self.jump_locked = False
        self.double_jumping = False
        self.ducked = False
        self.lock_ducked = False
        self.lock_ducked_time = 0
        self.action = 'none'
        self.on_action = False # VERDADEIRO PARA QUANDO O PERSONAGEM ESTÁ EXECUTANDO UMA AÇÃO NÃO CANCELAVEL
        self.action_time = 0
        self.action_recovery_time = 0
        self.special_frame_ajusted = False

        # PROPRIEDADES DE COMBATE
        self.max_hp = 100
        self.hp = 100
        self.heart_hp_restore = 100
        self.invencible = False
        self.invenvible_frames = 20
        self.invencible_timer = 0
        self.jump_atk = 20
        self.jump_combo = 0
        self.score_jump_atk = 2
        self.bomb_ball_p_atk = 2
        self.ball_on_bag = True
        self.bounce_ball_atk = 50
        self.critical_bounce = 2.5
        self.score_per_bounce = 2
        self.energy_ball_atk = 2
        self.initial_bombs_on_bag = 0
        self.bombs_on_bag = self.initial_bombs_on_bag
        self.bombs_refill = 5
        self.laser_dmg = 100
        self.laser_refill = 50
        self.laser_consume = 2
        self.score_per_kill = 25
        self.auto_heal = False
        self.coin_score = 1
        self.mega_coin_score = 200
        self.god_mode = False
        self.god_mode_fuel = 0 
        self.laser_fuel = 0 

        # GRUPOS DAS SPRITES SECUNDÁRIAS DO PERSONAGEM
        self.bomb_balls = pygame.sprite.GroupSingle()
        self.explosion_projectiles = pygame.sprite.Group()
        self.bounce_balls = pygame.sprite.GroupSingle()
        self.lasers = pygame.sprite.Group()
        self.god_mode_energy = pygame.sprite.GroupSingle()
        self.enemy_particles = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.enemy_smoke = pygame.sprite.Group()

        # BARRA DE VIDA DO PERSONAGEM
        self.life_bar = LifeBar([199, 9], [51, 56], self.max_hp, 'brown', 'green')

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_fps = 60
        self.animation_frames = self.jump_animation_r
        self.current_animation_frame = 0
        self.animation_speed = 0.2
        self.sfx = 'none'
        self.playing_sfx = False


        # TOCA A MUSICA DO JOGO

    # *******************************************************************************
    # FUNÇÕES DE UTILIDADE INTERNA
    # *******************************************************************************

    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        ### COM A BOLA ###
        self.run_animation_r     = convert_animation_imgs(ANIMATION_RUN_R, 0, 1)
        self.run_animation_l     = convert_animation_imgs(ANIMATION_RUN_L, 0, 1)
        self.idle_animation_r    = convert_animation_imgs(ANIMATION_IDLE_R, 0, 1)
        self.idle_animation_l    = convert_animation_imgs(ANIMATION_IDLE_L, 0, 1)
        self.jump_animation_r    = convert_animation_imgs(ANIMATION_JUMP_R, 0, 1)
        self.jump_animation_l    = convert_animation_imgs(ANIMATION_JUMP_L, 0, 1)
        self.fall_animation_r    = convert_animation_imgs(ANIMATION_FALL_R, 0, 1)
        self.fall_animation_l    = convert_animation_imgs(ANIMATION_FALL_L, 0, 1)
        self.shoot_animation_r   = convert_animation_imgs(ANIMATION_SHOOT_R, 0, 1)
        self.shoot_animation_l   = convert_animation_imgs(ANIMATION_SHOOT_L, 0, 1)
        self.slide_animation_r   = convert_animation_imgs(ANIMATION_SLIDE_R, 0, 1)
        self.slide_animation_l   = convert_animation_imgs(ANIMATION_SLIDE_L, 0, 1)
        self.duck_animation_r      = convert_animation_imgs(ANIMATION_DUCK_R, 0, 1)
        self.duck_animation_l      = convert_animation_imgs(ANIMATION_DUCK_L, 0, 1)
        self.energy_animation_r  = convert_animation_imgs(ANIMATION_ENERGY_R, 0, 1)
        self.energy_animation_l  = convert_animation_imgs(ANIMATION_ENERGY_L, 0, 1)
        self.pass_animation_r    = convert_animation_imgs(ANIMATION_THROW_LOW_R, 0, 1)
        self.pass_animation_l    = convert_animation_imgs(ANIMATION_THROW_LOW_L, 0, 1)
        self.bomb_animation_r    = convert_animation_imgs(ANIMATION_THROW_BOMB_R, 0, 1)
        self.bomb_animation_l    = convert_animation_imgs(ANIMATION_THROW_BOMB_L, 0, 1)
        self.throw_animation_r   = convert_animation_imgs(ANIMATION_THROW_HIGH_R, 0, 1)
        self.throw_animation_l   = convert_animation_imgs(ANIMATION_THROW_HIGH_L, 0, 1)
        self.duck_walk_animation_r = convert_animation_imgs(ANIMATION_DUCK_WALK_R, 0, 1)
        self.duck_walk_animation_l = convert_animation_imgs(ANIMATION_DUCK_WALK_L, 0, 1)
        self.duck_shoot_animation_r = convert_animation_imgs(ANIMATION_DUCK_SHOOT_R, 0, 1)
        self.duck_shoot_animation_l = convert_animation_imgs(ANIMATION_DUCK_SHOOT_L, 0, 1)
        self.jump_n_run_animation_r   = convert_animation_imgs(ANIMATION_JUMP_N_SHOOT_R, 0, 1)
        self.jump_n_run_animation_l   = convert_animation_imgs(ANIMATION_JUMP_N_SHOOT_L, 0, 1)
        self.shoot_n_run_animation_r   = convert_animation_imgs(ANIMATION_SHOOT_N_RUN_R, 0, 1)
        self.shoot_n_run_animation_l   = convert_animation_imgs(ANIMATION_SHOOT_N_RUN_L, 0, 1)
        ### SEM A BOLA ###
        self.no_ball_run_animation_r     = convert_animation_imgs(ANIMATION_RUN_NB_R, 0, 1)
        self.no_ball_run_animation_l     = convert_animation_imgs(ANIMATION_RUN_NB_L, 0, 1)
        self.no_ball_idle_animation_r    = convert_animation_imgs(ANIMATION_IDLE_NB_R, 0, 1)
        self.no_ball_idle_animation_l    = convert_animation_imgs(ANIMATION_IDLE_NB_L, 0, 1)
        self.no_ball_jump_animation_r    = convert_animation_imgs(ANIMATION_JUMP_NB_R, 0, 1)
        self.no_ball_jump_animation_l    = convert_animation_imgs(ANIMATION_JUMP_NB_L, 0, 1)
        self.no_ball_fall_animation_r    = convert_animation_imgs(ANIMATION_FALL_NB_R, 0, 1)
        self.no_ball_fall_animation_l    = convert_animation_imgs(ANIMATION_FALL_NB_L, 0, 1)
        self.no_ball_shoot_animation_r   = convert_animation_imgs(ANIMATION_SHOOT_NB_R, 0, 1)
        self.no_ball_shoot_animation_l   = convert_animation_imgs(ANIMATION_SHOOT_NB_L, 0, 1)
        self.no_ball_slide_animation_r   = convert_animation_imgs(ANIMATION_SLIDE_NB_R, 0, 1)
        self.no_ball_slide_animation_l   = convert_animation_imgs(ANIMATION_SLIDE_NB_L, 0, 1)
        self.no_ball_duck_animation_r      = convert_animation_imgs(ANIMATION_DUCK_NB_R, 0, 1)
        self.no_ball_duck_animation_l      = convert_animation_imgs(ANIMATION_DUCK_NB_L, 0, 1)
        self.no_ball_energy_animation_r  = convert_animation_imgs(ANIMATION_ENERGY_NB_R, 0, 1)
        self.no_ball_energy_animation_l  = convert_animation_imgs(ANIMATION_ENERGY_NB_L, 0, 1)
        self.no_ball_pass_animation_r    = convert_animation_imgs(ANIMATION_THROW_LOW_NB_R, 0, 1)
        self.no_ball_pass_animation_l    = convert_animation_imgs(ANIMATION_THROW_LOW_NB_L, 0, 1)
        self.no_ball_bomb_animation_r    = convert_animation_imgs(ANIMATION_THROW_BOMB_NB_R, 0, 1)
        self.no_ball_bomb_animation_l    = convert_animation_imgs(ANIMATION_THROW_BOMB_NB_L, 0, 1)
        self.no_ball_throw_animation_r   = convert_animation_imgs(ANIMATION_THROW_HIGH_NB_R, 0, 1)
        self.no_ball_throw_animation_l   = convert_animation_imgs(ANIMATION_THROW_HIGH_NB_L, 0, 1)
        self.no_ball_duck_walk_animation_r = convert_animation_imgs(ANIMATION_DUCK_WALK_NB_R, 0, 1)
        self.no_ball_duck_walk_animation_l = convert_animation_imgs(ANIMATION_DUCK_WALK_NB_L, 0, 1)
        self.no_ball_duck_shoot_animation_r = convert_animation_imgs(ANIMATION_DUCK_SHOOT_NB_R, 0, 1)
        self.no_ball_duck_shoot_animation_l = convert_animation_imgs(ANIMATION_DUCK_SHOOT_NB_L, 0, 1)
        self.no_ball_jump_n_run_animation_r   = convert_animation_imgs(ANIMATION_JUMP_N_SHOOT_NB_R, 0, 1)
        self.no_ball_jump_n_run_animation_l   = convert_animation_imgs(ANIMATION_JUMP_N_SHOOT_NB_L, 0, 1)
        self.no_ball_shoot_n_run_animation_r   = convert_animation_imgs(ANIMATION_SHOOT_N_RUN_NB_R, 0, 1)
        self.no_ball_shoot_n_run_animation_l   = convert_animation_imgs(ANIMATION_SHOOT_N_RUN_NB_L, 0, 1)
       

    # ATUALIZA AS INFORMAÇÕES NECESSÁRIAS QUANDO MUDAR AS DIMENSÕES DA TELA
    def update_window_info(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.level.update_window_info(screen_w, screen_h)


    # MOVE O PERSONAGEM PRA DIREITA SE FOR POSSÍVEL (SYSTEM)
    def move_right(self, distance, tiles):
        # VERIFICA SE AO MOVIMENTAR NÃO BATERÁ EM UMA PAREDE
        # for tile in tiles:
        #     if tile.rect.right > -100 and tile.rect.left < self.screen_w + 100:
        #         if tile.rect.collidepoint((self.rect.bottomright[0] + distance, self.rect.bottomright[1] -1)) or tile.rect.collidepoint((self.rect.midright[0] + distance, self.rect.midright[1])) or tile.rect.collidepoint((self.rect.topright[0] + distance, self.rect.topright[1])):
        #             self.rect.right = tile.rect.left - 1
        #             return False
        self.rect.x += distance
        colliding_tiles = pygame.sprite.spritecollide(self, self.level.tiles_group, False)
        for tile in colliding_tiles:
            self.rect.right = tile.rect.left -1
            return False
        self.rect.x -= distance


        # MOVE O PERSONAGEM PARA A DIREITA, SE ELE NÃO VAI ALCANÇAR O LIMITE DA TELA + TH
        if self.rect.right + distance < self.screen_w - self.screen_treshold:
            self.rect.x += distance
        # MOVE O BG PARA A ESQUERDA SE AINDA EXISTE BG POR VIR
        elif self.bg_pan[0] - distance >= -self.level.width + self.screen_w:
            self.rect.right = self.screen_w - self.screen_treshold
            self.bg_pan[0] -= distance
        # MOVE O PERSONAGEM PARA A DIREITA SE O BG JÁ FOI TOD0 PERCORRIDO E AINDA HÁ ESPAÇO
        elif self.rect.right + distance < self.screen_w - GAME_SCREEN_MARGIN:
            #self.bg_pan[0] = -self.level.width + self.screen_
            self.rect.x += distance
        # COLOCA O PERSONAGEM NO FIM DA TELA + MARGEM
        else:
            #self.bg_pan[0] = -self.level.width + self.screen_
            self.rect.right = self.screen_w - GAME_SCREEN_MARGIN
        return True
             
    
    # MOVE O PERSONAGEM PRA ESQUERDA SE FOR POSSÍVEL (SYSTEM)
    def move_left(self, distance, tiles):
        # for tile in tiles:
        #     if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
        #         if tile.rect.collidepoint((self.rect.bottomleft[0] - distance, self.rect.bottomleft[1] -1)) or tile.rect.collidepoint((self.rect.midleft[0] - distance, self.rect.midright[1])) or tile.rect.collidepoint((self.rect.topright[0] - distance, self.rect.topright[1])):
        #             self.rect.left = tile.rect.right + 1
        #             return False
        self.rect.x -= distance
        colliding_tiles = pygame.sprite.spritecollide(self, self.level.tiles_group, False)
        for tile in colliding_tiles:
            self.rect.left = tile.rect.right + 1
            return False
        self.rect.x += distance

        # MOVE O PERSONAGEM PARA A ESQUERDA, SE ELE NÃO VAI ALCANÇAR O LIMITE DA TELA + TH
        if self.rect.left - distance > 0 + self.screen_treshold:
            self.rect.x -= distance
        # MOVE O BG PARA A DIREITA SE AINDA EXISTE BG POR VIR
        elif self.bg_pan[0] + distance <= 0:
            self.rect.left = 0 + self.screen_treshold
            self.bg_pan[0] += distance
        # MOVE O PERSONAGEM PARA A ESQUERDA SE O BG JÁ FOI TOD0 PERCORRIDO E AINDA HÁ ESPAÇO
        elif self.rect.left - distance > 0 + GAME_SCREEN_MARGIN:
            #self.bg_pan[0] = 0
            self.rect.x -= distance
        # COLOCA O PERSONAGEM NO INÍCIO DA TELA + MARGEM
        else:
            #self.bg_pan[0] = 0
            self.rect.left = 0 + GAME_SCREEN_MARGIN
        return True


    # REDEFINE O PERSONAGEM DO ZERO
    def reset(self):
        self.move_state = 'falling'
        self.on_air = True
        self.double_jumping = False
        self.rect.update(self.origin, (self.width, self.height))
        self.vy = 0
        self.hp = self.max_hp
        self.life_bar.update_life(self.hp)
        self.bg_pan = [0,0]
        self.level.get_tiles_map()
        self.level.get_enemys_map()
        self.level.get_collectables_map()
        self.ball_on_bag = True
        self.bombs_on_bag = self.initial_bombs_on_bag
        self.laser_fuel = 0 
        self.god_mode_fuel = 0 
        self.score = 0
        self.time  = 0
        self.coins_collecteds = 0
        self.bounce_balls.empty()
        self.enemy_smoke.empty()
        self.enemy_particles.empty()
        SFX_RESTART.play()


    # ARREMESSA UMA BOLA BOMBA QUE SEGUE UM CAMINHO DE PARÁBOLA, SOME AO SAIR DA TELA
    def use_bomb_ball(self, vx, vy):
        g = 1
        n_projectiles = 3
        original_pos = [self.rect.centerx - self.bg_pan[0], self.rect.centery - self.bg_pan[1]]
        recovery_frames = 30
        ball_animation_speed = 0.20
        ball_size = 42
        if self.facing_right: distance_per_frame = [vx, vy]
        else: distance_per_frame = [-vx, vy]

        self.bomb_balls.add(BombBall(original_pos, ball_size / 32 , distance_per_frame, g, n_projectiles, ball_animation_speed, self.screen_w, self.screen_h))
        SFX_BALL_THROW.play()
        # self.action_recovery_time = recovery_frames


    # ARREMESSA UMA BOLA BOMBA QUE QUICA NAS PAREDES, SOME AO SAIR VOLTAR PRO JOGADOR
    def use_bounce_ball(self, v):
        vx = v[0]
        vy = v[1]
        player_vy_influence = 1
        g = 0.5
        elastic_bounce =[1, 0.97]
        return_radius = 1 * 128
        original_pos = [self.rect.centerx - self.bg_pan[0], self.rect.centery - self.bg_pan[1]]
        recovery_frames = 50
        ball_animation_speed = 0.34
        ball_size = 42
        if self.facing_right: distance_per_frame = [vx, player_vy_influence * self.vy + vy]
        else: distance_per_frame = [-vx, player_vy_influence * self.vy + vy]

        self.bounce_balls.add(BouncingBall(original_pos, ball_size / 32, distance_per_frame, g, elastic_bounce, return_radius, ball_animation_speed,  self.screen_w, self.screen_h))
        SFX_BALL_THROW.play()
        # self.action_recovery_time = recovery_frames


    # TIRO BOLADO
    def use_laser_gun(self, y_ajust):
        if self.laser_fuel <= 0:
            self.laser_fuel = 0 
            SFX_NO_BOMB.play()
            return
        v = [15, 0]
        if self.facing_right: original_pos = [self.rect.centerx - self.bg_pan[0] + 32, self.rect.centery - self.bg_pan[1] + y_ajust]
        else: original_pos = [self.rect.centerx - self.bg_pan[0] - 32, self.rect.centery - self.bg_pan[1] + y_ajust]
        recovery_frames = 12
        if self.facing_right: v = [25, 0]
        else: v = [-25, 0]

        self.lasers.add(Laser(original_pos, v))
        SFX_LASER.play()
        # self.action_recovery_time = recovery_frames
        self.laser_fuel -= self.laser_consume


    # CAUSA A EXPLOSÃO DA BOMB BALL
    def bomb_ball_explode(self, pos):
        self.explosion_projectiles.empty()
        SFX_BALL_EXPLODE.play()
        for i in range(200):
            # self.explosion_projectiles.add(ExplosionProjectile(5, [pos[0], pos[1]]))
            self.explosion_projectiles.add(ExplosionProjectile([pos[0]-self.bg_pan[0], pos[1]-self.bg_pan[1]]))


    # RECEBE DANO E ATUALIZA O QUE FOR NESCESSÁRIO
    def get_hit(self, damage, pop = True, n_particles = 50, ouch = True):
        self.hp -= damage
        # self.life_bar.update_pos(self.rect.bottomleft)
        self.life_bar.update_life(self.hp)
        if ouch: SFX_DAMAGE.play()
        if not pop: return
        self.particles.add(PlayerHurt([-self.bg_pan[0] + self.rect[0] + self.width / 2, -self.bg_pan[1] + self.rect[1] + self.height / 2]))
        # for i in range (n_particles):
        #     self.particles.add(ExplosionParticle([-self.bg_pan[0] + self.rect[0] + self.width / 2, -self.bg_pan[1] + self.rect[1] + self.height / 2], 2, 4, 5, 10, 64, self.colors))

    
    # FASE CONCLUÍDA
    def victory(self):
        if not self.won:
            self.won = True
            SFX_VICTORY1.play()
        else:
            if self.victory_count >= 0:
                self.victory_count -= 1
                self.walk_right(self.ground_speed)
                self.move_state = 'on action'
                self.action = 'sliding'
            else:
                SFX_VICTORY2.play()
                if self.level.id == 16: self.coins_collecteds = 3
                self.game_on = False
                self.stage_clear = True

    # *******************************************************************************
    # HABILIDADES DO PERSONAGEM
    # *******************************************************************************

    # CORRE PARA A DIREITA (SKILL)
    def walk_right(self, tiles):
        self.facing_right = True 

        if self.walk_locked and not self.on_air: return

        # if self.action == 'sliding': return   

        # if self.on_action and not self.on_air and self.action != 'shooting and running': return
        
        if self.on_air: self.move_right(self.air_speed, tiles)
        elif self.lock_ducked:
            if self.lock_ducked_time < 5: return
            self.move_right(self.duck_speed, tiles)
            self.move_state = 'duck walk'
        else: 
            if self.ducked: return
            self.move_right(self.ground_speed, tiles)        
            if self.action != 'shooting and running': self.move_state = 'runnig'


    # CORRER PARA A ESQUERDA (SKILL)
    def walk_left(self, tiles):   
        self.facing_right = False

        if self.walk_locked and not self.on_air: return

        # if self.action == 'sliding': return  

        # if self.on_action and not self.on_air and self.action != 'shooting and running': return

        if self.on_air: self.move_left(self.air_speed, tiles)
        elif self.lock_ducked:
            if self.lock_ducked_time < 5: return
            self.move_left(self.duck_speed, tiles)
            self.move_state = 'duck walk'
        else: 
            if self.ducked: return
            self.move_left(self.ground_speed, tiles)    
            if self.action != 'shooting and running': self.move_state = 'runnig'
            # if not self.on_action: self.move_state = 'runnig'
        

    # ABAIXA (SKILL)
    def duck(self):
        # if not self.move_state == 'idle': return
        self.ducked = True  
        self.move_state = 'duking'  


    # EXECUTA O PULO(SKILL)
    def jump(self, tiles):
        # if self.on_action: return
        if self.jump_locked: return
        if self.on_air: return
        if self.lock_ducked: return

        for tile in tiles:
            if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                if tile.rect.collidepoint((self.rect.topleft[0], self.rect.topleft[1] + self.impulse)) or tile.rect.collidepoint((self.rect.midtop[0], self.rect.midtop[1] + self.impulse)) or tile.rect.collidepoint((self.rect.topright[0], self.rect.topright[1] + self.impulse)):
                    # if self.vy >self.g + 1: SFX_LANDING.play()
                    self.vy = 0
                    self.rect.top = tile.rect.bottom
                    self.double_jumping = True
                    return

        self.on_air = True
        self.vy = self.impulse
        SFX_JUMP.play()
        # if not self.on_action: self.move_state = 'jumping'
        # self.action_recovery_time = 10

    
    # EXECUTA O PULO SECUNDÁRIO
    def second_jump(self):
        if self.vy < -self.second_impulse * 0.5: return
        if self.double_jumping: return
        # if self.action_recovery_time >0 : return

        self.vy = self.second_impulse
        SFX_S_JUMP.play()
        self.double_jumping = True
        # if not self.on_action: self.move_state = 'jumping'


    # DÁ UM DASH NA DIREÇÃO QUE ESTÁ VIRADO
    def slide(self, tiles):
        distance_per_frame_ground = 6
        distance_per_frame_air = 6
        action_frames = int(len(self.slide_animation_r) / self.animation_speed)
        recovery_frames = 6

        self.walk_locked = True
        self.jump_locked = True

        
        if self.on_action:
            if self.action != 'sliding': return
            
            if self.on_air: distance_per_frame = distance_per_frame_air
            else: distance_per_frame = distance_per_frame_ground

            self.move_state = 'on action'
            self.action = 'sliding'
            if self.facing_right: self.move_right(distance_per_frame, tiles)
            else: self.move_left(distance_per_frame, tiles)
            # SFX_SLIDE.play()
            
        else:
            if self.action_recovery_time > 0: return
            if self.on_air: return
            if not self.lock_ducked and self.ducked: return
            self.on_action = True
            self.move_state = 'on action'
            self.action = 'sliding'
            self.action_time = action_frames
            self.action_recovery_time = self.action_time + recovery_frames
            self.current_animation_frame = 0 
            SFX_SLIDE.play()


    # USA A HABILIDADE BOUCE BALL
    def throw_bouncing_ball(self):
        # action_frames = len(self.throw_animation_r) * 1 / self.animation_speed
        action_frames = 6 * 1 / self.animation_speed
        recovery_frames = 0
        hability_frame = 3 # começa no 0


        if not self.on_action:
            # if self.action_recovery_time > 0: return
            if self.lock_ducked: return
            if not self.ball_on_bag: return  # ---- SÓ VOU USAR SE A BOUNCE BALL FOR ÚNICA
            self.jump_locked = True
            self.walk_locked = True
            self.on_action = True
            self.move_state = 'on action'
            self.action_time = action_frames
            # self.action_recovery_time = self.action_time + recovery_frames
            self.current_animation_frame = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:self.action = 'throwing'
            else:self.action = 'passing'


        else:
            if self.action != 'passing' and self.action != 'throwing': return

            self.jump_locked = True
            self.walk_locked = True

            self.move_state = 'on action'
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:self.action = 'throwing'
            else:self.action = 'passing'

            # HABILIDADE MESMO
            if action_frames - self.action_time == hability_frame * 1 / self.animation_speed:
                self.ball_on_bag = False
                if keys[pygame.K_UP]: self.use_bounce_ball([10, -15])
                elif keys[pygame.K_DOWN]: self.use_bounce_ball([10, 0])
                else: self.use_bounce_ball([15, -7])
         # FIM DA HABILIDADE


    # USA A HABILIDADE BOMB BALL
    def bomb_ball_hability(self):
        action_frames = len(self.bomb_animation_r) * 1 / self.animation_speed
        recovery_frames = 0
        hability_frame = 3 # começa no 0

        self.walk_locked = True
        self.jump_locked = True

        if not self.on_action:
            # if self.action_recovery_time > 0: return
            if self.lock_ducked: return
            if not self.bombs_on_bag: return
            self.on_action = True
            self.jump_locked = True
            self.walk_locked = True
            self.move_state = 'on action'
            self.action = 'bombing'
            self.action_time = action_frames
            # self.action_recovery_time = self.action_time + recovery_frames
            self.current_animation_frame = 0


        else:
  
            if self.action != 'bombing': return

            self.jump_locked = True
            self.walk_locked = True


            self.move_state = 'on action'
            self.action = 'bombing'
            # HABILIDADE MESMO
            keys = pygame.key.get_pressed()
            if self.bombs_on_bag <= 0:
                SFX_NO_BOMB.play()
                return
            if action_frames - self.action_time == hability_frame * 1 / self.animation_speed:
                self.bombs_on_bag -= 1
                # if keys[pygame.K_UP]: self.use_bomb_ball(2, -20.5)
                if keys[pygame.K_DOWN]: self.use_bomb_ball(2, -20.5)
                else:self.use_bomb_ball(10, -18)
        # FIM DA HABILIDADE


    # USA A HABILIDADE
    def laser_shoot(self):
        action_frames = len(self.shoot_animation_r) * 1 / self.animation_speed
        recovery_frames = 0
        hability_frame = 2 # começa no 0

        self.walk_locked = False
        

        if not self.on_action:
            if self.lock_ducked: return
            # if self.action_recovery_time > 0: return
            self.on_action = True
            self.move_state = 'on action'
            keys = pygame.key.get_pressed()
            if self.on_air: self.action = 'shooting on air'
            elif keys[pygame.K_DOWN]:
                self.action = 'duck shooting'
                self.walk_locked = True
            elif keys[pygame.K_RIGHT]: self.action = 'shooting and running'
            elif keys[pygame.K_LEFT]: self.action = 'shooting and running'
            else: self.action = 'shooting'
            self.action_time = action_frames
            # self.action_recovery_time = self.action_time + recovery_frames
            self.current_animation_frame = 0


        else:
            if self.action != 'shooting' and self.action != 'shooting and running' and self.action != 'shooting on air' and self.action != 'duck shooting': return

            keys = pygame.key.get_pressed()


            self.move_state = 'on action'

            # self.on_action = True
            # HABILIDADE MESMO
            if self.on_air:
                self.action = 'shooting on air'
                if action_frames - self.action_time == hability_frame * 1 / self.animation_speed: self.use_laser_gun(1)
            elif keys[pygame.K_DOWN]:
                self.action = 'duck shooting'
                self.walk_locked = True
                if action_frames - self.action_time == hability_frame * 1 / self.animation_speed: self.use_laser_gun(0)
            elif keys[pygame.K_RIGHT]:
                self.action = 'shooting and running'
                if action_frames - self.action_time == hability_frame * 1 / self.animation_speed: self.use_laser_gun(3)
            elif keys[pygame.K_LEFT]:
                self.action = 'shooting and running'
                if action_frames - self.action_time == hability_frame * 1 / self.animation_speed: self.use_laser_gun(3)
            else:
                self.action = 'shooting'
                if action_frames - self.action_time == hability_frame * 1 / self.animation_speed: self.use_laser_gun(-3)
            # FIM DA HABILIDADE


    # USA A HABILIDADE STEROID
    def use_steroid(self):
        if self.god_mode_fuel >= 0:
            self.god_mode = True
            self.god_mode_energy.add(GodModeEnegy(self))


    # *******************************************************************************
    # FUNÇÕES QUE RODAM A CADA FRAME
    # *******************************************************************************


    def update_fps(self, fps):
        try: fps_factor = 60 / fps
        except: fps_factor = 1

        # PROPRIEDADES DE MOVIMENTAÇÃO
        self.duck_speed = self.o_duck_speed * fps_factor
        self.ground_speed = self.o_ground_speed * fps_factor
        self.air_speed = self.o_air_speed * fps_factor
        self.g = self.o_g * fps_factor 
        self.impulse = self.o_impulse * fps_factor
        self.second_impulse = self.o_second_impulse * fps_factor
        self.enemy_bounce = self.o_enemy_bounce * fps_factor


    # VERIFICA SE A VIDA AINDA É MAIOR QUE ZERO
    def check_life(self):
        if self.hp <= 0: self.reset()
        if self.rect.bottom + self.vy > self.level.kill_height:
            SFX_HOLE.play()
            self.reset()


    #  VERIFICA SE A FASE FOI CONCLUIDA
    def victory_check(self):
        if self.level.id == 16 and self.level.enemys_group.sprites() != []: return
        if self.rect.right - self.bg_pan[0] >= self.level.victory_point: self.victory()


    # CONTROLA A QUEDA DO PERSONAGEM e bater a caça
    def fall(self, tiles):
        # BATER A CABEÇA
        if self.vy < 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.topleft[0], self.rect.topleft[1] + self.vy)) or tile.rect.collidepoint((self.rect.midtop[0], self.rect.midtop[1] + self.vy)) or tile.rect.collidepoint((self.rect.topright[0], self.rect.topright[1] + self.vy)):
                        # if self.vy >self.g + 1: SFX_LANDING.play()
                        self.vy = 0
                        self.rect.top = tile.rect.bottom
                        self.double_jumping = True
        # QUEDA
        if self.vy >= 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomleft[0], self.rect.bottomleft[1] + self.vy)) or tile.rect.collidepoint((self.rect.midbottom[0], self.rect.midbottom[1] + self.vy)) or tile.rect.collidepoint((self.rect.bottomright[0], self.rect.bottomright[1] + self.vy)):
                        if self.vy >self.g + 1: SFX_LANDING.play()
                        self.on_air = False
                        self.double_jumping = False
                        self.vy = 0
                        self.rect.bottom = tile.rect.top
                        self.jump_combo = 0
                        # if not self.lock_ducked: self.move_state = 'idle'
                        break
                    else: self.on_air = True
                        # if not self.lock_ducked: self.move_state = 'falling'


                    
        if self.on_air:
            if self.move_state == 'on action' and self.action == 'energing': self.vy = 0
            # if self.rect.bottom + self.vy < self.level.kill_height:
            self.rect.y += self.vy
            self.vy += self.g
 

    # FUNÇÃO UTILIZADA PARA CONCATENAR ALGUNS COMANDOS SECUNDÁRIOS QUE DEVEM SER EXECUTADO EM CADA FRAME
    def pre_maintenance(self, tiles):

        self.time += 1/FPS

        # LIBERA ANDAR POR ESSE FRAME
        self.walk_locked = False
        self.jump_locked = False

        # VERIFICA SE O PERSONAGEM DEVE ESTAR TRAVADO AGACHADO
        #   -- ALTERA O TAMANHO DO PERSONAGEM PRA TENTAR FICAR EM PÉ
        self.image = pygame.Surface((64,127))
        if self.facing_right: self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        else: self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)

        if self.lock_ducked:
            self.lock_ducked = False
            self.ducked = False
            self.rect.y -= 1
            if pygame.sprite.spritecollide(self, tiles, False):
                self.lock_ducked = True
                self.duck()
            if self.lock_ducked:
                self.move_state = 'ducking'
                self.lock_ducked_time += 1
            else:self.lock_ducked_time =0
            self.rect.y += 1

        else:
            self.lock_ducked = False
            self.ducked = False
            self.lock_ducked_time = 0
            if pygame.sprite.spritecollide(self, tiles, False):
                self.lock_ducked = True
                self.duck()
            if self.lock_ducked: self.move_state = 'ducking'

        #   -- RETORNA O RETANGULO PARA O TAMANHO DA IMAGEM ATUAL
        if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0
        self.image = self.animation_frames[int(self.current_animation_frame)]
        if self.facing_right: self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        else: self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)

        if self.on_air:
            if self.vy >= 0: self.move_state = 'falling'
            else: self.move_state = 'jumping'

        # if self.on_action or not self.on_air:
        if not self.on_air:
            if not self.lock_ducked:
                if self.action != 'sliding': self.move_state = 'idle'

        if not self.on_action: self.action_time = 0

        if self.action_time <= 0:
            self.action_time = 0
            self.on_action = False
            self.action = 'none'
        else: self.action_time -= 1

        if self.action_recovery_time > 0: self.action_recovery_time -= 1

        if self.invencible_timer > 0:
            self.invencible_timer -= 1
            self.invencible = True
        else: self.invencible = False


    # FUNÇÃO QUE RODA QUANDO O GOD MODE ESTÁ ATIVADO
    def update_god_mode(self):
        if self.god_mode:
            # PROPRIEDADES DE COMBATE
            self.jump_atk = 35
            self.bomb_ball_p_atk = 5
            self.bounce_ball_atk = 150
            self.critical_bounce = 2.5
            self.energy_ball_atk = 5
            # PROPRIEDADES DE MOVIMENTAÇÃO
            self.ground_speed = 6 
            self.air_speed = 7
            self.g = 0.5 
            self.impulse = -18
            self.second_impulse = -15
            self.enemy_bounce = -15
            # ADICIONAIS
            self.hp += 3
            if self.hp >= self.max_hp: self.hp = self.max_hp
            self.life_bar.update_life(self.hp)

            #MANUTENÇÃO
            if self.god_mode_fuel > 0: self.god_mode_fuel -= 0.05
            else:
                self.god_mode_fuel = 0
                self.god_mode = False
                self.god_mode_energy.empty()

        else:
            # PROPRIEDADES DE COMBATE
            self.max_hp = 100
            self.jump_atk = 20
            self.bomb_ball_p_atk = 2
            self.bounce_ball_atk = 50
            self.critical_bounce = 2.5
            self.energy_ball_atk = 2
            # PROPRIEDADES DE MOVIMENTAÇÃO
            self.ground_speed = 5 
            self.air_speed = 6
            self.g = 1 
            self.impulse = -18
            self.second_impulse = -15
            self.enemy_bounce = -15


    # FUNÇÃO UTILIZADA PARA CONCATENAR ALGUNS COMANDOS SECUNDÁRIOS QUE DEVEM SER EXECUTADO NO FINAL DE CADA FRAME
    def post_maintenance(self):  
        pass                         
        # if self.auto_heal:
        #     self.hp += self.heart_hp_restore
        #     if self.hp >= self.max_hp: self.hp = self.max_hp
        #     self.life_bar.update_life(self.hp)
  

    # ATUALIZA A AÇÃO, CASO O PERSONAGEM ESTEJA EXECUTANDO ALGUMA
    def update_action(self, tiles):
        if not self.on_action: return

        self.slide(tiles)


    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self, tiles):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.width, self.height))
            # self.image.fill(self.color)
                

        if self.facing_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomleft[0], self.rect.bottomleft[1] -1)):
                        self.rect.left = tile.rect.right + 1
            
        else:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomright[0], self.rect.bottomright[1] -1)):
                        self.rect.right = tile.rect.left - 1
        

    # CONTROLA A ANIMAÇÃO QUE DEVE SER UTILIZADA BASEADA NAS INFORMAÇÕES DO PERSONAGEM
    def define_animation_state(self):
        if self.lock_ducked:
            if not self.move_state == 'on action' or not self.action == 'sliding':
                if self.move_state == 'duck walk':
                    if self.ball_on_bag:
                        if self.facing_right: self.animation_frames = self.duck_walk_animation_r
                        else: self.animation_frames = self.duck_walk_animation_l
                    else:
                        if self.facing_right: self.animation_frames = self.no_ball_duck_walk_animation_r
                        else: self.animation_frames = self.no_ball_duck_walk_animation_l
                else:
                    if self.ball_on_bag:
                        if self.facing_right: self.animation_frames = self.duck_animation_r
                        else: self.animation_frames = self.duck_animation_l
                    else:
                        if self.facing_right: self.animation_frames = self.no_ball_duck_animation_r
                        else: self.animation_frames = self.no_ball_duck_animation_l
                return
        if self.ball_on_bag:
            if self.facing_right:
                if self.move_state == 'idle': self.animation_frames = self.idle_animation_r
                elif self.move_state == 'runnig': self.animation_frames = self.run_animation_r
                elif self.move_state == 'jumping': self.animation_frames = self.jump_animation_r
                elif self.move_state == 'falling': self.animation_frames = self.fall_animation_r
                elif self.move_state == 'duking': self.animation_frames = self.duck_animation_r
                elif self.move_state == 'duck walk': self.animation_frames = self.duck_walk_animation_r
                elif  self.move_state == 'on action':
                    if self.action == 'sliding': self.animation_frames = self.slide_animation_r
                    if self.action == 'throwing': self.animation_frames = self.throw_animation_r
                    if self.action == 'passing': self.animation_frames = self.pass_animation_r
                    if self.action == 'bombing': self.animation_frames = self.bomb_animation_r
                    if self.action == 'shooting': self.animation_frames = self.shoot_animation_r
                    if self.action == 'duck shooting': self.animation_frames = self.duck_shoot_animation_r
                    if self.action == 'shooting on air': self.animation_frames = self.jump_n_run_animation_r
                    if self.action == 'shooting and running': self.animation_frames = self.shoot_n_run_animation_r
            else:
                if self.move_state == 'idle': self.animation_frames = self.idle_animation_l
                elif self.move_state == 'runnig': self.animation_frames = self.run_animation_l
                elif self.move_state == 'jumping': self.animation_frames = self.jump_animation_l
                elif self.move_state == 'falling': self.animation_frames = self.fall_animation_l
                elif self.move_state == 'duking': self.animation_frames = self.duck_animation_l
                elif self.move_state == 'duck walk': self.animation_frames = self.duck_walk_animation_l
                elif  self.move_state == 'on action':
                    if self.action == 'sliding': self.animation_frames = self.slide_animation_l
                    if self.action == 'throwing': self.animation_frames = self.throw_animation_l
                    if self.action == 'passing': self.animation_frames = self.pass_animation_l
                    if self.action == 'bombing': self.animation_frames = self.bomb_animation_l
                    if self.action == 'shooting': self.animation_frames = self.shoot_animation_l
                    if self.action == 'duck shooting': self.animation_frames = self.duck_shoot_animation_l
                    if self.action == 'shooting on air': self.animation_frames = self.jump_n_run_animation_l
                    if self.action == 'shooting and running': self.animation_frames = self.shoot_n_run_animation_l
        else:
            if self.facing_right:
                if self.move_state == 'idle': self.animation_frames = self.no_ball_idle_animation_r
                elif self.move_state == 'runnig': self.animation_frames = self.no_ball_run_animation_r
                elif self.move_state == 'jumping': self.animation_frames = self.no_ball_jump_animation_r
                elif self.move_state == 'falling': self.animation_frames = self.no_ball_fall_animation_r
                elif self.move_state == 'duking': self.animation_frames = self.no_ball_duck_animation_r
                elif self.move_state == 'duck walk': self.animation_frames = self.no_ball_duck_walk_animation_r
                elif  self.move_state == 'on action':
                    if self.action == 'sliding': self.animation_frames = self.no_ball_slide_animation_r
                    if self.action == 'throwing': self.animation_frames = self.no_ball_throw_animation_r
                    if self.action == 'passing': self.animation_frames = self.no_ball_pass_animation_r
                    if self.action == 'bombing': self.animation_frames = self.no_ball_bomb_animation_r
                    if self.action == 'shooting': self.animation_frames = self.no_ball_shoot_animation_r
                    if self.action == 'duck shooting': self.animation_frames = self.no_ball_duck_shoot_animation_r
                    if self.action == 'shooting on air': self.animation_frames = self.no_ball_jump_n_run_animation_r
                    if self.action == 'shooting and running': self.animation_frames = self.no_ball_shoot_n_run_animation_r
            else:
                if self.move_state == 'idle': self.animation_frames = self.no_ball_idle_animation_l
                elif self.move_state == 'runnig': self.animation_frames = self.no_ball_run_animation_l
                elif self.move_state == 'jumping': self.animation_frames = self.no_ball_jump_animation_l
                elif self.move_state == 'falling': self.animation_frames = self.no_ball_fall_animation_l
                elif self.move_state == 'duking': self.animation_frames = self.no_ball_duck_animation_l
                elif self.move_state == 'duck walk': self.animation_frames = self.no_ball_duck_walk_animation_l
                elif  self.move_state == 'on action':
                    if self.action == 'sliding': self.animation_frames = self.no_ball_slide_animation_l
                    if self.action == 'throwing': self.animation_frames = self.no_ball_throw_animation_l
                    if self.action == 'passing': self.animation_frames = self.no_ball_pass_animation_l
                    if self.action == 'bombing': self.animation_frames = self.no_ball_bomb_animation_l
                    if self.action == 'shooting': self.animation_frames = self.no_ball_shoot_animation_l
                    if self.action == 'duck shooting': self.animation_frames = self.no_ball_duck_shoot_animation_l
                    if self.action == 'shooting on air': self.animation_frames = self.no_ball_jump_n_run_animation_l
                    if self.action == 'shooting and running': self.animation_frames = self.no_ball_shoot_n_run_animation_l


    # VERIFICA AS COLISÕES QUE CAUSAM DANO NO INIMIGO
    def colision_atk(self):
        # COLISÕES DO PERSONAGENS COM OS INIMIGOS
        for enemy in self.level.enemys_group:
            if enemy.inert: continue
            if enemy.rect.right > -10 and enemy.rect.left < self.screen_w + 10:
                # -- COLISÃO COM OS "PÉS"
                if enemy.rect.collidepoint((self.rect.bottomleft[0], self.rect.bottomleft[1] + self.vy)) or enemy.rect.collidepoint((self.rect.midbottom[0], self.rect.midbottom[1] + self.vy)) or enemy.rect.collidepoint((self.rect.bottomright[0], self.rect.bottomright[1] + self.vy)):
                    # if self.vy > 0:
                    if enemy.fragile_head:
                        enemy.get_hit(self.jump_atk, self ,self.particles)
                        self.score += self.score_jump_atk * self.jump_combo
                        self.jump_combo += 1
                    else: SFX_E_PROTECTED.play()
                    if enemy.spike_head :
                        if not self.invencible:
                            self.get_hit(enemy.atk)
                            self.invencible = True
                            self.invencible_timer = self.invenvible_frames
                    else:
                        SFX_E_JUMP.play()
                    self.vy = self.enemy_bounce
                    self.rect.y += self.vy
                    self.vy += self.g
                    self.on_air = True

                # -- COLISÃO COM OS PROJETEIS DA BOMBBALL
                collided_p = pygame.sprite.spritecollide(enemy, self.explosion_projectiles, False)
                for n, p in enumerate(collided_p):
                    if enemy.explosion_protected: continue
                    hited = False
                    for e in p.hited_enemys_list:
                        if e == enemy:
                            hited = True
                    if not hited:
                        p.hited_enemys_list.append(enemy)
                        if n == 0: enemy.get_hit(self.bomb_ball_p_atk, self, self.particles)
                        else: enemy.get_hit(self.bomb_ball_p_atk, self, self.particles, False)

                # COLISÃO COM A BOLA QUICANTE
                if not self.bounce_balls.sprite == None:
                    # COLISÃO COM A PARTE DE BAIXO DA BOLA
                    # elif self.bounce_balls.sprite.v[1] < 0 and (enemy.rect.collidepoint((self.bounce_balls.sprite.rect.topleft[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.topleft[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midtop[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midtop[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.topright[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.topright[1] + self.bounce_balls.sprite.v[1]))):
                    if self.bounce_balls.sprite.v[1] < 0 and enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midtop[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midtop[1] + self.bounce_balls.sprite.v[1])):
                        if not enemy.bounce_protected and enemy.fragile_head: 
                            enemy.get_hit(self.bounce_ball_atk, self, self.particles)
                            self.score += self.score_per_bounce * self.bounce_balls.sprite.combo
                            self.bounce_balls.sprite.combo *= 2
                        else: SFX_E_PROTECTED.play()
                        self.bounce_balls.sprite.v[1] = - self.bounce_balls.sprite.v[1]
                        self.bounce_balls.sprite.rect.bottom = enemy.rect.top - 5
                        self.bounce_balls.sprite.returning = True
                        SFX_BALL_BOUNCE.play()

                    # COLISÃO COM A PARTE DA DIREITA
                    elif self.bounce_balls.sprite.v[0] > 0 and (enemy.rect.collidepoint((self.bounce_balls.sprite.rect.bottomright[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.bottomright[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midright[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midright[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.topright[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.topright[1] + self.bounce_balls.sprite.v[1]))):
                        if not enemy.bounce_protected and not enemy.front_protected:
                            enemy.get_hit(self.bounce_ball_atk, self, self.particles)
                            self.score += self.score_per_bounce * self.bounce_balls.sprite.combo
                            self.bounce_balls.sprite.combo *= 2
                        else: SFX_E_PROTECTED.play()
                        self.bounce_balls.sprite.v[0] = - self.bounce_balls.sprite.v[0]
                        self.bounce_balls.sprite.rect.right = enemy.rect.left - 5
                        self.bounce_balls.sprite.returning = True
                        SFX_BALL_BOUNCE.play()
                    # COLISÃO COM A PARTE DA ESQUERDA
                    elif self.bounce_balls.sprite.v[0] < 0 and (enemy.rect.collidepoint((self.bounce_balls.sprite.rect.bottomleft[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.bottomleft[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midleft[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midleft[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.topleft[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.topleft[1] + self.bounce_balls.sprite.v[1]))):
                        if not enemy.bounce_protected and not enemy.front_protected: 
                            enemy.get_hit(self.bounce_ball_atk, self, self.particles)
                            self.score += self.score_per_bounce * self.bounce_balls.sprite.combo
                            self.bounce_balls.sprite.combo *= 2
                        else: SFX_E_PROTECTED.play()
                        self.bounce_balls.sprite.v[0] = - self.bounce_balls.sprite.v[0]
                        self.bounce_balls.sprite.rect.left = enemy.rect.right + 5
                        self.bounce_balls.sprite.returning = True
                        SFX_BALL_BOUNCE.play()
                    # COLISÃO COM A PARTE DE CIMA DA BOLA
                    # elif self.bounce_balls.sprite.v[1] > 0 and (enemy.rect.collidepoint((self.bounce_balls.sprite.rect.bottomleft[0] + self.bounce_balls.sprite.v[0], self.bounce_balls.sprite.rect.bottomleft[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midbottom[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midbottom[1] + self.bounce_balls.sprite.v[1])) or enemy.rect.collidepoint((self.bounce_balls.sprite.rect.bottomright[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.bottomright[1] + self.bounce_balls.sprite.v[1]))):
                    elif self.bounce_balls.sprite.v[1] > 0 and enemy.rect.collidepoint((self.bounce_balls.sprite.rect.midbottom[0] + self.bounce_balls.sprite.v[0],self.bounce_balls.sprite.rect.midbottom[1] + self.bounce_balls.sprite.v[1])):
                        if not enemy.bounce_protected: 
                            enemy.get_hit(self.bounce_ball_atk * self.critical_bounce, self, self.particles)
                            self.score += self.score_per_bounce * self.bounce_balls.sprite.combo
                            self.bounce_balls.sprite.combo *= 2
                        else: SFX_E_PROTECTED.play()
                        self.bounce_balls.sprite.v[1] = - self.bounce_balls.sprite.v[1]
                        self.bounce_balls.sprite.rect.top = enemy.rect.bottom + 5
                        self.bounce_balls.sprite.returning = True
                        SFX_BALL_BOUNCE.play()
           
                # COLISÃO COM OS TIROS
                collided_p = pygame.sprite.spritecollide(enemy, self.lasers, False)
                for p in collided_p:
                    p.explode(10, self)
                    if not enemy.laser_protected: enemy.get_hit(self.laser_dmg, self, self.particles)
                    else: SFX_E_PROTECTED.play()


    # VERIFICA AS COLISÕES QUE CAUSAM DANO NO PLAYER E QUE COLETA OBJETOS
    def colision_hit(self):
        colliding_enemys = pygame.sprite.spritecollide(self, self.level.enemys_group, False)
        for enemy in colliding_enemys:
            if not self.invencible and not enemy.harmless and not enemy.inert:
                self.get_hit(enemy.atk)
                self.invencible = True
                self.invencible_timer = self.invenvible_frames
        colliding_projectiles = pygame.sprite.spritecollide(self, self.enemy_particles, True)
        for p in colliding_projectiles:
            if p.type == 'basic':
                if not self.invencible:
                    self.get_hit(p.damage)
                    self.invencible = True
                    self.invencible_timer = self.invenvible_frames
        colliding_collectables = pygame.sprite.spritecollide(self, self.level.collectables_group, False)
        for c in colliding_collectables:
            if c.type == 'heart':
                SFX_COLLECT_HEART.play()
                self.hp += self.heart_hp_restore
                if self.hp >= self.max_hp: self.hp = self.max_hp
                self.life_bar.update_life(self.hp)
            elif c.type == 'bomb':
                SFX_COLLECT_BOMB.play()
                self.bombs_on_bag += self.bombs_refill
            elif c.type == 'coin':
                SFX_COLLECT_SHIME.play()
                self.score += self.coin_score
            elif c.type == 'mega coin':
                SFX_COLLECT_SHIME.play()
                self.coins_collecteds += 1                
                self.score += self.mega_coin_score
            elif c.type == 'cristal':
                SFX_COLLECT_SHIME.play()
                self.laser_fuel += self.laser_refill
                if self.laser_fuel >= 100: self.laser_fuel = 100
            elif c.type == 'syringe':
                SFX_COLLECT_SHIME.play()
                self.god_mode_fuel = 100
            elif c.type == 'pills':
                SFX_COLLECT_SHIME.play()
                self.god_mode_fuel += 50
                if self.god_mode_fuel >= 100: self.god_mode_fuel = 100
            c.pop()
        # BOLA QUICANTE COM OS COLETÁVEIS
        if not self.bounce_balls.sprite == None:
            colliding_collectables = pygame.sprite.spritecollide(self.bounce_balls.sprite, self.level.collectables_group, False)
            for c in colliding_collectables:
                # if c.type == 'heart':
                #     SFX_COLLECT_HEART.play()
                #     self.hp += self.heart_hp_restore
                #     if self.hp >= self.max_hp: self.hp = self.max_hp
                #     self.life_bar.update_life(self.hp)
                # elif c.type == 'bomb':
                #     SFX_COLLECT_BOMB.play()
                #     self.bombs_on_bag += self.bombs_refill
                if c.type == 'coin':
                    SFX_COLLECT_SHIME.play()
                    c.pop()
                    self.score += self.coin_score
                elif c.type == 'mega coin':
                    self.coins_collecteds += 1                
                    c.pop()
                    SFX_COLLECT_SHIME.play()
                    self.score += self.mega_coin_score
        
        
    # RECEBE OS COMANDO DO USUÁRIO E EXECUTA AS FUNÇÕES
    def input_read(self, tiles):

        keys = pygame.key.get_pressed()
 
        if keys[pygame.K_DOWN]: self.duck()
     
        if keys[pygame.K_q]: self.throw_bouncing_ball()

        if keys[pygame.K_w]: self.bomb_ball_hability()

        if keys[pygame.K_e]: self.laser_shoot()

        if keys[pygame.K_r]: self.use_steroid()


        if keys[pygame.K_RIGHT]: self.walk_right(tiles)

        elif keys[pygame.K_LEFT]: self.walk_left(tiles)

        if keys[pygame.K_UP]:
            if self.on_air: self.second_jump()
            else: self.jump(tiles)

        if keys[pygame.K_SPACE]: self.slide(tiles)

        # if keys[pygame.K_x]: self.reset()

        # if keys[pygame.K_i]: self.edit_mode = True


    # RECEBE OS COMANDO DO USUÁRIO E EXECUTA AS FUNÇÕES
    def edit_mode_input_read(self):

        keys = pygame.key.get_pressed()
 
        if keys[pygame.K_RIGHT]: self.move_right(30, 'nanado')

        elif keys[pygame.K_LEFT]: self.move_left(30, 'nanado')

        if keys[pygame.K_m]: self.move_right(5, 'nanado')

        elif keys[pygame.K_n]: self.move_left(5, 'nanado')

        if keys[pygame.K_UP]: self.rect.y -= 10

        if keys[pygame.K_DOWN]: self.rect.y += 10

        if keys[pygame.K_o]: self.edit_mode = False


    # ATUALIZA O PERSONAGEM COMO UM TOD0 CADA FRAME
    def update(self, screen):
        # ATUALIZAÇÕES DO MODO DE EDIÇÃO
        # if self.edit_mode:
        #     self.edit_mode_input_read()
        #     self.animate(self.level.tiles_group.sprites())
        #     # -- ATUALIZAÇÕES DOS AGREGADOS
        #     self.level.tiles_group.update(self.bg_pan)
        #     self.level.enemys_group.update(self)
        #     self.level.collectables_group.update(self)
        #     self.level.objects_group.update(self)
        #     self.god_mode_energy.update(self)
        #     self.lasers.update(self)
        #     self.bounce_balls.update(self.bg_pan, self, self.level.tiles_group)
        #     self.bomb_balls.update(self.bg_pan, self.level.tiles_group, self.level.enemys_group)
        #     if self.bomb_balls.sprite:
        #         if self.bomb_balls.sprite.exploded:
        #             self.bomb_ball_explode(self.bomb_balls.sprite.rect.midtop)            
        #     self.explosion_projectiles.update(self.bg_pan)
        #     self.enemy_particles.update(self)
        #     self.particles.update(self.bg_pan)

        #     self.paint(screen)
        #     return

        # self.update_fps(last_fps)
        # -- ATUALIZAÇÕES PRÓPRIAS
        self.check_life()
        self.pre_maintenance(self.level.tiles_group)
        self.update_action(self.level.tiles_group.sprites())
        self.fall(self.level.tiles_group.sprites())
        self.victory_check()
        if not self.won: self.input_read(self.level.tiles_group.sprites())
        self.update_god_mode()
        self.post_maintenance()
        # self.life_bar.update_pos(self.rect.bottomleft)
        self.define_animation_state()
        self.animate(self.level.tiles_group.sprites())
        # -- COLISÕES
        self.colision_atk() 
        # -- ATUALIZAÇÕES DOS AGREGADOS
        self.level.tiles_group.update(self.bg_pan)
        self.level.enemys_group.update(self)
        self.level.collectables_group.update(self)
        self.level.objects_group.update(self)
        self.god_mode_energy.update(self)
        self.lasers.update(self)
        self.bounce_balls.update(self.bg_pan, self, self.level.tiles_group)
        self.bomb_balls.update(self.bg_pan, self.level.tiles_group, self.level.enemys_group)
        if self.bomb_balls.sprite:
            if self.bomb_balls.sprite.exploded:
                self.bomb_ball_explode(self.bomb_balls.sprite.rect.midtop)            
        self.explosion_projectiles.update(self.bg_pan)
        self.enemy_particles.update(self)
        self.particles.update(self.bg_pan)
         # -- COLISÕES
        self.colision_hit()
        # -- DESENHA TUDO NA TELA
        self.paint(screen)


    def paint(self, screen):
        # self.level.tiles_group.paint(screen, self)
        self.level.objects_group.draw(screen)
        self.level.tiles_group.draw(screen)
        for enemy in self.level.enemys_group.sprites():
            enemy.life_bar.update_pos(enemy.rect.bottomleft)
            enemy.life_bar.paint(screen)
        self.level.collectables_group.draw(screen)
        self.enemy_smoke.draw(screen)          
        self.level.enemys_group.draw(screen)
        self.group.draw(screen)
        self.bomb_balls.draw(screen)
        self.explosion_projectiles.draw(screen)
        self.bounce_balls.draw(screen)  
        self.lasers.draw(screen)
        self.god_mode_energy.draw(screen)
        self.life_bar.paint(screen)
        self.enemy_particles.draw(screen)
        self.particles.draw(screen)


# CLASSE DASPRITE DA ENERGIA DO GOD MODE
class GodModeEnegy(pygame.sprite.Sprite):
    def __init__(self, player):
        # INICIALIZAÇÂO
        super().__init__()

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = []
        self.animation_speed = 0.34

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((player.rect.width, player.rect.height))
        # self.image.fill('light blue')
        self.rect = self.image.get_rect(center = player.rect.center)

        self.import_images()


    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        self.animation = convert_animation_imgs(ANIMATION_GOD_MODE_ENERGY, 0, 1)
        self.animation_frames = self.animation

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
        
        self.rect = self.image.get_rect(bottomright = self.rect.bottomright) 
    

    # AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O DESLOCAMENTO DO CENÁRIO
    def pos_ajust(self, player):
        self.rect.bottomright = player.rect.bottomright


    def update(self, player):
        self.pos_ajust(player)
        self.animate()


# CLASSE DO PROJETIL LASER
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, v):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.v = v
        self.type = 'laser'
        self.size = 1
        self.render_distance = 64
        self.colors = ['#0C5DF8', '#0B87D9', '#00D1F0', '#0BD9BC', '#0CF895']

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = []
        self.animation_speed = 0.1

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.size, self.size))
        # self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)

        self.import_images()

    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        self.animation = convert_animation_imgs(ANIMATION_LASER, 0, self.size)
        self.animation_frames = self.animation

    # MOVE O SPRITE
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]


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

    #  ANIMAÇÂO DE EXPLODIR
    def explode(self, n, player):
        for i in range (n):
            player.particles.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))
        self.kill()


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
        collinding_tile = pygame.sprite.spritecollide(self, player.level.tiles_group, False)
        if collinding_tile: self.explode(10, player)

    def update(self, player):
        # if not self.in_render_distance(player): return
        self.move()
        self.pan_ajust(player.bg_pan)
        self.life_check(player)
        self.animate()


# CLASSE DA SPRITE DA BOLA DE BOMBA 
class BombBall(pygame.sprite.Sprite):
    def __init__(self, pos, size, v, g, n_projectiles, animation_speed, screen_w, screen_h):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = size  # UM NUMERO QUE MULTIPLICA O TAMANHO ORIGINAL DE 32X32
        self.v = v
        self.g = g
        self.n_projectiles = n_projectiles
        self.screen_w = screen_w
        self.screen_h = screen_h

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = []
        self.animation_speed = animation_speed

        # PROPRIEDADES
        self.exploded = False

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.size, self.size))
        # self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)

        self.import_images()


    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        self.animation = convert_animation_imgs(ANIMATION_BOMB_BALL, 0, self.size)
        self.animation_frames = self.animation

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


    # MOVE A BOMBBALL
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.v[1] += self.g
    

    # AJUSTA A POSIÇÃO DA BOLA DE ACORDO COM O PAN
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


    # VERIFICA SE A BOMBBALL AINDA DEVE EXISTIR
    def check_life(self, tiles, enemys):
        # VERIFICA SE A BOLA SAIU DA TELA, EXETO PELO TOPO
        # if self.rect.top >= self.screen_h: self.exploded = True
        # elif self.rect.left >= self.screen_w + 10: self.exploded = True
        # elif self.rect.right <= 0 - 10: self.exploded = True

        # VERIFICA A COLISÃO DA BOLA COM O TERRENO
        if pygame.sprite.spritecollide(self, tiles, False): self.exploded = True 

        # VERIFICA A COLISÃO DA BOLA COM OS INIMIGOS
        for e in enemys:
            if e.rect.collidepoint(self.rect.center): self.exploded = True



    # ATUALIZA O OBJETO 
    def update(self, bg_pan, tiles, enemys):
        if self.exploded: self.kill()
        self.pan_ajust(bg_pan)
        self.move()
        self.check_life(tiles, enemys)
        self.animate()


# CLASSE DA SPRITE DA BOLA DE QUICANTES 
class BouncingBall(pygame.sprite.Sprite):
    def __init__(self, pos, size, v, g, elastic_bounce, return_radius, animation_speed, screen_w, screen_h):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = size # UM NUMERO QUE MULTIPLICA O TAMANHO ORIGINAL DE 32X32
        self.v = v
        self.g = g
        self.elastic_bounce = elastic_bounce
        self.return_radius = return_radius
        self.screen_w = screen_w
        self.screen_h = screen_h

        # PROPRIEDADES
        self.returning = False
        self.speed = math.sqrt(self.v[0] ** 2 + self.v[1] ** 2)
        self.critical = 1
        self.combo = 1

        
        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = []
        self.animation_speed = animation_speed

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.size, self.size))
        # self.image.fill(SALMON)
        self.rect = self.image.get_rect(center = pos)
                
        self.import_images()


    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        self.animation = convert_animation_imgs(ANIMATION_BOUNCE_BALL, 0, self.size)
        self.animation_frames = self.animation

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


    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.v[1] += self.g


    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]


    def bounce(self, player, tiles):
        # DIRECIONA A BOLA AO PERSONAGEM SE ESTIVER PERTO
        if self.returning and math.sqrt((player.rect.centery - self.rect.centery) ** 2 + (player.rect.centerx - self.rect.centerx) ** 2) < self.return_radius:
            self.v[0] = self.speed * math.cos(math.atan2(player.rect.centery - self.rect.centery,  player.rect.centerx - self.rect.centerx))
            self.v[1] = self.speed * math.sin(math.atan2(player.rect.centery - self.rect.centery,  player.rect.centerx - self.rect.centerx))

        # COLISÃO COM AS EXTREMIDADES DA TELA
        else:
            if self.rect.left + self.v[0] <= 0 or self.rect.right + self.v[0] >= self.screen_w:
                self.v[0] = - self.v[0]
                self.returning = True
                SFX_BALL_BOUNCE.play()
            if self.rect.top + self.v[1] <= 0: # or self.rect.bottom + self.v[1] >= self.screen_h:
                self.v[1] = - self.v[1]
                # self.returning = True

        # COLISÃO COM TOPO DOS TILES
        if self.v[1] > 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomleft[0], self.rect.bottomleft[1] + self.v[1])) or tile.rect.collidepoint((self.rect.midbottom[0], self.rect.midbottom[1] + self.v[1])) or tile.rect.collidepoint((self.rect.bottomright[0], self.rect.bottomright[1] + self.v[1])):
                        self.v[1] = - self.v[1] * self.elastic_bounce[1]
                        SFX_BALL_BOUNCE.play()
                        #self.returning = True
                        break
        if self.v[1] < 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.topleft[0], self.rect.topleft[1] + self.v[1])) or tile.rect.collidepoint((self.rect.midtop[0], self.rect.midtop[1] + self.v[1])) or tile.rect.collidepoint((self.rect.topright[0], self.rect.topright[1] + self.v[1])):
                        self.v[1] = - self.v[1] * self.elastic_bounce[1]
                        SFX_BALL_BOUNCE.play()
                        #self.returning = True
                        break

        if self.v[0] > 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomright[0] + self.v[0], self.rect.bottomright[1] -1)) or tile.rect.collidepoint((self.rect.midright[0] + self.v[0], self.rect.midright[1])) or tile.rect.collidepoint((self.rect.topright[0] + self.v[0], self.rect.topright[1])):
                        self.v[0] = - self.v[0] * self.elastic_bounce[0]
                        self.returning = True
                        SFX_BALL_BOUNCE.play()
                        break

        elif self.v[0] < 0:
            for tile in tiles:
                if tile.rect.right > -10 and tile.rect.left < self.screen_w + 10:
                    if tile.rect.collidepoint((self.rect.bottomleft[0] + self.v[0], self.rect.bottomleft[1] -1)) or tile.rect.collidepoint((self.rect.midleft[0] + self.v[0], self.rect.midleft[1])) or tile.rect.collidepoint((self.rect.topleft[0] + self.v[0], self.rect.topleft[1])):
                        self.v[0] = - self.v[0] * self.elastic_bounce[0]
                        self.returning = True
                        SFX_BALL_BOUNCE.play()


    def check_life(self, player):
        # if self.rect.left + self.v[0] > self.screen_w: self.kill() 
        # if self.rect.right + self.v[0] < 0: self.kill() 
        # if self.rect.bottom + self.v[1] < 0: self.kill() 
        if self.rect.top + self.v[1] > self.screen_h: self.kill() 
        if not self.returning: return
        if pygame.sprite.collide_rect(self, player):
            player.ball_on_bag = True
            self.kill() 


    def update(self, bg_pan, player, tiles):
        self.pan_ajust(bg_pan)
        self.bounce(player, tiles)
        self.move()
        self.check_life(player)
        self.animate()


# CLASSE DOS PROJETEIS DE EXPLOSÃO
class ExplosionProjectile(pygame.sprite.Sprite):
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
        self.life_radius = 64
        self.hited_enemys_list = []

        # PROPRIEDADES DO SPRITE
        if self.p_speed < 3: self.color = 'black'
        elif self.p_speed < 7: self.color = 'red'
        else: self.color = 'yellow'
        self.image = pygame.Surface((self.size, self.size))
        # self.image.fill(self.color)
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
    def update(self, bg_pan):
        self.move()
        self.pan_ajust(bg_pan)
        self.check_life()

 


