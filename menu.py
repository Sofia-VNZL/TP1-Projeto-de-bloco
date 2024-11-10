from listas import *
from outras import *


def exibir_menu():
    '''
    Função para mostrars as opções para navegar pelo programa

    recebe: 

    retorna:
    vários prints com as opções
    
    '''
    print("**** Menu ****")
    print("[1] - Exibir tarefas")
    print("[2] - Alterar status da tarefa")
    print("[3] - Excluir")
    print("[4] - Adicionar tarefa")
    print("[0] - Sair")

def entrar_opcao():
    '''
    Função para entrar a opção para navegar pelo programa

    recebe:
    número inteiro que corresponde a alguma das opções de operação

    retorna:
    o valor do numero que irá ser executada na função que chame ela. caso nçao seja digitado um valor válido aparecerá a mensagem de "opção inválida"
    
    '''
    while (True):
        exibir_menu()
        opcao = int(input("Operação: "))
        if ((opcao < 0) or (opcao > 4)):
            print("Erro: opção inválida")
        else:
            break
    return opcao

def inicio():
    '''
    Função que navega pelo programa ao chamar as outras funções

    recebe: o valor inteiro da função entrar_opção()

    retorna: a função que tenha sido chamada a menos que seja uma opção inválida
    '''
    opcao = entrar_opcao()
    while (opcao != 0):
        match (opcao):
            case 1: exibir_tarefas(tarefas)
            case 2: mudar_status()
            case 3: excluir_tarefa()
            case 4: criar_tarefa()
            case _: print("Erro: opção inválida")
        opcao = entrar_opcao()

inicio()