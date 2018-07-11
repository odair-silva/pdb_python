

def tela_inicial():


    
    print("*******************************")
    print("*********NOME DO JOGO**********")
    print("*******************************")

    print("\n(1)-Começar\n(2)-Sair\n")
    print("Dica: utilize os números indicados após 'Ação: ' para navegar pelo jogo.")
    escolha = int(input("Ação: "))

    linha_separacao()

    

    if(escolha == 1):
        print("Jogando forca!")
        forca.jogar()
    elif(escolha == 2):
        quit()

def linha_separacao():
    print("======================================================\n")

if(__name__ == "__main__"):
    tela_inicial()