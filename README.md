Parece que há problemas de formatação nos gráficos Mermaid. Vamos garantir que a sintaxe esteja correta e usar a formatação adequada para gráficos Mermaid no Markdown.

Aqui está uma versão atualizada do README com os gráficos corrigidos:

### README do Projeto

# Projeto de Data Warehouse de Commodities

Este projeto tem como objetivo criar um Data Warehouse (DW) para armazenar e analisar dados de commodities, utilizando uma arquitetura moderna de ETL (Extract, Transform, Load). O projeto inclui:

1. **Parte de Extract_Load**: Responsável por extrair dados de uma API e carregar diretamente no banco de dados PostgreSQL.
2. **Parte de Seed**: Utiliza seeds do DBT para carregar dados de movimentações de commodities a partir de arquivos CSV.
3. **Models**: Define as transformações de dados usando DBT, criando tabelas de staging e de datamart.
4. **Dashboard**: Implementado em Streamlit, exibe dados e visualizações das commodities a partir do Data Warehouse.

## Estrutura do Projeto

### 1. Extract_Load

A parte de `extract_load` é responsável por extrair dados de uma API e carregar diretamente no banco de dados PostgreSQL. O script `extract_load.py` realiza essa operação.

### 2. Seed

A parte de seed utiliza o DBT para carregar dados de movimentações de commodities a partir de arquivos CSV. Esses dados são carregados diretamente no Data Warehouse.

### 3. Models

Os models do DBT são usados para transformar os dados carregados em tabelas de staging e de datamart. As transformações incluem a limpeza dos dados e a criação de métricas agregadas.

### 4. Dashboard

O dashboard é implementado em Streamlit e permite visualizar os dados das commodities armazenados no Data Warehouse. Ele exibe tabelas e gráficos interativos para análise dos dados.

## Gráficos Mermaid

### Movimentação entre Sistemas

```mermaid
graph TD;
    A[API de Commodities] -->|Extrai Dados| B[Extract_Load]
    B -->|Carrega Dados| C[PostgreSQL]
    C -->|Armazena Dados| D[Data Warehouse]
    D -->|Transforma Dados| E[DBT Models]
    E -->|Cria Views| F[Dashboard (Streamlit)]
```

### Ideia de ETL

```mermaid
graph TD;
    A[Extract] -->|Extrai Dados da API| B[Transform]
    B -->|Limpa e Transforma Dados| C[Load]
    C -->|Carrega Dados no DW| D[Data Warehouse]
    D -->|Exibe Dados| E[Dashboard (Streamlit)]
```