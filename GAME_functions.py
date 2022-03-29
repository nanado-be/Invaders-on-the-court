# IMPORTA AS BIBLIOTECAS USADAS
from locale import strcoll
import pygame
pygame.init()
import json

# IMPORTA OUTROS ARQUIVOS
from CONFIG_texts import *

empty_stages = [
    ['BOM DIA, BASQUETE'       , 1, 0, '-', 0 ],
    ['ISSO É FALTA, PROFESSOR' , 0, 0, '-', 1 ],
    ['JOGO DURO'               , 0, 0, '-', 2 ],
    ['METENDO O PÉ'            , 0, 0, '-', 3 ],
    ['ENTRANDO PELO CANO'      , 0, 0, '-', 4 ],
    ['BASQUETE UNDERGROUND'    , 0, 0, '-', 5 ],
    ['SAI DA RETRANCA, MERMÃO' , 0, 0, '-', 6 ],
    ['SÓ DE TRÊS'              , 0, 0, '-', 7 ],
    ['BACK TO BACK'            , 0, 0, '-', 8 ],
    ['BASQUETE DE RUA'         , 0, 0, '-', 9 ],
    ['DE TABELA'               , 0, 0, '-', 10],
    ['MATA-MATA'               , 0, 0, '-', 11],
    ['MUITA FIRULA'            , 0, 0, '-', 12],
    ['TIRO LIVRE'              , 0, 0, '-', 13],
    ['MVP'                     , 0, 0, '-', 14],
    ['DEU RUIM'                , 0, 0, '-', 15],
    ['CLUTCH TIME'             , 0, 0, '-', 16]
] # [Nome, Disponível 0/1, Maior Pontuação (MOEDAS), Menor Tempo, Id]
		

# CONVERTE UMA LISTA DE STRINGS COM CAMINHOS DE IMAGENS PARA O FORMATO USADO NO PYGAME
# ROTACIONA E AMPLIA A IMAGEM CONFORME OS VALORES FORNECIDOS
def convert_animation_imgs(path_list, rotation, zoom):
    converted_list = []
    for img_path in path_list:
        aux = pygame.transform.rotozoom(pygame.image.load(img_path).convert_alpha(),rotation, zoom)
        converted_list.append(aux)

    return converted_list


# CONVERTE UMA STRING COM O CAMINHO DE UMA IMAGEM PARA O FORMATO USADO NO PYGAME
# ROTACIONA E AMPLIA A IMAGEM CONFORME OS VALORES FORNECIDOS    
def convert_img(img_path, rotation, zoom):
    return pygame.transform.rotozoom(pygame.image.load(img_path).convert_alpha(),rotation, zoom)


#  RESETA A LISTA DE ESTÁGIOS
def reset_stages(save):
    with open(f'./resources/saves/{save}/stages.txt', 'w') as file:
        json.dump(json.dumps(empty_stages), file)
    update_current_stage(save, 0)


#  ATUALIZA O LEVEL COM A PATUAÇÃO E O TEMPO SE FOREM MELHORES QUE OS ATUAIS E LIBERA O PRÓXIMO LEVEL
def update_save(save, stage_id, score, time):
    with open(f'./resources/saves/{save}/stages.txt') as file:
        stages = json.loads(json.load(file))

    # atualiza as informações do próprio estágio
    if score > stages[stage_id][2]: stages[stage_id][2] = score
    if '-' == stages[stage_id][3]: stages[stage_id][3] = time
    elif time < stages[stage_id][3]: stages[stage_id][3] = time

    with open(f'./resources/saves/{save}/stages.txt', 'w') as file:
        json.dump(json.dumps(stages), file)
        

    # libera o próximo estágio se existir
    try: stages[stage_id  + 1][1] = 1
    except: return False

    with open(f'./resources/saves/{save}/stages.txt', 'w') as file:
        json.dump(json.dumps(stages), file)

    # atualiza o level atual
    update_current_stage(save, stage_id + 1)


#  ATUALIZA O ESTÁGIO ATUAL COM UM ID DE ESTÁGIO FORNECIDO
def update_current_stage(save, stage_id):
    with open(f'./resources/saves/{save}/stages.txt') as file:
        stages = json.loads(json.load(file))
        
    current_stage = stages[stage_id]

    with open(f'./resources/saves/{save}/current_stage.txt', 'w') as file:
        json.dump(json.dumps(current_stage), file)


#  RETORNA UMA LISTA COM OS ESTÁGIOS DISPONÍVEIS PARA JOGAR
def load_available_stages(save):
    with open(f'./resources/saves/{save}/stages.txt') as file:
        stages = json.loads(json.load(file))

    available_stages = []
    for stage in stages:
        if stage[1]: available_stages.append(stage)

    return available_stages


# RETORNA O ESTÁGIO ATUAL ==> ['Nome', situação, score, time, id]
def load_current_stage(save):
    with open(f'./resources/saves/{save}/current_stage.txt') as file:
        current_stage = json.loads(json.load(file))
    
    return current_stage


#  ATUALIZA O SAVE ATUAL COM UM ID DE ESTÁGIO FORNECIDO
def update_current_save(save):
    with open(f'./resources/saves/current_save.txt', 'w') as file:
        json.dump(save, file)

# RETORNA O SAVE ATUAL ==> 'Nome']
def load_current_save():
    with open(f'./resources/saves/current_save.txt') as file:
        current_save = json.load(file)
    
    return current_save

#  ATUALIZA O IDIOMA ATUAL COM O NOME FORNECIDO
def update_current_idiom(idiom: str):
    with open(f'./resources/saves/current_idiom.txt', 'w') as file:
        json.dump(idiom, file)
    rewrite_stages_names()

# RETORNA O IDIOMA ATUAL ==> 'Nome']
def load_current_idiom() -> str:
    with open(f'./resources/saves/current_idiom.txt') as file:
        current_save = json.load(file)
    
    return current_save

# RETORNA O DICIONÁRIO COM OS TEXTOS ATUAIS
def load_current_texts() -> dict:
    return LANGUAGES[load_current_idiom()]


def rewrite_stages_names() -> None:
    for i in range(1, 5, 1):
        with open(f'./resources/saves/Save {i}/stages.txt') as file:
            stages = json.loads(json.load(file))
        for j in range(len(empty_stages)):
            stages[j][0] = load_current_texts()[f'lvl name {j}']
        with open(f'./resources/saves/Save {i}/stages.txt', 'w') as file:
            json.dump(json.dumps(stages), file)
        update_current_stage(f'Save {i}', load_current_stage(f'Save {i}')[4])


        



# update_current_idiom('EN-US')
# print(load_current_texts())


# for i in range(1, 5, 1):
#	update_current_save(f'Save {i}')
#	reset_stages(load_current_save())
#	update_current_stage(load_current_save(), 0)



















