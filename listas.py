import datetime 
#tempo como global nesse caso
hoje = datetime.date.today()


#comecemos com uma base que já tenha algumas tarefas por fazer:
tarefas = [[1, "limpar cozinha", "Realizar limpeza da cozinha com desinfectante", hoje, "urgente", f"Entrega: 13-11-2024", "Concluída"],
           [2, "Comprar leite", "Comprar leite no mercadinho perto de casa, integral!", hoje, "Não urgente", f"Entrega: 08-12-2024", "Pendente"],
           [3, "Fazer carinho no gato", "fazer carinho no gato por 30min se não fica carente", hoje, "Urgente", f"Entrega: {hoje}", "Pendente"]]


#Exibir

def exibir_tarefas(tarefas): 
    '''
    Função para exibir todas as tarefas.

    Recebe:
    tarefas: listas

    retorna: mensagem com as informações das tarefas
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

def gerar_id(tarefas):
    '''
    Função para gerar ID para novas tarefas.

    Recebe:
    tarefas: listas

    retorna: um número que equivale ao comprimento da lista de tarefas + 1
    '''

    if not tarefas:
        return 1
    return max(tarefa[0] for tarefa in tarefas) + 1

def criar_tarefa():
    '''
    Função para criar novas tarefas.

    Recebe:
    O input com os dados do usuário para a tarefa nova

    retorna: uma nova lista (tarefa) adicionada à lista de tarefas 
    '''

    print("Adicione nova tarefa: ")
    id_novo = gerar_id(tarefas)
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("É Urgente ou Não urgente?: ")
    prazo = input("Data de entrega: ")

    nova_tarefa = [id_novo, titulo, descricao, hoje, prioridade, f"Entrega: {prazo}", "Pendente"]
    tarefas.append(nova_tarefa)

    print("Tarefa criada com sucesso!")
    exibir_tarefas([nova_tarefa])
    
#Editar

    #marcar como concluída

def procurar_tarefa(tarefas, id):
    for tarefa in tarefas:
        if tarefa[0] == id:
            return tarefa
    return None

"""def achar_tarefa():
    id = int(input("Qual o ID da tarefa que deseja selecionar"))
    tarefa_achada = procurar_tarefa(tarefas, id)


    if tarefa_achada:
        return tarefa_achada
    else:
        print("Tarefa não encontrada.")"""
    
def mudar_status():
    id = int(input("Qual o ID da tarefa que deseja marcar como concluída? "))
    tarefa = procurar_tarefa(tarefas, id)

    if tarefa:
        tarefa[6] = "Concluída"  # Atualiza o status da tarefa para "Concluída"
        print(f"Tarefa {id} foi atualizada com sucesso para status 'Concluída'.")
    else:
        print("Tarefa não encontrada.")



#Excluir
 
def excluir_tarefa():
    id = int(input("Qual o ID da tarefa que deseja excluir? "))
    tarefa = procurar_tarefa(tarefas, id)

    if tarefa:
        tarefas.remove(tarefa) 
        print(f"Tarefa {id} foi excluída com sucesso.")
    else:
        print("Tarefa não encontrada.")

    
    
