# Projeto Agente CNPJ via OpenAI Function Calling

Assistente conversacional em linha de comando que consulta e resume informações de empresas a partir do CNPJ, usando a API pública da [CNPJá](https://cnpja.com/api/open) e inteligência artificial da OpenAI.

---

## Setup em até 5 minutos

---

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/agentcnpj.git
cd agent-cnpj-openai

---

### 2. Criação e configuração de ambiente virtual
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

---

### 3. Instale as dependências
pip install -r requirements.txt

---

### 4. Configure variáveis de ambiente
Crie um arquivo .env na raiz do projeto com os seguintes campos
"
OPENAI_API_KEY=sua-chave-openai
CNPJA_API_TOKEN=seu-token-cnpja
CNPJ_API_BASE=https://cnpja.com/api/open
TIMEOUT=10
"

**Dica:** Você pode usar o arquivo `.env.example` como base, copiando e renomeando:
```bash
cp .env.example .env

---

### 5. Executar o assistente
Rode o script abaixo no terminal
python main.py

---

### 6. Executar os testes
Valide os testes com
pytest test_tools.py
# Rode os testes (certifique-se de que pytest está instalado)

---

### Validação de estrutura de arquivos
main.py – ponto de entrada do bot conversacional
tools.py – chamada à API da CNPJá + tratamento de erros + cache leve
utils.py – formatação dos dados de saída
config.py – leitura de variáveis sensíveis via .env
test_tools.py – testes unitários com mocks
.env.example – modelo das variáveis
evidencias_teste.md – evidências de testes realizados
design-decisions.md – documento explicando as principais decisões do projeto

---

### Tecnologias envolvidas
Python 3.10+
OpenAI GPT-3.5 Turbo
API CNPJá (open)
Requests
Dotenv
Pytest

---

Desenvolvido por Victor Alves como entregável do desafio técnico para a Patagon AI.