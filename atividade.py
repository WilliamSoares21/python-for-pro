def centesimo():
    n = int(input("numero: "))

    for linha in range(1, n+1):
        espacos=" " * (n - linha)
        asteriscos = "*" * linha
        print(f"{espacos}{asteriscos}")
centesimo()
