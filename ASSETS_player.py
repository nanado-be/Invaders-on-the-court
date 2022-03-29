import pygame
pygame.init()
pygame.mixer.init()

# ANIMATIONS IMAGES
ANIMATION_IDLE_R = [
    './resources/player/imgs/rigth/idle/Idle1.png',
    './resources/player/imgs/rigth/idle/Idle2.png',
    './resources/player/imgs/rigth/idle/Idle3.png',
    './resources/player/imgs/rigth/idle/Idle4.png',
    './resources/player/imgs/rigth/idle/Idle5.png',
    './resources/player/imgs/rigth/idle/Idle6.png',
    './resources/player/imgs/rigth/idle/Idle7.png',
    './resources/player/imgs/rigth/idle/Idle8.png',
    './resources/player/imgs/rigth/idle/Idle9.png'
]

ANIMATION_IDLE_L = [
    './resources/player/imgs/left/idle/Idle_left1.png',
    './resources/player/imgs/left/idle/Idle_left2.png',
    './resources/player/imgs/left/idle/Idle_left3.png',
    './resources/player/imgs/left/idle/Idle_left4.png',
    './resources/player/imgs/left/idle/Idle_left5.png',
    './resources/player/imgs/left/idle/Idle_left6.png',
    './resources/player/imgs/left/idle/Idle_left7.png',
    './resources/player/imgs/left/idle/Idle_left8.png',
    './resources/player/imgs/left/idle/Idle_left9.png'
]

ANIMATION_RUN_R = [
    './resources/player/imgs/rigth/run/run1.png',
    './resources/player/imgs/rigth/run/run2.png',
    './resources/player/imgs/rigth/run/run3.png',
    './resources/player/imgs/rigth/run/run4.png',
    './resources/player/imgs/rigth/run/run5.png',
    './resources/player/imgs/rigth/run/run6.png',
    './resources/player/imgs/rigth/run/run7.png',
    './resources/player/imgs/rigth/run/run8.png',
    './resources/player/imgs/rigth/run/run9.png',
    './resources/player/imgs/rigth/run/run10.png'
]

ANIMATION_RUN_L = [
    './resources/player/imgs/left/run/run1.png',
    './resources/player/imgs/left/run/run2.png',
    './resources/player/imgs/left/run/run3.png',
    './resources/player/imgs/left/run/run4.png',
    './resources/player/imgs/left/run/run5.png',
    './resources/player/imgs/left/run/run6.png',
    './resources/player/imgs/left/run/run7.png',
    './resources/player/imgs/left/run/run8.png',
    './resources/player/imgs/left/run/run9.png',
    './resources/player/imgs/left/run/run10.png'
]

ANIMATION_JUMP_R = [
    './resources/player/imgs/rigth/jump/jump1.png',
    './resources/player/imgs/rigth/jump/jump2.png'
]

ANIMATION_JUMP_L = [
    './resources/player/imgs/left/jump/jump1.png',
    './resources/player/imgs/left/jump/jump2.png'
]

ANIMATION_FALL_R = [
    './resources/player/imgs/rigth/fall/fall1.png',
    './resources/player/imgs/rigth/fall/fall2.png'
]

ANIMATION_FALL_L = [
    './resources/player/imgs/left/fall/fall1.png',
    './resources/player/imgs/left/fall/fall2.png'
]

ANIMATION_SLIDE_R = [
    './resources/player/imgs/rigth/slide/slide1.png',
    # './resources/player/imgs/rigth/slide/slide2.png',
    './resources/player/imgs/rigth/slide/slide3.png',
    # './resources/player/imgs/rigth/slide/slide4.png',
    './resources/player/imgs/rigth/slide/slide5.png',
    # './resources/player/imgs/rigth/slide/slide6.png',
    './resources/player/imgs/rigth/slide/slide7.png',
    # './resources/player/imgs/rigth/slide/slide8.png',
    # './resources/player/imgs/rigth/slide/slide9.png',
    './resources/player/imgs/rigth/slide/slide10.png'
]

ANIMATION_SLIDE_L = [
    './resources/player/imgs/left/slide/slide1.png',
    # './resources/player/imgs/left/slide/slide2.png',
    './resources/player/imgs/left/slide/slide3.png',
    # './resources/player/imgs/left/slide/slide4.png',
    './resources/player/imgs/left/slide/slide5.png',
    # './resources/player/imgs/left/slide/slide6.png',
    './resources/player/imgs/left/slide/slide7.png',
    # './resources/player/imgs/left/slide/slide8.png',
    # './resources/player/imgs/left/slide/slide9.png',
    './resources/player/imgs/left/slide/slide10.png'
]

