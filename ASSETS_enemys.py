import pygame
pygame.init()
pygame.mixer.init()

from ASSETS_player import ANIMATION_BOMB_BALL


ANIMATION_FLY = [
    './resources/enemys/flying/flying1.png',
    './resources/enemys/flying/flying2.png',
    './resources/enemys/flying/flying3.png',
    './resources/enemys/flying/flying4.png',
    './resources/enemys/flying/flying5.png',
    './resources/enemys/flying/flying6.png',
    './resources/enemys/flying/flying7.png',
    './resources/enemys/flying/flying8.png',
    './resources/enemys/flying/flying9.png',
    './resources/enemys/flying/flying10.png',
    './resources/enemys/flying/flying11.png',
    './resources/enemys/flying/flying12.png'
]

ANIMATION_FLY_B1 = [
    './resources/enemys/flying_b1/flying1.png',
    './resources/enemys/flying_b1/flying2.png',
    './resources/enemys/flying_b1/flying3.png',
    './resources/enemys/flying_b1/flying4.png',
    './resources/enemys/flying_b1/flying5.png',
    './resources/enemys/flying_b1/flying6.png',
    './resources/enemys/flying_b1/flying7.png',
    './resources/enemys/flying_b1/flying8.png',
    './resources/enemys/flying_b1/flying9.png',
    './resources/enemys/flying_b1/flying10.png',
    './resources/enemys/flying_b1/flying11.png',
    './resources/enemys/flying_b1/flying12.png'
]
ANIMATION_FLY_B2 = [
    './resources/enemys/flying_b2/flying1.png',
    './resources/enemys/flying_b2/flying2.png',
    './resources/enemys/flying_b2/flying3.png',
    './resources/enemys/flying_b2/flying4.png',
    './resources/enemys/flying_b2/flying5.png',
    './resources/enemys/flying_b2/flying6.png',
    './resources/enemys/flying_b2/flying7.png',
    './resources/enemys/flying_b2/flying8.png',
    './resources/enemys/flying_b2/flying9.png',
    './resources/enemys/flying_b2/flying10.png',
    './resources/enemys/flying_b2/flying11.png',
    './resources/enemys/flying_b2/flying12.png'
]

ANIMATION_BALL = [
    './resources/enemys/rolling/basic alien1.png',
    './resources/enemys/rolling/basic alien2.png',
    './resources/enemys/rolling/basic alien3.png',
    './resources/enemys/rolling/basic alien4.png',
    './resources/enemys/rolling/basic alien5.png',
    './resources/enemys/rolling/basic alien6.png',
    './resources/enemys/rolling/basic alien7.png',
    './resources/enemys/rolling/basic alien8.png',
    './resources/enemys/rolling/basic alien9.png',
    './resources/enemys/rolling/basic alien10.png',
    './resources/enemys/rolling/basic alien11.png',
    './resources/enemys/rolling/basic alien12.png'
]

ANIMATION_OCTOPUS = [
    './resources/enemys/octopus/octopus1.png',
    './resources/enemys/octopus/octopus2.png',
    './resources/enemys/octopus/octopus3.png',
    './resources/enemys/octopus/octopus4.png',
    './resources/enemys/octopus/octopus5.png',
    './resources/enemys/octopus/octopus6.png',
    './resources/enemys/octopus/octopus7.png',
    './resources/enemys/octopus/octopus8.png',
    './resources/enemys/octopus/octopus9.png',
    './resources/enemys/octopus/octopus10.png',
    './resources/enemys/octopus/octopus11.png',
    './resources/enemys/octopus/octopus12.png',
    './resources/enemys/octopus/octopus13.png',
    './resources/enemys/octopus/octopus14.png',
    './resources/enemys/octopus/octopus15.png',
    './resources/enemys/octopus/octopus16.png',
    './resources/enemys/octopus/octopus17.png',
    './resources/enemys/octopus/octopus18.png'
]

