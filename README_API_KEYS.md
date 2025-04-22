# Configuração de Chaves de API para Execução Local

Este guia explica como configurar as chaves de API necessárias para executar o notebook `ai_agent_stocks_insights_updated.ipynb` localmente.

## Pré-requisitos

1. Você precisa ter instalado a biblioteca python-dotenv:
   ```
   pip install python-dotenv
   ```

2. Você precisa ter contas e chaves de API para os seguintes serviços:
   - Google AI (Gemini API): https://ai.google.dev/
   - Alpha Vantage (dados financeiros): https://www.alphavantage.co/
   - News API (artigos de notícias): https://newsapi.org/

## Configuração

1. Copie o arquivo `.env.example` para um novo arquivo chamado `.env`:
   ```
   cp .env.example .env
   ```

2. Edite o arquivo `.env` e substitua os valores de exemplo pelas suas chaves de API reais:
   ```
   GOOGLE_API_KEY=sua_chave_google_aqui
   ALPHAVANTAGE_KEY=sua_chave_alphavantage_aqui
   NEWSAPI_KEY=sua_chave_newsapi_aqui
   ```

3. Certifique-se de que o arquivo `.env` está no mesmo diretório do notebook.

4. Execute o notebook `ai_agent_stocks_insights_updated.ipynb` em vez do arquivo original.

## Segurança

- **IMPORTANTE**: Nunca compartilhe ou cometa suas chaves de API em repositórios públicos
- O arquivo `.env` já está incluído no `.gitignore` para evitar que seja acidentalmente adicionado ao controle de versão
- Em ambientes de produção, considere usar variáveis de ambiente do sistema ou um serviço de gerenciamento de segredos

## Solução de Problemas

Se você encontrar mensagens de aviso sobre chaves de API ausentes:

1. Verifique se o arquivo `.env` está no diretório correto
2. Confirme se as chaves estão corretamente formatadas (sem espaços extras ou aspas)
3. Reinicie o kernel do notebook para recarregar as variáveis de ambiente 