ANIMATION_BOMB_BALL = [
    './resources/objects/imgs/bomb_ball/Sprite-0001.png',
    './resources/objects/imgs/bomb_ball/Sprite-0002.png',
    './resources/objects/imgs/bomb_ball/Sprite-0003.png',
    './resources/objects/imgs/bomb_ball/Sprite-0004.png'
]

ANIMATION_BOUNCE_BALL = [
    './resources/objects/imgs/bounce_ball/bouce_ball1.png',
    './resources/objects/imgs/bounce_ball/bouce_ball2.png',
    './resources/objects/imgs/bounce_ball/bouce_ball3.png',
    './resources/objects/imgs/bounce_ball/bouce_ball4.png',
    './resources/objects/imgs/bounce_ball/bouce_ball5.png',
    './resources/objects/imgs/bounce_ball/bouce_ball6.png'
]

ANIMATION_ENERGY_BALL = [
    './resources/objects/imgs/energy_ball/energy_ball1.png',
    './resources/objects/imgs/energy_ball/energy_ball2.png',
    './resources/objects/imgs/energy_ball/energy_ball3.png',
    './resources/objects/imgs/energy_ball/energy_ball4.png',
    './resources/objects/imgs/energy_ball/energy_ball5.png',
    './resources/objects/imgs/energy_ball/energy_ball6.png',
    './resources/objects/imgs/energy_ball/energy_ball7.png',
    './resources/objects/imgs/energy_ball/energy_ball8.png',
    './resources/objects/imgs/energy_ball/energy_ball9.png',
    './resources/objects/imgs/energy_ball/energy_ball10.png',
    './resources/objects/imgs/energy_ball/energy_ball11.png',
    './resources/objects/imgs/energy_ball/energy_ball12.png',
    './resources/objects/imgs/energy_ball/energy_ball13.png',
    './resources/objects/imgs/energy_ball/energy_ball14.png',
    './resources/objects/imgs/energy_ball/energy_ball15.png',
    './resources/objects/imgs/energy_ball/energy_ball16.png',
    './resources/objects/imgs/energy_ball/energy_ball17.png',
]

ANIMATION_GOD_MODE_ENERGY = [
    './resources/objects/imgs/god_energy/energy1.png',
    './resources/objects/imgs/god_energy/energy2.png',
    './resources/objects/imgs/god_energy/energy3.png',
    './resources/objects/imgs/god_energy/energy4.png'
]

ANIMATION_THROW_HIGH_R = [
    './resources/player/imgs/rigth/throw/shot1.png',
    './resources/player/imgs/rigth/throw/shot2.png',
    './resources/player/imgs/rigth/throw/shot3.png',
    './resources/player/imgs/rigth/throw/shot4.png',
    './resources/player/imgs/rigth/throw/shot5.png',
    './resources/player/imgs/rigth/throw/shot6.png'
]

ANIMATION_THROW_HIGH_L = [
    './resources/player/imgs/left/throw/shot1.png',
    './resources/player/imgs/left/throw/shot2.png',
    './resources/player/imgs/left/throw/shot3.png',
    './resources/player/imgs/left/throw/shot4.png',
    './resources/player/imgs/left/throw/shot5.png',
    './resources/player/imgs/left/throw/shot6.png'
]

ANIMATION_THROW_LOW_R = [
    './resources/player/imgs/rigth/throw_low/shot1.png',
    './resources/player/imgs/rigth/throw_low/shot2.png',
    './resources/player/imgs/rigth/throw_low/shot3.png',
    './resources/player/imgs/rigth/throw_low/shot4.png',
    './resources/player/imgs/rigth/throw_low/shot5.png',
    './resources/player/imgs/rigth/throw_low/shot6.png'
]

ANIMATION_THROW_LOW_L = [   
    './resources/player/imgs/left/throw_low/shot1.png',
    './resources/player/imgs/left/throw_low/shot2.png',
    './resources/player/imgs/left/throw_low/shot3.png',
    './resources/player/imgs/left/throw_low/shot4.png',
    './resources/player/imgs/left/throw_low/shot5.png',
    './resources/player/imgs/left/throw_low/shot6.png'
]

