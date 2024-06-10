import yfinance as yf
import os

# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

def fetch_commodity_data(symbol, period='1y', interval='1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    return data

def save_data(data, symbol):
    # Garantir que o diretório exista
    os.makedirs('data/raw', exist_ok=True)
    file_path = f"data/raw/{symbol}_data.csv"
    data.to_csv(file_path)
    print(f"Dados salvos em {file_path}")

if __name__ == "__main__":
    for symbol in commodities:
        data = fetch_commodity_data(symbol)
        save_data(data, symbol)
