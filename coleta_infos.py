#aqui serão apresentados o enredo, os personagens e o jogador irá inserir seu nome
import random
import fases

def coleta_infos():
    
    #pega os nomes dos NPCs do txt
    npcs = importa_NPCs()
    #cria atributos dos personagens
    vida, dano = att_NPCs(npcs)
    #cria o dicionario relacionando as infos dos NPCs e seus atributos
    personagens_definidos = dict_NPCs(npcs, vida, dano)
    

    print("         Você acorda com uma gota de orvalho escorrendo pelo seu rosto. Você está em uma clareira e não sabe porque raios foi parar ali. Ao menos você está vestido...")
    print("         Ao se levantar e olha em volta, você percebe que nem tudo está em paz como imaginava e então você vê alguém correndo em sua direção: ")
    print("         'O que você está fazendo aqui no meio do nada?! Bateu a cabeça? Qual seu nome?'\n")
    print("'Qual meu nome?'")
    print("(1) - Não sei, não me lembro...")
    print("(2) - Meu nome é ")

    #usuario insere seu nome
    escolha = int(input("Ação: "))

    if(escolha == 1):
        jogador = nao_sei_nome()
    elif(escolha == 2):
        jogador = digite_nome()

    #muda de fase
    fases.fase1(jogador, personagens_definidos)
    

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
        att = random.randrange(5,11)
        dano.append(att)

    return vida, dano

def dict_NPCs(npcs, vida, dano):
    personagens = []
    index = 0
    for personagem in npcs:
        personagem = {'Nome': npcs[index], 'Vida': vida[index], 'Dano':dano[index]}
        personagens.append(personagem)
        index += 1
    
    return personagens

def nao_sei_nome():
    jogador = {'Nome': 'Zé', 'Vida': int(random.randrange(90,121)), 'Dano': int(random.randrange(8,11))}
    print("================================================================================\n")
    return jogador

def digite_nome():
    nome_jogador = input("Ação: Digite seu nome: ")
    jogador = {'Nome': nome_jogador, 'Vida': int(random.randrange(90,121)), 'Dano': int(random.randrange(8,11))}
    print("================================================================================\n")
    return jogador

if(__name__ == "__main__"):
    coleta_infos()