ANIMATION_THROW_BOMB_R = [
    './resources/player/imgs/rigth/throw_bomb/shot1.png',
    './resources/player/imgs/rigth/throw_bomb/shot2.png',
    './resources/player/imgs/rigth/throw_bomb/shot3.png',
    './resources/player/imgs/rigth/throw_bomb/shot4.png',
    './resources/player/imgs/rigth/throw_bomb/shot5.png',
    './resources/player/imgs/rigth/throw_bomb/shot6.png'
]

ANIMATION_THROW_BOMB_L = [   
    './resources/player/imgs/left/throw_bomb/shot1.png',
    './resources/player/imgs/left/throw_bomb/shot2.png',
    './resources/player/imgs/left/throw_bomb/shot3.png',
    './resources/player/imgs/left/throw_bomb/shot4.png',
    './resources/player/imgs/left/throw_bomb/shot5.png',
    './resources/player/imgs/left/throw_bomb/shot6.png'
]

ANIMATION_SHOOT_R = [
    './resources/player/imgs/rigth/shoot/shoot1.png',
    './resources/player/imgs/rigth/shoot/shoot2.png',
    './resources/player/imgs/rigth/shoot/shoot3.png',
    './resources/player/imgs/rigth/shoot/shoot4.png',
    './resources/player/imgs/rigth/shoot/shoot5.png'
]

ANIMATION_SHOOT_L = [
    './resources/player/imgs/left/shoot/shoot1.png',
    './resources/player/imgs/left/shoot/shoot2.png',
    './resources/player/imgs/left/shoot/shoot3.png',
    './resources/player/imgs/left/shoot/shoot4.png',
    './resources/player/imgs/left/shoot/shoot5.png'
]

ANIMATION_SHOOT_N_RUN_R = [
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run2.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run3.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run4.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run5.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run6.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run7.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run8.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run9.png',
    './resources/player/imgs/rigth/shoot_n_run/shoot_n_run10.png'
]

ANIMATION_SHOOT_N_RUN_L = [
    './resources/player/imgs/left/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run2.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run3.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run4.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run5.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run6.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run7.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run8.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run9.png',
    './resources/player/imgs/left/shoot_n_run/shoot_n_run10.png'
]

ANIMATION_JUMP_N_SHOOT_R = [
    './resources/player/imgs/rigth/shoot_n_jump/jump_n_shoot1.png',
    './resources/player/imgs/rigth/shoot_n_jump/jump_n_shoot2.png',
    './resources/player/imgs/rigth/shoot_n_jump/jump_n_shoot3.png',
    './resources/player/imgs/rigth/shoot_n_jump/jump_n_shoot4.png',
    './resources/player/imgs/rigth/shoot_n_jump/jump_n_shoot5.png'
]

ANIMATION_JUMP_N_SHOOT_L = [
    './resources/player/imgs/left/shoot_n_jump/jump_n_shoot1.png',
    './resources/player/imgs/left/shoot_n_jump/jump_n_shoot2.png',
    './resources/player/imgs/left/shoot_n_jump/jump_n_shoot3.png',
    './resources/player/imgs/left/shoot_n_jump/jump_n_shoot4.png',
    './resources/player/imgs/left/shoot_n_jump/jump_n_shoot5.png'
]

ANIMATION_ENERGY_R = [
    './resources/player/imgs/rigth/energy/energy1.png',
    './resources/player/imgs/rigth/energy/energy2.png',
    './resources/player/imgs/rigth/energy/energy3.png',
    './resources/player/imgs/rigth/energy/energy4.png',
    './resources/player/imgs/rigth/energy/energy5.png',
    './resources/player/imgs/rigth/energy/energy6.png',
    './resources/player/imgs/rigth/energy/energy7.png',
    './resources/player/imgs/rigth/energy/energy8.png',
    './resources/player/imgs/rigth/energy/energy9.png',
    './resources/player/imgs/rigth/energy/energy10.png',
    './resources/player/imgs/rigth/energy/energy11.png',
    './resources/player/imgs/rigth/energy/energy12.png',
]

ANIMATION_ENERGY_L = [
    './resources/player/imgs/left/energy/energy1.png',
    './resources/player/imgs/left/energy/energy2.png',
    './resources/player/imgs/left/energy/energy3.png',
    './resources/player/imgs/left/energy/energy4.png',
    './resources/player/imgs/left/energy/energy5.png',
    './resources/player/imgs/left/energy/energy6.png',
    './resources/player/imgs/left/energy/energy7.png',
    './resources/player/imgs/left/energy/energy8.png',
    './resources/player/imgs/left/energy/energy9.png',
    './resources/player/imgs/left/energy/energy10.png',
    './resources/player/imgs/left/energy/energy11.png',
    './resources/player/imgs/left/energy/energy12.png',
]