ANIMATION_ELETRIC_OCTOPUS = [
    './resources/enemys/octopus/eletric1.png',
    './resources/enemys/octopus/eletric2.png',
    './resources/enemys/octopus/eletric3.png',
    './resources/enemys/octopus/eletric4.png',
    './resources/enemys/octopus/eletric5.png',
    './resources/enemys/octopus/eletric6.png',
    './resources/enemys/octopus/eletric7.png',
    './resources/enemys/octopus/eletric8.png',
    './resources/enemys/octopus/eletric9.png',
    './resources/enemys/octopus/eletric10.png',
    './resources/enemys/octopus/eletric11.png',
    './resources/enemys/octopus/eletric12.png',
    './resources/enemys/octopus/eletric13.png',
    './resources/enemys/octopus/eletric14.png',
    './resources/enemys/octopus/eletric15.png',
    './resources/enemys/octopus/eletric16.png',
    './resources/enemys/octopus/eletric17.png',
    './resources/enemys/octopus/eletric18.png'
]

ANIMATION_TANK = [
    './resources/enemys/tank/tank1.png',
    './resources/enemys/tank/tank2.png',
    './resources/enemys/tank/tank3.png',
    './resources/enemys/tank/tank4.png',
    './resources/enemys/tank/tank5.png',
    './resources/enemys/tank/tank6.png',
    './resources/enemys/tank/tank7.png',
    './resources/enemys/tank/tank8.png',
    './resources/enemys/tank/tank9.png',
    './resources/enemys/tank/tank10.png',
    './resources/enemys/tank/tank11.png',
    './resources/enemys/tank/tank12.png'
]

ANIMATION_SPIKE = [
    './resources/enemys/spike/spike1.png',
    './resources/enemys/spike/spike2.png',
    './resources/enemys/spike/spike3.png',
    './resources/enemys/spike/spike4.png',
    './resources/enemys/spike/spike5.png',
    './resources/enemys/spike/spike6.png',
    './resources/enemys/spike/spike7.png',
    './resources/enemys/spike/spike8.png',
    './resources/enemys/spike/spike9.png',
    './resources/enemys/spike/spike10.png',
    './resources/enemys/spike/spike11.png',
    './resources/enemys/spike/spike12.png'
]

ANIMATION_SHOOTER = [
    './resources/enemys/shooter/shooter1.png',
    './resources/enemys/shooter/shooter2.png',
    './resources/enemys/shooter/shooter3.png',
    './resources/enemys/shooter/shooter4.png',
    './resources/enemys/shooter/shooter5.png',
    './resources/enemys/shooter/shooter6.png',
    './resources/enemys/shooter/shooter7.png',
    './resources/enemys/shooter/shooter8.png',
    './resources/enemys/shooter/shooter9.png',
    './resources/enemys/shooter/shooter10.png',
    './resources/enemys/shooter/shooter11.png',
    './resources/enemys/shooter/shooter12.png'
]

ANIMATION_C_SHOOTER = [
    './resources/enemys/c_shooter/crazy shooter1.png',
    './resources/enemys/c_shooter/crazy shooter2.png',
    './resources/enemys/c_shooter/crazy shooter3.png',
    './resources/enemys/c_shooter/crazy shooter4.png',
    './resources/enemys/c_shooter/crazy shooter5.png',
    './resources/enemys/c_shooter/crazy shooter6.png',
    './resources/enemys/c_shooter/crazy shooter7.png',
    './resources/enemys/c_shooter/crazy shooter8.png',
    './resources/enemys/c_shooter/crazy shooter9.png',
    './resources/enemys/c_shooter/crazy shooter10.png',
    './resources/enemys/c_shooter/crazy shooter11.png',
    './resources/enemys/c_shooter/crazy shooter12.png'
]

ANIMATION_B_SHOOTER = [
    './resources/enemys/b_shooter/bomb shooter1.png',
    './resources/enemys/b_shooter/bomb shooter2.png',
    './resources/enemys/b_shooter/bomb shooter3.png',
    './resources/enemys/b_shooter/bomb shooter4.png',
    './resources/enemys/b_shooter/bomb shooter5.png',
    './resources/enemys/b_shooter/bomb shooter6.png',
    './resources/enemys/b_shooter/bomb shooter7.png',
    './resources/enemys/b_shooter/bomb shooter8.png',
    './resources/enemys/b_shooter/bomb shooter9.png',
    './resources/enemys/b_shooter/bomb shooter10.png',
    './resources/enemys/b_shooter/bomb shooter11.png',
    './resources/enemys/b_shooter/bomb shooter12.png'
]

