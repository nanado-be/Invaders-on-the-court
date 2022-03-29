import pygame
pygame.init()
pygame.mixer.init()

#################
### ESTÁGIO 1 ###
#################

ANIMATION_IDLE = [
    './resources/boss/idle/img1.png' ,
    './resources/boss/idle/img2.png' ,
    './resources/boss/idle/img3.png' ,
    './resources/boss/idle/img4.png' ,
    './resources/boss/idle/img5.png' ,
    './resources/boss/idle/img6.png' ,
    './resources/boss/idle/img7.png' ,
    './resources/boss/idle/img8.png' ,
    './resources/boss/idle/img9.png' ,
    './resources/boss/idle/img10.png',
    './resources/boss/idle/img11.png',
    './resources/boss/idle/img12.png',
    './resources/boss/idle/img13.png',
    './resources/boss/idle/img14.png',
    './resources/boss/idle/img15.png',
    './resources/boss/idle/img16.png',
    './resources/boss/idle/img17.png',
    './resources/boss/idle/img18.png',
    './resources/boss/idle/img19.png',
    './resources/boss/idle/img20.png',
    './resources/boss/idle/img21.png',
    './resources/boss/idle/img22.png',
    './resources/boss/idle/img23.png',
    './resources/boss/idle/img24.png'
]
ANIMATION_CREATE_BALL = [
    './resources/boss/create_ball/img1.png',
    './resources/boss/create_ball/img2.png',
    './resources/boss/create_ball/img3.png',
    './resources/boss/create_ball/img4.png',
    './resources/boss/create_ball/img5.png'
]
ANIMATION_BREAK = [
    './resources/boss/break/img1.png',
    './resources/boss/break/img2.png',
    './resources/boss/break/img3.png',
    './resources/boss/break/img4.png',
    './resources/boss/break/img5.png',
    './resources/boss/break/img6.png',
    './resources/boss/break/img7.png',
    './resources/boss/break/img8.png',
    './resources/boss/break/img9.png',
    './resources/boss/break/img10.png'
]
ANIMATION_WALK_R = [
    './resources/boss/walk_r/img1.png',
    './resources/boss/walk_r/img2.png',
    './resources/boss/walk_r/img3.png',
    './resources/boss/walk_r/img4.png',
    './resources/boss/walk_r/img5.png',
    './resources/boss/walk_r/img6.png',
    './resources/boss/walk_r/img7.png',
    './resources/boss/walk_r/img8.png'
]
ANIMATION_WALK_L = [
    './resources/boss/walk_l/img1.png',
    './resources/boss/walk_l/img2.png',
    './resources/boss/walk_l/img3.png',
    './resources/boss/walk_l/img4.png',
    './resources/boss/walk_l/img5.png',
    './resources/boss/walk_l/img6.png',
    './resources/boss/walk_l/img7.png',
    './resources/boss/walk_l/img8.png'
]
ANIMATION_JUMP_R =  [
    './resources/boss/jump_r/img1.png',
    './resources/boss/jump_r/img2.png',
    './resources/boss/jump_r/img3.png',
    './resources/boss/jump_r/img4.png',
    './resources/boss/jump_r/img5.png',
    './resources/boss/jump_r/img6.png',
    './resources/boss/jump_r/img7.png',
    './resources/boss/jump_r/img8.png'
]
ANIMATION_JUMP_L =  [
    './resources/boss/jump_l/img1.png',
    './resources/boss/jump_l/img2.png',
    './resources/boss/jump_l/img3.png',
    './resources/boss/jump_l/img4.png',
    './resources/boss/jump_l/img5.png',
    './resources/boss/jump_l/img6.png',
    './resources/boss/jump_l/img7.png',
    './resources/boss/jump_l/img8.png'
]
ANIMATION_KICK_R = [
    './resources/boss/kick_r/img1.png',
    './resources/boss/kick_r/img2.png',
    './resources/boss/kick_r/img3.png',
    './resources/boss/kick_r/img4.png',
    './resources/boss/kick_r/img5.png',
    './resources/boss/kick_r/img6.png',
    './resources/boss/kick_r/img7.png',
    './resources/boss/kick_r/img8.png',
    './resources/boss/kick_r/img9.png',
    './resources/boss/kick_r/img10.png',
    './resources/boss/kick_r/img11.png',
    './resources/boss/kick_r/img12.png'
]
ANIMATION_KICK_L = [
    './resources/boss/kick_l/img1.png',
    './resources/boss/kick_l/img2.png',
    './resources/boss/kick_l/img3.png',
    './resources/boss/kick_l/img4.png',
    './resources/boss/kick_l/img5.png',
    './resources/boss/kick_l/img6.png',
    './resources/boss/kick_l/img7.png',
    './resources/boss/kick_l/img8.png',
    './resources/boss/kick_l/img9.png',
    './resources/boss/kick_l/img10.png',
    './resources/boss/kick_l/img11.png',
    './resources/boss/kick_l/img12.png'
]
ANIMATION_SLIDE_R = [
    './resources/boss/slide_r/img1.png',
    './resources/boss/slide_r/img2.png',
    './resources/boss/slide_r/img3.png',
    './resources/boss/slide_r/img4.png',
    './resources/boss/slide_r/img5.png'
]
ANIMATION_SLIDE_L = [
    './resources/boss/slide_l/img1.png',
    './resources/boss/slide_l/img2.png',
    './resources/boss/slide_l/img3.png',
    './resources/boss/slide_l/img4.png',
    './resources/boss/slide_l/img5.png'
]

