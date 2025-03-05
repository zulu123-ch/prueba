import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Proyección de Flujo de Ingresos y Costos con Valor Presente')

# Entradas editables por el usuario
precio = st.number_input('Precio (USD)', value=4.6, step=0.1)
costo_unitario = st.number_input('Costo unitario (USD)', value=3.5, step=0.1)
cantidad = st.number_input('Cantidad', value=1328, step=1)

# Configuración desplegable para tasa de descuento
with st.expander("Configuración de Tasa de Descuento"):
    equity_risk_premium = st.number_input('Equity Risk Premium (%)', value=4.0, step=0.1)
    spread = st.number_input('Spread (%)', value=4.0, step=0.1)

# Cálculo de la tasa de descuento total
tasa_descuento_total = (equity_risk_premium + spread) / 100
st.write(f"**Tasa de descuento total:** {tasa_descuento_total*100:.2f}%")

# Años para la proyección
años = [f'{a}-{a+1}' for a in range(2024, 2044)]

# Cálculos
ingresos = [precio * cantidad for _ in range(20)]
costos = [costo_unitario * cantidad for _ in range(20)]
margen_bruto = [ing - cost for ing, cost in zip(ingresos, costos)]
valor_presente = [mb / ((1 + tasa_descuento_total) ** (i + 1)) for i, mb in enumerate(margen_bruto)]

# Creación de DataFrame para mostrar resultados
df = pd.DataFrame({
    'Año': años,
    'Ingresos (USD)': ingresos,
    'Costos (USD)': costos,
    'Margen Bruto (USD)': margen_bruto,
    'Valor Presente (USD)': valor_presente
})

# Mostrar DataFrame en la aplicación
st.write('### Proyección de Ingresos, Costos, Margen Bruto y Valor Presente a 20 años')
st.dataframe(df, hide_index=True)

# Totales
st.write(f"**Ingreso Total Proyectado:** USD {sum(ingresos):,.2f}")
st.write(f"**Costo Total Proyectado:** USD {sum(costos):,.2f}")
st.write(f"**Margen Bruto Total Proyectado:** USD {sum(margen_bruto):,.2f}")
st.write(f"**Valor Presente Total Proyectado:** USD {sum(valor_presente):,.2f}")
