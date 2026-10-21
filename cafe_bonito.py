import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Inicializa o console da biblioteca Rich para estilização
console = Console()

# 1. Dados centralizados e estruturados
MENU_CAFE = {
    "Espresso": {"tipo": "Forte", "tempo_segundos": 5, "leva_leite": False},
    "Cappuccino": {"tipo": "Cremoso", "tempo_segundos": 10, "leva_leite": True},
    "Latte": {"tipo": "Suave", "tempo_segundos": 15, "leva_leite": True}
}

# 2. Decorador de Cronômetro
def cronometro(func):
    def wrapper(tipo, detalhes):
        start = time.time()
        func(tipo, detalhes)
        end = time.time()
        console.print(f"[bold cyan]⏱️  O processo completo levou {end - start:.2f} segundos.[/bold cyan]\n")
    return wrapper

# 3. Função de Preparo Otimizada (Sem repetição de código)
@cronometro
def cafe(tipo, detalhes):
    console.print(f"\n[bold yellow]☕ Iniciando o preparo do seu {tipo}...[/bold yellow]")
    
    # Configura uma barra de progresso visual moderna no terminal
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=30, complete_style="green", finished_style="bold green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        tempo_total = detalhes["tempo_segundos"]
        
        # Etapa 1: Esquentar a água (Metade do tempo total do café)
        tarefa_agua = progress.add_task("[cyan]Esquentando a água...", total=tempo_total // 2)
        while not progress.finished:
            progress.update(tarefa_agua, advance=1)
            time.sleep(1)
            
        # Etapa opcional baseada no dicionário (Evita ifs duplicados para cada tipo de café)
        if detalhes["leva_leite"]:
            console.print("[blue]🥛 Adicionando e vaporizando o leite...[/blue]")
            time.sleep(2)
            
        # Etapa 2: Finalização (Metade restante do tempo)
        tarefa_Preparo = progress.add_task("[magenta]Extraindo o café e finalizando...", total=tempo_total // 2)
        while not progress.finished:
            progress.update(tarefa_Preparo, advance=1)
            time.sleep(1)
            
    console.print(f"[bold green]✨ Perfeito! Seu {tipo} está pronto para consumo. Aproveite![/bold green]")

# 4. Menu do Café com Tabela Colorida
def cafe_menu():
    nomes_do_cafe = list(MENU_CAFE.keys())
    
    # Cria a tabela estilizada
    tabela = Table(title="\n☕ CARDÁPIO DIGITAL ☕", title_style="bold magenta", show_lines=True)
    tabela.add_column("Nº", style="cyan", justify="center")
    tabela.add_column("Bebida", style="bold yellow")
    tabela.add_column("Intensidade", style="green")
    tabela.add_column("Preparo", style="magenta", justify="right")
    
    for indice, c in enumerate(nomes_do_cafe, start=1):
        detalhes = MENU_CAFE[c]
        tabela.add_row(str(indice), c, detalhes['tipo'], f"{detalhes['tempo_segundos']}s")
        
    console.print(tabela)
    console.print("[bold red]0[/bold red] - Voltar ao menu principal")
    
    try:
        opcao = int(input("\nQual deseja? "))
        
        if opcao == 0:
            console.print("[yellow]Voltando...[/yellow]")
            return
            
        # Validação do intervalo numérico para evitar estouro de índice (IndexError)
        if 1 <= opcao <= len(nomes_do_cafe):
            nome_escolhido = nomes_do_cafe[opcao - 1]
            detalhes_escolhidos = MENU_CAFE[nome_escolhido]
            
            # Executa a função decorada de preparo
            cafe(nome_escolhido, detalhes_escolhidos)
        else:
            console.print("[bold red]❌ Opção inválida! Escolha um número do cardápio.[/bold red]")
            
    except ValueError:
        console.print("[bold red]❌ Erro: Insira apenas números inteiros.[/bold red]")

# 5. Loop Principal do Sistema
def menu():
    while True:
        console.print("\n[bold border]=== SEJA BEM VINDO ===[/bold border]")
        console.print("1 - Menu Café")
        console.print("0 - Sair")
        try:
            op = int(input("Escolha uma opção: "))
            match op:
                case 1:
                    cafe_menu()
                case 0:
                    console.print("[bold red]Fechando o sistema. Até logo![/bold red]")
                    break
                case _:
                    console.print("[bold red]❌ Opção inválida. Tente novamente.[/bold red]")
        except ValueError:
            console.print("[bold red]❌ Insira apenas números inteiros.[/bold red]")

# Ponto de entrada oficial do script Python
if __name__ == "__main__":
    menu()

