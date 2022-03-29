# IMPORTA OS ARQUIVOS USADOS
from CONFIG_colors import *
from CONFIG_fonts import *
from CONFIG_game import *
from GAME_levels import level_list
from GAME_functions import *
from PREFAB_main_menu import MainMenu
from PREFAB_player import Player
from PREFAB_map_screen import *
from PREFAB_b_screen import *
from PREFAB_c_screen import *
from PREFAB_e_screen import *
from PREFAB_t_screen import *
from PREFAB_level import Level
from ASSETS_player import SFX_BEEP, set_p_volume, mute_p_volume
from ASSETS_boss import set_b_volume, mute_b_volume
from ASSETS_enemys import set_e_volume, mute_e_volume
import PyInstaller
''

try:
    import pyi_splash
    pyi_splash.close()
except:
    pass


# IMPORTA AS BIBLIOTECS USADAS
import pygame
import math
import ctypes




muted = False
music_muted = False

pygame.init()
pygame.mixer.init()
pygame.font.init()


def init_game():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    global GAME_SCREEN_H, GAME_SCREEN_W, STORY_FONT, BOMB_COUNT_FONT, FUEL_COUNT_FONT, TIME_COUNT_FONT, clock, game_screen, game_on, game_paused, victory_screen_on, start_screen_on, save, continue_playing, muted, music_muted

    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)
    GAME_SCREEN_H = user32.GetSystemMetrics(1)

    set_b_volume()
    set_p_volume()
    set_e_volume()

    
    # FONTES
    STORY_FONT = pygame.font.SysFont('Comic Sans MS', 30)
    BOMB_COUNT_FONT = pygame.font.SysFont('Comic Sans MS', 22)
    FUEL_COUNT_FONT = pygame.font.SysFont('Comic Sans MS', 20)
    TIME_COUNT_FONT = pygame.font.SysFont('Consolas', 15)


    # INICIA E CONFIGURA A JANELA E AS CONFIGURAÇÕES BASICAS DO JOGO
    save = load_current_save()
    game_screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
    icon = convert_img('./resources/ilustrations/icone_grande.png', 0, 1)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Invaders on the Court')
    # game_screen = pygame.display.set_mode([GAME_SCREEN_W, GAME_SCREEN_H])
    clock = pygame.time.Clock()
    game_on = True
    game_paused = False
    victory_screen_on = True
    start_screen_on = True
    continue_playing = True


    # ESCONDE O MOUSE
    pygame.mouse.set_visible(False)

    # b_screen()
    # map_screen()
        # ---- TOCA A MUSICA
    music = './resources/music/CHILL.mp3'
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.5)
    if not music_muted: pygame.mixer.music.play(-1)
    main_menu()


def main_menu() -> None:
    clock = pygame.time.Clock()
    on_menu = True

    global muted, music_muted


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)
    GAME_SCREEN_H = user32.GetSystemMetrics(1)


    # INICIA UMA SPRITE DO PLAYER NO MAPA
    menu = MainMenu(GAME_SCREEN_W, GAME_SCREEN_H)
    

    # LOOP DA TELA DO MAPA
    while on_menu:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                on_map = False

            # REDIMENSIONAMENTO DA JANELA
            elif e.type == pygame.VIDEORESIZE:
                GAME_SCREEN_W = e.w
                GAME_SCREEN_H = e.h
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    pygame.mixer.stop()
                    click = menu.click()
                    if click == 'play': map_screen()
                    elif click == 'credits': c_screen()
                    elif click == 'quit': on_menu = False
                elif e.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    on_menu = False
                elif e.key == pygame.K_DOWN:
                    SFX_BEEP.play()
                    menu.next_index()
                elif e.key == pygame.K_UP:
                    SFX_BEEP.play()
                    menu.prev_index()
                elif e.key == pygame.K_LEFT:
                    SFX_BEEP.play()
                    menu.left_click()
                elif e.key == pygame.K_RIGHT:
                    SFX_BEEP.play()
                    menu.right_click()
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()

                # elif e.key == pygame.K_UP: 
                #     if current_world < 4: current_world += 1 
                # elif e.key == pygame.K_DOWN: 
                #     if current_world > 0: current_world -= 1 



  
   
        # PINTA A TELA
        
        # BACKGROUND


        # ATUALIZA O MAP PLAYER
        menu.update(game_screen)



        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)

    pygame.quit()
    

