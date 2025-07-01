# Tool: função que consulta a API do CNPJá com tratamento e logging
import requests
import time
from config import CNPJA_API_TOKEN, CNPJ_API_BASE, TIMEOUT

# Cache leve em memória para evitar chamadas duplicadas durante a sessão
cache_cnpjs = {}

def consultar_cnpj(cnpj: str) -> dict:
    """
    Consulta o CNPJ na API do cnpja.com usando o token fornecido.
    Aplica timeout e trata erros conforme especificações.
    """

    # Verifica cache antes de consultar
    if cnpj in cache_cnpjs:
        return cache_cnpjs[cnpj]

    url = f"{CNPJ_API_BASE}/{cnpj}?token={CNPJA_API_TOKEN}"
    inicio = time.time()

    try:
        response = requests.get(url, timeout=int(TIMEOUT))
        duracao = round(time.time() - inicio, 2)
        print(f"ℹ️  Status: {response.status_code} | Tempo: {duracao}s")

        if response.status_code == 200:
            dados = response.json()
            cache_cnpjs[cnpj] = dados  # Salva no cache
            return dados

        elif response.status_code == 400:
            return {"erro": "CNPJ inválido, revise e envie novamente."}
        elif response.status_code == 404:
            return {"erro": "Não localizamos esse CNPJ na base pública. Tente novamente."}
        elif response.status_code == 429:
            return {"erro": "Muitas solicitações de consulta de CNPJ estão acontecendo, tente novamente em alguns minutos."}
        elif response.status_code >= 500:
            return {"erro": "Serviço externo indisponível, tente mais tarde."}
        else:
            return {"erro": f"Erro inesperado: {response.status_code}"}

    except requests.RequestException as e:
        return {"erro": f"Erro ao consultar API: {e}"}

def buscar_dados_por_cnpj(cnpj: str) -> dict:
    """
    Função intermediária que chama a consulta e retorna o conteúdo se não houver erro.
    """
    dados = consultar_cnpj(cnpj)
    if "erro" in dados:
        print(f"❌ {dados['erro']}")
        return None
    return dados
