users = []

users_list = []


def menu():
    while True:
        print("Escolha")
        print("1 = Add users")
        print("2 - delete users")
        print("3 - consultar users")
        print("0 - sair")
        entrada = input("")
        match entrada:
            case "1":
                add_user(users)
            case "2":
                dell_user(users)
            case "3":
                consult_users(users)
            case "0":
                break
            case _:
                print("ENTRADA INVALIDA!")


def add_user(users_list):
    new_user = {}
    new_user["nome"] = input("Insira o nome do user:").lower()
    while True:
        try:
            new_user["idade"] = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")
    new_user["email"] = input("Digite o email: ").lower()
    new_user["ativo"] = False

    users_list.append(new_user)

    print("=" * 30)
    print("     PERFIL DO USUÁRIO     ")
    print("=" * 30)
    print(f"Nome:     {new_user['nome']}")
    print(f"Idade:    {new_user['idade']} anos")
    print(f"E-mail:   {new_user['email']}")
    print(f"Ativo:    {'Sim' if new_user['ativo'] else 'Não'}")


def dell_user(users_list):
    if not users_list:
        print("Não há usuários cadastrados.")
        return
    email_to_delete = input(
        "Digite o email do usuário que deseja deletar: "
    ).lower()
    user = achar_user_por_email(email_to_delete, users_list)

    if user:
        users_list.remove(user)
        print(f"Usuário com email {email_to_delete} foi deletado com sucesso.")
    else:
        print("E-mail de usuário inserido não existente.")


def consult_users(users_list):
    if not users_list:
        print("Não há usuários cadastrados.")
        return
    print("\nVoce deeseja:")
    print("1 - consultar todos os usuarios")
    print("2 - consultar usuario por email")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("=" * 30)
        print("        LISTA DE USUÁRIOS        ")
        print("=" * 30)
        for user_data in users_list:
            print(f"Nome:     {user_data.get('nome').title()}")
            print(f"Idade:    {user_data.get('idade')} anos")
            print(f"E-mail:   {user_data.get('email')}")
            print(f"Ativo:    {'Sim' if user_data.get('ativo') else 'Não'}")
            print("-" * 30)  # Separador para cada usuário
        if not users_list:
            print("Nenhum usuário cadastrado.")
    elif opcao == "2":
        email_to_consult = input(
            "Informe o email do usuário para consultar: "
        ).lower()
        user_data = achar_user_por_email(email_to_consult, users_list)

        if user_data:
            print("=" * 30)
            print("     PERFIL DO USUÁRIO CONSULTADO     ")
            print("=" * 30)
            print(f"Nome:     {user_data.get('nome').title()}")
            print(f"Idade:    {user_data.get('idade')} anos")
            print(f"E-mail:   {user_data.get('email')}")
            # Apresentação do booleano formatada de forma amigável e consistente
            print(f"Ativo:    {'Sim' if user_data.get('ativo') else 'Não'}")
            print("=" * 30)
        else:
            print("Usuário não encontrado com o e-mail fornecido.")
    else:
        print("Opção inválida para consulta.")

        # Apresentação do booleano formatada de forma amigável
        ativo = users_list.get("ativo")
        if ativo == True:
            print(f"Ativo {ativo}")
        else:
            print(f"Ativo: Não")

        print("=" * 30)


def gerir_status(users_list):
    while True:
        print("\nVoce deseja")
        print("1 - ativar")
        print("2 - desativar")
        print("0 - sair")

        entrada = input("")
        match entrada:
            case "1":
                dado_user = input(
                    "Informe o email do user desejado para ativação: "
                ).lower()
                user = achar_user_por_email(dado_user, users_list)
                user = achar_user_por_email(dado_user, users_list)

                if user is not None:
                    # Correção aqui: Comparar o valor booleano 'ativo' diretamente
                    if not user["ativo"]:
                        user["ativo"] = True
                        print(
                            f"Usuário '{user.get('nome').title()}' agora está ativado."
                        )
                    else:
                        print(
                            f"Usuário '{user.get('nome').title()}' já está ativado."
                        )
                else:
                    print("E-mail de usuário inserido não existente.")

            case "2":
                dado_user = input(
                    "Informe o email do user desejado para desativação: "
                ).lower()
                user = achar_user_por_email(dado_user, users_list)

                if user is not None:
                    if user["ativo"]:  # Verifica se está ativo para desativar
                        user["ativo"] = False
                        print(
                            f"Usuário '{user.get('nome').title()}' agora está desativado."
                        )
                    else:
                        print(
                            f"Usuário '{user.get('nome').title()}' já está desativado."
                        )
                else:
                    print("E-mail de usuário inserido não existente.")

            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Entrada incorreta. Por favor, escolha 1, 2 ou 0.")


def achar_user_por_email(email_to_find, users_list):
    for user_data in users_list:
        if user_data.get("email") == email_to_find:
            return user_data
    return None


menu()