def map_screen() -> None:
    clock = pygame.time.Clock()
    on_map = True

    global muted, music_muted


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)
    GAME_SCREEN_H = user32.GetSystemMetrics(1)


    # INICIA UMA SPRITE DO PLAYER NO MAPA
    map_screen = MapScreen(GAME_SCREEN_W, GAME_SCREEN_H, game_screen)
    

    # LOOP DA TELA DO MAPA
    while on_map:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                on_map = False

            # REDIMENSIONAMENTO DA JANELA
            elif e.type == pygame.VIDEORESIZE:
                GAME_SCREEN_W = e.w
                GAME_SCREEN_H = e.h
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    pygame.mixer.stop()
                    if not music_muted: pygame.mixer.music.fadeout(2000)
                    b_screen()
                    map_screen.player.define_worl_n_stage()
                    map_screen.fix_imgs_paint(game_screen)
                    if not music_muted:pygame.mixer.music.fadeout(2000)
                    # ---- TOCA A MUSICA
                    music = './resources/music/CHILL.mp3'
                    pygame.mixer.music.load(music)
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    if music_muted: pygame.mixer.music.pause()
                elif e.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    on_map = False
                # elif e.key == pygame.K_UP: 
                #     if current_world < 4: current_world += 1 
                # elif e.key == pygame.K_DOWN: 
                #     if current_world > 0: current_world -= 1 
                elif e.key == pygame.K_RIGHT:
                    # SFX_BEEP.play()
                    map_screen.next_stage(game_screen)
                elif e.key == pygame.K_LEFT:
                    # SFX_BEEP.play()
                    map_screen.prev_stage(game_screen)
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()
   
        # PINTA A TELA
        
        # BACKGROUND


        # ATUALIZA O MAP PLAYER
        map_screen.update(game_screen)



        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)


# FUNÇÃO QUE RODA A TELA DO INÍCIO E INICIA O LEVEL
def b_screen():

    global muted, music_muted


    # DEFINE O LEVEL ATUAL
    lvl = level_list[load_current_stage(load_current_save())[4]]

    # INICIALIZA O LEVEL ATUAL
    current_lvl = Level(lvl['id'], lvl['name'], lvl['layout'], lvl['tile_family'],
     lvl['ground_tile'], lvl['killer_tile'], lvl['tile_size'], lvl['music'], lvl['music_volume'], lvl['b_texts'], lvl['e_texts'],
     lvl['b_img'], lvl['e_img'], lvl['tutorial'])
    pygame.mixer.music.load(current_lvl.music)
    pygame.mixer.music.set_volume(current_lvl.music_volume)


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)  
    GAME_SCREEN_H = user32.GetSystemMetrics(1)

    # PRÉ GAME
    clock = pygame.time.Clock()
    start_screen_on = True
    continue_playing = True

    # INICIA UMA TELA DE INICIO DE JOGO
    pre_lvl_screen = BeginScreen(GAME_SCREEN_W, GAME_SCREEN_H, current_lvl.b_texts, current_lvl.b_img)


    # GROUPS
    # --PLAYER GROUP
    player = pygame.sprite.GroupSingle()
    player.add(Player(current_lvl))
    pygame.mixer.music.play(-1)
    if music_muted: pygame.mixer.music.pause()


    # COLOCA A JANELA EM TELA CHEIA E ATUALIZA
    player.sprite.update_window_info(pygame.display.Info().current_w, pygame.display.Info().current_h)

    # LOOP DA TELA DE VITÓRIA
    while start_screen_on:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                start_screen_on = False

            # REDIMENSIONAMENTO DA JANELA
            elif e.type == pygame.VIDEORESIZE:
                GAME_SCREEN_W = e.w
                GAME_SCREEN_H = e.h
                player.sprites()[0].update_window_info(e.w, e.h)
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    start_screen_on = False
                elif e.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    start_screen_on = False
                    continue_playing = False
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()
  
   
        # PINTA A TELA
        pre_lvl_screen.paint(game_screen)


        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)
    
    # MOSTRAS OS TUTORIAIS
    for t in current_lvl.tutorial:
        t_screen(t)

    if continue_playing: play_game(current_lvl, player)


