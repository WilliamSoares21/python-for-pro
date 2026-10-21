import time
from rich.progress import Progress

import time
from tqdm import tqdm

def carregamento_semcor():
    print("Baixando pacotes do sistema...")

    # Apenas embrulhe o seu range com tqdm()
    for i in tqdm(range(100), desc="Progresso", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"):
        time.sleep(0.05)  # Simula uma tarefa

    print("✅ Concluído!")

def carregar_comcor():
    # Usando o gerenciador de contexto 'with' da biblioteca Rich
    with Progress() as progress:
        # Cria uma tarefa com um total de 100 passos
        tarefa = progress.add_task("[cyan]Processando café...", total=100)
        
        while not progress.finished:
            progress.update(tarefa, advance=1) # Avança 1% da barra
            time.sleep(0.05)

    print("[bold green]✅ Pronto![/bold green]")

carregamento_semcor()
carregar_comcor()
