# IMPORTA OS ARQUIVOS UTILIZADOS
from PREFAB_tile import Tile
from CONFIG_game import *
from PREFAB_enemy import *
from PREFAB_boss import *
from PREFAB_collectables import *
from PREFAB_objects import *

# IMPORTA AS BIBLIOTECAS USADAS
import pygame


class Level:
    def __init__(self, id, name, layout, tile_family, ground_tile, killer_tile, tile_size, music, music_volume, b_texts, e_texts, b_img, e_img, tutorial = []):
        pygame.init()
        pygame.mixer.init()
        # PROPRIEDADES DE INICIAÇÂO
        self.id = id
        self.name = name
        self.layout = layout
        self.tile_family = tile_family
        self.tile_size = tile_size
        self.ground_tile = ground_tile
        self.killer_tile = killer_tile
        self.music = music
        self.music_volume = music_volume
        self.b_texts = b_texts
        self.e_texts = e_texts
        self.b_img = b_img
        self.e_img = e_img
        self.tutorial = tutorial


        # PROPRIEDADES
        self.screen_w = GAME_SCREEN_W
        self.screen_h = GAME_SCREEN_H

        self.length = len(self.layout[0]) # medido em tiles
        self.width = self.length * self.tile_size
        self.victory_point = self.width - 5 * self.tile_size

        self.size = len(self.layout) # medido em tiles
        self.height = self.size * self.tile_size

        self.height_layouttop_to_grond = self.ground_tile * self.tile_size
        self.height_screenbottom_to_ground = 192

        self.tiles_group = pygame.sprite.Group()
        # self.tiles_group = TileGroup()
        self.enemys_group = pygame.sprite.Group()
        self.collectables_group = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()

        self.get_tiles_map()
        self.get_enemys_map()
        self.get_collectables_map()
        self.get_objects_map()

        
    def get_tiles_map(self):

        self.height_layouttop_to_grond = self.ground_tile * self.tile_size
        self.air_space = self.screen_h - self.height_layouttop_to_grond - self.height_screenbottom_to_ground
        self.kill_height = self.killer_tile * self.tile_size + self.air_space

        self.tiles_group.empty()

        for row_index, row in enumerate(self.layout):
            for col_index, element in enumerate(row):
                if element == 'T': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'top', 0 ))
                if element == 'L': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'lside', 0 ))
                if element == 'R': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'rside', 0 ))
                if element == 'M': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'mid', 0 ))
                if element == 'C': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'lcorner', 0 ))
                if element == 'J': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'i_lcorner', 0 ))
                if element == 'Ç': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'rcorner', 0 ))
                if element == 'B': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'single', 0 ))
                if element == 'F': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'single2', 0 ))
                if element == 'D': self.tiles_group.add(Tile((col_index * self.tile_size, self.air_space + row_index * self.tile_size), self.tile_size, self.tile_family, 'single3', 0 ))


    def get_enemys_map(self):
        self.enemys_group.empty()

        for row_index, row in enumerate(self.layout):
            for col_index, element in enumerate(row):
                if element == 'a': self.enemys_group.add(Fly1([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'b': self.enemys_group.add(Fly2([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'c': self.enemys_group.add(Fly3([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'd': self.enemys_group.add(Fly4([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'e': self.enemys_group.add(Fly5([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'f': self.enemys_group.add(Octopus([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'g': self.enemys_group.add(EletricOctopus([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'h': self.enemys_group.add(Tank([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'i': self.enemys_group.add(Spike([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'j': self.enemys_group.add(Ball1([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'k': self.enemys_group.add(Ball2([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'l': self.enemys_group.add(Ball3([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'm': self.enemys_group.add(Ball4([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'n': self.enemys_group.add(Ball5([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'o': self.enemys_group.add(Ball6([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'p': self.enemys_group.add(Ball7([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'q': self.enemys_group.add(BigShooter([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'r': self.enemys_group.add(SmallShooter([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 's': self.enemys_group.add(CrazyShooter([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 't': self.enemys_group.add(BombShooter([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'u': self.enemys_group.add(BombShooter2([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'v': self.enemys_group.add(Shootank([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'w': self.enemys_group.add(Shootank2([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'ŵ': self.enemys_group.add(Shootank2b([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'x': self.enemys_group.add(Shootank3([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'y': self.enemys_group.add(Shootank4([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'z': self.enemys_group.add(MegaOctopus([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size], tiles = self.tiles_group))
                if element == 'á': self.enemys_group.add(SpikeBall([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'é': self.enemys_group.add(BombSpikeBall30([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'í': self.enemys_group.add(DamageBubble([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'ó': self.enemys_group.add(MagnBubble([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'ú': self.enemys_group.add(BombSpikeBall60([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'â': self.enemys_group.add(ShootankSpawner([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'ê': self.enemys_group.add(EletricOctopusSpawner([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'î': self.enemys_group.add(ShootankSpawnerBlue([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'ô': self.enemys_group.add(OctopusSpawner([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'û': self.enemys_group.add(ShootankSpawnerRed([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                if element == 'Ã': self.enemys_group.add(Boss1([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
        

    def get_collectables_map(self):
        self.collectables_group.empty()

        for row_index, row in enumerate(self.layout):
            for col_index, element in enumerate(row):
                if element == '0': self.collectables_group.add(C_Coin([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '1': self.collectables_group.add(C_Bomb([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '2': self.collectables_group.add(C_Heart([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '3': self.collectables_group.add(C_MegaCoin([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '4': self.collectables_group.add(C_Cristal([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '5': self.collectables_group.add(C_Syringe([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                if element == '6': self.collectables_group.add(C_Pills([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
              

    def get_objects_map(self):
        self.objects_group.empty()

        for row_index, row in enumerate(self.layout):
            for col_index, element in enumerate(row):
                # CIDADE DE DIA
                if self.tile_family == 'day_city':
                    if element == '?': self.objects_group.add(Flag([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                    if element == '!': self.objects_group.add(DayLightPost([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                    if element == '#': self.objects_group.add(DayBench([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                    if element == '$': self.objects_group.add(DayHydrant([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                # ESGOTO
                elif self.tile_family == 'sewage':
                    if element == '?': self.objects_group.add(S_Flag([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                    if element == '@': self.objects_group.add(Waterfall([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == '#': self.objects_group.add(Stair([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                    if element == 'º': self.objects_group.add(Lamp([col_index * self.tile_size, self.air_space + row_index * self.tile_size]))
                elif self.tile_family == 'night_city':
                    if element == '?': self.objects_group.add(N_Flag([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                elif self.tile_family == 'spaceship':
                    if element == '?': self.objects_group.add(Flag([col_index * self.tile_size, self.air_space + row_index * self.tile_size + self.tile_size]))
                    if element == '>': self.objects_group.add(SignR([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == '<': self.objects_group.add(SignL([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == '^': self.objects_group.add(SignU([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == '|': self.objects_group.add(SignD([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == '(': self.objects_group.add(SignLU([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))
                    if element == ')': self.objects_group.add(SignLD([col_index * self.tile_size, self.air_space + (row_index) * self.tile_size ]))


              

    def update_window_info(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.get_tiles_map()
        self.get_enemys_map()
        self.get_collectables_map()
        self.get_objects_map()