# FUNÇÃO QUE INICIA E RODA O JOGO
def play_game(lvl, player):

    clock = pygame.time.Clock()
    game_on = True
    game_paused = False

    global muted, music_muted


    # Eventos personalizados
    COUNT_1S = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT_1S, 200)
    FPS_COUNT = 0
    LAST_FPS = 30

    # CABEÇALHO
    interface = convert_img('./resources/ilustrations/inteface.png', 0, 1)
    interface_2 = convert_img('./resources/ilustrations/interface2.png', 0, 1)
    coin_collected = convert_img('./resources/ilustrations/coin.png', 0, 1)
    header_margin = (10,10)
    no_ball_interface = convert_img('./resources/ilustrations/no_ball_interface.png', 0, 1)
    bomb_img = convert_img('./resources/objects/imgs/bomb/bomb1.png', 0, 1.5)
    pause_art = pygame.sprite.Sprite()
    pause_art.image = convert_img('./resources/ilustrations/PAUSE.png', 0, 1.5)
    pause_art.rect = pause_art.image.get_rect(center = [player.sprite.screen_w / 2, player.sprite.screen_h / 2])
    pause_screen = pygame.sprite.GroupSingle()
    pause_screen.add(pause_art)

    # BACKGROUND
    horizon = pygame.transform.scale(convert_img(f'./resources/map/horizon/{lvl.tile_family}.png', 0, 1),(player.sprite.screen_w, player.sprite.screen_h))
    
    bg_image1 = pygame.transform.scale(convert_img(f'./resources/map/background/{lvl.tile_family}.png', 0, 1),(player.sprite.screen_w, player.sprite.screen_h))
    bg_image2 = pygame.transform.scale(convert_img(f'./resources/map/background/{lvl.tile_family}.png', 0, 1),(player.sprite.screen_w, player.sprite.screen_h))
    bg_width = bg_image1.get_width()
    bg_height = bg_image1.get_height()

    # LOOP DO JOGO
    while game_on:

        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                game_on = False

            # EVENTO DE 1 SEGUNDO PARA CONTAR O FPS
            elif e.type == COUNT_1S:
                LAST_FPS = FPS_COUNT * 5
                FPS_COUNT = 0

            # REDIMENSIONAMENTO DA JANELA
            elif e.type == pygame.VIDEORESIZE:
                GAME_SCREEN_W = e.w
                GAME_SCREEN_H = e.h
                player.sprites()[0].update_window_info(e.w, e.h)

            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if game_paused:
                        pygame.mixer.stop()
                        SFX_BEEP.play()
                        game_on = False
                    else: game_paused = True
                elif not game_paused and e.key == pygame.K_RETURN:
                    SFX_BEEP.play()
                    game_paused = True
                elif game_paused and e.key == pygame.K_RETURN:
                    SFX_BEEP.play()
                    game_paused = False
                elif e.key == pygame.K_x: player.sprites()[0].reset()
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    if player.sprites()[0].action == 'passing' or player.sprites()[0].action == 'throwing':
                        player.sprites()[0].on_action = False
                        player.sprites()[0].current_animation_frame = 0
                        player.sprites()[0].action_recovery_time = 0
                if e.key == pygame.K_w:
                    if player.sprites()[0].action == 'bombing':
                        player.sprites()[0].on_action = False
                        player.sprites()[0].current_animation_frame = 0
                        player.sprites()[0].action_recovery_time = 0

            


        # VERIFIA SE O JOGO ESTÁ PAUSADO
        if game_paused:
            pause_screen.draw(game_screen)
            pygame.display.update()
            clock.tick(FPS)
            continue

            

        # VERIFICA SE O JOGO ACABOU PELO PLAYER
        if not player.sprite.game_on: game_on = False

            
        # PINTA A TELA
        
        # HORIZON
        game_screen.blit(horizon, (0,0))

        # BACKGROUND
        i = math.trunc(-player.sprite.bg_pan[0] / bg_width)
	# BG POR DE BAIXO
        game_screen.blit(bg_image1, [i * bg_width + player.sprite.bg_pan[0], player.sprites()[0].screen_h - bg_height])
        game_screen.blit(bg_image2, [bg_width + i * bg_width + player.sprite.bg_pan[0], player.sprites()[0].screen_h - bg_height])
	# BG POR DE CIMA
        game_screen.blit(bg_image1, [i * bg_width + player.sprite.bg_pan[0], 0])
        game_screen.blit(bg_image2, [bg_width + i * bg_width + player.sprite.bg_pan[0], 0])
        



        # PLAYER
        player.update(game_screen)

        # CABEÇALHO

        ### INTERFACE DA ESQUERDA

        bomb_count = BOMB_COUNT_FONT.render(f'{player.sprite.bombs_on_bag}', False, SALMON)
        bomb_count_shadow = BOMB_COUNT_FONT.render(f'{player.sprite.bombs_on_bag}', False, 'black')
        laser_count = FUEL_COUNT_FONT.render(f'{int(player.sprite.laser_fuel)}%', False, SALMON)
        laser_count_shadow = FUEL_COUNT_FONT.render(f'{int(player.sprite.laser_fuel)}%', False, 'black')
        steroid_count = FUEL_COUNT_FONT.render(f'{int(player.sprite.god_mode_fuel)}%', False, SALMON)
        steroid_count_shadow = FUEL_COUNT_FONT.render(f'{int(player.sprite.god_mode_fuel)}%', False, 'black')


        game_screen.blit(interface, [0,0])

        if not player.sprite.ball_on_bag:
            game_screen.blit(no_ball_interface, (5,5))

        game_screen.blit(bomb_count_shadow,(80, 10))
        game_screen.blit(bomb_count,(80, 8))

        game_screen.blit(laser_count_shadow,(150, 10))
        game_screen.blit(laser_count,(150, 8))

        game_screen.blit(steroid_count_shadow,(245, 10))
        game_screen.blit(steroid_count,(245, 8))

        ### INTERFACE DA DIREITA
        game_screen.blit(interface_2, [player.sprite.screen_w - interface_2.get_width(),0])

        if player.sprite.coins_collecteds >= 1: game_screen.blit(coin_collected, (player.sprite.screen_w - 136, 45))
        if player.sprite.coins_collecteds >= 2: game_screen.blit(coin_collected, (player.sprite.screen_w - 119, 45))
        if player.sprite.coins_collecteds >= 3: game_screen.blit(coin_collected, (player.sprite.screen_w - 102, 45))


        time_txt = TIME_COUNT_FONT.render(f'Time: {player.sprite.time:.2f}', False, SALMON)
        time_txt_shadow = TIME_COUNT_FONT.render(f'Time: {player.sprite.time:.2f}', False, 'black')
        fps_txt = TIME_COUNT_FONT.render(f'FPS:{LAST_FPS:.0f}', False, SALMON)
        fps_txt_shadow = TIME_COUNT_FONT.render(f'FPS:{LAST_FPS:.0f}', False, 'black')

        game_screen.blit(fps_txt_shadow,(player.sprite.screen_w - 62, 44))
        game_screen.blit(fps_txt,(player.sprite.screen_w - 61, 45))
        game_screen.blit(time_txt_shadow,(player.sprite.screen_w - 135, 9))
        game_screen.blit(time_txt,(player.sprite.screen_w - 134, 10))

        # ATUALIZA O DISPLAY
        pygame.display.update()


        # CONTA O FPS REAL
        FPS_COUNT += 1
        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)



    # RODA A TELA DE FIM DE LEVEL SE O A FASE FOI CONCLUIDA
    if player.sprite.stage_clear: e_screen(player, lvl)


