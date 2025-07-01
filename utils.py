# Funções auxiliares: validação de CNPJ, tratamento de erros

import re

def extrair_cnpj(texto: str) -> str | None:
    """
    Extrai um CNPJ válido (14 dígitos) de um texto, mesmo que esteja com pontos, barra ou traço.
    """
    apenas_numeros = re.sub(r'\D', '', texto)
    if len(apenas_numeros) == 14:
        return apenas_numeros
    return None


# Formatação da resposta: prepara os dados principais da empresa para o prompt do agente
def formatar_resposta(dados: dict) -> str:
    """
    Formata os dados principais da empresa para uso no prompt do agente.
    """
    razao = dados.get("razao_social", "Não disponível")
    fantasia = dados.get("nome_fantasia", "Não disponível")
    cnpj = dados.get("cnpj", "Não disponível")
    telefone = dados.get("telefone", "Não disponível")
    email = dados.get("email", "Não disponível")
    endereco = dados.get("logradouro", "") + ", " + dados.get("numero", "") + " - " + dados.get("municipio", "") + "/" + dados.get("uf", "")
    atividade_principal = dados.get("atividade_principal", {}).get("descricao", "Não disponível")
    natureza = dados.get("natureza_juridica", "Não disponível")
    situacao = dados.get("situacao_cadastral", "Não disponível")

    return f"""
Razão Social: {razao}
Nome Fantasia: {fantasia}
CNPJ: {cnpj}
Telefone: {telefone}
Email: {email}
Endereço: {endereco}
Atividade Principal: {atividade_principal}
Natureza Jurídica: {natureza}
Situação Cadastral: {situacao}
""".strip()
