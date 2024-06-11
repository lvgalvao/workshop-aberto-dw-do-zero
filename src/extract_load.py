import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da conexão com o banco de dados PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo  # Adiciona a coluna do símbolo
    return dados

def buscar_todos_dados_commodities():
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)  # Concatena todos os dados em um único DataFrame

def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)
    print(f"Dados salvos no schema '{schema}' do banco de dados PostgreSQL")

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities()
    salvar_no_postgres(dados_concatenados, schema='public')