ANIMATION_DUCK_R = [
    './resources/player/imgs/rigth/duck/duck1.png',
    './resources/player/imgs/rigth/duck/duck2.png',
    './resources/player/imgs/rigth/duck/duck3.png',
    './resources/player/imgs/rigth/duck/duck4.png'
]

ANIMATION_DUCK_L = [
    './resources/player/imgs/left/duck/duck1.png',
    './resources/player/imgs/left/duck/duck2.png',
    './resources/player/imgs/left/duck/duck3.png',
    './resources/player/imgs/left/duck/duck4.png'
]

ANIMATION_DUCK_WALK_R = [
    './resources/player/imgs/rigth/duck_walk/duck_walk1.png',
    './resources/player/imgs/rigth/duck_walk/duck_walk2.png',
    './resources/player/imgs/rigth/duck_walk/duck_walk3.png',
    './resources/player/imgs/rigth/duck_walk/duck_walk4.png'
]

ANIMATION_DUCK_WALK_L = [
    './resources/player/imgs/left/duck_walk/duck_walk1.png',
    './resources/player/imgs/left/duck_walk/duck_walk2.png',
    './resources/player/imgs/left/duck_walk/duck_walk3.png',
    './resources/player/imgs/left/duck_walk/duck_walk4.png'
]

ANIMATION_DUCK_SHOOT_R = [
    './resources/player/imgs/rigth/duck_shoot/shoot1.png',
    './resources/player/imgs/rigth/duck_shoot/shoot2.png',
    './resources/player/imgs/rigth/duck_shoot/shoot3.png',
    './resources/player/imgs/rigth/duck_shoot/shoot4.png',
    './resources/player/imgs/rigth/duck_shoot/shoot5.png'
]

ANIMATION_DUCK_SHOOT_L = [
    './resources/player/imgs/left/duck_shoot/shoot1.png',
    './resources/player/imgs/left/duck_shoot/shoot2.png',
    './resources/player/imgs/left/duck_shoot/shoot3.png',
    './resources/player/imgs/left/duck_shoot/shoot4.png',
    './resources/player/imgs/left/duck_shoot/shoot5.png'
]


###### SEM BOLA ######

ANIMATION_IDLE_NB_R = [
    './resources/player/imgs/no_ball_rigth/idle/Idle1.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle2.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle3.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle4.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle5.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle6.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle7.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle8.png',
    './resources/player/imgs/no_ball_rigth/idle/Idle9.png'
]

ANIMATION_IDLE_NB_L = [
    './resources/player/imgs/no_ball_left/idle/Idle1.png',
    './resources/player/imgs/no_ball_left/idle/Idle2.png',
    './resources/player/imgs/no_ball_left/idle/Idle3.png',
    './resources/player/imgs/no_ball_left/idle/Idle4.png',
    './resources/player/imgs/no_ball_left/idle/Idle5.png',
    './resources/player/imgs/no_ball_left/idle/Idle6.png',
    './resources/player/imgs/no_ball_left/idle/Idle7.png',
    './resources/player/imgs/no_ball_left/idle/Idle8.png',
    './resources/player/imgs/no_ball_left/idle/Idle9.png'
]

ANIMATION_RUN_NB_R = [
    './resources/player/imgs/no_ball_rigth/run/run1.png',
    './resources/player/imgs/no_ball_rigth/run/run2.png',
    './resources/player/imgs/no_ball_rigth/run/run3.png',
    './resources/player/imgs/no_ball_rigth/run/run4.png',
    './resources/player/imgs/no_ball_rigth/run/run5.png',
    './resources/player/imgs/no_ball_rigth/run/run6.png',
    './resources/player/imgs/no_ball_rigth/run/run7.png',
    './resources/player/imgs/no_ball_rigth/run/run8.png',
    './resources/player/imgs/no_ball_rigth/run/run9.png',
    './resources/player/imgs/no_ball_rigth/run/run10.png'
]

ANIMATION_RUN_NB_L = [
    './resources/player/imgs/no_ball_left/run/run1.png',
    './resources/player/imgs/no_ball_left/run/run2.png',
    './resources/player/imgs/no_ball_left/run/run3.png',
    './resources/player/imgs/no_ball_left/run/run4.png',
    './resources/player/imgs/no_ball_left/run/run5.png',
    './resources/player/imgs/no_ball_left/run/run6.png',
    './resources/player/imgs/no_ball_left/run/run7.png',
    './resources/player/imgs/no_ball_left/run/run8.png',
    './resources/player/imgs/no_ball_left/run/run9.png',
    './resources/player/imgs/no_ball_left/run/run10.png'
]

