# Testes de Validação

import pytest
from unittest.mock import patch
from tools import buscar_dados_por_cnpj

# Cenário 1: CNPJ válido e resposta bem-sucedida
@patch("tools.consultar_cnpj")
def test_cnpj_valido(mock_consulta):
    mock_consulta.return_value = {"razao_social": "Empresa Teste LTDA"}
    resultado = buscar_dados_por_cnpj("12345678000195")
    assert resultado["razao_social"] == "Empresa Teste LTDA"

# Cenário 2: CNPJ não encontrado (404)
@patch("tools.consultar_cnpj")
def test_cnpj_nao_encontrado(mock_consulta):
    mock_consulta.return_value = {"erro": "CNPJ não encontrado na base pública (404)."}
    resultado = buscar_dados_por_cnpj("11111111111111")
    assert resultado is None

# Cenário 3: Rate limit atingido (429)
@patch("tools.consultar_cnpj")
def test_rate_limit(mock_consulta):
    mock_consulta.return_value = {"erro": "Muitos pedidos seguidos. Aguarde um momento e tente novamente. (429)"}
    resultado = buscar_dados_por_cnpj("22222222222222")
    assert resultado is None

# Cenário 4: Erro do servidor (5xx)
@patch("tools.consultar_cnpj")
def test_erro_servidor(mock_consulta):
    mock_consulta.return_value = {"erro": "Erro no servidor da API (500). Tente novamente mais tarde."}
    resultado = buscar_dados_por_cnpj("33333333333333")
    assert resultado is None

# Cenário 5: CNPJ mal formatado (400)
@patch("tools.consultar_cnpj")
def test_cnpj_invalido(mock_consulta):
    mock_consulta.return_value = {"erro": "CNPJ inválido. Revise e envie novamente. (400)"}
    resultado = buscar_dados_por_cnpj("abcdefg")
    assert resultado is None