from re import I
import time

MENU_CAFE = {
    "Espresso": {"tipo": "Forte", "tempo_segundos": 5, "leva_leite": False},
    "Cappuccino": {"tipo": "Cremoso", "tempo_segundos": 10, "leva_leite": True},
    "Latte": {"tipo": "Suave", "tempo_segundos": 15, "leva_leite": True}
}

def menu_principal():
    while True:
        print("\n=== SEJA BEM VINDO ===")
        print("1 - menu café")
        print("0 - Sair")
        try:
            op = int(input("Escolha: "))
            match op:
                case 1:
                    cafe_menu()
                case 0:
                    print("Fechando o sistema. Até logo!")
                    return False
                case _:
                    print("❌ Opção inexistente. Tente novamente.")
        except ValueError:
            print("Insira apenas numeros inteiros")


def cafe_menu():

    # Transformamos as chaves em lista localmente (evita variáveis globais soltas)
    nomes_do_cafe = list(MENU_CAFE.keys())

    print("\n--- Cafés Disponíveis ---")

    for i, c in enumerate(nomes_do_cafe, start=1):
        detalhes = MENU_CAFE[c]
        print(f"{i} - {c} ({detalhes['tipo']}) | Pronto em: {detalhes['tempo_segundos']}s")
    print("0 -  Voltar para o Menu Principal")

    try:
        opcao = int(input("\nQual deseja ?"))
        if opcao == 0:
            print("Voltando")
            return

        # Validação do mundo real: impede que o usuário digite um número que não existe (ex: 5)
        if 1 <= opcao <= len(nomes_do_cafe):
            nome_escolhido = nomes_do_cafe[opcao - 1] # Traduz o número para o nome
            detalhes_escolhidos = MENU_CAFE[nome_escolhido] # Pega o dicionário interno
            preparar_cafe(nome_escolhido, detalhes_escolhidos)
        else:
             print("❌ Opção inválida! Escolha um número do menu.")
    except ValueError as error:
        print(f"Algo deu errodo error:{error}")
        print("Error: Insira apenas números inteiros")


def cronometro(func):
    def wrapper(tipo, tempo, *args, **kwargs):
        start =  time.time()
        func(tipo, tempo, *args, **kwargs)
        end = time.time()
        print(f"\n⏱️  [INFO] Demorou {end - start:.2f}s para o preparo finalizar.")
    return wrapper

@cronometro
def preparar_cafe(nome, detalhes):
    print(f"\n[Iniciando] Preparando seu {nome} ({detalhes['tipo']})...")
    print("-> Esquentando a água...")
    time.sleep(detalhes['tempo_segundos'] / 5) # Divisão apenas para o teste rodar mais rápido

    print("-> Moendo e extraindo o café na vasilha...")
    time.sleep(1)

    if detalhes["leva_leite"]:
        print("-> Vaporizando e adicionando o leite...")
        time.sleep(1)

    print("-> Finalizando detalhes...")
    time.sleep(1)
    print(f"☕ O seu {nome} está pronto! Aproveite.")
#def cha():
#def suco():

if __name__ == "__main__":
    menu_principal()
