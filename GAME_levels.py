# IMPORTA OUTROS ARQUIVOS USADOS
from GAME_functions import load_current_texts
from PREFAB_level import Level
from PREFAB_tile import Tile

import ctypes

# TAMANHO DA TELA
user32 = ctypes.windll.user32
GAME_SCREEN_W = user32.GetSystemMetrics(0)
GAME_SCREEN_H = user32.GetSystemMetrics(1)
tiles_in_screen = int(GAME_SCREEN_W / 64) + 1
ajusted_screen_void_tiles = []
ajusted_screen_top_tiles = []
ajusted_screen_mid_tiles = []
for i in range(tiles_in_screen):
    ajusted_screen_void_tiles.append(' ')
    ajusted_screen_top_tiles.append('T')
    ajusted_screen_mid_tiles.append('M')

# LISTA COM T0DOS OS LEVEIS
level_list = []


# LEVEL 01

layout_01 = (
    '                                                               b                                                  3                                                                                                         ',
    '                                                                                                          b   b                                                                                    f                        ',
    '                                                                         b   b                       a                                                                         f f       f       BBBB                       ',
    '                                            b                                        a         BBBB                                                                           CTTÇ      BBBB  b                             ',
    '                          a          b      b                  b              CÇ                                                    a                               e  CTTÇ   LMMR                                          ',
    '                                                                          CÇ  LR                                              a                    b     f f    f f    LMMR   LMMR                             ! $  #  ? !  ',
    ' !  #     $            CTÇ   CÇ         !             CTÇ  $          CÇ3 LR  LR3        BBB !  #    !    2              !        B     BB              CTTTÇ   CTTÇ   LMMR   LMMR                          CTTTTTTTTTTTTTTT',
    'TTTTTTTTTTTÇ   CTTTÇ   LMR   LR   CTTTTTTTTTTTTTÇ     LMMTTTTTTTTTTÇ  LR  LR  LR        CTTTTTTTTTTTTTTTTTTÇf f f f f f CTÇ   B   B     BB           CTTMMMMR   LMMR   LMMR   LMMR                          LMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMR   LMMMR   LMR   LR   LMMMMMMMMMMMMMR     LMMMMMMMMMMMMR  LR  LR  LR     CTTMMMMMMMMMMMMMMMMMMMMTTTTTTTTTTTTMMR   B   B     BB         CTMMMMMMMR   LMMR   LMMR   LMMR                          LMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMR   LMMMR   LMR   LR   LMMMMMMMMMMMMMR     LMMMMMMMMMMMMR  LR  LR  LR     LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR   B   B     BB     B   LMMMMMMMMR   LMMR   LMMR   LMMR                          LMMMMMMMMMMMMMMM',
)
lvl1 = {
    'id' : 0,
    'name' : 'World 1 - Stage 1',
    'layout' : layout_01,
    'tile_family' : 'day_city',
    'ground_tile' : 7,
    'killer_tile' : 14,
    'tile_size' : 64,
    'music' : './resources/music/BASKET.mp3',
    'music_volume': 0.15,
    'b_texts': load_current_texts()['b_texts 0'],
    'e_texts': load_current_texts()['e_texts 0'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': [0, 1]
}

layout_02 = (
    '                                                                       3                                                                                                ',
    '                                                                 b                                 a                                            bb                      ',
    '                                                              a     a                                                      f         CTTTTTÇ                            ',
    '                             F        rBBBB                b                                              a                B        rLMMMMMR                            ',
    '                                 F   rBBBr                     CÇ                                                       f          rCMMMMMMR                            ',
    '                    q     b     FF  3BBBBBB f f f f          CTMR                               2                       B        q CMMMMMMMR                            ',
    '   ! $  # F  ! F    CTTTÇ   CTTTTTTTTTTTTTTTTTTTTTTÇ         LMMR           F        r     q    B     CÇ     CTÇ     B           CTMMMMMMMMR             B         ? q B',
    'CTTTTTTTTTTTTTTTÇ   CTTTÇ   LMMMMMMMMMMMMMMMMMMMMMMR   CTÇ   LMMR          rF        F    CTÇ   B     LR     LMMTÇ   B f3f B   q LMMMMMMMMMR         CTTTTTTTTTTTTTTTTTR',
    'LMMMMMMMMMMMMMMMR   LMMMR   LMMMMMMMMMMMMMMMMMMMMMMR   LMR   LMMMTTTTTTTTTTTTTTTTTTTTTTTTTMMMTTTÇ     LR     LMMMMTTTTTTTTTTTTTTTMMMMMMMMMMR         LMMMMMMMMMMMMMMMMMR',
    'LMMMMMMMMMMMMMMMR   LMMMR   LMMMMMMMMMMMMMMMMMMMMMMR   LMR   LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR     LR     LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR         LMMMMMMMMMMMMMMMMMR',
)
lvl2 = {
    'id' : 1,
    'name' : 'World 1 - Stage 2',
    'layout' : layout_02,
    'tile_family' : 'day_city',
    'ground_tile' : 7,
    'killer_tile' : 14,
    'tile_size' : 64,
    'music' : './resources/music/MORNIG.mp3',
    'music_volume': 0.2,
    'b_texts': load_current_texts()['b_texts 1'],
    'e_texts': load_current_texts()['e_texts 1'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_03 = (
    '                                            BBBB    BBBB     BBBB     BBBB                                                                                                     B    B    B                         ',
    '                                            BBBB    BBBB     BBBB     BBBB                                                                                                     B    B    B                         ',
    '                                            BBBB    BBBB     BBBB     BBBB                                                                                                     B    B    B                         ',
    '                                            BBBB    BBBB     BBBB     BBBB                                                                                                     B    B3   B                         ',
    '                                            BBBB    BBBB     BBBB     BBBB                                                                        b                            B         B                         ',
    '                                            BBBB    BBBB    3FBBB     BBB                                                                                                                B                         ',
    '                                            BBBB    B  B b   BBBB      B                                      2                 b                   CÇ                 b                                           ',
    '                                   f        BBBB             BBBB                                             CÇ                      BBB           LR   a         B      a                                        ',
    '                                 CTTTÇ      BBB   b           BB   b              b                    CTÇ    LR     B        b     BBB        CÇ   LR        a                     f                              ',
    '              ffff              rLMMMR                                          b                      LMR    LR                               LR   LR                         f    B    f                    ?    ',
    '             CTTTTÇ             CMMMMr              BFBB              BBBB   b                 CTTÇ    LMR    LR            b                  LR   LR                         B    B    B   CTÇ      CTTTTTTTTTTTT',
    '            CMMMMMMÇ   a       CMMMMMÇ              BBBr  3   f       BBBB             f f     LMMR    LMR    LR         B                     LR   LR                                       LMR      LMMMMMMMMMMMM',
    'TTTTTTTTTTTTMMMMMMMR         CTMMMMMMR      BBBB    BBBB     BBBB     BBBB            CTTTÇ    LMMR    LMR    LR                               LR   LR                                       LMR      LMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMR         LMMMMMMMR      BBBB    BBBB     BBBB     BBBB            LMMMR    LMMR    LMR    LR                               LR   LR                                       LMR      LMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMR         LMMMMMMMR      BBBB    BBBB     BBBB     BBBB            LMMMR    LMMR    LMR    LR                               LR   LR                                       LMR      LMMMMMMMMMMMM'
)
lvl3 = {
    'id' : 2,
    'name' : 'World 1 - Stage 3',
    'layout' : layout_03,
    'tile_family' : 'day_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/ADVENTURE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 2'],
    'e_texts': load_current_texts()['e_texts 2'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_04 = (
    '          B                                                          BBBB                                                                                                BBBBB                                                         ',
    '          B                                                          BBBB3                                                                                               BBBBB                                                         ',
    '          B                                                          BBBB                                                                                                BBBBB                                                         ',
    '          B                                                          BBBB                                                                                                BBBBB                                                         ',
    '          B                                                           BBB                                                                                                 BBBBB                                                        ',
    '          B                                                            BB                                                                                                  BBBBB                                                  ?    ',
    '        ^ B                                                            BBB                                                                   b CTTTTTTTTTÇ                  BBBBB                                     rCTTTTTTTTTTTTTTT',
    ' B        B                                                            BBBB                                                                b   LMr                           BBBBB                                  rCTMMMMMMMMMMMMMMMM',
    '          B                                                                                                                 CTTÇ         b     LMTTÇ                          BB BB                                rCMMMMMMMMMMMMMMMMMM',
    'BBBB    BBB      BBBBBB                                                              2                                     CMMr3       b       LMMMMTTÇr                                                        rCTTMMMMMMMMMMMMMMMMMMM',
    'Br3            rBBB  BB                 q BB         B       rB                     CTTÇ                CTTÇ              CMMMTTÇ    b         LMMMMMMMTTÇ                                                   rCTTMMMMMMMMMMMMMMMMMMMMMM',
    'BBB          BBBBBBq r              f   BBBr                BBB                  b  LMr         b      CMMr   b  b  b  CTTMMMMMMR  b           LMMMMMMMMMMTTTÇr                          B               rCTTTMMMMMMMMMMMMMMMMMMMMMMMMM',
    'TTTTTTTTTTTTTTTTTTTTTTTTTTTÇ   CÇ   B     BBB  f  f     FBBBBBB        b       b    LMÇr              CMMMÇr           LMMMMMMMMR              LMMMMMMMMMMMMMMTTTÇr                    BBBBB         rCTTTMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMR   LR   B          B  B     Fr                   b      LMMTTTTTTÇ     CTTMMMMMÇ           LMMMMMMMMR              LMMMMMMMMMMMMMMMMMMÇ    F f     f     f  BBBBB        CMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMMMMMR   LR   B                   CTTTTTTÇ   a      F         LMMMMMMMMR     LMMMMMMMR           LMMMMMMMMR              LMMMMMMMMMMMMMMMMMMMTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
)
lvl4 = {
    'id' : 3,
    'name' : 'World 1 - Stage 4',
    'layout' : layout_04,
    'tile_family' : 'day_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/ADRENALINE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 3'],
    'e_texts': load_current_texts()['e_texts 3'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/bueiro_in.png',
    'tutorial': []

}

layout_05 = (
    '                                                     FFFFFFFF                                                                                                                                                                  ',
    '                                                     FFFFFFFF                                                                                                                                                                  ',
    '                                                     FFFFFFFF                                                                                                                                                                  ',
    '#                                                    FFFFFFFF                                                                                                                                                                  ',
    '                                                     FFFFFF                                                                                                                                                                    ',
    '                                                     FF3 F                                                                                         FFFFFFFF                                                                    ',
    '                                                      F                                                                                            FFFFFFFFFFFF                                                                ',
    '                                                        h h                                                3                                       FFFFFFFFFFFFF                                                               ',
    '                                                     FFFFFFFF                                             FFF                                         FFFFFFFFF                                    z                          B',
    '                                                    FFFFFFFFFFF                                                                                    á            e                                  FF       a                BB',
    'FFFF              DD           z                 FFFFFF     FFFF                                    d                                              FFFFFFFFFFFF                               h    FF           B   BB    ? BBB',
    'FF1              CTTÇ      z  CTTÇ     h        FFFFFF                              z     z       b                                  h                FFFFFFFFFF                      h      FF    FF      TTTTTTTTTTTTTTTTTTTT',
    'TTTTTTTTTTÇ   CTTMMMM @ CTTÇ  MMMM   CTTTTÇ         FF  1FFFFFFFFF           @a    TTT   TTT  a            2z    a      @ FFF   b   FFF            á         3FF  z           1B      FF  @  FF    FF      MMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMM   MMMMMMM   MMMM  MMMM   MMMMMM  TTTFF      FFFFFFFFFF  TTT   d        MMM   MMM           TTTTTTTT                             FFF    FFFFFFFFFFFFFFFFFF      FFFFF      FF     FF    FF      MMMMMMMMMMMMMMMMMMMM',
    'MMMMMMMMMMM   MMMMMMM   MMMM  MMMM   MMMMMM  MMMMFFFFFFFFFFFFFFFFF  MMM            MMM   MMM           MMMMMMMM          c                        FFFFFFFFFFFFFFFFFFFFF    FFFFF      FF     FF    FF      MMMMMMMMMMMMMMMMMMMM'
)
lvl5 = {
    'id' : 4,
    'name' : 'World 2 - Stage 1',
    'layout' : layout_05,
    'tile_family' : 'sewage',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/TRANSITION.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 4'],
    'e_texts': load_current_texts()['e_texts 4'],
    'b_img': './resources/ilustrations/lvl_arts/bombs.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': [2]

}

layout_06 = (
    '         ^                    F                                           FFFFFFFFFF                   MM             MMM               MMMMM                                               ',
    '         ^                    F                                             3FFFFFFF                   MM             MMM               MMMMM                                               ',
    '         ^                    F                                               FFFFF                    MM             MMM               MMMMM                                               ',
    '         ^                    F                                                FFF                     MM             MMM               MMMMM                                               ',
    '                              F                                                FF                      MM             MMM                MMMM                                               ',
    '                FFF3          F                                           FFFFFFFF                     MM     TTTTT   MMM                rMMM        e                                      ',
    '                FFFFFFFF      F                                             FFFFFFF                     MTTT  MMMMM   MMM   z   TTTT     MMMM                    z     e                    ',
    '                 FFFFFFFFFFF                                              á   3FFF                            MMMMM   MMM  TTTTTMMMMTTT  MMMM            z       TT                    ?    ',
    '                                                                   h     FFFFFFF                              MMMMM   MMM         rMMMM  MMMM    z       TT      MM             TTTTTTTTTTTT',
    '                 t                                          h      FF                                        2MMMMM   MMM        TTMMMM  MMMM    TT      MM      MM        e    MMMMMMMMMMMM',
    '                FFFF       FFFF                    h       FF      FF                     z       z         TTMMMMM   MMMTTTTT   MMMMMM  MMMM    MM      MM      MM             MMMMMMMMMMMM',
    '                FFFFD       rr                     FF      FF      FF                t   TTTT     TTTT  a   MMMMMMM   MMMMMMMM    rMMMM  MMMMTT  MM      MM      MM             MMMMMMMMMMMM',
    'TTTTTTTTTTTTT     1FFFFFFFFFFFFF   a  @a    F      FF      FF  @   FF                TTTTMM         MM  @   MMMMMMM              TTMMMM  MMMMMM  MM      MM      MM    @     @  MMMMMMMMMMMM',
    'MMMMMMMMMMMMMTTTTTFFFFFFFFFFFFFF            F      FF      FF      FF    F   2    F  MMMMMMu  FFF u MM      MMMMMMMTTTTTTTTTTTTTMMMMMMM          MM      MM      MM             MMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMFFFFFFFFFFFFFFF            F      FF      FF      FF    F   FF   F  MMMMMMTTTTTTTTTMM      MMMMMMMMMMMMMMMMMMMMMMMMMMMTTTTTTTTTTMM      MM      MM             MMMMMMMMMMMM'
)
lvl6 = {
    'id' : 5,
    'name' : 'World 2 - Stage 2',
    'layout' : layout_06,
    'tile_family' : 'sewage',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/WAITING.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 5'],
    'e_texts': load_current_texts()['e_texts 5'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_07 = (
    '         ^                                                           MM                 MM                                                                                                   ',
    '         ^                                                           MM                 MM                                                                                                   ',
    '         ^                                                           MM                 MM              MMMMMMMMMMMMM            MMMMMM           MMMM          MM                           ',
    '         ^                                                           MM                 MM              MMMMMMMMMMMMM            MMMMMM           MMMM          MM                           ',
    '                                                                     MM                 MM               MMMMMMMMMMMM            MMMMMM           MMMM                                       ',
    '                                                                     MM                 MM                MMM      MM                                                                        ',
    '                                                             t       MM                TMM               á    z                  t                u                                          ',
    '                            FF                               TT      Mr                rMM              TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT        TT             t        ?    ',
    '                          z 1F                               MM      MT    TTTTTTT á TTTMM               MMMMM     FF  MMM                          rMMM        MM           TTTTTTTTTTTTTTTT',
    '                          TTTT                          TF   MM      MM    MMMMMMM   MMMMM               M  Mr  1   F         z    z                TMMM     c  MM    TT     MMMMMMMMMMMMMMMM',
    'FFF                       MMMM                          MT   MMTTTT  MMTT  MMMMMMM   MMMMM               M  MTTTT      z    TTT TTTT TTTTTTTTTTTT  MMMMM        MM    MM     MMMMMMMMMMMMMMMM',
    'F3 á           i   i      MMMM    i i       i i    TT   MM   MMM              MMMM   MMMMM         TTT   M     MMTTTTTTTTTTTMMMFMMMMFMMMr      MM  MMMMM        MM    MM     MMMMMMMMMMMMMMMM',
    'TTTTT  TTTTT @ TTTTTTTT   MMMM    TTTT @    TTTT   MM   MM   MMM3i   i        MMMM     2   h  h  h M3r          MM          MM    MMFMMMM           MMMM @      MM    MM     MMMMMMMMMMMMMMMM',
    'MMMMM  MMMMM   MMMMMMMM   MMMM    MMMM      MMMM   MM   MM   MMTTTTTTTTTTTTTTTTMMMTTTTTTTTTTTTTTTTTMTTTTTTTTT         z                    TTTTTTTTTMMMM        MM    MM     MMMMMMMMMMMMMMMM',
    'MMMMM  MMMMM   MMMMMMMMF  MMMM    MMMM      MMMM   MM   MM   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTMMMMMMMMMMMMM        MM    MM     MMMMMMMMMMMMMMMM'
)
lvl7 = {
    'id' : 6,
    'name' : 'World 2 - Stage 3',
    'layout' : layout_07,
    'tile_family' : 'sewage',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/LI E CONCORDO.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 6'],
    'e_texts': load_current_texts()['e_texts 6'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_08 = (
    '         ^                                                         FFF3                                                                          FF                                                                                         ',
    '         ^                                                         FFF                                                                           FF                                                                                         ',
    '         ^                                                         FFFFF                 FFFFFFF                                                 FF                                                                                         ',
    '         ^                                                         FFFFFFF             FFFFFFFFFFFF                          F                   FF                                                                                       # ',
    '                                                                  3FFF  FFFF           FFFFFFFFFFFF                          FF                  FF                                                                                         ',
    '                                                                 FFFFF    FFF            FFFFFFFF                            FF        FF        FF                                               F         F                               ',
    '                                                                  FFFF     FFFF                                      F       FF       FFí    FF  FF                  FFF              F           FF        Fí                              ',
    '                  FFFF                                              FF       FFF       FFFFFFFFFFFFF         F      Fí 2     FF      FFFF    FF  FF                 FFFFFF            FF          FFF       F                               ',
    '                 FFFFFFF                            FFFFF   d       FF        FFF      FíFFFFíFFFFFFF       Fí         F     FF      FFFFF   FF  FF                 FFFFFFF           FF                    F                               ',
    '                FFFFFFFFF                          FíFFFF            F        FFFF    FF FFFF FFFFFFF                        FF      FFFFFF  FF  FF                 FFFFFFFFF         F           t         F  FFF                          ',
    'B11            FíFFFFr3                     FFFF  FFFFFF          q          FíFFF               FFFFFF                   F  FF      FFFFFF  FF  FF                    rFFFFF             r       FFFFF     F                               ',
    'BBB            FFFFFFFFFFr         D          rFF   FFFFF         TTTTTT                           FFFF                  Fí  FF      á       FF               B    t  1FFFFFFF    B   t   F         FFr     á            FF            ?    ',
    'TTTTTTTTTT   @ TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  F  @   MMMMMM    TTTTTTT                TTTT   @          @   FF  FF     TTTTTTTTTFFFFFFF   TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT @  FFF          Fí  @  TTTTTTTTTTTTT',
    'MMMMMMMMMM     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM         MMMMMM    MMMMMMM                MMMM                  FF         MMMMMMMMMFFFFFFF   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                        MMMMMMMMMMMMM',
    'MMMMMMMMMM     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM         MMMMMM    MMMMMMMTTTTTTTTTTTTTTTTMMMM                  FFFFFFFF   MMMMMMMMMFFFFFFF   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                        MMMMMMMMMMMMM',
)
lvl8 = {
    'id' : 7,
    'name' : 'World 2 - Stage 4',
    'layout' : layout_08,
    'tile_family' : 'sewage',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/ONE_MORE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 7'],
    'e_texts': load_current_texts()['e_texts 7'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/bueiro_out.png',
    'tutorial': []
}

layout_09 = (
    '         ^                                                                                                                                                                                                                     ',
    '         ^                                                                                                                                                                                                                     ',
    '         ^                                                                                                                                                                                                                     ',
    '         ^                                                                                                                                                                                                                     ',
    '              BB                                                                                                                                                                                                               ',
    '              BBB                                                                                                            BB     BBB                                                                                        ',
    '              BBBB                                                                             FF          BBBBBBBBB3                 BBB                                                                                      ',
    '              á3BBBB                   BBB         B BBBBB                                     FF BBBBBBBBBBBBBBBBBBBB    B             BB                                                                                     ',
    '              BBBBBBBB     n            BBBBBBBBB BBBBBBBBBB                                       BBBBBBBBBBBBBBBBBBB                  BB                      BBB                                                            ',
    '              BB                        BBBBBBBBBBBB     BBBB            o                                      BBBBBB              ŵ   BB                                                                                     ',
    '4             BB                          B      BB                                     p      4                  BBBB            BB    BB                      é         j   p    B                                      ?    ',
    'BB              h   BB                               F v       v            n                  FF    i i F v    v   2            BBB    BB3                            p           B   x            x                CTTTTTTTTT',
    'TTTÇ    CTTTTTTTTTTTTTTÇ   p    CTTÇ      v   F v    BBBBBBBBBBBB                           CTTTTTTTTTTTTTTTTTTTTTTTTTÇ         BBBB    BB       i   i   ô      CTTÇ               B          â               j   m  LMMMMMMMMM',
    'MMMMTTTTMMMMMMMMMMMMMMMR        LMMR    BBBBBBBBBBBBBBBBBBBBBB     w                  ŵ  CTTMMMMMMMMMMMMMMMMMMMMMMMMMMR                 BB     CTTTTTTTTTTTTÇ   LMMR              CTTTTTTTTTTTTTTTTTTTTTTTÇ          LMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMMMR        LMMR     BBBBBBBBBBBBB                                   LMMMMMMMMMMMMMMMMMMMMMMMMMMMMR  w              BB     LMMMMMMMMMMMMR   LMMR              LMMMMMMMMMMMMMMMMMMMMMMMR          LMMMMMMMMM'
)
lvl9 = {
    'id' : 8,
    'name' : 'World 3 - Stage 1',
    'layout' : layout_09,
    'tile_family' : 'night_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/GOING ON.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 8'],
    'e_texts': load_current_texts()['e_texts 8'],
    'b_img': './resources/ilustrations/lvl_arts/cristais.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': [3]
}

layout_10 = (
    '         ^                                                                                                                                                                                                                        ',
    '         ^                                                                                                                                                                                                                        ',
    '         ^                                                                                                                                                                                                                        ',
    '         ^                                                                                                                                                                                                                        ',
    '                                                                                                                                                                                                                                  ',
    '                                                                                                                                                                                                                                  ',
    '                                                                                                                                                                                                        BBBB                      ',
    '                                                                                        BBBBBBB                                                                                    BBB                 BBBB                       ',
    '                                                                                        B 4B 3B                               BB      BB3                           í               B BBB             BBB                         ',
    '                            á                                           j               BááBááB                á     á        BBBB  BBBB                                            BBBBBBBBBBBBBBBBBBBBB                         ',
    '        j                   á                                              j                                                  áBBBááBBBá                                          í    Bá  BáBáá  Bá  Bá              á           ',
    '3          j         1F               p       l   áá           áá                   j                                  2                          o         j         j   ô           í       á     á     ô      l   áá       ?   ',
    'TTÇ             p  CTTTTTÇ     m   j     B        CÇ   j   j   CÇ             j   j    CTTTTTTTTTÇ                 ŵ CTTÇ    CTTTTTTTTTTÇ   m          4           j     CTTTTTÇ  CTTTTTTTTTTTTTTTTTTTTTTTTTÇ        CTTTTTTTTTTTT',
    'MMR               CMMMMMMR                        LR           LR   k                  LMMMMMMMMMRw     k            LMMR    LMMMMMMMMMMR            CTTTÇ      j        LMMMMMR  LMMMMMMMMMMMMMMMMMMMMMMMMMR        LMMMMMMMMMMMM',
    'MMR               LMMMMMMR                        LR           LR                      LMMMMMMMMMR                   LMMR    LMMMMMMMMMMR            LMMMR               LMMMMMR  LMMMMMMMMMMMMMMMMMMMMMMMMMR        LMMMMMMMMMMMM'
)
lvl10 = {
    'id' : 9,
    'name' : 'nome 1',
    'layout' : layout_10,
    'tile_family' : 'night_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/DANCE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 9'],
    'e_texts': load_current_texts()['e_texts 9'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_11 = (
    '        ^            B                                                                                                                    F3                                                                                                        ',
    '        ^            B                                                                                                                    F                                                                                                         ',
    '        ^            B                                                                                                                    FF                                                                                                        ',
    '        ^            B                                                        B                   B                                       FF                                                                                                        ',
    '                     B                                                        B                   B                                       FF                                                                          p                             ',
    '                     B                                                        B                   B                                 BBBB  FFF                                                                    o    B                             ',
    '                  á  B                BB                                      B                   B                                    B  FFF                                                                                                       ',
    '                  á  B             Bí B3                             B        B3                  B                                 B  B  FFF                                q   î          q       B     p      B                                  ',
    '                  B  B             Bí B                           p      B    B               B   B                           F     B íB  FFF                               CTTTTTTTTTTTTTTTTÇ            B                                         ',
    '                  BííB             Bí B                        n         B    B               Bí  B                           F     B íB  FFFF                        ô     LMMMMMMMMMMMMMMMMR      m                        B                      ',
    '4                 B  B             Bí B                      p           B  BB       áá   j   BB              á            B  F     B íB  FFFF                   CTTTTTTÇ   LMMMMMMMMMMMMMMMMR                                                      ',
    'BBB  â                       n  B  Bí B        p   o n CTTÇ              BííB           j                á        á        Bí B     B íB  FFFF             ô     LMMMMMMR   LMMMMMMMMMMMMMMMMR                               m      B          ?    ',
    'TTTTTTTTTTTTÇ    CTTTTTTTÇ                   n         LMMR              B  B    á   CÇ           BBBB              CÇ        B     B  B         2    CTTTTTTÇ   LMMMMMMR   LMMMMMMMMMMMMMMMMR                                      n      CTTTTTTTT',
    'MMMMMMMMMMMMR    LMMMMMMMR                 p           LMMR                      p   LR         BBBB x              LR    BBBBB                44F    LMMMMMMR   LMMMMMMR   LMMMMMMMMMMMMMMMMR                                             LMMMMMMMM',
    'MMMMMMMMMMMMR    LMMMMMMMR        CTTTTTÇ              LMMR          BBBBBBBBBB      LR      BBBBBBB                LR        B     CTTTTTTTTTTTTTÇ   LMMMMMMR   LMMMMMMR   LMMMMMMMMMMMMMMMMR                                             LMMMMMMMM'
)
lvl11 = {
    'id' : 10,
    'name' : 'nome 1',
    'layout' : layout_11,
    'tile_family' : 'night_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/FOCUS.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 10'],
    'e_texts': load_current_texts()['e_texts 10'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_12 = (
    '        ^    LMMMMMMR     LMMR      LMMR                                                                                                            BBBBBBBBBB                                                                                      ',
    '        ^    LMMMMMMR     LMMR3     LMMR                                                                                                            BBBBBBBBBB                                                                                      ',
    '        ^    LMMMMMMR     LMMR      LMMR                                                                                                            BBBBBBBBBB                                                                                      ',
    '        ^    LMMMMMMR     LMMR      LMMR                                                              BBBBBBBBBBBB                                  BBBBBBBBBB                                                                                      ',
    '             LMMMMMMR     LMMRj     LMMR                                                 y            BBBBBBBBBBBB                                  BBBBBBBBBB                                                                                      ',
    '             LMMMMMMR     LMMR                                                           CTTTÇ        BBBBBBBBBBBB                                  BBBBBBBBBB                                                 B                                    ',
    '             LMMMMMMR     LMMR  j                                                    B   LMMMR                   á                                  BBBBBBBBBB                                                 BB                                   ',
    '             LMMMMMMR     LMMR             42         p                          B       LMMMR    â              áô       42                        BBBBBBBBBB                                                 BBB áá        á                      ',
    '             LMMMMMMR     LMr       CTTTTTTTTÇ  p  n     CÇ                ééy           LMMMR    BBBBBBBBBBBBBBBBBBB     BB          B             é   BBBBB                    á               á   F          ú   Fú  Fú  ú                       ',
    '                  LMR     LMTÇ      LMMMMMMMMR           LR                BB            LMMMR      FFF         FFF                                 é    BBB                                          â                 áá                          ',
    '4            ér  y        LMMR  éé  LMMR   3LR           LR                              LMMMR       F           F                  4     B         éF       4                        á               CTTTTTTTTTTTTTTTTTTTTTTTTÇ                    ',
    'FF        ô  CTTTTTTÇ     LMMMTÇ  CTMMMR    LR           LR                              LMMMR       F           F                  B               BBBBBBBBBB     î         á   á                    LMMMMMMMMMMMMMMMMMMMMMMMMR               ?    ',
    'TTTTTTTTTTTTTMMMMMMMR                       LR           LRî                         î   LMMMR       F           F            û              û       BBBBBBBB     CTTTTÇ            3                 LMMMMMMMMMMMMMMMMMMMMMMMMR         CTTTTTTTTTT',
    'MMMMMMMMMMMMMMMMMMMMRâ                  â   LR           LMTTTTÇ  CTTTTTTTTTTTTTTÇ  CTTTTMMMMR       F           F           CTTTTTTTTTTTTTTTTTTTÇ    FFFFFF      LMMMMR                              LMMMMMMMMMMMMMMMMMMMMMMMMR         LMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMMMMTTTTTTTTTTTTTTTTTTTTTTTMM           LMMMMMR  LMMMMMMMMMMMMMMR yLMMMMMMMMR       F           F           LMMMMMMMMMMMMMMMMMMMR     F  F       LMMMMR                              LMMMMMMMMMMMMMMMMMMMMMMMMR         LMMMMMMMMMM'
)
lvl12 = {
    'id' : 11,
    'name' : 'nome 1',
    'layout' : layout_12,
    'tile_family' : 'night_city',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/CHALENGE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 11'],
    'e_texts': load_current_texts()['e_texts 11'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/court.png',
    'tutorial': []
}

layout_13 = (
    '                                                                                                                                                                                                                                                                                                                                                                                ',
    '                                                                                                                                                                                                                                                                                                                                                                                ',
    '                                                                                                                                                                                                                                                                                                                                                                                ',
    '                                                                                                                                                                                                                                                                                                                                                                                ',
    '  B                                                                                                                                                                                                                                                                                                                                                                             ',
    '3 B                                                 á                                                                                                                                              y                                                                                                    4                                                                       ',
    'BBB                                                 á                                                         3                                                                                 BB                                                                                                     BBB                                                                      ',
    '                                            ( CTÇ             á             4                            BBBBBBBBBB                                               B                                   gg      5    á                              p   BB                            o   á            á                                        á                                 ',
    '                                        (     LMR             á            4B                            á        á                                                                    2 y  B        CTTÇ    BBB   B           á               n          )                             á                                            á        á                                 ',
    '                          (         (         LMR             á           CTÇ                            á g  g  gá                  á                        B        BB              BB            LMMR               k      á            p                )                    (                                    á       á    BBB       á                                 ',
    '6                    (         CTÇ            LMR       m           m     LMR              s             BBBBBBBBBB                 á                                                                LMMR                                                       )                            m   m              ê                   BóB              ê                     ?    ',
    'Fs   FFF                       LMR            LMR                         LMr     g  g  g FFF g  g  g     BBBBBBBB                 á    s                 B                         B            y3  LMMR                             m                            )         (                   (             BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB       CTTTTTTTTTTTTTTT',
    'TTTTTTTTTTTTTTTTTTÇ            LMR            LMR                         LTÇ    CTTTTTTTTTTTTTTTTTTTÇ (   CÇ  CÇ  )           sB      BBB    k    CTÇ                û       BBB                 B  LMMR               ^                                             BBB     m                                 í  í  í  í  í  í  í  í  í  í  í  í  í  í        LMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMR            LMR            LMR                         LMR    LMMMMMMMMMMMMMMMMMMMR     LR  LR    BBB      BBB      CTÇ         LMR                CTTÇ             BB            LMMR                                                                                                      CTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTÇ       LMMMMMMMMMMMMMMM',
    'MMMMMMMMMMMMMMMMMMR            LMR            LMR                         LMR    LMMMMMMMMMMMMMMMMMMMR     LR  LR             CTÇ      LMR         LMR                LMMR                   B       LMMR                                                                                                      LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR       LMMMMMMMMMMMMMMM'   
)
lvl13 = {
    'id' : 12,
    'name' : 'nome 1',
    'layout' : layout_13,
    'tile_family' : 'spaceship',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/SYFY-FUNK.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 12'],
    'e_texts': load_current_texts()['e_texts 12'],
    'b_img': './resources/ilustrations/lvl_arts/pills.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': [4]
}

layout_14 = (
    '              BB                          BBBBB                                           B                           B                                                                      ',
    '              BB                           BBB                                            B                           B                                                                      ',
    '              BB                           BBB                                            B                           B                                                                      ',
    '              BB                           BBB                                            B                           BíB                                                                    ',
    '              BB                           BBB                                            B                           BB                                                                     ',
    '              BB                           BBB                                            BBB          sB           BBB3                                                                     ',
    '              BB 3       B                 BBB                                            Bs    BBBBBBBBBBBBBBBBB    sB    B                                                                 ',
    '              BB g g u  B                   B                                             BBB           B           BBB   BóB                                                                ',
    '              BBBBBBBBBB                    B                                             B g g g g    BBB    g g g g B    B                                                                 ',
    'BBBBBBBB       BBB                          B              2                    g g       BBBBBBBBB    sBs    BBBBBBBBBBB                                             g                      ',
    '      3B        s            BBBB           B             CÇB                  sCTTÇ      Br    BB     BBB     BBBBBBB                                          g    BBB                     ',
    '       B4     BBB             rr                        CTTÇr             BB   BCTTTÇ     BBB        BBBBBBB     BBBBB                           B       o      B     áB                     ',
    'q      BB                    CTTÇ           x           LMMRB            B     rLMMMR          FFFv   rBBBr             B    1    B      B      BóB      B            áB                     ',
    'FFv           t    CÇ       rLMMR   v   v       v   v   LMMRs        CÇ        CLMMMRv  CTTTTTTTTTTTÇBBBBBBBCTTTTTTTTTTTÇv  CTÇv  BááááááóáááááááááááááááóáááááááááááááB                ?    ',
    'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTÇnCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
)
lvl14 = {
    'id' : 13,
    'name' : 'nome 1',
    'layout' : layout_14,
    'tile_family' : 'spaceship',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/CYBER-CRAZY.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 13'],
    'e_texts': load_current_texts()['e_texts 13'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_15 = (
    '                                                                                                                                                                                                                                                                                                                                              ',
    '                                                                                                                                                                                                                                                                                                                                              ',
    '                                                                                                                                                                                                                                                                                                                                              ',
    '                                                                                                                            BBB                                                                                                                                                                                                               ',
    '                                                                                                                            B á                               BBB                                                                                                                                                                             ',
    '                                                                                                                            B3á                              BBíBB       2                       á                                                                                                                                            ',
    '                                                     B                                                                      BBB                           BBBBB BBBBBíBBBBBBB                         á        á      á                                                                                                                       ',
    '                                                     B                                                                             h  h                   B           BBBBBBBB       BBB                    n                                                                                                                                 ',
    '                                                     B                 b        e                                                BBBBBBBB            BB   B                  BB     Bí   w                ŵw          BB              BBBBBB                                                                                                  ',
    '                             g                                              BBB     BBB                                        BBBBBBBBBBB                B                  BB                                            )          BBBBBBBBBBBBBBBBBBBBBBB                      B    >    >    B                          p           ?    ',
    '                        g    CÇ             sBBBB                    b    BBB         BBB                 b                 BBBBBB    BBBBB               B     F           ásBB                                                      BBBBBBBBB     Bá3 Bá Báá       5         (                      )                  p              CTTTTT',
    '  f  f   f      g g    CTÇ   LR            sBBBrá                                           a         j      a             BBBBBB                        Bí  BBBB            BBB                                                      BB                             CÇ   (                                )         p              CTTTTTTTTT',
    'TTTTTTTTTTTÇ   CTTTÇ   LMR3  LR       FF   BBBBBB g á g á          b                             a                             BB  1BBBBBBBBB     z      B         BBBB      BBBB                                              ê        i   i   i  CTTTTTTTTTTTÇ     LR                                          p               CTTTTTTTTTTTT',
    'MMMMMMMMMMMR   LMMMR   LMR   LR   CTTTTTTTTTTTTTTTTTTTTTTÇ    CTÇ                                                   g    CÇBB      BBBBBBBBBB    CTTÇ             árBrá     4BBBB                                             CTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTÇ   LR                                       o                  LMMMMMMMMMMMM',
    'MMMMMMMMMMMR   LMMMR   LMR   LR   LMMMMMMMMMMMMMMMMMMMMMMR    LMR                                                 CTTÇ  CTTÇBBBBBBBBBBBBBBBBB    LMMR   CTTTTTTTTTTTTTTTTTTTTTTTÇ                                             LMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMR   LR                                                          LMMMMMMMMMMMM'
)
lvl15 = {
    'id' : 14,
    'name' : 'nome 1',
    'layout' : layout_15,
    'tile_family' : 'spaceship',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/ENJOY.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 14'],
    'e_texts': load_current_texts()['e_texts 14'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_16 = (
    '                                                                                                                                                                                                                         ',
    '                                                                                                                                                                                                                         ',
    '3                                                                                                                                                                                                                        ',
    '                                                                                                                                                                                                                         ',
    '                                                                                                                                                                                                                3        ',
    '                                                                                                     3                                                                                                                   ',
    '                                                                                                                                                                                                                         ',
    '                                                                                                                                        p    n                                                                           ',
    '                                                                 n     j                                         o                p             )                                                                        ',
    '                                                            n                                       6                       n                                                                                            ',
    ' 6            >                                   p    k                             o              j     n           p     p                         p         n      m     j            j           k                  ',
    'FF   g                           o          p                                m                  p                     n                                                             j            j                  ?    ',
    'TTTTTTTTTTTÇ        l                  p                                                  p                      m                                         p                                                 CTTTTTTTTTTT',
    'MMMMMMMMMMMR              m                                                                                                                                                                                  LMMMMMMMMMMM',
    'MMMMMMMMMMMR                                                                                                                                                                                                 LMMMMMMMMMMM'
)
lvl16 = {
    'id' : 15,
    'name' : 'nome 1',
    'layout' : layout_16,
    'tile_family' : 'spaceship',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/CYBER-CRAZY.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 15'],
    'e_texts': load_current_texts()['e_texts 15'],
    'b_img': './resources/ilustrations/lvl_arts/standard_begin.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

layout_17 = (
    ajusted_screen_void_tiles,
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '                          ',
    '             Ã            ',
    ajusted_screen_top_tiles,
    ajusted_screen_mid_tiles,
    ajusted_screen_mid_tiles
)
lvl17 = {
    'id' : 16,
    'name' : 'nome 1',
    'layout' : layout_17,
    'tile_family' : 'spaceship',
    'ground_tile' : 12,
    'killer_tile' : 18,
    'tile_size' : 64,
    'music' : './resources/music/SUSPENSE.mp3',
    'music_volume': 0.4,
    'b_texts': load_current_texts()['b_texts 16'],
    'e_texts': load_current_texts()['e_texts 16'],
    'b_img': './resources/ilustrations/lvl_arts/door.png',
    'e_img': './resources/ilustrations/lvl_arts/standard_end.png',
    'tutorial': []
}

level_list.append(lvl1)
level_list.append(lvl2)
level_list.append(lvl3)
level_list.append(lvl4)
level_list.append(lvl5)
level_list.append(lvl6)
level_list.append(lvl7)
level_list.append(lvl8)
level_list.append(lvl9)
level_list.append(lvl10)
level_list.append(lvl11)
level_list.append(lvl12)
level_list.append(lvl13)
level_list.append(lvl14)
level_list.append(lvl15)
level_list.append(lvl16)
level_list.append(lvl17)
