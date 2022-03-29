# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from CONFIG_game import *
from CONFIG_fonts import *
from GAME_functions import *
from PREFAB_enemy import *
from ASSETS_player import *
from ASSETS_others import *
from ASSETS_menu import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import math
import random
import pygame

pygame.init() 

class MapScreen:
    def __init__(self, screen_w, screen_h, screen) -> None:

        self.map_offset = (104,104)
        self.shadow_offset = (50, 50)
        self.map_border_size = 2
        self.map_border_color = 'brown'
        self.shadow_color = ORANGE
        self.map_w = screen_w - 2 * self.map_offset[0]
        self.map_h = screen_h - 2 * self.map_offset[1]

        self.bg_img = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/map_bg.png'), (screen_w, screen_h))

        # FONTES
        self.LEVEL_TIME_FONT = pygame.font.SysFont('Helvetica', 25)

        # MENU DE INFORMAÇÔES DAS FASES
        self.stage_menu_offset = (50, 30)
        self.stage_menu_row_offset = 40
        self.stage_menu_coin_space = 32 + 16
        # BACKGROUND
        self.stage_menu_bg_img = convert_img('./resources/ilustrations/stage_menu_bg.png', 0, 1)
        # PROPRIEDADES DOS TEXTOS
        self.top_text_offset = (20,10)
        self.level_name_pos = (self.stage_menu_offset[0] + self.top_text_offset[0], self.stage_menu_offset[1] +self.top_text_offset[1])
        self.level_time_pos = (self.stage_menu_offset[0] + self.top_text_offset[0], self.stage_menu_row_offset + self.stage_menu_offset[1] +self.top_text_offset[1])
        #  MOEDAS DE LEVEL
        self.coins_pos = [
            (self.stage_menu_offset[0] + self.top_text_offset[0] + 0 * self.stage_menu_coin_space, 2 * self.stage_menu_row_offset + self.stage_menu_offset[1] +self.top_text_offset[1]),
            (self.stage_menu_offset[0] + self.top_text_offset[0] + 1 * self.stage_menu_coin_space, 2 * self.stage_menu_row_offset + self.stage_menu_offset[1] +self.top_text_offset[1]),
            (self.stage_menu_offset[0] + self.top_text_offset[0] + 2 * self.stage_menu_coin_space, 2 * self.stage_menu_row_offset + self.stage_menu_offset[1] +self.top_text_offset[1])
        ]
        self.coin_img = convert_img('./resources/ilustrations/menu_coin.png', 0, 1)
        self.no_coin_img = convert_img('./resources/ilustrations/menu_no_coin.png', 0, 1)


        # PERSONAGEM QUE ANDA NO MAPA
        self.player = MapPlayer(self.map_w, self.map_h, self.map_offset)
        
        # SOMBRA DO MAPA NA TELA
        self.map_shadow_img = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/shadow.png'), (self.map_w, self.map_h))
        self.map_shadow_pos = (self.map_offset[0] + self.shadow_offset[0], self.map_offset[1] + self.shadow_offset[1])
       
        # BORDA DO MAPA
        self.map_border = pygame.Surface((self.map_w  + 2 * self.map_border_size , self.map_h + 2 * self.map_border_size ))
        self.map_border.fill(self.map_border_color)
        self.map_border_pos = (self.map_offset[0] - self.map_border_size, self.map_offset[1] - self.map_border_size)

        # ILUSTRAÇÕES
        self.ilustrations_list = []
        self.ilustrations_group = pygame.sprite.Group()

        # LOGO (Games.be)
        self.logo_offset = (10, 10)
        self.logo_img = convert_img('./resources/ilustrations/logo.png', 0, 1)
        self.logo_pos = (screen_w - self.logo_img.get_width() - self.logo_offset[0], screen_h - self.logo_img.get_height() - self.logo_offset[1])

        # STATUS BAR
        self.status_bar_offset = self.logo_offset
        status_bar_txt = FONT_VT323.render(f'Press Enter to play or ESC to return to main menu...', False, 'white')
        self.status_bar_pos = (self.status_bar_offset[0], screen_h - self.status_bar_offset[1] - status_bar_txt.get_height())

        # MENU SUPERIOR 
        # self.menu = MapMenu(self.map_w, self.map_h)

        self.map_w1 = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/map_w1.png'), [self.map_w, self.map_h])
        self.map_w2 = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/map_w2.png'), [self.map_w, self.map_h])
        self.map_w3 = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/map_w3.png'), [self.map_w, self.map_h])
        self.map_w4 = pygame.transform.scale(pygame.image.load(f'./resources/ilustrations/map_w4.png'), [self.map_w, self.map_h])

        # CRIA OS CADEADOS DO JOGO
        self.fix_imgs_paint(screen)
        self.get_locks()



    # ANDA PRO PROXIMO ESTÁGIO SE FOR POSSÍVEL
    def next_stage(self, screen) -> None:
        next_id = load_current_stage(load_current_save())[4] + 1
        if len(load_available_stages(load_current_save())) <= next_id: return False
        if self.player.move_state == 'idle':
            self.player.next_stage()
            self.fix_imgs_paint(screen)
        else: return False

    # ANDA PRO ESTÁGIO ANTERIOR SE POSSÍVEL   
    def prev_stage(self, screen) -> None:
        if self.player.move_state == 'idle':
            self.player.prev_stage()
            self.fix_imgs_paint(screen)
        else: return False

    # DESENHA O MENU QUE MOSTRA AS PROPRIEDADES DAS FASES
    def print_stage_props(self, screen):
        if self.player.move_state != 'idle': return

        # CARREGA AS PROPRIEDADES DA FASE ATUAL
        stage = load_current_stage(load_current_save())

        # O FUNDO DO MENU
        screen.blit(self.stage_menu_bg_img, self.stage_menu_offset)
        # NOME DO LEVEL
        lvl_name = FONT_BUNGEE.render(stage[0], False, 'white')
        screen.blit(lvl_name, self.level_name_pos)
        # MENOR TEMPO
        if stage[3] == '-': lvl_time = FONT_BUNGEE.render(f'{load_current_texts()["best time"]}   ---', False, 'white')
        else: lvl_time = FONT_BUNGEE.render(f'{load_current_texts()["best time"]}:   {stage[3]:.2f}   s', False, 'white')
        screen.blit(lvl_time, self.level_time_pos)
        # MOEDAS
        for i in range(3):
            screen.blit(self.no_coin_img, self.coins_pos[i])

        for i in range(stage[2]):
            screen.blit(self.coin_img, self.coins_pos[i])

    # DESENHA AS IMAGENS QUE NÃO DEVEM MUDAR A CADA FRAME
    def fix_imgs_paint(self, screen) -> None:
        # FUNDO
        screen.blit(self.bg_img, (0,0))

        # SOMBRA DO MAPA
        screen.blit(self.map_shadow_img, self.map_shadow_pos)

        # BORDA DO MAPA
        screen.blit(self.map_border, self.map_border_pos)

        # LOGO
        screen.blit(self.logo_img, self.logo_pos)

    # DESENHA OS TEXTOS DO RODAPÉ
    def print_status_bar(self, screen) -> None:
        save = load_current_save()
        status_bar_txt = FONT_VT323.render(f'{save} - {load_current_texts()["status bar"]}', False, 'black')
        screen.blit(status_bar_txt, self.status_bar_pos)

    # FUNÇÃO QUE CRIA OS SPRITES DOS CADEADOS DOS LVLS
    def get_locks(self):
        lock_pos = self.player.define_lock_positions()
        world = 1
        for i in range(len(lock_pos)):
            if i >= 4: world = 2
            if i >= 8: world = 3
            if i >= 12: world = 4
            self.ilustrations_list.append(StageLock(lock_pos[i], world, i ))
            self.ilustrations_group.add(StageLock(lock_pos[i], world, i ))

    # VERIFICA AS FASES QUE DEVEM ESTAR COM O CADEADO
    def check_lock_show(self):
        for i in self.ilustrations_group:
            if i.type != 'stage lock': continue
            # i.verify_world(self.player.world)p
            i.verify_stage()

    # VERIFICA AS ILUSTRAÇÕES QUE DEVEM SER DESENHADAS
    def check_ilustration_list(self):
        self.ilustrations_group.empty()
        for i in self.ilustrations_list:
            if i.show and i.world == self.player.world: self.ilustrations_group.add(i)

    # ATUALIZA A TELA DE MAP A CADA FRAME
    def update(self, screen) -> None:
        # self.menu.update()
        self.player.update()
        self.ilustrations_group.update()

        # ILUSTRAÇÔES
        self.check_lock_show()
        self.check_ilustration_list()

        self.paint(screen)



    # PINTA TUDO
    def paint(self, screen) -> None:
        # DEFINE O MUNDO E PINTA SEU MAPA
        if self.player.world == 1: screen.blit(self.map_w1, self.map_offset)
        elif self.player.world == 2: screen.blit(self.map_w2, self.map_offset)
        elif self.player.world == 3: screen.blit(self.map_w3, self.map_offset)
        elif self.player.world == 4: screen.blit(self.map_w4, self.map_offset)

        self.print_stage_props(screen)

        self.print_status_bar(screen)

        self.ilustrations_group.draw(screen)

        self.player.group.draw(screen)
        # self.menu.group.draw(screen)
        