ANIMATION_JUMP_NB_R = [
    './resources/player/imgs/no_ball_rigth/jump/jump1.png',
    './resources/player/imgs/no_ball_rigth/jump/jump2.png'
]

ANIMATION_JUMP_NB_L = [
    './resources/player/imgs/no_ball_left/jump/jump1.png',
    './resources/player/imgs/no_ball_left/jump/jump2.png'
]

ANIMATION_FALL_NB_R = [
    './resources/player/imgs/no_ball_rigth/fall/fall1.png',
    './resources/player/imgs/no_ball_rigth/fall/fall2.png'
]

ANIMATION_FALL_NB_L = [
    './resources/player/imgs/no_ball_left/fall/fall1.png',
    './resources/player/imgs/no_ball_left/fall/fall2.png'
]

ANIMATION_SLIDE_NB_R = [
    './resources/player/imgs/no_ball_rigth/slide/slide1.png',
    # './resources/player/imgs/no_ball_rigth/slide/slide2.png',
    './resources/player/imgs/no_ball_rigth/slide/slide3.png',
    # './resources/player/imgs/no_ball_rigth/slide/slide4.png',
    './resources/player/imgs/no_ball_rigth/slide/slide5.png',
    # './resources/player/imgs/no_ball_rigth/slide/slide6.png',
    './resources/player/imgs/no_ball_rigth/slide/slide7.png',
    # './resources/player/imgs/no_ball_rigth/slide/slide8.png',
    # './resources/player/imgs/no_ball_rigth/slide/slide9.png',
    './resources/player/imgs/no_ball_rigth/slide/slide10.png'
]

ANIMATION_SLIDE_NB_L = [
    './resources/player/imgs/no_ball_left/slide/slide1.png',
    # './resources/player/imgs/no_ball_left/slide/slide2.png',
    './resources/player/imgs/no_ball_left/slide/slide3.png',
    # './resources/player/imgs/no_ball_left/slide/slide4.png',
    './resources/player/imgs/no_ball_left/slide/slide5.png',
    # './resources/player/imgs/no_ball_left/slide/slide6.png',
    './resources/player/imgs/no_ball_left/slide/slide7.png',
    # './resources/player/imgs/no_ball_left/slide/slide8.png',
    # './resources/player/imgs/no_ball_left/slide/slide9.png',
    './resources/player/imgs/no_ball_left/slide/slide10.png'
]

ANIMATION_THROW_HIGH_NB_R = [
    './resources/player/imgs/rigth/throw/shot1.png',
    './resources/player/imgs/rigth/throw/shot2.png',
    './resources/player/imgs/rigth/throw/shot3.png',
    './resources/player/imgs/rigth/throw/shot4.png',
    './resources/player/imgs/rigth/throw/shot5.png',
    './resources/player/imgs/rigth/throw/shot6.png'
]

ANIMATION_THROW_HIGH_NB_L = [
    './resources/player/imgs/left/throw/shot1.png',
    './resources/player/imgs/left/throw/shot2.png',
    './resources/player/imgs/left/throw/shot3.png',
    './resources/player/imgs/left/throw/shot4.png',
    './resources/player/imgs/left/throw/shot5.png',
    './resources/player/imgs/left/throw/shot6.png'
]

ANIMATION_THROW_LOW_NB_R = [
    './resources/player/imgs/rigth/throw_low/shot1.png',
    './resources/player/imgs/rigth/throw_low/shot2.png',
    './resources/player/imgs/rigth/throw_low/shot3.png',
    './resources/player/imgs/rigth/throw_low/shot4.png',
    './resources/player/imgs/rigth/throw_low/shot5.png',
    './resources/player/imgs/rigth/throw_low/shot6.png'
]

ANIMATION_THROW_LOW_NB_L = [   
    './resources/player/imgs/left/throw_low/shot1.png',
    './resources/player/imgs/left/throw_low/shot2.png',
    './resources/player/imgs/left/throw_low/shot3.png',
    './resources/player/imgs/left/throw_low/shot4.png',
    './resources/player/imgs/left/throw_low/shot5.png',
    './resources/player/imgs/left/throw_low/shot6.png'
]