#################
### ESTÁGIO 2 ###
#################

ANIMATION_IDLE_S2 = [
    './resources/boss/idle_s2/img1.png' ,
    './resources/boss/idle_s2/img2.png' ,
    './resources/boss/idle_s2/img3.png' ,
    './resources/boss/idle_s2/img4.png' ,
    './resources/boss/idle_s2/img5.png' ,
    './resources/boss/idle_s2/img6.png' ,
    './resources/boss/idle_s2/img7.png' ,
    './resources/boss/idle_s2/img8.png' ,
    './resources/boss/idle_s2/img9.png' ,
    './resources/boss/idle_s2/img10.png',
    './resources/boss/idle_s2/img11.png',
    './resources/boss/idle_s2/img12.png',
    './resources/boss/idle_s2/img13.png',
    './resources/boss/idle_s2/img14.png',
    './resources/boss/idle_s2/img15.png',
    './resources/boss/idle_s2/img16.png',
    './resources/boss/idle_s2/img17.png',
    './resources/boss/idle_s2/img18.png',
    './resources/boss/idle_s2/img19.png',
    './resources/boss/idle_s2/img20.png',
    './resources/boss/idle_s2/img21.png',
    './resources/boss/idle_s2/img22.png',
    './resources/boss/idle_s2/img23.png',
    './resources/boss/idle_s2/img24.png'
]
ANIMATION_CREATE_BALL_S2 = [
    './resources/boss/create_ball_s2/img1.png',
    './resources/boss/create_ball_s2/img2.png',
    './resources/boss/create_ball_s2/img3.png',
    './resources/boss/create_ball_s2/img4.png',
    './resources/boss/create_ball_s2/img5.png'
]
ANIMATION_BREAK_S2 = [
    './resources/boss/break_s2/img1.png',
    './resources/boss/break_s2/img2.png',
    './resources/boss/break_s2/img3.png',
    './resources/boss/break_s2/img4.png',
    './resources/boss/break_s2/img5.png',
    './resources/boss/break_s2/img6.png',
    './resources/boss/break_s2/img7.png',
    './resources/boss/break_s2/img8.png',
    './resources/boss/break_s2/img9.png',
    './resources/boss/break_s2/img10.png'
]
ANIMATION_WALK_R_S2 = [
    './resources/boss/walk_r_s2/img1.png',
    './resources/boss/walk_r_s2/img2.png',
    './resources/boss/walk_r_s2/img3.png',
    './resources/boss/walk_r_s2/img4.png',
    './resources/boss/walk_r_s2/img5.png',
    './resources/boss/walk_r_s2/img6.png',
    './resources/boss/walk_r_s2/img7.png',
    './resources/boss/walk_r_s2/img8.png'
]
ANIMATION_WALK_L_S2 = [
    './resources/boss/walk_l_s2/img1.png',
    './resources/boss/walk_l_s2/img2.png',
    './resources/boss/walk_l_s2/img3.png',
    './resources/boss/walk_l_s2/img4.png',
    './resources/boss/walk_l_s2/img5.png',
    './resources/boss/walk_l_s2/img6.png',
    './resources/boss/walk_l_s2/img7.png',
    './resources/boss/walk_l_s2/img8.png'
]
ANIMATION_JUMP_R_S2 =  [
    './resources/boss/jump_r_s2/img1.png',
    './resources/boss/jump_r_s2/img2.png',
    './resources/boss/jump_r_s2/img3.png',
    './resources/boss/jump_r_s2/img4.png',
    './resources/boss/jump_r_s2/img5.png',
    './resources/boss/jump_r_s2/img6.png',
    './resources/boss/jump_r_s2/img7.png',
    './resources/boss/jump_r_s2/img8.png'
]
ANIMATION_JUMP_L_S2 =  [
    './resources/boss/jump_l_s2/img1.png',
    './resources/boss/jump_l_s2/img2.png',
    './resources/boss/jump_l_s2/img3.png',
    './resources/boss/jump_l_s2/img4.png',
    './resources/boss/jump_l_s2/img5.png',
    './resources/boss/jump_l_s2/img6.png',
    './resources/boss/jump_l_s2/img7.png',
    './resources/boss/jump_l_s2/img8.png'
]
ANIMATION_KICK_R_S2 = [
    './resources/boss/kick_r_s2/img1.png',
    './resources/boss/kick_r_s2/img2.png',
    './resources/boss/kick_r_s2/img3.png',
    './resources/boss/kick_r_s2/img4.png',
    './resources/boss/kick_r_s2/img5.png',
    './resources/boss/kick_r_s2/img6.png',
    './resources/boss/kick_r_s2/img7.png',
    './resources/boss/kick_r_s2/img8.png',
    './resources/boss/kick_r_s2/img9.png',
    './resources/boss/kick_r_s2/img10.png',
    './resources/boss/kick_r_s2/img11.png',
    './resources/boss/kick_r_s2/img12.png'
]
ANIMATION_KICK_L_S2 = [
    './resources/boss/kick_l_s2/img1.png',
    './resources/boss/kick_l_s2/img2.png',
    './resources/boss/kick_l_s2/img3.png',
    './resources/boss/kick_l_s2/img4.png',
    './resources/boss/kick_l_s2/img5.png',
    './resources/boss/kick_l_s2/img6.png',
    './resources/boss/kick_l_s2/img7.png',
    './resources/boss/kick_l_s2/img8.png',
    './resources/boss/kick_l_s2/img9.png',
    './resources/boss/kick_l_s2/img10.png',
    './resources/boss/kick_l_s2/img11.png',
    './resources/boss/kick_l_s2/img12.png'
]
ANIMATION_SLIDE_R_S2 = [
    './resources/boss/slide_r_s2/img1.png',
    './resources/boss/slide_r_s2/img2.png',
    './resources/boss/slide_r_s2/img3.png',
    './resources/boss/slide_r_s2/img4.png',
    './resources/boss/slide_r_s2/img5.png'
]
ANIMATION_SLIDE_L_S2 = [
    './resources/boss/slide_l_s2/img1.png',
    './resources/boss/slide_l_s2/img2.png',
    './resources/boss/slide_l_s2/img3.png',
    './resources/boss/slide_l_s2/img4.png',
    './resources/boss/slide_l_s2/img5.png'
]
#################
### ESTÁGIO 3 ###
#################

