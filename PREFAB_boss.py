# IMPORTA AS BIBLIOTECAS USADAS
import pygame
pygame.init()
import math
import random

# IMPORTA OS OUTROS ARQUIVOS USADOS
from GAME_functions import *
from ASSETS_boss import *
from PREFAB_enemy import *


class Boss1(Enemy):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        self.size = 96
        self.type = "boss"
        self.ground_y = pos[1]

        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = convert_animation_imgs(ANIMATION_IDLE, 0, self.size / 64)
        self.animation_speed = 0.2


        #PROPRIEDADES DE MOVIMENTAÇÃO
        ### ESTADOS DE MOVIMENTAÇÃO
        self.face_right = True
        self.on_air = True
        self.on_action = False
        self.broken = False
        ### VALORES DE MOVIMENTAÇÂO
        self.vx = 2
        self.vy = 0
        self.impulse = -19
        self.mini_impulse = -14
        self.up_g = 0.5
        self.down_g = 0.1
        ### VALORES PARA A INTELIGÊNCIA DE MOVIMENTÇÃO
        self.height_difference_to_jump = 64
        self.player_distance = 0

        ### TEMPOS DAS HABILIDADES
        self.slide_action_time = int(5 / self.animation_speed)
        self.walk_action_time = 80
        self.idle_action_time = int(24 / self.animation_speed)
        self.create_ball_action_time = int(5 / self.animation_speed)
        self.break_action_time = int(10 / self.animation_speed)

        self.run_aceleration = 0.04
        self.run_extra_speed = 0 

        self.action_timer = 0
        self.move_timer = 0
        self.move_state = 'idle'
        self.time_moving = self.idle_action_time

        #PROPRIEDADES DE COMBATE
        self.max_hp = 3 * 5 * 50 
        self.atk = 40

        self.health_state = 1
        self.invencible = False
        self.invencible_timer = 0
        self.invencible_time  = 50 * 2

        self.kick_count = 0 
        
        super().__init__(pos)

        self.fragile_head = False


        self.convert_animation_frames()

        # SFX_B_BORN.play()


    ################################
    ###### FUNÇÕES DO SISTEMA ######
    ################################

    def convert_animation_frames(self):
        self.animation_idle   = convert_animation_imgs(ANIMATION_IDLE, 0, self.size / 64)
        self.animation_break  = convert_animation_imgs(ANIMATION_BREAK, 0, self.size / 64)
        self.animation_walk_r = convert_animation_imgs(ANIMATION_WALK_R, 0, self.size / 64)
        self.animation_walk_l = convert_animation_imgs(ANIMATION_WALK_L, 0, self.size / 64)
        self.animation_jump_r = convert_animation_imgs(ANIMATION_JUMP_R, 0, self.size / 64)
        self.animation_jump_l = convert_animation_imgs(ANIMATION_JUMP_L, 0, self.size / 64)
        self.animation_kick_r = convert_animation_imgs(ANIMATION_KICK_R, 0, self.size / 64)
        self.animation_kick_l = convert_animation_imgs(ANIMATION_KICK_L, 0, self.size / 64)
        self.animation_slide_r = convert_animation_imgs(ANIMATION_SLIDE_R, 0, self.size / 64)
        self.animation_slide_l = convert_animation_imgs(ANIMATION_SLIDE_L, 0, self.size / 64)
        self.animation_create_ball = convert_animation_imgs(ANIMATION_CREATE_BALL, 0, self.size / 64)

        self.animation_idle_s2   = convert_animation_imgs(ANIMATION_IDLE_S2, 0, self.size / 64)
        self.animation_break_s2   = convert_animation_imgs(ANIMATION_BREAK_S2, 0, self.size / 64)
        self.animation_walk_r_s2  = convert_animation_imgs(ANIMATION_WALK_R_S2, 0, self.size / 64)
        self.animation_walk_l_s2  = convert_animation_imgs(ANIMATION_WALK_L_S2, 0, self.size / 64)
        self.animation_jump_r_s2  = convert_animation_imgs(ANIMATION_JUMP_R_S2, 0, self.size / 64)
        self.animation_jump_l_s2  = convert_animation_imgs(ANIMATION_JUMP_L_S2, 0, self.size / 64)
        self.animation_kick_r_s2  = convert_animation_imgs(ANIMATION_KICK_R_S2, 0, self.size / 64)
        self.animation_kick_l_s2  = convert_animation_imgs(ANIMATION_KICK_L_S2, 0, self.size / 64)
        self.animation_slide_r_s2  = convert_animation_imgs(ANIMATION_SLIDE_R_S2, 0, self.size / 64)
        self.animation_slide_l_s2  = convert_animation_imgs(ANIMATION_SLIDE_L_S2, 0, self.size / 64)
        self.animation_create_ball_s2  = convert_animation_imgs(ANIMATION_CREATE_BALL_S2, 0, self.size / 64)

        self.animation_idle_s3   = convert_animation_imgs(ANIMATION_IDLE_S3, 0, self.size / 64)
        self.animation_break_s3   = convert_animation_imgs(ANIMATION_BREAK_S3, 0, self.size / 64)
        self.animation_walk_r_s3  = convert_animation_imgs(ANIMATION_WALK_R_S3, 0, self.size / 64)
        self.animation_walk_l_s3  = convert_animation_imgs(ANIMATION_WALK_L_S3, 0, self.size / 64)
        self.animation_jump_r_s3  = convert_animation_imgs(ANIMATION_JUMP_R_S3, 0, self.size / 64)
        self.animation_jump_l_s3  = convert_animation_imgs(ANIMATION_JUMP_L_S3, 0, self.size / 64)
        self.animation_kick_r_s3  = convert_animation_imgs(ANIMATION_KICK_R_S3, 0, self.size / 64)
        self.animation_kick_l_s3  = convert_animation_imgs(ANIMATION_KICK_L_S3, 0, self.size / 64)
        self.animation_slide_r_s3  = convert_animation_imgs(ANIMATION_SLIDE_R_S3, 0, self.size / 64)
        self.animation_slide_l_s3  = convert_animation_imgs(ANIMATION_SLIDE_L_S3, 0, self.size / 64)
        self.animation_create_ball_s3  = convert_animation_imgs(ANIMATION_CREATE_BALL_S3, 0, self.size / 64)




    # APLICA UMA CERTA QUANTIDADE DE DANO AO PERSONAGEM
    def get_hit(self, damage, player, particles_group, pop = True, n_particles = 25):
        if self.invencible: return
        self.hp -= damage
        if self.hp <= 0 and self.living:
            player.score += 5
            self.living = False

        self.invencible_timer = self.invencible_time

        SFX_B_DAMAGE.play()

        if not pop: return
        for i in range (n_particles):
            particles_group.add(ExplosionParticle([self.pos[0] + self.size / 2, self.pos[1] - self.size / 2], 2, 4, 5, 10, 64, self.colors))


    def shoot_ball(self, player):
        ball_size =  1.75 * 19
        for i in range(self.health_state):
            if self.face_right:
                player.enemy_particles.add(SoccerBall([self.pos[0] + self.size, self.pos[1] - ball_size * 2], ball_size, [10, random.randint(-20,-5)], 0.5, [1, 0,98], self.ground_y, player.level.width))
            else:   
                player.enemy_particles.add(SoccerBall([self.pos[0], self.pos[1] - ball_size * 2], ball_size, [-10,random.randint(-20,-5)], 0.5, [1, 0,98], self.ground_y, player.level.width))
            while len(player.enemy_particles.sprites()) > 5: player.enemy_particles.sprites()[0].explode(player)

    ##########################
    ####### HABILIDADES ######
    ##########################

    # EXECUTA O PULO(SKILL)
    def jump(self, impulse):
        # if self.on_action: return
        # if self.jump_locked: return
        if self.on_air: return

        self.on_air = True
        self.vy = impulse
        self.move_state = 'jump'
        self.move_timer = 'free'
        SFX_B_JUMP.play()

    
    def kick(self, player):
        if not self.on_action:
            self.on_action = True
            self.action_timer = int(len(self.animation_kick_r) / self.animation_speed) - 1
            self.move_state = 'kick'
            self.move_timer = 'free'
            self.current_animation_frame = 0
            SFX_B_KICK.play()
        else:
            if self.move_state != 'kick': return
            if self.action_timer > 0:
                if self.action_timer == int(6 / self.animation_speed): self.shoot_ball(player)
                self.action_timer -= 1
                self.move_state = 'kick'
                self.move_timer = 'free'
            else:
                self.action_timer = 0
                self.on_action = False
                self.move_state = 'create ball'
                self.move_timer = self.create_ball_action_time


    def walk(self, distance):
        if self.face_right: self.pos[0] += distance
        else: self.pos[0] -= distance


    def slide(self):
        if not self.on_action:
            self.on_action = True
            self.action_timer = self.slide_action_time
            self.move_state = 'slide'
            self.move_timer = 'free'
            self.current_animation_frame = 0
            SFX_B_SLIDE.play()
        else:
            if self.move_state != 'slide': return
            if self.action_timer > 0:
                self.action_timer -= 1
                self.move_state = 'slide'
                self.move_timer = 'free'
                self.walk(10)
            else:
                self.action_timer = 0
                self.on_action = False
                self.jump(self.impulse)

    
    def break_(self, player):
        if not self.broken:
            self.on_action = True
            self.broken = True
            self.action_timer = self.break_action_time
            self.move_state = 'break'
            self.move_timer = 'free'
            self.current_animation_frame = 0
            # SFX_B_BREAK.play()
            SFX_B_BREAK2.play()
        else:
            # if self.move_state != 'break': return
            if self.action_timer > 0:
                self.action_timer -= 1
                self.move_state = 'break'
                self.move_timer = 'free'
            else:
                if self.health_state == 1:
                    self.health_state = 2
                    self.animation_idle   = self.animation_idle_s2
                    self.animation_break  = self.animation_break_s2
                    self.animation_walk_r = self.animation_walk_r_s2
                    self.animation_walk_l = self.animation_walk_l_s2
                    self.animation_jump_r = self.animation_jump_r_s2
                    self.animation_jump_l = self.animation_jump_l_s2
                    self.animation_kick_r = self.animation_kick_r_s2
                    self.animation_kick_l = self.animation_kick_l_s2
                    self.animation_slide_r = self.animation_slide_r_s2
                    self.animation_slide_l = self.animation_slide_l_s2
                    self.animation_create_ball = self.animation_create_ball
                    SFX_B_RECOVER.play()
                elif self.health_state == 2:
                    self.health_state = 3
                    self.animation_idle   = self.animation_idle_s3
                    self.animation_break  = self.animation_break_s3
                    self.animation_walk_r = self.animation_walk_r_s3
                    self.animation_walk_l = self.animation_walk_l_s3
                    self.animation_jump_r = self.animation_jump_r_s3
                    self.animation_jump_l = self.animation_jump_l_s3
                    self.animation_kick_r = self.animation_kick_r_s3
                    self.animation_kick_l = self.animation_kick_l_s3
                    self.animation_slide_r = self.animation_slide_r_s3
                    self.animation_slide_l = self.animation_slide_l_s3
                    self.animation_create_ball = self.animation_create_ball_s3
                    SFX_B_RECOVER.play()

                elif self.health_state == 3: self.explode(player)
                self.action_timer = 0
                self.on_action = False
                self.broken = False
                # self.jump(self.impulse)
                self.move_state = 'walk'
                self.move_timer = self.walk_action_time

    
    def explode(self, player):
        SFX_B_EXPLOSION.play()   
        player.particles.add(DeathExplosion([self.pos[0] + self.size/2 , self.pos[1] - self.size/2], self.size))
        self.kill()


                
    #######################################
    ###### ATUALIZAÇÕES POR FRAME #########
    #######################################
    def pre_mantinence(self):
        if self.invencible_timer < 0:
            self.invencible_timer -= 1
            self.invencible = True
        else:
            self.invencible_timer = 0
            self.invencible = False


    def check_health_state(self):
        if self.health_state == 1 and self.hp <= 2 * self.max_hp / 3 : self.move_state = 'break'
        if self.health_state == 2 and self.hp <= self.max_hp / 3 : self.move_state = 'break'
        if self.health_state == 3 and self.hp <= 0 : self.move_state = 'break'


    # CONTROLA A QUEDA DO PERSONAGEM e bater a caça
    def fall(self, player):
        # QUEDA
        if self.vy >= 0:
            for tile in player.level.tiles_group.sprites():
                if tile.rect.collidepoint((self.rect.bottomleft[0], self.rect.bottomleft[1] + self.vy)) or tile.rect.collidepoint((self.rect.midbottom[0], self.rect.midbottom[1] + self.vy)) or tile.rect.collidepoint((self.rect.bottomright[0], self.rect.bottomright[1] + self.vy)):
                    # if self.vy >self.g + 1: SFX_LANDING.play()
                    self.on_air = False
                    self.vy = 0
                    self.pos[1] = tile.rect.top
                    if self.move_state == 'jump':
                        if self.player_distance >= 8 * 64:
                            self.move_state = 'slide'
                            self.move_timer = 0
                        else:
                            self.current_animation_frame = 0
                            self.move_timer = self.idle_action_time
                            self.move_state = 'idle'
                    break
                else: self.on_air = True
        if self.on_air:
            self.pos[1] += self.vy
            if self. vy <= 0:
                self.vy += self.up_g
            else:
                self.vy += self.down_g


    def define_action(self, player):
        # DEFINE A ORIENTAÇÃO DO BOSS BASEADA NO PLAYER
        if not self.on_action:
            if self.rect.centerx < player.rect.centerx: self.face_right = True
            else: self.face_right = False
        
        # CALCULA A DISTANCIA PRO PLAYER
        self.player_distance = math.sqrt((player.rect.centerx - self.rect.centerx) ** 2 + (player.rect.centery - self.rect.centery) ** 2)

        # DEFINE O ESTADO DE MOVIMENTAÇÃO
        ### AÇÕES SITUACIONAIS:
        if not self.on_action:
            ### AÇÕES QUE SÓ ACONTECEM COM O PLAYER PERTO
            ##### PULA SE A BOLA TÁ PERTO E VINDO DE TRÁS
            if player.bounce_balls.sprite != None:
                if self.rect.centerx > player.rect.centerx and player.bounce_balls.sprite.rect.centerx - self.rect.centerx >= 4 * 64 and player.bounce_balls.sprite.rect.centery > self.rect.centery:
                    self.jump(self.mini_impulse)
                elif self.rect.centerx < player.rect.centerx and self.rect.centerx - player.bounce_balls.sprite.rect.centerx >= 4 * 64 and player.bounce_balls.sprite.rect.centery > self.rect.centery:
                    self.jump(self.mini_impulse)
            ##### PULA SE O PLAYER TA PERTO E NO ALTO
            elif self.player_distance <= 6 * 64:
                if self.rect.top - self.height_difference_to_jump > player.rect.bottom: self.jump(self.mini_impulse)

        ### AÇÕES PADRÃO:
        if self.move_timer != 'free':
            if self.move_timer > 0: self.move_timer -= 1
            else:
                if self.move_state == 'create ball':
                    self.kick_count += 1
                    if self.kick_count < self.health_state:
                        self.move_state = 'kick'
                    else:
                        self.kick_count = 0
                        self.move_state = 'walk'
                        self.move_timer = self.walk_action_time
                elif self.move_state == 'walk':
                    self.move_state = 'slide'
                elif self.move_state == 'idle':
                    self.move_state = 'kick'


    def act(self, player):
        # AÇÕES  QUE DEVEM RODAR EM CADA FRAME
        if self.move_state == 'kick': self.kick(player)
        elif self.move_state == 'slide': self.slide()
        elif self.move_state == 'break': self.break_(player)
        if self.move_state == 'walk':
            self.walk(self.vx + self.run_extra_speed)
            self.run_extra_speed += self.run_aceleration
        else: self.run_extra_speed = 0


    def define_animation_frames(self):
        if self.move_state == 'idle': self.animation_frames = self.animation_idle
        elif self.move_state == 'create ball': self.animation_frames = self.animation_create_ball
        elif self.move_state == 'break': self.animation_frames = self.animation_break
        elif self.face_right:
            if self.move_state == 'walk': self.animation_frames = self.animation_walk_r
            if self.move_state == 'jump': self.animation_frames = self.animation_jump_r
            if self.move_state == 'kick': self.animation_frames = self.animation_kick_r
            if self.move_state == 'slide': self.animation_frames = self.animation_slide_r
        else:
            if self.move_state == 'walk': self.animation_frames = self.animation_walk_l     
            if self.move_state == 'jump': self.animation_frames = self.animation_jump_l
            if self.move_state == 'kick': self.animation_frames = self.animation_kick_l
            if self.move_state == 'slide': self.animation_frames = self.animation_slide_l


    def update(self, player):
        self.pre_mantinence()
        self.check_health_state()
        self.define_action(player)
        self.act(player)
        self.fall(player)
        self.pan_ajust(player.bg_pan)
        self.define_animation_frames()
        self.animate()




