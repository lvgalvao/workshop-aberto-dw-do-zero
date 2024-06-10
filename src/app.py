import pandas as pd
import sqlite3
import streamlit as st
import plotly.express as px

def load_data():
    conn = sqlite3.connect('data/dw/commodities_dw.db')
    df = pd.read_sql_query("SELECT * FROM commodities", conn)
    conn.close()
    return df

def analyze_data(df):
    # Calcular o ganho ou perda com as operações
    df['operation_value'] = df['quantity'] * df['close'] * df.apply(lambda x: 1 if x['action'] == 'sell' else -1, axis=1)
    total_gain_loss = df['operation_value'].sum()

    # Calcular o saldo atual de cada commodity
    balance = df.groupby('symbol')['quantity'].sum()

    # Calcular o valor atual das commodities baseando-se no preço mais recente
    latest_prices = df.groupby('symbol')['close'].last()
    current_value = balance * latest_prices

    # Adicionar o valor atual das commodities ao ganho ou perda total
    net_gain_loss = total_gain_loss + current_value.sum()

    return net_gain_loss, total_gain_loss, balance, current_value

def plot_balance(balance):
    fig = px.bar(balance, title='Saldo Atual de Cada Commodity', labels={'value': 'Quantidade', 'index': 'Commodity'})
    st.plotly_chart(fig)

def plot_current_value(current_value):
    fig = px.bar(current_value, title='Valor Atual de Cada Commodity', labels={'value': 'Valor (USD)', 'index': 'Commodity'})
    st.plotly_chart(fig)

def main():
    st.title('Análise de Commodities')

    df = load_data()
    net_gain_loss, total_gain_loss, balance, current_value = analyze_data(df)

    st.write(f"Total de ganho ou perda com as operações: {total_gain_loss}")
    st.write(f"Total de ganho ou perda incluindo valor atual das commodities: {net_gain_loss}")
    st.write("Saldo atual de cada commodity:")
    st.write(balance)
    st.write("Valor atual das commodities:")
    st.write(current_value)

    plot_balance(balance)
    plot_current_value(current_value)

if __name__ == "__main__":
    main()