# FUNÇÃO QUE RODA A TELA DE FIM DO LEVEL
def e_screen(player, lvl):

    clock = pygame.time.Clock()
    victory_screen_on = True

    global muted, music_muted


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)
    GAME_SCREEN_H = user32.GetSystemMetrics(1)

    post_game_screen = EndScreen(GAME_SCREEN_W, GAME_SCREEN_H, lvl.e_texts,  lvl.e_img)

    # STAGE CLEAR

    # ATUALIZA O SAVE
    update_save(load_current_save(), lvl.id, player.sprite.coins_collecteds, player.sprite.time)

    # LOOP DA TELA DE VITÓRIA
    while victory_screen_on:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                victory_screen_on = False

            # REDIMENSIONAMENTO DA JANELA
            elif e.type == pygame.VIDEORESIZE:
                GAME_SCREEN_W = e.w
                GAME_SCREEN_H = e.h
                player.sprites()[0].update_window_info(e.w, e.h)
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    victory_screen_on = False
                elif e.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    victory_screen_on = False
                    continue_playing = False
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()


        # PINTA A TELA
        post_game_screen.paint(game_screen)



        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)


# FUNÇÃO QUE RODA A TELA DO INÍCIO E INICIA O LEVEL
def t_screen(tutorial: int):

    global muted, music_muted


    # DEFINE O LEVEL ATUAL


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)  
    GAME_SCREEN_H = user32.GetSystemMetrics(1)

    # PRÉ GAME
    clock = pygame.time.Clock()
    tutorial_screen_on = True
    continue_playing = True

    # INICIA UMA TELA DE TUTORIAL
    tutorial_screen = TutorialScreen(GAME_SCREEN_W, GAME_SCREEN_H, tutorial)



    # LOOP DA TELA DE VITÓRIA
    while tutorial_screen_on:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                tutorial_screen_on = False
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    tutorial_screen_on = False
                elif e.key == pygame.K_ESCAPE:
                    pygame.mixer.stop()
                    SFX_BEEP.play()
                    tutorial_screen_on = False
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()
  
   
        # PINTA A TELA
        tutorial_screen.paint(game_screen)


        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)