# CLASSE DA SPRITE DA BOLA DE QUICANTES 
class SoccerBall(pygame.sprite.Sprite):
    def __init__(self, pos, size, v, g, elastic_bounce, ground_y, lvl_limit):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos
        self.size = size # A BASE É 19x19
        self.v = v
        self.g = g
        self.elastic_bounce = elastic_bounce
        self.ground_y = ground_y
        self.lvl_limit = lvl_limit


        # PROPRIEDADES
        self.returning = False
        self.speed = math.sqrt(self.v[0] ** 2 + self.v[1] ** 2)
        self.life_time = 50 * 60
        self.type = 'basic'
        self.damage = 35

        
        # PROPRIEDADES DE ANIMAÇÃO
        self.current_animation_frame = 0
        self.animation_frames = []
        self.animation_speed = 0.1

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)
                
        self.import_images()


    # DEFINE AS LISTAS DE IMAGENS USADAS NAS ANIMAÇÕES
    def import_images(self):
        self.animation_frames = convert_animation_imgs(ANIMATION_SOCCER_BALL, 0, self.size / 19)

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

    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.v[1] += self.g
    
    def pan_ajust(self, bg_pan):
        self.rect.centerx = self.pos[0] + bg_pan[0]
        self.rect.centery = self.pos[1] + bg_pan[1]

    def bounce(self):
        # # DIRECIONA A BOLA AO PERSONAGEM SE ESTIVER PERTO
        # if self.returning and math.sqrt((boss.rect.centery - self.rect.centery) ** 2 + (boss.rect.centerx - self.rect.centerx) ** 2) < self.return_radius:
        #     self.v[0] = self.speed * math.cos(math.atan2(boss.rect.centery - self.rect.centery,  boss.rect.centerx - self.rect.centerx))
        #     self.v[1] = self.speed * math.sin(math.atan2(boss.rect.centery - self.rect.centery,  boss.rect.centerx - self.rect.centerx))

        # COLISÃO COM AS EXTREMIDADES DO LEVEL
        ### TOPO DA TELA
        if self.v[1] <= 0:
            if self.pos[1] - self.size + self.v[1] <= 0: self.v[1] = - self.v[1]
        ### CHÃO
        else:
            if self.pos[1] + self.v[1] >= self.ground_y: self.v[1] = - self.v[1]
        ### INÍCIO DO LEVEL
        if self.v[0] <= 0:
            if self.pos[0] + self.v[0] <= 0: self.v[0] = - self.v[0]
        ### FIM DO LEVEL
        else:
            if self.pos[0] + self.size + self.v[1] >= self.lvl_limit: self.v[0] = - self.v[0]


    def explode(self, player):
        player.particles.add(BornSmoke([self.pos[0], self.pos[1]]))
        SFX_B_BALL_DEATH.play()
        self.kill()



    def check_life(self, player):
        # if self.rect.left + self.v[0] > player.screen_w: self.kill() 
        # if self.rect.right + self.v[0] < 0: self.kill() 
        # if self.rect.bottom + self.v[1] < 0: self.kill() 
        if self.rect.top + self.v[1] > player.screen_h: self.kill() 
        # if pygame.sprite.collide_rect(self, boss):
        #     boss.with_ball = True
        #     self.kill()
        self.life_time -= 1
        if self.life_time <= 0: self.kill()


    def update(self, player):
        self.pan_ajust(player.bg_pan)
        self.bounce()
        self.move()
        self.check_life(player)
        self.animate()
