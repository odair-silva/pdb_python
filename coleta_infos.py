#aqui serão apresentados o enredo, os personagens e o jogador irá inserir seu nome
import random

def coleta_infos():
    
    #pega os nomes dos NPCs do txt
    npcs = importa_NPCs()

    #cria atributos dos personagens
    vida, dano = att_NPCs(npcs)
    #cria o dicionario relacionando as infos dos NPCs e seus atributos
    dict_NPCs(npcs, vida, dano)

def importa_NPCs():
    arquivo = open("personagens.txt", "r")
    personagens = []

    for linha in arquivo:
        linha = linha.strip()
        personagens.append(linha)
    arquivo.close()

    return(personagens)

def att_NPCs(npcs):
    vida = []
    dano = []
    for att in npcs:
        att = random.randrange(80,101)
        vida.append(att)
        att = random.randrange(5,10)
        dano.append(att)

    return vida, dano

def dict_NPCs(npcs, vida, dano):
    personagens = []
    index = 0
    for personagem in npcs:
        personagem = {'Nome: ': npcs[index], 'Vida: ': vida[index], 'Dano: ':dano[index]}
        personagens.append(personagem)
        index += 1
    
    print(personagens[1])

if(__name__ == "__main__"):
    coleta_infos()