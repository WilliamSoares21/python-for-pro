def menu():
    try:
        n = int(input("n: "))
        validador(n)
        print(f"Deu certo, numero apresentado se encaixa nos padrões: {n}")
    except ValueError:  # Capture o ValueError especificamente
        print(
            "Algo deu errado, certifique-se de inserir um número inteiro positivo."
        )
    except Exception:  # Capture outras exceções inesperadas
        print("Ocorreu um erro inesperado, tente novamente.")


def validador(entrada):
    if entrada <= 0:
        raise ValueError(
            "Entrada menor ou igual a 0. Por favor, insira um número maior que 0."
        )


menu()
