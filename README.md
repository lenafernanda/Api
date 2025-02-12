# Api
Esse código cria um servidor web que simula dados de anúncios do Facebook e YouTube. Ele calcula coisas como o total de cliques, gastos e quanto custou cada clique. Quando você acessa os endereços no navegador, ele mostra esses dados de forma organizada.
# Projeto Flask: Análise de Anúncios

Este projeto é um servidor web feito em Flask que simula dados de anúncios do **Facebook** e **YouTube**. Ele calcula métricas como total de cliques, gastos e custo por clique, e retorna esses dados em formato JSON.

## Como Funciona?

O código cria um servidor web que:
1. Simula dados de anúncios do Facebook e YouTube.
2. Calcula métricas como:
   - Total de cliques.
   - Total de gastos.
   - Custo por clique.
3. Retorna os dados em formato JSON quando você acessa as rotas do servidor.

## Rotas Disponíveis

- **`/facebook/resumo`**: Retorna um resumo dos dados do Facebook.
- **`/youtube/resumo`**: Retorna um resumo dos dados do YouTube.
- **`/geral`**: Retorna todos os dados do Facebook e YouTube.
- **`/geral/resumo`**: Retorna um resumo geral dos dados do Facebook e YouTube.

## Como Usar?

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/desenvolvimento_web.git
