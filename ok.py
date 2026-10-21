def teste(n):
    cont = 1
    for linha in range(cont, n+1):
        for coluna in range(linha):
            print(cont, end=" ")
            cont+=1
        print()


teste(4)