ANIMATION_IDLE_S3 = [
    './resources/boss/idle_s3/img1.png' ,
    './resources/boss/idle_s3/img2.png' ,
    './resources/boss/idle_s3/img3.png' ,
    './resources/boss/idle_s3/img4.png' ,
    './resources/boss/idle_s3/img5.png' ,
    './resources/boss/idle_s3/img6.png' ,
    './resources/boss/idle_s3/img7.png' ,
    './resources/boss/idle_s3/img8.png' ,
    './resources/boss/idle_s3/img9.png' ,
    './resources/boss/idle_s3/img10.png',
    './resources/boss/idle_s3/img11.png',
    './resources/boss/idle_s3/img12.png',
    './resources/boss/idle_s3/img13.png',
    './resources/boss/idle_s3/img14.png',
    './resources/boss/idle_s3/img15.png',
    './resources/boss/idle_s3/img16.png',
    './resources/boss/idle_s3/img17.png',
    './resources/boss/idle_s3/img18.png',
    './resources/boss/idle_s3/img19.png',
    './resources/boss/idle_s3/img20.png',
    './resources/boss/idle_s3/img21.png',
    './resources/boss/idle_s3/img22.png',
    './resources/boss/idle_s3/img23.png',
    './resources/boss/idle_s3/img24.png'
]
ANIMATION_CREATE_BALL_S3 = [
    './resources/boss/create_ball_s3/img1.png',
    './resources/boss/create_ball_s3/img2.png',
    './resources/boss/create_ball_s3/img3.png',
    './resources/boss/create_ball_s3/img4.png',
    './resources/boss/create_ball_s3/img5.png'
]
ANIMATION_BREAK_S3 = [
    './resources/boss/break_s3/img1.png',
    './resources/boss/break_s3/img2.png',
    './resources/boss/break_s3/img3.png',
    './resources/boss/break_s3/img4.png',
    './resources/boss/break_s3/img5.png',
    './resources/boss/break_s3/img6.png',
    './resources/boss/break_s3/img7.png',
    './resources/boss/break_s3/img8.png',
    './resources/boss/break_s3/img9.png',
    './resources/boss/break_s3/img10.png'
]
ANIMATION_WALK_R_S3 = [
    './resources/boss/walk_r_s3/img1.png',
    './resources/boss/walk_r_s3/img2.png',
    './resources/boss/walk_r_s3/img3.png',
    './resources/boss/walk_r_s3/img4.png',
    './resources/boss/walk_r_s3/img5.png',
    './resources/boss/walk_r_s3/img6.png',
    './resources/boss/walk_r_s3/img7.png',
    './resources/boss/walk_r_s3/img8.png'
]
ANIMATION_WALK_L_S3 = [
    './resources/boss/walk_l_s3/img1.png',
    './resources/boss/walk_l_s3/img2.png',
    './resources/boss/walk_l_s3/img3.png',
    './resources/boss/walk_l_s3/img4.png',
    './resources/boss/walk_l_s3/img5.png',
    './resources/boss/walk_l_s3/img6.png',
    './resources/boss/walk_l_s3/img7.png',
    './resources/boss/walk_l_s3/img8.png'
]
ANIMATION_JUMP_R_S3 =  [
    './resources/boss/jump_r_s3/img1.png',
    './resources/boss/jump_r_s3/img2.png',
    './resources/boss/jump_r_s3/img3.png',
    './resources/boss/jump_r_s3/img4.png',
    './resources/boss/jump_r_s3/img5.png',
    './resources/boss/jump_r_s3/img6.png',
    './resources/boss/jump_r_s3/img7.png',
    './resources/boss/jump_r_s3/img8.png'
]
ANIMATION_JUMP_L_S3 =  [
    './resources/boss/jump_l_s3/img1.png',
    './resources/boss/jump_l_s3/img2.png',
    './resources/boss/jump_l_s3/img3.png',
    './resources/boss/jump_l_s3/img4.png',
    './resources/boss/jump_l_s3/img5.png',
    './resources/boss/jump_l_s3/img6.png',
    './resources/boss/jump_l_s3/img7.png',
    './resources/boss/jump_l_s3/img8.png'
]
ANIMATION_KICK_R_S3 = [
    './resources/boss/kick_r_s3/img1.png',
    './resources/boss/kick_r_s3/img2.png',
    './resources/boss/kick_r_s3/img3.png',
    './resources/boss/kick_r_s3/img4.png',
    './resources/boss/kick_r_s3/img5.png',
    './resources/boss/kick_r_s3/img6.png',
    './resources/boss/kick_r_s3/img7.png',
    './resources/boss/kick_r_s3/img8.png',
    './resources/boss/kick_r_s3/img9.png',
    './resources/boss/kick_r_s3/img10.png',
    './resources/boss/kick_r_s3/img11.png',
    './resources/boss/kick_r_s3/img12.png'
]
ANIMATION_KICK_L_S3 = [
    './resources/boss/kick_l_s3/img1.png',
    './resources/boss/kick_l_s3/img2.png',
    './resources/boss/kick_l_s3/img3.png',
    './resources/boss/kick_l_s3/img4.png',
    './resources/boss/kick_l_s3/img5.png',
    './resources/boss/kick_l_s3/img6.png',
    './resources/boss/kick_l_s3/img7.png',
    './resources/boss/kick_l_s3/img8.png',
    './resources/boss/kick_l_s3/img9.png',
    './resources/boss/kick_l_s3/img10.png',
    './resources/boss/kick_l_s3/img11.png',
    './resources/boss/kick_l_s3/img12.png'
]
ANIMATION_SLIDE_R_S3 = [
    './resources/boss/slide_r_s3/img1.png',
    './resources/boss/slide_r_s3/img2.png',
    './resources/boss/slide_r_s3/img3.png',
    './resources/boss/slide_r_s3/img4.png',
    './resources/boss/slide_r_s3/img5.png'
]
ANIMATION_SLIDE_L_S3 = [
    './resources/boss/slide_l_s3/img1.png',
    './resources/boss/slide_l_s3/img2.png',
    './resources/boss/slide_l_s3/img3.png',
    './resources/boss/slide_l_s3/img4.png',
    './resources/boss/slide_l_s3/img5.png'
]

