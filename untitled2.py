import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Proyección de Flujo de Ingresos y Costos')

# Entradas editables por el usuario
precio = st.number_input('Precio (USD)', value=4.6, step=0.1)
costo_unitario = st.number_input('Costo unitario (USD)', value=3.5, step=0.1)
cantidad = st.number_input('Cantidad', value=1328, step=1)

# Años para la proyección
años = [f'{a}-{a+1}' for a in range(2024, 2044)]

# Cálculos
ingresos = [precio * cantidad for _ in range(20)]
costos = [costo_unitario * cantidad for _ in range(20)]
margen_bruto = [ing - cost for ing, cost in zip(ingresos, costos)]

# Creación de DataFrame para mostrar resultados
df = pd.DataFrame({
    'Año': años,
    'Ingresos (USD)': ingresos,
    'Costos (USD)': costos,
    'Margen Bruto (USD)': margen_bruto
})

# Mostrar DataFrame en la aplicación
st.write('### Proyección de Ingresos, Costos y Margen Bruto a 20 años')
st.dataframe(df, hide_index=True)

# Totales
st.write(f"**Ingreso Total Proyectado:** USD {sum(ingresos):,.2f}")
st.write(f"**Costo Total Proyectado:** USD {sum(costos):,.2f}")
st.write(f"**Margen Bruto Total Proyectado:** USD {sum(margen_bruto):

