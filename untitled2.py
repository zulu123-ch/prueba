import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Rentabilidades del S&P, NASDAQ y VFLO")

# Descargar datos desde Yahoo Finance
tickers = {'S&P 500': '^GSPC', 'NASDAQ': '^IXIC', 'VFLO ETF': 'VFLO'}
periods = {'1d': 1, '1w': 7, '1m': 30, '3m': 90, '1y': 365, '3y': 365*3, '5y': 365*5, '10y': 365*10}

data = {}
for name, ticker in tickers.items():
    ticker_data = yf.Ticker(ticker)
    returns = {}
    for label, days in periods.items():
        hist = ticker_data.history(period=f'{days+1}d')
        if len(hist) > 1:
            total_return = hist['Close'][-1] / hist.iloc[0]['Close'] - 1
            if label in ['3y', '5y', '10y']:
                annualized_return = (1 + total_return) ** (1/(days/365)) - 1
                returns[label] = annualized_return * 100
            else:
                returns[label] = total_return * 100
        else:
            returns[label] = None
    data[name] = returns

# Convertir a DataFrame
df = pd.DataFrame(data).T

# Mostrar resultados
st.write('### Rentabilidades S&P 500, NASDAQ y VFLO ETF')
st.dataframe(df.style.format("{:.2f}%"))