ANIMATION_SOCCER_BALL = [
    './resources/boss/ball/img1.png',
    './resources/boss/ball/img2.png',
    './resources/boss/ball/img3.png'
]


SFX_B_BALL_BORN = pygame.mixer.Sound('./resources/SFX/boss_ball_born.mp3')
SFX_B_BALL_BORN_V = 1
SFX_B_BALL_DEATH = pygame.mixer.Sound('./resources/SFX/boss_ball_death.mp3')
SFX_B_BALL_DEATH_V = 1
SFX_B_BORN = pygame.mixer.Sound('./resources/SFX/boss_born.ogg')
SFX_B_BORN_V = 1
SFX_B_BREAK = pygame.mixer.Sound('./resources/SFX/boss_break.wav')
SFX_B_BREAK_V = 1
SFX_B_BREAK2 = pygame.mixer.Sound('./resources/SFX/boss_break2.ogg')
SFX_B_BREAK2_V = 1
SFX_B_DAMAGE = pygame.mixer.Sound('./resources/SFX/boss_damage.mp3')
SFX_B_DAMAGE_V = 0.2
SFX_B_EXPLOSION = pygame.mixer.Sound('./resources/SFX/boss_explosion.ogg')
SFX_B_EXPLOSION_V = 1
SFX_B_JUMP = pygame.mixer.Sound('./resources/SFX/boss_jump.ogg')
SFX_B_JUMP_V = 0.4
SFX_B_KICK = pygame.mixer.Sound('./resources/SFX/boss_kick.mp3')
SFX_B_KICK_V = 1
SFX_B_RECOVER = pygame.mixer.Sound('./resources/SFX/boss_recover.ogg')
SFX_B_RECOVER_V = 0.4
SFX_B_RUN = pygame.mixer.Sound('./resources/SFX/boss_run.ogg')
SFX_B_RUN_V = 1
SFX_B_SLIDE = pygame.mixer.Sound('./resources/SFX/boss_slide.wav')
SFX_B_SLIDE_V = 1

