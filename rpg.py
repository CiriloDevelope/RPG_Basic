from random import randint

lista_npcs = []

#Criação de Player/Monstro

player = {
    'nome': 'Cirilo',
    'level': 1,
    'exp': 0,
    'exp_max': 30,
    'hp': 100,
    'hp_max': 100,
    'dano': 25
}

def criar_monstro(level):


    criar_monstro = {
        "nome": f'Monstro #{level}',
        'level' : level,
        'dano': 5 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'exp': 7 * level,
    }
    
    return criar_monstro

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        novo_monstros = criar_monstro(x + 1)
        lista_npcs.append(novo_monstros)
       

def exibir_monstro():
    for monstro in lista_npcs:
            exibir_monstro(monstro)

def exibir_player():
    print(f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}")

def reset_player():
    player['hp'] = player['hp_max']

def reset_monstro(monstro):
    monstro['hp'] = monstro['hp_max']

def level_up():
    if player ['exp'] >= player ['exp_max']:
        player ['level']+=1 
        player ['exp'] = 0
        player ['exp_max'] = player['exp_max'] * 2
        print('______________VOCE SUBIU DE NIVEL!!!______________\n')
        atributos = int(input('____ESCOLHA OS ATRIBUTOS____\n [ 1 ] +1 de Dano \n [ 2 ] +1 de HP\n Resposta:'))
        if atributos == 1:
            player['dano']+=1
        
        elif atributos == 2:
            player['hp_max']+=1



   
        
# Chamando as funções criadas

def iniciar_batalha(monstro):
    while player ['hp'] > 0 and monstro['hp'] > 0:
        atacar_player(monstro)
        atacar_monstro(monstro)
        exibir_dano(monstro)
    
    if player ['hp'] > 0:
        print(f'O {player["nome"]} VENCEU a batalha!! e GANHOU {monstro['exp']} de EXP\n')
        player ['exp'] += monstro['exp']
        print('=-'*20)
        exibir_player()
        print('=-'*20)
        
    
    else:
        print('_______VOCE MORREU!!!_______')
        exibir_monstro(monstro)

    level_up()
    reset_player()
    reset_monstro

 # Dano do player - HP do Monstro/ Exibiçao de Dano

def atacar_monstro(monstro):
     monstro['hp'] -= player['dano']
   

def atacar_player(monstro):
    player['hp'] -=  monstro['dano']
    


def exibir_dano(monstro):
    print (f'Player: {player["nome"]} {player["hp"]} // {player["hp_max"]}')
    print (f'Monstro: {monstro["nome"]} {monstro["hp"]} // {monstro["hp_max"]}')
    print ('=-'*20)

gerar_npcs(5)

monstro_selecionado = lista_npcs[0]
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)
iniciar_batalha(monstro_selecionado)

exibir_player()












