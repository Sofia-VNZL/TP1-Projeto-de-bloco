from listas import *
from datetime import datetime

'''
nessa página estão as funções que utilizei para montar outras. 
Foi pata evitar ter funções muito compridas tal e como aprendimos nas aulas de Pythom com LP.
'''



def gerar_id(tarefas):
    '''
    Função para gerar ID para novas tarefas.

    Recebe: o comprimento da lista de tarefas (uma lista com listas)

    retorna: um número que equivale ao comprimento da lista de tarefas + 1
    '''

    if not tarefas:
        return 1
    return max(tarefa[0] for tarefa in tarefas) + 1


def prioridade_tarefa():

    '''
    Função para facilitar a criação de tarefas, pergunta se uma tarefa é urgente o não.

    recebe: valor inteiro 1 ou 2.

    retorna: string com o valor "Urgente" ou "Não urgente" respetivamente
    '''

    while True:
        try:
            resposta = int(input("É [1] Urgente ou [2] Não urgente?: "))
            if resposta == 1:
                return "Urgente"
            elif resposta == 2:
                return "Não Urgente"
            else:
                print("A resposta precisa ser [1] ou [2]")
        except ValueError:
            print("Por favor, insira um número válido.")

def procurar_tarefa(tarefas, id):
    for tarefa in tarefas:
        if tarefa[0] == id:
            return tarefa
    return None

def achar_tarefa(tarefas):
    while True:
        try:
            id = int(input("ID:"))
            tarefa = procurar_tarefa(tarefas, id)
            if tarefa:
                return tarefa
            else:
                print("Tarefa não encontrada. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def obter_data_entrega():
    while True:
        data_input = input("Digite a data de entrega no formato dia-mes-ano (dd-mm-aaaa): ")
        try:
            data_formatada = datetime.strptime(data_input, "%d-%m-%Y")
            return data_formatada.strftime("%d-%m-%Y")
        except ValueError:
            print("Formato de data inválido. Por favor, use o formato dia-mes-ano (dd-mm-aaaa).")