ANIMATION_B_SHOOTER2 = [
    './resources/enemys/b_shooter2/bomb shooter2.png',
    './resources/enemys/b_shooter2/bomb shooter3.png',
    './resources/enemys/b_shooter2/bomb shooter4.png',
    './resources/enemys/b_shooter2/bomb shooter5.png',
    './resources/enemys/b_shooter2/bomb shooter6.png',
    './resources/enemys/b_shooter2/bomb shooter7.png',
    './resources/enemys/b_shooter2/bomb shooter8.png',
    './resources/enemys/b_shooter2/bomb shooter9.png',
    './resources/enemys/b_shooter2/bomb shooter10.png',
    './resources/enemys/b_shooter2/bomb shooter11.png',
    './resources/enemys/b_shooter2/bomb shooter12.png',
    './resources/enemys/b_shooter2/bomb shooter13.png'
]

ANIMATION_S_TANK = [
    './resources/enemys/s_tank2/s_tank1.png',
    './resources/enemys/s_tank2/s_tank2.png',
    './resources/enemys/s_tank2/s_tank3.png',
    './resources/enemys/s_tank2/s_tank4.png',
    './resources/enemys/s_tank2/s_tank5.png',
    './resources/enemys/s_tank2/s_tank6.png',
    './resources/enemys/s_tank2/s_tank7.png',
    './resources/enemys/s_tank2/s_tank8.png',
    './resources/enemys/s_tank2/s_tank9.png',
    './resources/enemys/s_tank2/s_tank10.png',
    './resources/enemys/s_tank2/s_tank11.png',
    './resources/enemys/s_tank2/s_tank12.png'
]

ANIMATION_S_TANK_FLY = [
    './resources/enemys/s_tank/s_tank1.png',
    './resources/enemys/s_tank/s_tank2.png',
    './resources/enemys/s_tank/s_tank3.png',
    './resources/enemys/s_tank/s_tank4.png',
    './resources/enemys/s_tank/s_tank5.png',
    './resources/enemys/s_tank/s_tank6.png',
    './resources/enemys/s_tank/s_tank7.png',
    './resources/enemys/s_tank/s_tank8.png',
    './resources/enemys/s_tank/s_tank9.png',
    './resources/enemys/s_tank/s_tank10.png',
    './resources/enemys/s_tank/s_tank11.png',
    './resources/enemys/s_tank/s_tank12.png',
]

ANIMATION_S_TANK_FLY_GREEN = [
    './resources/enemys/s_tank_green/s_tank1.png',
    './resources/enemys/s_tank_green/s_tank2.png',
    './resources/enemys/s_tank_green/s_tank3.png',
    './resources/enemys/s_tank_green/s_tank4.png',
    './resources/enemys/s_tank_green/s_tank5.png',
    './resources/enemys/s_tank_green/s_tank6.png',
    './resources/enemys/s_tank_green/s_tank7.png',
    './resources/enemys/s_tank_green/s_tank8.png',
    './resources/enemys/s_tank_green/s_tank9.png',
    './resources/enemys/s_tank_green/s_tank10.png',
    './resources/enemys/s_tank_green/s_tank11.png',
    './resources/enemys/s_tank_green/s_tank12.png',
]

ANIMATION_S_TANK_FLY_BLUE = [
    './resources/enemys/s_tank_blue/s_tank1.png',
    './resources/enemys/s_tank_blue/s_tank2.png',
    './resources/enemys/s_tank_blue/s_tank3.png',
    './resources/enemys/s_tank_blue/s_tank4.png',
    './resources/enemys/s_tank_blue/s_tank5.png',
    './resources/enemys/s_tank_blue/s_tank6.png',
    './resources/enemys/s_tank_blue/s_tank7.png',
    './resources/enemys/s_tank_blue/s_tank8.png',
    './resources/enemys/s_tank_blue/s_tank9.png',
    './resources/enemys/s_tank_blue/s_tank10.png',
    './resources/enemys/s_tank_blue/s_tank11.png',
    './resources/enemys/s_tank_blue/s_tank12.png',
]



ANIMATION_D_BUBBLE = [
    './resources/enemys/d_bubble/bubble1.png',
    './resources/enemys/d_bubble/bubble2.png',
    './resources/enemys/d_bubble/bubble3.png',
    './resources/enemys/d_bubble/bubble4.png',
    './resources/enemys/d_bubble/bubble5.png',
    './resources/enemys/d_bubble/bubble6.png',
    './resources/enemys/d_bubble/bubble7.png',
    './resources/enemys/d_bubble/bubble8.png',
    './resources/enemys/d_bubble/bubble9.png',
    './resources/enemys/d_bubble/bubble10.png',
    './resources/enemys/d_bubble/bubble11.png',
    './resources/enemys/d_bubble/bubble12.png'
] 

