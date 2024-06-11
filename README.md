Claro! Aqui está um exemplo de um arquivo `requirements.txt` para a parte do Streamlit do projeto:

```plaintext
streamlit==1.10.0
pandas==1.4.2
sqlalchemy==1.4.36
psycopg2-binary==2.9.3
python-dotenv==0.20.0
```

### Passos para Criação do Projeto Streamlit

1. **Crie um novo diretório para o projeto Streamlit**:
   ```bash
   mkdir streamlit_project
   cd streamlit_project
   ```

2. **Crie um ambiente virtual e ative-o**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Crie o arquivo `requirements.txt`**:
   ```plaintext
   streamlit==1.10.0
   pandas==1.4.2
   sqlalchemy==1.4.36
   psycopg2-binary==2.9.3
   python-dotenv==0.20.0
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Crie o arquivo `.env`**:
   ```plaintext
   DB_HOST_PROD=dpg-cpk81rect0pc73b46fj0-a.oregon-postgres.render.com
   DB_PORT_PROD=5432
   DB_NAME_PROD=databasesales
   DB_USER_PROD=postgres123
   DB_PASS_PROD=H5XgdTe7z3ujAMwa8grpKy28dTGjQshA
   DB_SCHEMA_PROD=public
   DB_THREADS_PROD=1
   DB_TYPE_PROD=postgres
   DBT_PROFILES_DIR=../
   ```

6. **Crie o arquivo `app.py`** com o conteúdo atualizado:

   ```python
   import os
   import pandas as pd
   import streamlit as st
   from sqlalchemy import create_engine
   from sqlalchemy.exc import ProgrammingError
   from dotenv import load_dotenv

   # Carregar variáveis de ambiente do arquivo .env
   load_dotenv()

   # Obter as variáveis do arquivo .env
   DB_HOST = os.getenv('DB_HOST_PROD')
   DB_PORT = os.getenv('DB_PORT_PROD')
   DB_NAME = os.getenv('DB_NAME_PROD')
   DB_USER = os.getenv('DB_USER_PROD')
   DB_PASS = os.getenv('DB_PASS_PROD')
   DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

   # Criar a URL de conexão do banco de dados
   DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

   # Criar o engine de conexão com o banco de dados
   engine = create_engine(DATABASE_URL)

   # Consultar os dados da tabela dm_commodities
   def get_data():
       query = f"""
       SELECT
           data,
           simbolo,
           valor_fechamento,
           acao,
           quantidade,
           valor,
           ganho
       FROM
           public.dm_commodities;
       """
       try:
           df = pd.read_sql(query, engine)
           return df
       except ProgrammingError as e:
           st.error(f"Erro ao acessar a tabela 'dm_commodities' no schema '{DB_SCHEMA}': {e}")
           return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

   # Configurar a página do Streamlit
   st.set_page_config(page_title='Dashboard de Commodities', layout='wide')

   # Título do Dashboard
   st.title('Dashboard de Commodities')

   # Descrição
   st.write("""
   Este dashboard mostra os dados de commodities e suas transações.
   """)

   # Obter os dados
   df = get_data()

   # Verificar se o DataFrame está vazio
   if df.empty:
       st.write("Não foi possível carregar os dados. Verifique se a tabela 'dm_commodities' existe no schema especificado.")
   else:
       # Exibir os dados
       st.write("### Dados das Commodities")
       st.dataframe(df)

       # Resumo estatístico
       st.write("### Resumo Estatístico")
       st.write(df.describe())

       # Gráficos
       st.write("### Gráficos")

       # Gráfico de barras para ganhos e perdas
       st.bar_chart(df[['data', 'ganho']].set_index('data'))

       # Gráfico de linha para valores de fechamento
       st.line_chart(df[['data', 'valor_fechamento']].set_index('data'))
   ```

7. **Executar o Aplicativo Streamlit**:
   ```bash
   streamlit run app.py
   ```

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

## Executando o Projeto

### Requisitos

- Python 3.7+
- PostgreSQL
- DBT
- Streamlit

### Passos para Execução

1. **Clonar o Repositório**:
   ```bash
   git clone <URL-do-Repositório>
   cd <Nome-do-Repositório>
   ```

2. **Configurar o Ambiente Virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Variáveis de Ambiente**:
   - Crie um arquivo `.env` com as seguintes variáveis:
     ```env
     DB_HOST_PROD=dpg-cpk81rect0pc73b46fj0-a.oregon-postgres.render.com
     DB_PORT_PROD=5432
     DB_NAME_PROD=databasesales
     DB_USER_PROD=postgres123
     DB_PASS_PROD=H5XgdTe7z3ujAMwa8grpKy28dTGjQshA
     DB_SCHEMA_PROD=public
     DB_THREADS_PROD=1
     DB_TYPE_PROD=postgres
     DBT_PROFILES_DIR=../
     ```

5. **Executar o Script de Extract_Load**:
   ```bash
   python src/extract_load.py
   ```

6. **Executar os Seeds do DBT**:
   ```bash
   dbt seed
   ```

7. **Executar as Transformações do DBT**:
   ```bash
   dbt run
   ```

8. **Executar o Dashboard Streamlit**:
   ```bash
   streamlit run app/app.py
   ```

### Contribuição

Para contribuir com o projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações.

---

### Imagens Mermaid

#### Movimentação entre Sistemas

```mermaid
graph TD;
    A[API de Commodities] -->|Extrai Dados| B[Extract_Load]
    B -->|Carrega Dados| C[PostgreSQL]
    C -->|Armazena Dados| D[Data Warehouse]
   

 D -->|Transforma Dados| E[DBT Models]
    E -->|Cria Views| F[Dashboard (Streamlit)]
```

#### Ideia de ETL

```mermaid
graph TD;
    A[Extract] -->|Extrai Dados da API| B[Transform]
    B -->|Limpa e Transforma Dados| C[Load]
    C -->|Carrega Dados no DW| D[Data Warehouse]
    D -->|Exibe Dados| E[Dashboard (Streamlit)]
```