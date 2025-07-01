# Configurações globais e sensíveis, carregadas do arquivo .env

import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (útil para dev/local)
load_dotenv()

# Chaves de API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CNPJA_API_TOKEN = os.getenv("CNPJA_API_TOKEN")

# Parâmetros adicionais
CNPJ_API_BASE = os.getenv("CNPJ_API_BASE")
TIMEOUT = int(os.getenv("TIMEOUT", 10))  # fallback para 10s se não definido no .env