ANIMATION_M_BUBBLE = [
    './resources/enemys/m_bubble/bubble1.png',
    './resources/enemys/m_bubble/bubble2.png',
    './resources/enemys/m_bubble/bubble3.png',
    './resources/enemys/m_bubble/bubble4.png',
    './resources/enemys/m_bubble/bubble5.png',
    './resources/enemys/m_bubble/bubble6.png',
    './resources/enemys/m_bubble/bubble7.png',
    './resources/enemys/m_bubble/bubble8.png',
    './resources/enemys/m_bubble/bubble9.png',
    './resources/enemys/m_bubble/bubble10.png',
    './resources/enemys/m_bubble/bubble11.png',
    './resources/enemys/m_bubble/bubble12.png'
] 

ANIMATION_SPIKE_BALL = [
    './resources/enemys/spike_ball/spike_ball1.png',
    './resources/enemys/spike_ball/spike_ball2.png',
    './resources/enemys/spike_ball/spike_ball3.png',
    './resources/enemys/spike_ball/spike_ball4.png',
    './resources/enemys/spike_ball/spike_ball5.png',
    './resources/enemys/spike_ball/spike_ball6.png',
    './resources/enemys/spike_ball/spike_ball7.png',
    './resources/enemys/spike_ball/spike_ball8.png',
    './resources/enemys/spike_ball/spike_ball9.png',
    './resources/enemys/spike_ball/spike_ball10.png'
]
ANIMATION_BOMB_SPIKE_BALL = [
    './resources/enemys/bomb_spike_ball/bomb_spike_ball1.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball2.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball3.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball4.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball5.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball6.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball7.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball8.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball9.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball10.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball11.png',
    './resources/enemys/bomb_spike_ball/bomb_spike_ball12.png'

]

ANIMATION_SPAWNER = [
    './resources/enemys/fly_spawn/spawn1.png',
    './resources/enemys/fly_spawn/spawn2.png'
]
ANIMATION_RED_SPAWNER = [
    './resources/enemys/fly_spawn_2/spawn1.png',
    './resources/enemys/fly_spawn_2/spawn2.png'
]
ANIMATION_BLUE_SPAWNER = [
    './resources/enemys/fly_spawn_3/spawn1.png',
    './resources/enemys/fly_spawn_3/spawn2.png'
]
ANIMATION_GREEN_SPAWNER = [
    './resources/enemys/fly_spawn_4/spawn1.png',
    './resources/enemys/fly_spawn_4/spawn2.png'
]
ANIMATION_PURPLE_SPAWNER = [
    './resources/enemys/fly_spawn_5/spawn1.png',
    './resources/enemys/fly_spawn_5/spawn2.png'
]

ANIMATION_SMOKE = [
    './resources/objects/imgs/smoke/smoke1.png',
    './resources/objects/imgs/smoke/smoke2.png',
    './resources/objects/imgs/smoke/smoke3.png',
    './resources/objects/imgs/smoke/smoke4.png',
    './resources/objects/imgs/smoke/smoke5.png'
]

ANIMATION_M_CIRCLE = [
    './resources/objects/imgs/m_circle/circle1.png',
    './resources/objects/imgs/m_circle/circle2.png',
    './resources/objects/imgs/m_circle/circle3.png',
    './resources/objects/imgs/m_circle/circle4.png',
    './resources/objects/imgs/m_circle/circle5.png'
]

ANIMATION_BORN_SMOKE = [
    './resources/objects/imgs/born_smoke/smoke1.png',
    './resources/objects/imgs/born_smoke/smoke2.png',
    './resources/objects/imgs/born_smoke/smoke3.png',
    './resources/objects/imgs/born_smoke/smoke4.png',
    './resources/objects/imgs/born_smoke/smoke5.png'
]

ANIMATION_E_DEATH_1 = [
    './resources/objects/imgs/e_death_1/e_death1.png',
    './resources/objects/imgs/e_death_1/e_death2.png',
    './resources/objects/imgs/e_death_1/e_death3.png',
    './resources/objects/imgs/e_death_1/e_death4.png',
    './resources/objects/imgs/e_death_1/e_death5.png',
    './resources/objects/imgs/e_death_1/e_death6.png'
]

