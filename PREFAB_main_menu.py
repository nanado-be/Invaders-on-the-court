# IMPORTA OS OUTROS ARQUIVOS
from CONFIG_colors import *
from CONFIG_game import *
from CONFIG_fonts import *
from CONFIG_texts import *
from GAME_functions import *

# IMPORTA AS BIBLIOTECAS UTILIZADAS
import pygame

pygame.init()

# ITENS :
# PLAY
# SAVE
# CRÉDITOS


class MainMenu:
    def __init__(self, screen_w, screen_h) -> None:

        self.screen_w = screen_w
        self.screen_h = screen_h
        
        self.bg_color = 'brown'
        self.fg_color = 'gray'
        self.width = 300
        self.height = 400

        self.index = 0
        self.itens = [
            load_current_texts()["menu iten 0"],
            f'< {load_current_save()} >',
            load_current_texts()["menu iten 2"],
            f'< {load_current_idiom()} >',
            load_current_texts()["menu iten 4"],
            load_current_texts()["menu iten 5"]
        ]
        self.itens_space = 38

        self.menu = convert_img('./resources/ilustrations/main_menu.png', 0, 1)
        self.menu_pos = (screen_w / 2 - self.menu.get_width() / 2, screen_h / 2 - self.menu.get_height() / 2)

        self.alert_box = None


    def next_index(self):
        if self.index + 1 < len(self.itens): self.index += 1

    def prev_index(self):
        if self.index - 1 >= 0: self.index -= 1


    def print_itens(self, screen):
        for index, iten in enumerate(self.itens):
            if self.index == index: txt = FONT_PS2P.render(iten, False, 'brown')
            else: txt = FONT_PS2P.render(iten, False, 'white')
            screen.blit(txt, (self.screen_w / 2 - txt.get_width() / 2, (self.screen_h - self.height) / 2 + self.itens_space * (index + 1) + index * txt.get_height()))

    def click(self):
        if self.alert_box != None:
            self.alert_box.click()
            self.alert_box = None
            return 'nothing'

        if self.index == 0: return 'play'
        if self.index == 1: return 'nothing'
        if self.index == 2:
            self.alert_box = AlertBox(self.screen_w, self.screen_h)
            return 'nothing'
        if self.index == 3: return 'nothing'
        if self.index == 4: return 'credits'
        if self.index == 5: return 'quit'

    def left_click(self):
        # CASO DA CAIXA DE MENSAGEM
        if self.alert_box != None:
            self.alert_box.change_yes_no()
            return False
        # CASO DE TROCAR SAVE
        if self.index == 1:
            save = load_current_save()
            if save == 'Save 2': update_current_save('Save 1')
            elif save == 'Save 3': update_current_save('Save 2')
            elif save == 'Save 4': update_current_save('Save 3')
        # CASO DE TROCAR IDIOMA
        elif self.index == 3:
            for i in range(len(LANGUAGES_NAMES)):
                if load_current_idiom() == LANGUAGES_NAMES[i]:
                    break
            update_current_idiom(LANGUAGES_NAMES[i - 1])

        self.itens = [
            load_current_texts()["menu iten 0"],
            f'< {load_current_save()} >',
            load_current_texts()["menu iten 2"],
            f'< {load_current_idiom()} >',
            load_current_texts()["menu iten 4"],
            load_current_texts()["menu iten 5"]
        ]

    def right_click(self):
        # CASO DA CAIXA DE MENSAGEM
        if self.alert_box != None: self.alert_box.change_yes_no()
        # CASO DE TROCAR SAVE
        if self.index == 1:
            save = load_current_save()
            if save == 'Save 1': update_current_save('Save 2')
            elif save == 'Save 2': update_current_save('Save 3')
            elif save == 'Save 3': update_current_save('Save 4')
        # CASO DE TROCAR IDIOMA
        elif self.index == 3:
            for i in range(len(LANGUAGES_NAMES)):
                if load_current_idiom() == LANGUAGES_NAMES[i]: break
            if i < len(LANGUAGES_NAMES) - 1: update_current_idiom(LANGUAGES_NAMES[i + 1])
            else: update_current_idiom(LANGUAGES_NAMES[0])

        self.itens = [
            load_current_texts()["menu iten 0"],
            f'< {load_current_save()} >',
            load_current_texts()["menu iten 2"],
            f'< {load_current_idiom()} >',
            load_current_texts()["menu iten 4"],
            load_current_texts()["menu iten 5"]
        ]


    def paint(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.menu, self.menu_pos)
        self.print_itens(screen)
        if self.alert_box != None: self.alert_box.paint(screen)

    def update(self, screen):
        self.paint(screen)


class AlertBox:
    def __init__(self, screen_w, screen_h) -> None:

        self.screen_w = screen_w
        self.screen_h = screen_h
        
        self.bg_color = 'brown'
        self.fg_color = 'gray'
        self.width = 600
        self.height = 200

        self.index = 1
        self.itens = [
            'Deseja resetar o save atual?',
            '< NO >'
        ]
        self.itens_space = 50

        self.box = convert_img('./resources/ilustrations/alert_box.png', 0, 1)
        self.box_pos = (screen_w / 2 - self.box.get_width() / 2, screen_h / 2 - self.box.get_height() / 2)

    def change_yes_no(self):
        if self.itens[1] == '< NO >': self.itens[1] = '< YES >'
        elif self.itens[1] == '< YES >': self.itens[1] = '< NO >'

    def click(self):
        if self.itens[1] == '< NO >': return False
        else:
            reset_stages(load_current_save())
            update_current_stage(load_current_save(), 0)
            return True


    def print_itens(self, screen):
        for index, iten in enumerate(self.itens):
            if self.index == index: txt = FONT_PS2P.render(iten, False, 'brown')
            else: txt = FONT_PS2P.render(iten, False, 'white')
            screen.blit(txt, (self.screen_w / 2 - txt.get_width() / 2, (self.screen_h - self.height) / 2 + self.itens_space * (index + 1) + index * txt.get_height()))

    def paint(self, screen):
        screen.fill(self.bg_color)
        screen.blit(self.box, self.box_pos)
        self.print_itens(screen)

    def update(self, screen):
        self.paint(screen)















