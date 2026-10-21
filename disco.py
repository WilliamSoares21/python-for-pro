contatos = {
    "alexandre": 456123789,
    "anderson": 1245698456,
    "antonio": 123456456,
    "carlos": 91257581,
    "cesar": 987458,
    "rosemary": 789456125,
}


def converter(numero):
    numero = numero / (1024 * 1024)
    return numero


def analisa_porcentagem(user_bytes, total_bytes):
    porcetagem = (user_bytes / total_bytes) * 100
    return porcetagem


total_bytes = sum(contatos.values())

media = total_bytes / len(contatos)
print("ACME Inc.        Uso do espaço em disco pelos usuários")
print("-" * 70)
print(f"{'Nr.':<4} {'Usuário':<15} {'Espaço utilizado':<16}   {'% do uso':>12}")
print("-" * 70)
for i, (nome, numero) in enumerate(
    sorted(contatos.items(), key=lambda item: item[1], reverse=True), start=1
):
    porcentagem = analisa_porcentagem(numero, total_bytes)

    espaco_mb = f"{converter(numero):.2f} MB"
    porcentagem_str = f"{porcentagem:.2f}%"

    # :<4 (ocupa 4 espaços alinhado à esquerda), :<15 (15 espaços à esquerda), :>8.2f (8 espaços à direita)
    print(f"{i:<4} {nome:<15} {espaco_mb:<16}   {porcentagem_str:>12}")

print("\n")


def verifica_espaco_total(contatos):
    total = sum(contatos.values())
    total = converter(total)
    return total


print(f"Espaço total ocupado : {verifica_espaco_total(contatos):.2f} MB")
print(f"Espaço medio ocupado : {converter(media):.2f} MB")