ANIMATION_E_DEATH_2 = [
    './resources/objects/imgs/e_death_2/e_death1.png',
    './resources/objects/imgs/e_death_2/e_death2.png',
    './resources/objects/imgs/e_death_2/e_death3.png',
    './resources/objects/imgs/e_death_2/e_death4.png',
    './resources/objects/imgs/e_death_2/e_death5.png',
    './resources/objects/imgs/e_death_2/e_death6.png'
]

ANIMATION_E_DEATH_3 = [
    './resources/objects/imgs/e_death_3/e_death1.png',
    './resources/objects/imgs/e_death_3/e_death2.png',
    './resources/objects/imgs/e_death_3/e_death3.png',
    './resources/objects/imgs/e_death_3/e_death4.png',
    './resources/objects/imgs/e_death_3/e_death5.png',
    './resources/objects/imgs/e_death_3/e_death6.png'
]

ANIMATION_E_DEATH_4 = [
    './resources/objects/imgs/e_death_4/e_death1.png',
    './resources/objects/imgs/e_death_4/e_death2.png',
    './resources/objects/imgs/e_death_4/e_death3.png',
    './resources/objects/imgs/e_death_4/e_death4.png',
    './resources/objects/imgs/e_death_4/e_death5.png',
    './resources/objects/imgs/e_death_4/e_death6.png'
]

ANIMATION_P_HURT = [
    './resources/objects/imgs/p_hurt/hurt1.png',
    './resources/objects/imgs/p_hurt/hurt2.png',
    './resources/objects/imgs/p_hurt/hurt3.png',
    './resources/objects/imgs/p_hurt/hurt4.png',
    './resources/objects/imgs/p_hurt/hurt5.png',
    './resources/objects/imgs/p_hurt/hurt6.png'
]

E_PROJECTILE = './resources/objects/imgs/enemy_projectiles/normal.png'

E_BOMB = './resources/objects/imgs/enemy_projectiles/bomb.png'

SFX_E_DEATH = [
    pygame.mixer.Sound('./resources/SFX/e_pop (1).mp3'),
    pygame.mixer.Sound('./resources/SFX/e_pop (2).mp3'),
    pygame.mixer.Sound('./resources/SFX/e_pop (3).mp3')
]
SFX_E_DEATH_V = 1
SFX_E_B_SHOOT = pygame.mixer.Sound('./resources/SFX/e_b_shoot.ogg')
SFX_E_B_SHOOT_V = 0.25
SFX_E_SHOOT = pygame.mixer.Sound('./resources/SFX/e_shoot.ogg')
SFX_E_SHOOT_V = 0.2
SFX_E_EXPLOSION = pygame.mixer.Sound('./resources/SFX/enemy_explosion.wav')
SFX_E_EXPLOSION_V = 0.5
SFX_E_WICK = pygame.mixer.Sound('./resources/SFX/enemy_wick.mp3') #14 segundos
SFX_E_WICK_V = 0.5
SFX_E_LAST_WICK = pygame.mixer.Sound('./resources/SFX/enemy_pre_explosion.mp3') # 3 segundos
SFX_E_LAST_WICK_V = 1
SFX_E_BORN = pygame.mixer.Sound('./resources/SFX/e_born.mp3')
SFX_E_BORN_V = 1


def set_e_volume():
    for s in SFX_E_DEATH:
        s.set_volume(SFX_E_DEATH_V)
    SFX_E_B_SHOOT.set_volume(SFX_E_B_SHOOT_V)
    SFX_E_SHOOT.set_volume(SFX_E_SHOOT_V)
    SFX_E_EXPLOSION.set_volume(SFX_E_EXPLOSION_V)
    SFX_E_WICK.set_volume(SFX_E_WICK_V)
    SFX_E_LAST_WICK.set_volume(SFX_E_LAST_WICK_V)
    SFX_E_BORN.set_volume(SFX_E_BORN_V)

def mute_e_volume():
    for s in SFX_E_DEATH:
        s.set_volume(0)
    SFX_E_B_SHOOT.set_volume(0)
    SFX_E_SHOOT.set_volume(0)
    SFX_E_EXPLOSION.set_volume(0)
    SFX_E_WICK.set_volume(0)
    SFX_E_LAST_WICK.set_volume(0)
    SFX_E_BORN.set_volume(0)