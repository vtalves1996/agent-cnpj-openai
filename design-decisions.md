# Decisões de Design e Arquitetura

###  Objetivo

Construir um assistente em linha de comando capaz de consultar dados públicos de CNPJs utilizando a API da [CNPJá](https://cnpja.com/api/open) e resumi-los com apoio da OpenAI, simulando uma aplicação com a abordagem OpenAI Function Calling.

---

## Decisões de arquitetura

### 1. Organização em múltiplos arquivos

- **main.py**: ponto de entrada do assistente.
- **tools.py**: chamadas para API da CNPJá + tratamento de erros + cache básico.
- **utils.py**: tratamento e formatação da resposta da API para envio ao modelo.
- **config.py**: centralização de variáveis sensíveis com uso do `.env`.

> Decisão baseada na clareza de responsabilidades, manutenção e testes.

---

### 2. Uso de `.env` e `dotenv`

As variáveis sensíveis (chaves de API e parâmetros) foram isoladas no `.env`, não versionado.  
Uso da biblioteca `python-dotenv` para facilitar carregamento em dev/local.

---

### 3. OpenAI Function Calling

Uso explícito do recurso `function_call` do modelo GPT-3.5 Turbo, permitindo simular o comportamento de um agente autônomo que:

- Decide quando acionar a API externa com base no input.
- Interpreta e resume a resposta usando IA.

---

### 4. Testes automatizados com mocks

Criação de testes em `test_tools.py`, validando o comportamento da chamada à API de forma isolada, sem depender da conexão externa.

---

### 5. Estrutura leve e de fácil setup

Priorizei um setup funcional em menos de 5 minutos, com:

- Ambiente virtual
- `requirements.txt`
- `.env.example`
- `README.md` completo

---

### 6. Cache leve em memória

Para evitar múltiplas requisições da mesma consulta CNPJ, um cache simples com dicionário em memória foi implementado conforme sugerido.

---

### 7. Foco em código limpo e didático

- Comentários explicativos
- Separação clara de responsabilidades
- Nomenclaturas descritivas

---

## Tecnologias e bibliotecas

- **Python 3.10+**
- **OpenAI GPT-3.5 Turbo**
- **API CNPJá (open)**
- `requests`, `dotenv`, `pytest`

---

## Melhorias Futuras

A seguir, algumas melhorias consideradas para evoluções futuras do projeto, dependendo das necessidades específicas do cliente ou da empresa:

- **Interface Web para Interação**  
  Implementar uma interface visual simples utilizando ferramentas como Streamlit ou Gradio, permitindo que usuários testem o assistente sem depender do terminal.

- **Execução com API Ativa**  
  Realizar os testes automatizados e a demonstração final com a API CNPJá em funcionamento, garantindo cobertura completa dos fluxos reais.

- **Logs Estruturados**  
  Aprimorar o sistema de logging para tornar os registros mais organizados, facilitando análise de erros e auditoria.

- **Customização conforme Cliente**  
  Deixar a estrutura do projeto aberta para ajustes de fluxo, mensagens ou integrações conforme o perfil e objetivo do cliente final.

---

## Autor

Desenvolvido por **Victor Alves** como parte do desafio técnico da **Patagon AI**.
