from listas import *
from datetime import datetime

'''
nessa página estão as funções que utilizei para montar outras. 
Foi pata evitar ter funções muito compridas tal e como aprendimos nas aulas de Pythom com LP.
'''



def gerar_id(tarefas):
    '''
    Função para gerar ID para novas tarefas.

    Parâmetros:
    tarefas (list): Uma lista de tarefas, onde cada tarefa é representada por uma lista

    Recebe: o comprimento da lista de tarefas (uma lista com listas)

    retorna: um número que equivale ao comprimento da lista de tarefas + 1
    '''

    if not tarefas:
        return 1
    return max(tarefa[0] for tarefa in tarefas) + 1


def prioridade_tarefa():

    '''
    Função para facilitar a criação de tarefas, pergunta se uma tarefa é urgente o não.

    recebe: valor inteiro 1 ou 2. (int)

    retorna: string com o valor "Urgente" ou "Não urgente" respectivamente.
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

    ''' 
    Função ara procurar uma tarefa em uma lista de tarefas pelo ID

    retorna:
    list ou None: A tarefa correspondente ao ID, caso achada
    
    Parâmetros:
    - tarefas: Lista de tarefas, onde cada tarefa é representada por uma lista ou dicionário,
    com o ID como o primeiro elemento.
    - id: O número inteiro que representa o ID da tarefa a ser procurada.'''

    for tarefa in tarefas:
        if tarefa[0] == id:
            return tarefa
    return None


def achar_tarefa(tarefas):

    '''
    Função para achar tarefa, ela se repete até ter um valor válido

    Parâmetros:
    tarefas (list): Uma lista de tarefas, onde cada tarefa é representada por uma lista.

    recebe: A tarefa correspondente ao ID fornecido.

    retorna: 
    list. A tarefa correspondente ao ID fornecido, caso encontrada.
    '''

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

    '''
    Função para obter uma data de entrega no formato "dd-mm-aaaa" do usuário.

    Recebe:
    Nenhum parâmetro de entrada.

    Retorna:
    string: A data de entrega formatada no formato "dd-mm-aaaa".

    '''

    while True:
        data_input = input("Digite a data de entrega no formato dia-mes-ano (dd-mm-aaaa): ")
        try:
            data_formatada = datetime.strptime(data_input, "%d-%m-%Y")
            return data_formatada.strftime("%d-%m-%Y")
        except ValueError:
            print("Formato de data inválido. Por favor, use o formato dia-mes-ano (dd-mm-aaaa).")