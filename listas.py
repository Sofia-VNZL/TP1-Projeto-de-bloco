from datetime import date
from outras import *

#tempo como global nesse caso
hoje = date.today()


#Base com algumas tarefas criadas hoje
tarefas = [[1, "limpar cozinha", "Realizar limpeza da cozinha com desinfectante", hoje, "urgente", f"Entrega: 13-11-2024", "Concluída"],
           [2, "Comprar leite", "Comprar leite no mercadinho perto de casa, integral!", hoje, "Não urgente", f"Entrega: 08-12-2024", "Pendente"],
           [3, "Fazer carinho no gato", "fazer carinho no gato por 30min se não fica carente", hoje, "Urgente", f"Entrega: {hoje}", "Pendente"]]


#Exibir

def exibir_tarefas(tarefas): 
    '''
    Função para exibir todas as tarefas.

    Recebe:
    tarefas: listas

    retorna: 
    mensagem com as informações das tarefas formatadas
    '''

    for tarefa in tarefas:
        print(f"""ID: {tarefa[0]}. {tarefa[1]}
        Descrição: {tarefa[2]}
        Data de Criação: {tarefa[3]}
        Prioridade: {tarefa[4]}
        Prazo: {tarefa[5]}
        Status: {tarefa[6]}
        *-*-*-*-*-*-*-*-*-*-*-*
        """)



#criação de tarefas

def criar_tarefa():
    '''
    Função para criar novas tarefas.

    Recebe:
    O input com os dados do usuário para a tarefa nova

    retorna: 
    uma nova lista (tarefa) adicionada à lista de tarefas, caso alguma das condições não seja válida, o programa vai perguntar de novo. 
    '''

    print("Adicione nova tarefa: ")
    id_novo = gerar_id(tarefas)
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = prioridade_tarefa()
    prazo = obter_data_entrega()

    nova_tarefa = [id_novo, titulo, descricao, hoje, prioridade, f"{prazo}", "Pendente"]
    tarefas.append(nova_tarefa)

    print("Tarefa criada com sucesso!")
    exibir_tarefas([nova_tarefa])
    


#Mudar status
    
def mudar_status():
    '''
    Função para criar novas tarefas.

    Recebe:
    O input com ID da tarefa que deseja mudar para concluída

    retorna: 
    uma nova lista (tarefa) adicionada à lista de tarefas 
    '''
    print("Qual o ID da tarefa que deseja marcar como concluída?")
    tarefa = achar_tarefa(tarefas)

    if tarefa:
        tarefa[6] = "Concluída"  
        print(f"Tarefa {tarefa[0]} foi atualizada com sucesso para status 'Concluída'.")
    else:
        print("Tarefa não encontrada.")



#Excluir
 
def excluir_tarefa():
    '''
    Função para excluir tarefas.

    Recebe:
    O input com ID da tarefa que deseja apagar

    retorna: 
    apaga a tarefa que tenha esse ID, caso não ache o ID, ele volta ao menu inicial
    '''
    id = int(input("Qual o ID da tarefa que deseja excluir? "))
    tarefa = procurar_tarefa(tarefas, id)

    if tarefa:
        tarefas.remove(tarefa) 
        print(f"Tarefa {id} foi excluída com sucesso.")
    else:
        print("Tarefa não encontrada.")

    
    