class MapPlayer(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, origin):
        super().__init__()
        # INICIALIZAÇÂO

        self.map_origin = origin
        self.width = 64
        self.height = 128
        self.color = 'green'
        self.origin = (0,0)
        self.screen_w = screen_w
        self.screen_h = screen_h

        # PROPRIEDADES
        self.world = 1
        self.stage = 1
        self.level_id = 0
        self.goal_stage = None
        self.goal_distance = 0
        self.facing_right = True
        self.move_state = 'idle'
        self.position = [0, 0]
        self.speed = 0.02 * screen_w
        self.vx = 0
        self.vy = 0

        self.stages = [
            'w1s1',
            'w1s2',
            'w1s3',
            'w1s4',
            'w2s1',
            'w2s2',
            'w2s3',
            'w2s4',
            'w3s1',
            'w3s2',
            'w3s3',
            'w3s4',
            'w4s1',
            'w4s2',
            'w4s3',
            'w4s4',
            'w4s5'
        ]

        self.stages_pos = {
            'w1s1': (self.screen_w * 0.188 + self.map_origin[0], self.screen_h * 0.625 + self.map_origin[1]),
            'w1s2': (self.screen_w * 0.391 + self.map_origin[0], self.screen_h * 0.285 + self.map_origin[1]),
            'w1s3': (self.screen_w * 0.724 + self.map_origin[0], self.screen_h * 0.460 + self.map_origin[1]),
            'w1s4': (self.screen_w * 0.547 + self.map_origin[0], self.screen_h * 0.830 + self.map_origin[1]),
            'w2s1': (self.screen_w * 0.412 + self.map_origin[0], self.screen_h * 0.490 + self.map_origin[1]),
            'w2s2': (self.screen_w * 0.103 + self.map_origin[0], self.screen_h * 0.720 + self.map_origin[1]),
            'w2s3': (self.screen_w * 0.750 + self.map_origin[0], self.screen_h * 0.720 + self.map_origin[1]),
            'w2s4': (self.screen_w * 0.544 + self.map_origin[0], self.screen_h * 0.350 + self.map_origin[1]),
            'w3s1': (self.screen_w * 0.408 + self.map_origin[0], self.screen_h * 0.830 + self.map_origin[1]),
            'w3s2': (self.screen_w * 0.230 + self.map_origin[0], self.screen_h * 0.460 + self.map_origin[1]),
            'w3s3': (self.screen_w * 0.565 + self.map_origin[0], self.screen_h * 0.280 + self.map_origin[1]),
            'w3s4': (self.screen_w * 0.770 + self.map_origin[0], self.screen_h * 0.625 + self.map_origin[1]),
            'w4s1': (self.screen_w * 0.178 + self.map_origin[0], self.screen_h * 0.623 + self.map_origin[1]),
            'w4s2': (self.screen_w * 0.349 + self.map_origin[0], self.screen_h * 0.795 + self.map_origin[1]),
            'w4s3': (self.screen_w * 0.479 + self.map_origin[0], self.screen_h * 0.440 + self.map_origin[1]),
            'w4s4': (self.screen_w * 0.647 + self.map_origin[0], self.screen_h * 0.805 + self.map_origin[1]),
            'w4s5': (self.screen_w * 0.771 + self.map_origin[0], self.screen_h * 0.640 + self.map_origin[1])
        }


        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(bottomleft = self.origin)
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)     

        self.import_images()
        self.define_worl_n_stage()
        
        # PROPRIEDADES DE ANIMAÇÃO
        self.animation_frames = self.idle_animation_r
        self.current_animation_frame = 0
        self.animation_speed = 0.2


    def import_images(self):
        self.idle_animation_r = convert_animation_imgs(ANIMATION_IDLE_R, 0, 1)
        self.run_animation_r  = convert_animation_imgs(ANIMATION_RUN_R, 0, 1)
        self.run_animation_l  = convert_animation_imgs(ANIMATION_RUN_L, 0, 1)

    
    def define_worl_n_stage(self):
        lvl = self.stages[load_current_stage(load_current_save())[4]]
        self.level_id = load_current_stage(load_current_save())[4]
        self.world = int(lvl[1])
        self.stage = int(lvl[3])


    def walk(self):
        if self.goal_stage == None: return
        if self.move_state == 'idle':
            self.move_state = 'runnig'
            dx = self.stages_pos[f'w{self.world}s{self.goal_stage}'][0] - self.stages_pos[f'w{self.world}s{self.stage}'][0]
            dy = self.stages_pos[f'w{self.world}s{self.goal_stage}'][1] - self.stages_pos[f'w{self.world}s{self.stage}'][1]
            self.goal_distance = math.sqrt(dx ** 2 + dy ** 2)
            try:
               alfa = math.atan2(dy, dx)
            except:
               alfa = 0
            self.vx = math.cos(alfa) * self.speed
            self.vy = math.sin(alfa) * self.speed
            self.position[0] += self.vx
            self.position[1] += self.vy
            self.goal_distance -= self.speed
            if dx >= 0: self.facing_right = True
            else: self.facing_right = False
        else:
            if self.goal_distance - self.speed > 0:
                self.position[0] += self.vx
                self.position[1] += self.vy
                self.goal_distance -= self.speed
            else:
                self.position = [self.stages_pos[f'w{self.world}s{self.goal_stage}'][0], self.stages_pos[f'w{self.world}s{self.goal_stage}'][1]]
                self.move_state = 'idle'
                self.stage = self.goal_stage
                self.goal_stage = None
                self.goal_distance = 0
                update_current_stage(load_current_save(), self.level_id)


    def define_position(self):
        if self.move_state == 'idle': self.position = [self.stages_pos[f'w{self.world}s{self.stage}'][0], self.stages_pos[f'w{self.world}s{self.stage}'][1]]
        self.rect = self.image.get_rect(bottomleft = self.position)


    def next_stage(self):
        if self.world != 4:
            if self.stage < 4:
                self.goal_stage = self.stage + 1
                self.level_id += 1
            else:
                self.world += 1
                self.stage = 1
                self.level_id += 1
                update_current_stage(load_current_save(), self.level_id)
        else:
            if self.stage < 5:
                self.goal_stage = self.stage + 1
                self.level_id += 1
            else: return False


    def prev_stage(self):
        if self.world != 1:
            if self.stage > 1:
                self.goal_stage = self.stage - 1
                self.level_id -= 1
            else:
                self.world -= 1
                self.stage = 4
                self.level_id -= 1
                update_current_stage(load_current_save(), self.level_id)
        else:
            if self.stage > 1:
                self.goal_stage = self.stage - 1
                self.level_id -= 1
            else: return False

    def define_lock_positions(self) -> list:
        lock_pos = []
        for s in self.stages:
            lock_pos.append(self.stages_pos[s])
        return lock_pos




    # CONTROLA OS FRAMES DA ANIMAÇÃO ATUAL E ATUALIZA A IMAGEM DO PERSONAGEM
    def animate(self):
        # VERIFICA SE HÁ IMAGENS NA LISTA DE ANIMAÇÃO
        if self.animation_frames:
            if self.current_animation_frame >= len(self.animation_frames): self.current_animation_frame = 0

            self.image = self.animation_frames[int(self.current_animation_frame)]

            self.current_animation_frame += self.animation_speed
        else: 
            self.image = pygame.Surface((self.width, self.height))
            # self.image.fill(self.color)


    # CONTROLA A ANIMAÇÃO QUE DEVE SER UTILIZADA BASEADA NAS INFORMAÇÕES DO PERSONAGEM
    def define_animation_state(self):
            if self.facing_right:
                if self.move_state == 'idle': self.animation_frames = self.idle_animation_r
                elif self.move_state == 'runnig': self.animation_frames = self.run_animation_r
            else:
                if self.move_state == 'idle': self.animation_frames = self.idle_animation_r
                elif self.move_state == 'runnig': self.animation_frames = self.run_animation_l

    # ATUALIZA O PERSONAGEM COMO UM TOD0 CADA FRAME
    def update(self):
        self.walk()
        self.define_position()
        self.define_animation_state()
        self.animate()

                
