# Projeto de Data Warehouse de Commodities

Quanto sua empresa vendeu ontem?
Se você demorar mais de 3 segundos para responder esse workshop de hoje é para você!

Este projeto tem como objetivo criar um Data Warehouse (DW) para armazenar e analisar dados de commodities, utilizando uma arquitetura moderna de ETL (Extract, Transform, Load). O projeto inclui:

[Documentação do DBT](https://lvgalvao.github.io/workshop-aberto-dw-do-zero/#!/overview)

[Dashboard](https://lvgalvao-workshop-aberto-dw-do-zero-appapp-vp0gw4.streamlit.app/)

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
    subgraph Extract_Load
        A1[buscar_dados_commodities] --> B1[buscar_todos_dados_commodities]
        B1 --> C1[carregar_dados_no_postgres]
    end

    subgraph Transform
        D1[stg_commodities.sql] --> E1[stg_movimentacao_commodities.sql]
        E1 --> F1[dm_commodities.sql]
    end

    A[API de Commodities] -->|Extrai Dados| Extract_Load
    Extract_Load -->|Carrega Dados| C[PostgreSQL]
    C -->|Armazena Dados| D[Data Warehouse]
    Data_Warehouse -->|Transforma Dados| Transform
    Transform -->|Cria Views| F[Dashboard Streamlit]
```

### Ideia de ETL

```mermaid
graph LR;
    A[Extract] -->|Extrai Dados da API| B[Load]
    B -->|Carrega Dados no DW| C[Transform]
    C -->|Limpa e Transforma Dados| D[Data Warehouse]
    D -->|Exibe Dados| E[Dashboard Streamlit]
```