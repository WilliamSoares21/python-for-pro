import requests
import json

from requests.models import Response

def repos_mais_estrelados():
    gh_api_repo_search_url = "https://api.github.com/search/repositories?q=Q"

    parametros = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=parametros)
    dados = response.json()
    json_formatado = json.dumps(dados, indent=4, ensure_ascii=False)
    print(json_formatado)

if __name__ == "__main__":

    repos_mais_estrelados()