# FUNÇÃO QUE RODA A TELA DE CREDITOS
def c_screen():
    
    global muted, music_muted


    # DEFINE O LEVEL ATUAL


    # TAMANHO DA TELA
    user32 = ctypes.windll.user32
    GAME_SCREEN_W = user32.GetSystemMetrics(0)  
    GAME_SCREEN_H = user32.GetSystemMetrics(1)

    # PRÉ GAME
    clock = pygame.time.Clock()
    credits_screen_on = True

    # INICIA UMA TELA DE TUTORIAL
    credits_screen = CreditsScreen(GAME_SCREEN_W, GAME_SCREEN_H)



    # LOOP DA TELA DE VITÓRIA
    while credits_screen_on:
        
        # LISTA DE EVENTOS
        for e in pygame.event.get():

            # BOTÂO DE SAIR (X)
            if e.type == pygame.QUIT:
                credits_screen_on = False
            
            # BOTÕES DO TECLADO
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    SFX_BEEP.play()
                    credits_screen_on = False
                elif e.key == pygame.K_m:
                    if muted:
                        muted = False
                        set_b_volume()
                        set_e_volume()
                        set_p_volume()
                    else:
                        muted = True
                        mute_b_volume()
                        mute_e_volume()
                        mute_p_volume()
                elif e.key == pygame.K_n:
                    if music_muted:
                        music_muted = False
                        pygame.mixer.music.unpause()
                    else:
                        music_muted = True
                        pygame.mixer.music.pause()
  
   
        # PINTA A TELA
        credits_screen.paint(game_screen)


        # ATUALIZA O DISPLAY
        pygame.display.update()


        # DEFINE A QUANTIDADE DE FRAMES POR SEGUNDO
        clock.tick(FPS)


######## RODA O JOGO ########
init_game()
 