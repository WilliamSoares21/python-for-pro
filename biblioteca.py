import math
import random
import matplotlib.pyplot as plt 
import statistics
from tabulate import tabulate
from datetime import date


runs = {
    "2026-01-05": 4.0,
    "2026-01-08": 3.0,
    "2026-01-12": 5.0,
    "2026-01-15": 4.0,
    "2026-01-19": 6.0,
    "2026-01-22": 4.0,
    "2026-01-26": 6.5,
    "2026-01-29": 5.0,
    "2026-02-02": 7.0,
    "2026-02-05": 4.5,
    "2026-02-09": 7.5,
    "2026-02-12": 5.0,
    "2026-02-16": 8.0,
    "2026-02-19": 4.0,
    "2026-02-23": 3.0,
    "2026-02-28": 5.0,
}
def media():
    media = statistics.mean(runs.values())
    print(f"The average distance is: {media:.2f}")

def raiz(n):
    raiz = math.sqrt(n)
    print(raiz)

def aleatorio():
    print(random.randint(1, 100))

def grafico():
    meses = ['Jan', 'Fev', 'Mar', 'Abr']
    vendas = [10, 15, 7, 19]

    plt.plot(meses, vendas, marker='o', color='blue')

    plt.title("Vendas no Primeiro Quadrimestre")
    plt.xlabel('Meses')
    plt.ylabel('Quantidade de Vendas')
    plt.grid(True)

    # Exibindo o gráfico na tela
    plt.show()

def problema3():
    sorted_runs = sorted(runs.items(), key=lambda pair: (pair[1], pair[0]), reverse=True)
    ranked = [(rank, date, distance) for rank, (date, distance) in enumerate(sorted_runs, start=1)] 
    cabecalhos: list[str] = ["Ranked", "Date", "Distance"]
    print(tabulate(ranked, headers=cabecalhos, tablefmt="fancy_grid"))

def teoria4():
    runs_dates = []
    for run_dates_str in runs:
        runs_dates.append(date.fromisoformat(run_dates_str))
    runs_dates.sort()

    rest_days = []

    for i in range(1, len(runs_dates)):
        gap =(runs_dates[i] - runs_dates[i - 1]).days
        rest_days.append(gap)
    plt.hist(rest_days, bins=range(min(rest_days), max(rest_days) + 2), color="skyblue", edgecolor="black", align="left")
    plt.xticks(range(min(rest_days), max(rest_days) + 1))
    plt.title("Distribuição de Dias de Descanso")
    plt.xlabel("Dias de Descanso")
    plt.ylabel("Frequência")
    plt.show()


teoria4()
