def teste():
    while True:
        print("O que deseja fazer ?")
        print("1 - inserir n")
        print("0 - sair")
        try:
            opcao = int(input())
        except ValueError:
            print("Por favor, digite um número válido.\n")
            continue

        match opcao:
            case 1:
                try:
                    n = int(input("Insira u numero entre 0 a 9: "))
                    if 0 <= n <= 9:
                        print(f"{n} é um input válido")
                    else:
                        print(f"{n} não é válido!")
                except ValueError:
                    print("Entrada inválida! Você deve digitar um número inteiro.\n")
            case 0:
                print("Saindo...")
                return False
            case _:
                print("Entrada inválida")
teste()

