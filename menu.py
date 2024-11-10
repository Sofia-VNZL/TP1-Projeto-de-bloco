from listas import *

def exibir_menu():
    print("**** Menu ****")
    print("[1] - Exibir tarefas")
    print("[2] - Alterar status da tarefa")
    print("[3] - Excluir")
    print("[4] - Adicionar tarefa")
    print("[0] - Sair")

def entrar_opcao():
    while (True):
        exibir_menu()
        opcao = int(input("Operação: "))
        if ((opcao < 0) or (opcao > 4)):
            print("Erro: opção inválida")
        else:
            break
    return opcao

def inicio():
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