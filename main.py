# Arquivo principal: integração com OpenAI e execução do agente

import openai
import os
from config import OPENAI_API_KEY
from tools import consultar_cnpj
from utils import extrair_cnpj

openai.api_key = OPENAI_API_KEY

def main():
    print("🔍 Digite uma mensagem com o CNPJ (ex: 'consulta o 12.345.678/0001-90'):")
    entrada = input("Você: ")

    cnpj = extrair_cnpj(entrada)

    if not cnpj:
        print("❌ Nenhum CNPJ válido encontrado na mensagem.")
        return

    print(f"🔎 Consultando dados da empresa com CNPJ {cnpj}...")
    dados = consultar_cnpj(cnpj)

    if "erro" in dados:
        print(f"❌ Erro: {dados['erro']}")
        return

    # Gerar prompt com os dados recebidos
    prompt = f"""Baseado nas seguintes informações da empresa com CNPJ {cnpj}, gere um resumo simples e amigável para entender o perfil da empresa:

{dados}
"""

    print("\n🤖 Gerando resumo com o modelo da OpenAI...\n")

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que resume perfis de empresas com base nos dados do CNPJ."},
                {"role": "user", "content": prompt}
            ]
        )

        resumo = resposta.choices[0].message.content
        print("🧠 Resumo do assistente:\n")
        print(resumo)

    except Exception as e:
        print(f"❌ Erro ao gerar resposta da OpenAI: {e}")

if __name__ == "__main__":
    main()