ANIMATION_THROW_BOMB_NB_R = [
    './resources/player/imgs/rigth/throw_bomb/shot1.png',
    './resources/player/imgs/rigth/throw_bomb/shot2.png',
    './resources/player/imgs/rigth/throw_bomb/shot3.png',
    './resources/player/imgs/rigth/throw_bomb/shot4.png',
    './resources/player/imgs/rigth/throw_bomb/shot5.png',
    './resources/player/imgs/rigth/throw_bomb/shot6.png'
]

ANIMATION_THROW_BOMB_NB_L = [   
    './resources/player/imgs/left/throw_bomb/shot1.png',
    './resources/player/imgs/left/throw_bomb/shot2.png',
    './resources/player/imgs/left/throw_bomb/shot3.png',
    './resources/player/imgs/left/throw_bomb/shot4.png',
    './resources/player/imgs/left/throw_bomb/shot5.png',
    './resources/player/imgs/left/throw_bomb/shot6.png'
]

ANIMATION_SHOOT_NB_R = [
    './resources/player/imgs/no_ball_rigth/shoot/shoot1.png',
    './resources/player/imgs/no_ball_rigth/shoot/shoot2.png',
    './resources/player/imgs/no_ball_rigth/shoot/shoot3.png',
    './resources/player/imgs/no_ball_rigth/shoot/shoot4.png',
    './resources/player/imgs/no_ball_rigth/shoot/shoot5.png'
]

ANIMATION_SHOOT_NB_L = [
    './resources/player/imgs/no_ball_left/shoot/shoot1.png',
    './resources/player/imgs/no_ball_left/shoot/shoot2.png',
    './resources/player/imgs/no_ball_left/shoot/shoot3.png',
    './resources/player/imgs/no_ball_left/shoot/shoot4.png',
    './resources/player/imgs/no_ball_left/shoot/shoot5.png'
]

ANIMATION_SHOOT_N_RUN_NB_R = [
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run2.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run3.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run4.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run5.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run6.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run7.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run8.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run9.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_run/shoot_n_run10.png'
]

ANIMATION_SHOOT_N_RUN_NB_L = [
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run2.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run3.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run4.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run5.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run1.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run6.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run7.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run8.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run9.png',
    './resources/player/imgs/no_ball_left/shoot_n_run/shoot_n_run10.png'
]

ANIMATION_JUMP_N_SHOOT_NB_R = [
    './resources/player/imgs/no_ball_rigth/shoot_n_jump/jump_n_shoot1.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_jump/jump_n_shoot2.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_jump/jump_n_shoot3.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_jump/jump_n_shoot4.png',
    './resources/player/imgs/no_ball_rigth/shoot_n_jump/jump_n_shoot5.png'
]

ANIMATION_JUMP_N_SHOOT_NB_L = [
    './resources/player/imgs/no_ball_left/shoot_n_jump/jump_n_shoot1.png',
    './resources/player/imgs/no_ball_left/shoot_n_jump/jump_n_shoot2.png',
    './resources/player/imgs/no_ball_left/shoot_n_jump/jump_n_shoot3.png',
    './resources/player/imgs/no_ball_left/shoot_n_jump/jump_n_shoot4.png',
    './resources/player/imgs/no_ball_left/shoot_n_jump/jump_n_shoot5.png'
]

ANIMATION_ENERGY_NB_R = [
    './resources/player/imgs/rigth/energy/energy1.png',
    './resources/player/imgs/rigth/energy/energy2.png',
    './resources/player/imgs/rigth/energy/energy3.png',
    './resources/player/imgs/rigth/energy/energy4.png',
    './resources/player/imgs/rigth/energy/energy5.png',
    './resources/player/imgs/rigth/energy/energy6.png',
    './resources/player/imgs/rigth/energy/energy7.png',
    './resources/player/imgs/rigth/energy/energy8.png',
    './resources/player/imgs/rigth/energy/energy9.png',
    './resources/player/imgs/rigth/energy/energy10.png',
    './resources/player/imgs/rigth/energy/energy11.png',
    './resources/player/imgs/rigth/energy/energy12.png',
]

ANIMATION_ENERGY_NB_L = [
    './resources/player/imgs/left/energy/energy1.png',
    './resources/player/imgs/left/energy/energy2.png',
    './resources/player/imgs/left/energy/energy3.png',
    './resources/player/imgs/left/energy/energy4.png',
    './resources/player/imgs/left/energy/energy5.png',
    './resources/player/imgs/left/energy/energy6.png',
    './resources/player/imgs/left/energy/energy7.png',
    './resources/player/imgs/left/energy/energy8.png',
    './resources/player/imgs/left/energy/energy9.png',
    './resources/player/imgs/left/energy/energy10.png',
    './resources/player/imgs/left/energy/energy11.png',
    './resources/player/imgs/left/energy/energy12.png',
]

