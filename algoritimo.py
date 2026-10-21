import time

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Divide a lista ao meio

        if lista[meio] == alvo:
            return meio  # Achou! Retorna o índice
        elif lista[meio] < alvo:
            inicio = meio + 1  # Descarta a metade esquerda
        else:
            fim = meio - 1  # Descarta a metade direita

    return -1  # Não encontrou


# Teste
dados = [10, 20, 30, 40, 50, 60, 70]
print(busca_binaria(dados, 40))  # Saída: 3
