lista_tarefas = []
tarefas_concluidas = []

def adicionar_tarefa():
    tarefa = input("O que você quer fazer?  ")
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas(lista):
    listagem = lista
    for indice, tarefa in enumerate(listagem, 1):
        print(f"{indice} - {tarefa}")

def concluir_tarefa():
    listar_tarefas(lista_tarefas)
    indice = int(input("Qual tarefa você quer concluir?  "))
    tarefa_concluida = lista_tarefas[indice - 1]
    tarefas_concluidas.append(tarefa_concluida)
    lista_tarefas.pop(indice -1)

def remover_tarefa():
    listar_tarefas(lista_tarefas)
    indice = int(input("Escolha qual tarefa quer excluir."))
    lista_tarefas.pop(indice - 1)

def menu():
    print("""
    [1] Adicionar tarefa
    [2] Listar tarefas
    [3] Concluir tarefa
    [4] Tarefas concluidas
    [5] Remover tarefa
    [6] Sair
    """)

    return input("Escolha uma opção: ")


while True:
    opcao = menu()
    if opcao == "1":
        print("\n========= NOVA TAREFA ========")
        adicionar_tarefa()
    elif opcao =="2":
        print("\n====== LISTA DE TAREFAS ======")
        listar_tarefas(lista_tarefas)
    elif opcao == "3":
        print("\n======= CONCLUIR TAREFA ======")
        concluir_tarefa()
    elif opcao == "4":
        print("\n===== TAREFAS CONCLUÍDAS =====")
        listar_tarefas(tarefas_concluidas)
    elif opcao == "5":
        print("\n======== EXCLUIR TAREFA ======")
        remover_tarefa()
    elif opcao == "6":
        break
    else:
        print("Opção inválida")
        menu

