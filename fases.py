import random
import coleta_infos
import luta

def fase1(jogador, personagens):

    print("     -{}!? Okay. Eu sou {} da terra de lá e não tenho tempo para te explicar o que está acontecendo, mas eu preciso que você venha comigo pois toda mão que pode carregar uma espada é necessária!". format(jogador['Nome'], personagens[1]['Nome']))
    print("(1) - Você não sabe o que está acontecendo mas confia que {} irá te ajudar.". format(personagens[1]['Nome']))
    print("(2) - Você está em choque e demora a responder.")
    escolha = int(input("Ação: "))

    if(escolha == 1):
        i = fase2_1(jogador, personagens)
    elif (escolha == 2):
        i = fase2_2(jogador, personagens)

def fase2_1(jogador, personagens):
    print("     -Então vamos!!! Toma, você VAI precisar disso.")
    print("     **Você recebe uma espada velha e enferrujada**")
    print("     -A cidade está sendo atacada pela nação vizinha, sempre nos odiamos e você aparentemente não é um deles. Nossa cidade está sendo saqueada e queimada por esses crápulas! Vamos rápido.")
    print("     Você então pensa consigo mesmo: 'gente...' e vai.")
    print("========================================================================\n")
    print("     Parem! Vocês não darão mais nenhum passo!")
    print("     Você olha em volta e vê duas pessoas armadas e em posição de luta preparadas para te atacar, devem ser os 'crápulas'. Mas é então que você enfrenta uma decisão:")
    print("(1) - Correr, não sei lutar e dane-se {}, não o conheço e nem a sua causa.". format(personagens[1]['Nome']))
    print("(2) - Eu vou lutar! O que é um p*ido pra quem já está c*g*d*?")

    escolha = int(input("Ação: "))
    if(escolha == 1):
        i = fase3_1(jogador, personagens)
    elif (escolha == 2):
        i = fase3_2(jogador, personagens)

def fase2_2(jogador, personagens):
    print("     -Então fica aí!")
    print("     **{} continua na sua corrida em direção a cidade**". format(personagens[1]['Nome']))
    print("     -Você começa a andar desnorteado e é surpreendido por 2 pessoas que gritam: Somos {} e {} da nação vizinha e é hoje que você morre!".format(personagens[3]['Nome'], personagens[2]['Nome']))
    print("     Você então pensa consigo mesmo: 'gente...'")
    print("     Mas quando eles se aproximam, dos arbustos aparece {} e diz: 'Viu só! Agora me ajuda!'")
    print("     *Então ele joga uma espada velha em sua direção e vocês estão em formação costas-costas.*")
    print("(1) - Correr, não sei lutar e dane-se {}, voltou porque quis.". format(personagens[1]['Nome']))
    print("(2) - Eu vou lutar! O que é um p*ido pra quem já está c*g*d*?")

    escolha = int(input("Ação: "))
    if(escolha == 1):
        i = fase3_1(jogador, personagens)
    elif (escolha == 2):
        i = fase3_2(jogador, personagens)

def fase3_1(jogador, personagens):
    print("     Covarde! Não vê que não tem para onde correr?! Diz {}. Entendo que tudo isso seja muito Cloverfield pra entender mas agora eu preciso da sua ajuda!". format(personagens[1]['Nome']))
    print("     Nesse momento {} e {} riem da sua covardia e isso te afeta.". format(personagens[2]['Nome'], personagens[3]['Nome']))
    print("     Você então percebe que não tem o que fazer e começa a luta.")

    luta.lutar(jogador, personagens)

def fase3_2(jogador, personagens):
    print("     AAAAAAAAAAAAAAAAAH! *você corre em direção ao inimigo para a surpresa de {}*". format(personagens[1]['Nome']))

    luta.lutar(jogador, personagens)

if(__name__ == "__main__"):
    fase1(jogador, personagens)