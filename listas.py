amigos = ["Julian", "Farah", "Alex", "Charlie", "Dana", "Brooke", "Eli"]

def pegar_meio(sua_lista):
    tamanho = len(sua_lista)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        return sua_lista[meio - 1 : meio + 1]
    else:
        return sua_lista[meio]

def adicionar_amigo():
    print("\n--- Adicionar Amigos ---")
    print("Para voltar ao menu principal, digite 0")
    while True:
        nome = input("Insira o nome do convidado: ")
        if nome == "0":
            break
        else:
            amigos.append(nome)
            print(f"'{nome}' foi adicionado!")

def remover():
    print("Para sair digite 0")
    while True:
        nome = input("Insira o nome que deseja remover: ")
        if nome == "0":
            break
        else:
            if nome in amigos:
                amigos.remove(nome)
                print(f"{nome} excluido com sucesso")
            else:
                print(f"{nome} não existe dentro da lista, ou já foi apagado.")

def ordenar():
    print("Lista antes da Ordenação")
    for nome in amigos:
        print(f" - {nome}")

    print("Depois da ordenação")
    ordenado = sorted(amigos)
    for amg in ordenado:
        print(f"- {amg}")



def exibir_menu():
    while True:
        print("\n======= MENU PRINCIPAL =======")
        print("1. Ver lista de amigos")
        print("2. Adicionar novo amigo")
        print("3. Ver amigo(s) do meio da lista")
        print("4. Remover convidado")
        print("4. Ver lista Ordenada")
        print("0. Sair")
        print("==============================")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            print("\nLista atual de amigos:")
            for nome in amigos:
                print(f"- {nome}")
        elif opcao == "2":
            adicionar_amigo()
        elif opcao == "3":
            resultado = pegar_meio(amigos)
            print(f"\nQuem está no meio da lista: {resultado}")
        elif opcao == "4":
            remover()
        elif opcao == "5":
            ordenar()
        elif opcao == "0":
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")

# Inicia o menu interativo
exibir_menu()
