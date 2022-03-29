# IMPORTA OUTROS ARQUIVOS
from GAME_main import *
from GAME_levels import level_list
from GAME_functions import *
from CONFIG_colors import *
from CONFIG_fonts import *

# IMPORTA AS BIBLIOTECAS USADAS
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox as msbx 
import pygame
pygame.init()
pygame.mixer.init()

# CLASSE DA INTERFACE INICIAL
class App(tk.Tk):
    # INICIA A CLASSE 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # CONFIGURAÇÕES DO SISTEMA
        self.lvls = level_list
        self.stage = tk.StringVar()
        self.available_stages = load_available_stages(load_current_save())


        # CONFIGURAÇÕES DA JANELA
        self.width = 475
        self.height = 475
        self.geometry(f'{self.width}x{self.height}')
        self.title('Invaders on the Court')
        self.resizable(0,0)


        # STYLES
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                                settings = {'TCombobox':
                                            {'configure':
                                            {'selectbackground': YELLOW,
                                            'selectforeground': BLUE,
                                            'fieldbackground': YELLOW,
                                            'background': ORANGE,
                                            'foreground': BLUE
                                            }}}
                                )
        combostyle.theme_use('combostyle')


        # MAIN FRAME
        self.main_frame = tk.Frame(self, bg = BLUE)
        self.main_frame.pack(expand = True, fill = 'both')

        # -- SPLASH ART
        # --- FRAME
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.pack(expand = True, fill = 'both')
        # --- IMAGE
        self.art_image = tk.PhotoImage(file = './resources/ilustrations/SPLASH.png')
        self.art_lbl = tk.Label(self.image_frame, image = self.art_image)
        self.art_lbl.pack()

        
        # -- STAGE SELECTION
        # --- FRAME
        self.stage_frame = tk.Frame(self.main_frame, bg = SALMON)
        self.stage_frame.pack(fill = 'x', anchor = 'n')
        # ---- LABEL
        self.stage_lbl = tk.Label(self.stage_frame, text = 'Sellect Stage', bg = ORANGE, fg = BLUE, font = HEAD_LBL)
        self.stage_lbl.pack(expand = True, fill = 'x', side = 'left')
        # ---- COMBOBOX
        self.stage_cbbx = ttk.Combobox(self.stage_frame, textvariable = self.stage, font = SELECTED, state = 'readonly', justify = 'center')
        self.update_stage_cbbx()
        self.stage_cbbx.option_add('*TCombobox*Listbox.Justify', 'center') 
        self.stage_cbbx.option_add('*TCombobox*Listbox.Background', YELLOW) 
        self.stage_cbbx.option_add('*TCombobox*Listbox.Foreground', BLUE) 
        self.stage_cbbx.pack(pady = 0, expand = True, fill = 'x', side = 'left')
        # ----- BINDING
        self.stage_cbbx.bind("<<ComboboxSelected>>", self.change_current_stage)
        # ---- SEPARATOR
        ttk.Separator(self.main_frame).pack(fill = 'x')


        # -- SAVE SELECTION
        # --- FRAME
        self.save_frame = tk.Frame(self.main_frame, bg = SALMON)
        self.save_frame.pack(fill = 'x', anchor = 'n')
        # ---- LABEL    
        self.save_lbl = tk.Label(self.save_frame, text = 'Sellect Save ', bg = ORANGE, fg = BLUE, font = HEAD_LBL)
        self.save_lbl.pack(expand = True, fill = 'x', side = 'left')
        # ---- COMBOBOX
        self.save = tk.StringVar()
        self.available_saves = ['Save 1', 'Save 2', 'Save 3', 'Save 4']
        self.save_cbbx = ttk.Combobox(self.save_frame, textvariable = self.save, font = SELECTED, state = 'readonly', justify = 'center')
        self.save_cbbx['values'] = self.available_saves
        self.save_cbbx.set(load_current_save())
        self.save_cbbx.pack(pady = 0, expand = True, fill = 'x', side = 'left')
        # ----- BINDING
        self.save_cbbx.bind("<<ComboboxSelected>>", self.update_current_save)
        # ---- SEPARATOR
        ttk.Separator(self.main_frame).pack(fill = 'x')

        # -- PLAY BUTTON
        # --- FRAME
        self.bttns_frame = tk.Frame(self.main_frame, bg = SALMON)
        self.bttns_frame.pack(fill = 'x', anchor = 'n')
        # ---- PLAY BUTTON
        self.play_button = tk.Button(self.bttns_frame, text = 'Play', pady = 0, padx = 150, bg = ORANGE, fg = BLUE , font = PLAY, command = lambda : self.play())
        self.play_button. pack(fill = 'x', pady = 0, side = 'left')
        # ---- RESET SAVE BUTTON
        self.reset_save_button = tk.Button(self.bttns_frame, text = 'Reset Save', pady = 0, padx = 10, bg = ORANGE, fg = BLUE , font = OPTIONS, command = lambda : self.reset_save())
        self.reset_save_button. pack(expand = True, fill = 'both', pady = 0)
        # ---- SEPARATOR
        ttk.Separator(self.main_frame).pack(fill = 'x')

        # ---- TOCA A MUSICA
        self.music = './resources/music/CHILL.mp3'
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def get_availabe_stages_names(self):
        self.stage_cbbx_values = [] 
        for stage in load_available_stages(load_current_save()):
            self.stage_cbbx_values.append(stage[0])


    def update_stage_cbbx(self):
        self.get_availabe_stages_names()
        self.stage_cbbx['values'] = self.stage_cbbx_values
        self.stage_cbbx.set(load_current_stage(load_current_save())[0])

    def change_current_stage(self, event):
        stage_name = event.widget.get()
        stage_id = 0
        for stage in load_available_stages(load_current_save()):
            if stage[0] == stage_name: stage_id = stage[4]
        update_current_stage(load_current_save(), stage_id)



    def update_current_save(self, event):
        update_current_save(event.widget.get())
        self.update_stage_cbbx()
        self.stage_cbbx.set(load_current_stage(load_current_save())[0])

    def reset_save(self):
        if not(msbx.askyesno(title='Warning', message= 'DO YOU WANT TO RESET THE CURRENT SAVE?')): return
        reset_stages(load_current_save())
        self.update_stage_cbbx()
        self.stage_cbbx.set(load_current_stage(load_current_save())[0])
        msbx.showinfo(title='Information', message= 'Save Reseted!')
        
    def select_lvl(self):
        for lvl in self.lvls:
            if lvl['name'] == self.stage_cbbx.get():
                return lvl
        return 0

    def play(self):
        init_game()
        self.update_stage_cbbx()
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        




if __name__ == '__main__':
    app = App()
    app.mainloop()