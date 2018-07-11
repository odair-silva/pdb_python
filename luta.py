import random
import fases

def lutar(jogador, personagens, inimigo, amigo):

    tela_infos(jogador, personagens)
    inimigo_vivo, amigo_vivo = ataques(jogador, personagens, inimigo, amigo)

    if(not inimigo_vivo):
        fases.game_over()
    elif(not amigo_vivo):
        fases.fase_final()




def tela_infos(jogador, personagens):
    print("Amigos: ")
    print("Nome: {}   {}". format(jogador['Nome'],personagens[1]['Nome']))
    print("Vida: {}   {}\n". format(jogador['Vida'],personagens[1]['Vida']))

    print("Inimigos: ")
    print("Nome: {}   {}". format(personagens[2]['Nome'],personagens[3]['Nome']))
    print("Vida: {}   {}\n". format(personagens[2]['Vida'],personagens[3]['Vida']))



def ataques(jogador, personagens, inimigo, amigo):
    
    amigo_vivo = True
    inimigo_vivo = True
    estado = 0

    while(amigo_vivo and inimigo_vivo):

        if(jogador['Vida'] <= 0 and personagens[1]['Vida'] <= 0):
            amigo_vivo = False
    
        if(personagens[2]['Vida'] <= 0 and personagens[3]['Vida'] <= 0):
            inimigo_vivo = False

        if(estado == 0):
            if(personagens[2]['Vida'] >= 0):
                personagens[2]['Vida'] = personagens[2]['Vida'] - round(jogador['Dano']*random.uniform(0, 1))
            if(personagens[3]['Vida'] >= 0):
                personagens[3]['Vida'] = personagens[3]['Vida'] - round(jogador['Dano']*random.uniform(0, 1))
        estado = 1

        if(estado == 1):
            if(personagens[2]['Vida'] >= 0):
                personagens[2]['Vida'] = personagens[2]['Vida'] - round(personagens[1]['Dano']*random.uniform(0, 1))
            if(personagens[3]['Vida'] >= 0):
                personagens[3]['Vida'] = personagens[3]['Vida'] - round(personagens[1]['Dano']*random.uniform(0, 1))
        estado = 2

        if(estado == 2):
            if(personagens[1]['Vida'] >= 0):
                personagens[1]['Vida'] = personagens[1]['Vida'] - round(personagens[2]['Dano']*random.uniform(0, 1))
            if(jogador['Vida'] >= 0):
                jogador['Vida'] = jogador['Vida'] - round(personagens[2]['Dano']*random.uniform(0, 1))
        estado = 3

        if(estado == 3):
            if(personagens[1]['Vida'] >= 0):
                personagens[1]['Vida'] = personagens[1]['Vida'] - round(personagens[3]['Dano']*random.uniform(0, 1))
            if(jogador['Vida'] >= 0):
                jogador['Vida'] = jogador['Vida'] - round(personagens[3]['Dano']*random.uniform(0, 1))
        estado = 0

        tela_infos(jogador, personagens)
    
    return amigo_vivo, inimigo_vivo
 


if(__name__ == "__main__"):
    lutar(jogador, personagens, inimigo, amigo)