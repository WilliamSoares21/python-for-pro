def converter(hr):
    periodo = 'P' if hr >= 12 else 'A'

    novo_horario = 12 if hr in (0, 12) else (hr - 12 if hr > 12 else hr)
    return novo_horario, periodo

def gerar_saida():
    while True:
        try:
            print("Para sair digite -1")
            hr = input("Insira o horario no formato de 24 horas: ")
            if hr == "-1":
                print("saindo ...")
                break
            if ":" not in hr or len(hr.split(":")) != 2:
                print("Error: Use o formato HH:MM (ex: 14:25).\n")
                continue

            periodo = ''
            partes = hr.split(":")
            horas = int(partes[0])
            minutos = int(partes[1])
            novo_horario, periodo = converter(horas)

            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                print("A hora inserido não segue o formato requerido...")
                continue
            
            sufixo = "am" if periodo == 'A' else 'pm'
            print(f"{hr} convertida fica {novo_horario}:{minutos:02d} {sufixo}")
        except ValueError:
            print("Tem que ser float e não string, burro")
gerar_saida()
