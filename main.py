import requests
import teste

def main():
    print("Aqui é a main archive!")

    print("Welcome to this main archive")

    meu_nome = "Julian Casasblancas"

    name_upper = teste.upper_case_name(meu_nome)
    print(f"Nome maiusculo {name_upper}")

    print("dunder __name__ no main.py é: ", __name__)

if __name__ == '__main__':
    main()