def set_b_volume():
    SFX_B_BALL_BORN.set_volume(SFX_B_BALL_BORN_V)
    SFX_B_BALL_DEATH.set_volume(SFX_B_BALL_DEATH_V)
    SFX_B_BORN.set_volume(SFX_B_BORN_V)
    SFX_B_BREAK.set_volume(SFX_B_BREAK_V)
    SFX_B_BREAK2.set_volume(SFX_B_BREAK2_V)
    SFX_B_DAMAGE.set_volume(SFX_B_DAMAGE_V)
    SFX_B_EXPLOSION.set_volume(SFX_B_EXPLOSION_V)
    SFX_B_JUMP.set_volume(SFX_B_JUMP_V)
    SFX_B_KICK.set_volume(SFX_B_KICK_V)
    SFX_B_RECOVER.set_volume(SFX_B_RECOVER_V)
    SFX_B_RUN.set_volume(SFX_B_RUN_V)
    SFX_B_SLIDE.set_volume(SFX_B_SLIDE_V)

def mute_b_volume():
    SFX_B_BALL_BORN.set_volume(0)
    SFX_B_BALL_DEATH.set_volume(0)
    SFX_B_BORN.set_volume(0)
    SFX_B_BREAK.set_volume(0)
    SFX_B_BREAK2.set_volume(0)
    SFX_B_DAMAGE.set_volume(0)
    SFX_B_EXPLOSION.set_volume(0)
    SFX_B_JUMP.set_volume(0)
    SFX_B_KICK.set_volume(0)
    SFX_B_RECOVER.set_volume(0)
    SFX_B_RUN.set_volume(0)
    SFX_B_SLIDE.set_volume(0)



