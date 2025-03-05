import streamlit as st
import pandas as pd

st.title('Modelo Integral de Flujo de Caja - Avellanos')

# Sidebar para Supuestos Editables
st.sidebar.header('Supuestos Editables')
valor_tierra = st.sidebar.number_input('Valor Tierra (USD)', value=15000, step=500)
revalorizacion_tierra = st.sidebar.number_input('Revalorización Tierra (%)', value=4.0, step=0.1) / 100
tasa_deuda = st.sidebar.number_input('Tasa Deuda Nominal (%)', value=7.0, step=0.1) / 100
pct_deuda = st.sidebar.number_input('Deuda (%)', value=30.0, step=1.0) / 100
pct_equity = st.sidebar.number_input('Equity (%)', value=70.0, step=1.0) / 100
arriendo_real = st.sidebar.number_input('Arriendo Real (%)', value=4.0, step=0.1) / 100
costo_tributario_terreno = st.sidebar.number_input('Costo Tributario Terreno (USD)', value=4237.0)
tax_inversiones = st.sidebar.number_input('Tax Inversiones (%)', value=27.0, step=0.1) / 100
costo_cosecha_kg = st.sidebar.number_input('Costo por kg (USD)', value=0.36, step=0.01)
precio_kg = st.sidebar.number_input('Precio por kg (USD)', value=4.0, step=0.1)
inflacion_us = st.sidebar.number_input('Inflación EEUU (%)', value=2.0, step=0.1) / 100

# Configuración tasa de descuento desplegable
with st.expander('Configuración Tasa de Descuento'):
    equity_risk_premium = st.number_input('Equity Risk Premium (%)', value=4.0, step=0.1)
    spread = st.number_input('Spread (%)', value=4.0, step=0.1)

tasa_descuento = (equity_risk_premium + spread) / 100
st.write(f'**Tasa Descuento Total:** {tasa_descuento*100:.2f}%')

# Proyección temporal
años = [f'{a}-{a+1}' for a in range(2024, 2044)]

# Proyecciones
kg_por_ha = [400, 1800, 2300, 3200, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600]
precio_kg = [4 * (1 + 0.02)**i for i in range(20)]  # Precio ajustado por inflación US
ingresos = [kg * precio * 1328 for kg, precio in zip(kg_por_ha, precio_kg)]
costos_cosecha = [kg * costo_cosecha_kg * 1328 for kg in kg_por_ha]
margen_bruto = [ing - costo for ing, costo in zip(ingresos, costos_cosecha)]

# Cálculo de valor presente
valor_presente = [mb / ((1 + (equity_risk_premium + spread)/100)**(i+1)) for i, mb in enumerate(margen_bruto)]

# DataFrame completo
proyeccion_df = pd.DataFrame({
    'Año': años,
    'Kg/ha': kg_por_ha,
    'Precio por kg (USD)': precio_kg,
    'Ingresos Totales (USD)': ingresos,
    'Costos Cosecha (USD)': costos_cosecha,
    'Margen Bruto (USD)': [i - c for i, c in zip(ingresos, costos_cosecha)],
    'Valor Presente (USD)': valor_presente
})

# Visualización resultados
st.write('### Proyección detallada del proyecto Avellanos')
st.dataframe(proyeccion_df, hide_index=True)

# Totales
st.write(f"**Ingreso Total Proyectado:** USD {sum(ingresos):,.2f}")
st.write(f"**Costo Total Cosecha:** USD {sum(costos_cosecha):,.2f}")
st.write(f"**Margen Bruto Total:** USD {sum(margen_bruto):,.2f}")
st.write(f"**Valor Presente Neto (VPN):** USD {sum(valor_presente):,.2f}")