class MapMenu(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h):
        super().__init__()
        # INICIALIZAÇÂO

        self.width = screen_w
        self.height = 50
        self.border = 5
        self.bg_color = SALMON
        self.fg_color = ORANGE
        self.origin = (0,0)
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.group = pygame.sprite.Group()

        # PROPRIEDADES DO SPRITE (BG)
        self.bg = pygame.sprite.Sprite()
        self.bg.image = pygame.Surface((self.width, self.height))
        self.bg.image.fill(self.bg_color)
        self.bg.rect = self.bg.image.get_rect(topleft = self.origin)
        self.group.add(self.bg)
        # PROPRIEDADES DO SPRITE (FG)
        self.fg = pygame.sprite.Sprite()
        self.fg.image = pygame.Surface((self.width - 2 * self.border, self.height - 2 * self.border))
        self.fg.image.fill(self.fg_color)
        self.fg.rect = self.fg.image.get_rect(topleft = (self.origin[0] + self.border, self.origin[1] + self.border))
        self.group.add(self.fg)
        # PROPRIEDADES DO SPRITE (LB)
        self.lb = pygame.sprite.Sprite()
        self.lb.image = pygame.Surface((self.border, self.screen_h))
        self.lb.image.fill(self.bg_color)
        self.lb.rect = self.lb.image.get_rect(topleft = (self.origin))
        self.group.add(self.lb)
        # PROPRIEDADES DO SPRITE (RB)
        self.rb = pygame.sprite.Sprite()
        self.rb.image = pygame.Surface((self.border, self.screen_h))
        self.rb.image.fill(self.bg_color)
        self.rb.rect = self.rb.image.get_rect(topleft = (self.width - self.border, self.origin[1]))
        self.group.add(self.rb)
        # PROPRIEDADES DO SPRITE (DB)
        self.db = pygame.sprite.Sprite()
        self.db.image = pygame.Surface((self.width, self.border))
        self.db.image.fill(self.bg_color)
        self.db.rect = self.db.image.get_rect(topleft = (self.origin[0], self.screen_h - self.border))
        self.group.add(self.db)

    # ATUALIZA O PERSONAGEM COMO UM TOD0 CADA FRAME
    def update(self):
        pass


# CLASSE DE OBJETO EM GERAL
class MenuIlustration(pygame.sprite.Sprite):
    def __init__(self, pos):
        # INICIALIZAÇÂO
        super().__init__()
        self.pos = pos

        # PROPRIEDADES DO SPRITE
        self.image = pygame.Surface((32,32))
        # self.image.fill('#812F33')
        self.rect = self.image.get_rect(bottomleft = self.pos)

        self.current_animation_frame = 0
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
            # self.image.fill('black')
        
        self.rect = self.image.get_rect(center = self.rect.center)


    def update(self):
        self.animate()


class StageLock(MenuIlustration):
    def __init__(self, pos, world, stage_id):
        super().__init__(pos)

        self.type = 'stage lock'
        self.world = world
        self.stage_id = stage_id
        self.size = 64
        self.animation_frames = convert_animation_imgs(ANIMATION_LOCK, 0, self.size/64) 
        self.show = True
    
    def verify_world(self, world):
        if world == self.world: self.show = True
        else: self.show = False

    def verify_stage(self):
        stages = load_available_stages(load_current_save())
        if self.stage_id >= len(stages): self.show = True
        else: self.show = False