ANIMATION_DUCK_NB_R = [
    './resources/player/imgs/no_ball_rigth/duck/duck1.png',
    './resources/player/imgs/no_ball_rigth/duck/duck2.png',
    './resources/player/imgs/no_ball_rigth/duck/duck3.png',
    './resources/player/imgs/no_ball_rigth/duck/duck4.png'
]

ANIMATION_DUCK_NB_L = [
    './resources/player/imgs/no_ball_left/duck/duck1.png',
    './resources/player/imgs/no_ball_left/duck/duck2.png',
    './resources/player/imgs/no_ball_left/duck/duck3.png',
    './resources/player/imgs/no_ball_left/duck/duck4.png'
]

ANIMATION_DUCK_WALK_NB_R = [
    './resources/player/imgs/no_ball_rigth/duck_walk/duck_walk1.png',
    './resources/player/imgs/no_ball_rigth/duck_walk/duck_walk2.png',
    './resources/player/imgs/no_ball_rigth/duck_walk/duck_walk3.png',
    './resources/player/imgs/no_ball_rigth/duck_walk/duck_walk4.png'
]

ANIMATION_DUCK_WALK_NB_L = [
    './resources/player/imgs/no_ball_left/duck_walk/duck_walk1.png',
    './resources/player/imgs/no_ball_left/duck_walk/duck_walk2.png',
    './resources/player/imgs/no_ball_left/duck_walk/duck_walk3.png',
    './resources/player/imgs/no_ball_left/duck_walk/duck_walk4.png'
]

ANIMATION_DUCK_SHOOT_NB_R = [
    './resources/player/imgs/no_ball_rigth/duck_shoot/shoot1.png',
    './resources/player/imgs/no_ball_rigth/duck_shoot/shoot2.png',
    './resources/player/imgs/no_ball_rigth/duck_shoot/shoot3.png',
    './resources/player/imgs/no_ball_rigth/duck_shoot/shoot4.png',
    './resources/player/imgs/no_ball_rigth/duck_shoot/shoot5.png'
]

ANIMATION_DUCK_SHOOT_NB_L = [
    './resources/player/imgs/no_ball_left/duck_shoot/shoot1.png',
    './resources/player/imgs/no_ball_left/duck_shoot/shoot2.png',
    './resources/player/imgs/no_ball_left/duck_shoot/shoot3.png',
    './resources/player/imgs/no_ball_left/duck_shoot/shoot4.png',
    './resources/player/imgs/no_ball_left/duck_shoot/shoot5.png'
]

ANIMATION_LASER = [
    './resources/objects/imgs/player_projectile/laser1.png',
    './resources/objects/imgs/player_projectile/laser2.png',
    './resources/objects/imgs/player_projectile/laser3.png'
]


