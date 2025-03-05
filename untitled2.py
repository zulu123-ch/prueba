import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Resumen de Mercados")

# Definir tickers para cada categoría
tickers = {
    'Monedas': ['CLP=X', 'UF=X', 'BRL=X', 'ARS=X', 'PEN=X', 'MXN=X', 'AUDUSD=X', 'CAD=X', 'GBPUSD=X', 'JPY=X', 'CNY=X'],
    'Commodities': ['HG=F', 'CL=F', 'NG=F', 'GC=F'],
    'Mercados': ['^IPSA', '^GSPC', '^IXIC', '^DJI', '^FTSE', '^GDAXI', '^N225', '000300.SS'],
    'Tasas de Interés': ['^TNX', '^TYX']
}

# Mostrar cada categoría en Streamlit
for categoria, tickers_lista in tickers.items():
    st.header(categoria)
    data = yf.download(tickers_lista, period='5d')['Close']
    if not data.empty:
        ultimos_valores = data.iloc[-1]
        variacion = ((data.iloc[-1] / data.iloc[-2] - 1) * 100).round(2)
        df_categoria = pd.DataFrame({'Valor': ultimos_valores, 'Var%': variacion})
        st.dataframe(df_categoria.style.format({'Valor': '{:,.2f}', 'Var%': '{:+.2f}%'}))
    else:
        st.write("Datos no disponibles actualmente.")
