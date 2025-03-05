import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Proyección Integral de Flujo de Caja')

# Supuestos Generales Editables
st.sidebar.header("Supuestos Editables")
precio = st.sidebar.number_input('Precio (USD)', value=4.6, step=0.1)
costo_unitario = st.sidebar.number_input('Costo unitario (USD)', value=3.5, step=0.1)
cantidad = st.sidebar.number_input('Cantidad', value=1328, step=1)
valor_tierra = st.sidebar.number_input('Valor Tierra (USD)', value=15000, step=500)
equity = st.sidebar.number_input('Equity (%)', value=70.0, step=1.0) / 100
deuda = st.sidebar.number_input('Deuda (%)', value=30.0, step=1.0) / 100
costo_cosecha_kg = st.sidebar.number_input('Costo por kg (cosecha)', value=0.5, step=0.01)

# Tasa de Descuento (Equity Risk Premium + Spread)
with st.expander("Configuración de Tasa de Descuento"):
    equity_risk_premium = st.number_input('Equity Risk Premium (%)', value=4.0, step=0.1)
    spread = st.number_input('Spread (%)', value=4.0, step=0.1)

tasa_descuento_total = (equity_risk_premium + spread) / 100
st.write(f"**Tasa de descuento total:** {tasa_descuento_total*100:.2f}%")

# Años para la proyección
años = [f'{a}-{a+1}' for a in range(2024, 2044)]

# Cálculos de Flujos
ingresos = [precio * cantidad for _ in años]
costos = [3.5 * cantidad for _ in años]
margen_bruto = [ing - cost for ing, cost in zip(ingresos, costos)]
valor_presente = [mb / ((1 + tasa_descuento_total) ** (i + 1)) for i, mb in enumerate(margen_bruto)]

# DataFrame Resultados
df = pd.DataFrame({
    'Año': años,
    'Ingresos (USD)': ingresos,
    'Costos (USD)': costos,
    'Margen Bruto (USD)': margen_bruto,
    'Valor Presente (USD)': valor_presente
})

# Mostrar tabla
st.write('### Proyección Completa del Flujo de Caja')
st.dataframe(df, hide_index=True)

# Totales
st.write(f"**Ingreso Total:** USD {sum(ingresos):,.2f}")
st.write(f"**Costo Total:** USD {sum(costos):,.2f}")
st.write(f"**Margen Bruto Total:** USD {sum(margen_bruto):,.2f}")
st.write(f"**Valor Presente Neto (VPN):** USD {sum(valor_presente):,.2f}")