#SOUND EFECTS
SFX_WALK = pygame.mixer.Sound('./resources/SFX/walk.ogg')
SFX_WALK_V = 1
SFX_JUMP = pygame.mixer.Sound('./resources/SFX/jump.wav')
SFX_JUMP_V = 0.5
SFX_S_JUMP = pygame.mixer.Sound('./resources/SFX/second_jump.mp3')
SFX_S_JUMP_V = 0.3
SFX_E_JUMP = pygame.mixer.Sound('./resources/SFX/e_bounce.wav')
SFX_E_JUMP_V = 0.15
SFX_LANDING = pygame.mixer.Sound('./resources/SFX/landing.mp3')
SFX_LANDING_V = 1
SFX_DAMAGE = pygame.mixer.Sound('./resources/SFX/damage (2).wav')
SFX_DAMAGE_V = 0.4
SFX_HOLE = pygame.mixer.Sound('./resources/SFX/hole.mp3')
SFX_HOLE_V = 1
SFX_RESTART = pygame.mixer.Sound('./resources/SFX/death.mp3')
SFX_RESTART_V = 0.15
SFX_BALL_THROW = pygame.mixer.Sound('./resources/SFX/slide.wav')
SFX_BALL_THROW_V = 0.5
SFX_BALL_EXPLODE = pygame.mixer.Sound('./resources/SFX/explosion.ogg')
SFX_BALL_EXPLODE_V = 0.5
SFX_BALL_BOUNCE = pygame.mixer.Sound('./resources/SFX/ball_bounce.mp3')
SFX_BALL_BOUNCE_V = 0.4
SFX_LASER = pygame.mixer.Sound('./resources/SFX/laser.mp3')
SFX_LASER_V = 1
SFX_SLIDE = pygame.mixer.Sound('./resources/SFX/slide.wav')
SFX_SLIDE_V = 0.1
SFX_COLLECT_SHIME = pygame.mixer.Sound('./resources/SFX/Collect Chime.ogg')
SFX_COLLECT_SHIME_V = 0.3
SFX_COLLECT_HEART = pygame.mixer.Sound('./resources/SFX/collect_heart.ogg')
SFX_COLLECT_HEART_V = 1
SFX_COLLECT_BOMB = pygame.mixer.Sound('./resources/SFX/collect_bombs.ogg')
SFX_COLLECT_BOMB_V = 1
SFX_NO_BOMB = pygame.mixer.Sound('./resources/SFX/no_bomb.ogg')
SFX_NO_BOMB_V = 0.1
SFX_VICTORY1 = pygame.mixer.Sound('./resources/SFX/victory1.wav')
SFX_VICTORY1_V = 1
SFX_VICTORY2 = pygame.mixer.Sound('./resources/SFX/victory2.wav')
SFX_VICTORY2_V = 1
SFX_BEEP = pygame.mixer.Sound('./resources/SFX/beep.wav')
SFX_BEEP_V = 0.1
SFX_E_PROTECTED = pygame.mixer.Sound('./resources/SFX/e_protected.ogg')
SFX_E_PROTECTED_V =  0.3

def set_p_volume()-> None:
    SFX_WALK.set_volume(SFX_WALK_V)
    SFX_JUMP.set_volume(SFX_JUMP_V)
    SFX_S_JUMP.set_volume(SFX_S_JUMP_V)
    SFX_E_JUMP.set_volume(SFX_E_JUMP_V)
    SFX_LANDING.set_volume(SFX_LANDING_V)
    SFX_DAMAGE.set_volume(SFX_DAMAGE_V)
    SFX_HOLE.set_volume(SFX_HOLE_V) 
    SFX_RESTART.set_volume(SFX_RESTART_V)
    SFX_BALL_THROW.set_volume(SFX_BALL_THROW_V) 
    SFX_BALL_EXPLODE.set_volume(SFX_BALL_EXPLODE_V)
    SFX_BALL_BOUNCE.set_volume(SFX_BALL_BOUNCE_V)
    SFX_LASER.set_volume(SFX_LASER_V) 
    SFX_SLIDE.set_volume(SFX_SLIDE_V) 
    SFX_COLLECT_SHIME.set_volume(SFX_COLLECT_SHIME_V)
    SFX_COLLECT_HEART.set_volume(SFX_COLLECT_HEART_V)
    SFX_COLLECT_BOMB.set_volume(SFX_COLLECT_BOMB_V) 
    SFX_NO_BOMB.set_volume(SFX_NO_BOMB_V) 
    SFX_VICTORY1.set_volume(SFX_VICTORY1_V)
    SFX_VICTORY2.set_volume(SFX_VICTORY2_V)
    SFX_BEEP.set_volume(SFX_BEEP_V)
    SFX_E_PROTECTED.set_volume(SFX_E_PROTECTED_V)



def mute_p_volume()-> None:
    SFX_WALK.set_volume(0)
    SFX_JUMP.set_volume(0)
    SFX_S_JUMP.set_volume(0)
    SFX_E_JUMP.set_volume(0)
    SFX_LANDING.set_volume(0)
    SFX_DAMAGE.set_volume(0)
    SFX_HOLE.set_volume(0) 
    SFX_RESTART.set_volume(0)
    SFX_BALL_THROW.set_volume(0) 
    SFX_BALL_EXPLODE.set_volume(0)
    SFX_BALL_BOUNCE.set_volume(0)
    SFX_LASER.set_volume(0) 
    SFX_SLIDE.set_volume(0) 
    SFX_COLLECT_SHIME.set_volume(0)
    SFX_COLLECT_HEART.set_volume(0)
    SFX_COLLECT_BOMB.set_volume(0) 
    SFX_NO_BOMB.set_volume(0) 
    SFX_VICTORY1.set_volume(0)
    SFX_VICTORY2.set_volume(0)
    SFX_BEEP.set_volume(0)
    SFX_E_PROTECTED.set_volume(0)


