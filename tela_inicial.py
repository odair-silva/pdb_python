import coleta_infos

def tela_inicial():

    print("*******************************")
    print("*************LOST**************")
    print("*******************************")

    print("\n(1)-Começar\n(2)-Sair\n")
    print("Dica: utilize os números indicados após 'Ação: ' para navegar pelo jogo.")
    escolha = int(input("Ação: "))
    print("================================================================================\n")

    

    if(escolha == 1):
        coleta_infos.coleta_infos()
    elif(escolha == 2):
        quit()

if(__name__ == "__main__"):
    tela_inicial()