import pandas as pd
import sqlite3
import os

def create_dw():
    os.makedirs('data/dw', exist_ok=True)
    conn = sqlite3.connect('data/dw/commodities_dw.db')
    df = pd.read_csv('data/processed/commodities_data.csv')
    df.to_sql('commodities', conn, if_exists='replace', index=False)
    conn.close()
    print("Data Warehouse criado em data/dw/commodities_dw.db")

if __name__ == "__main__":
    create_dw()
