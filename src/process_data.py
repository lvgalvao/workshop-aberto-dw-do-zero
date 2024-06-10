import pandas as pd
import os

def process_commodity_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df = df.rename(columns={
        'Date': 'date',
        'Close': 'close'
    })
    df['date'] = pd.to_datetime(df['date'], utc=True).dt.date  # Garantir conversão para datetime e então para apenas data
    df['symbol'] = os.path.basename(file_path).split('_')[0]  # Extrai o símbolo do nome do arquivo
    return df

def process_movimentacao_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'])
    df['date'] = pd.to_datetime(df['date']).dt.date  # Converter para apenas data
    return df

def integrate_data(commodity_dfs, movimentacao_df):
    all_data = []
    for df in commodity_dfs:
        symbol = df['symbol'].iloc[0]
        symbol_data = movimentacao_df[movimentacao_df['symbol'] == symbol]
        integrated_df = df.merge(symbol_data, on='date', how='inner')  # Mudar para 'inner' para manter apenas datas com movimentação
        integrated_df['value'] = integrated_df['quantity'] * integrated_df['close']
        all_data.append(integrated_df)
    result_df = pd.concat(all_data)
    return result_df.drop(columns=['symbol_y']).rename(columns={'symbol_x': 'symbol'})

if __name__ == "__main__":
    data_dir = 'data/raw'
    files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('_data.csv')]
    commodity_dfs = [process_commodity_data(f) for f in files]
    movimentacao_df = process_movimentacao_data('data/external/movimentacao_commodities.csv')
    integrated_df = integrate_data(commodity_dfs, movimentacao_df)
    os.makedirs('data/processed', exist_ok=True)
    integrated_df.to_csv('data/processed/commodities_data.csv', index=False)
    print("Dados integrados salvos em data/processed/commodities_data.csv")
