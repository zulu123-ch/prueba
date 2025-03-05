import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

st.title("Rentabilidades del S&P y NASDAQ")

# Descargar datos desde Yahoo Finance
tickers = {'S&P 500': '^GSPC', 'NASDAQ': '^IXIC'}
periods = {'1d': 1, '1w': 7, '1m': 30, '3m': 90, '1y': 365}

data = {}
for name, ticker in zip(['S&P 500', 'NASDAQ'], ['^GSPC', '^IXIC']):
    ticker_data = yf.Ticker(ticker)
    returns = {}
    for label, days in periods.items():
        hist = ticker_data.history(period=f'{days+1}d')
        ret = (hist['Close'][-1] / hist.iloc[0]['Close'] - 1) * 100
        data.setdefault(name, {})[label] = ret

# Convertir a DataFrame
df = pd.DataFrame(data).T

# Mostrar resultados
st.title('Rentabilidades S&P 500 y NASDAQ')
st.dataframe(df.style.format("{:.2f}%"))
