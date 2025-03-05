import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Proyección de Flujo de Ingresos')

# Entradas editables por el usuario
precio = st.number_input('Precio (USD)', value=4.6, step=0.1)
cantidad = st.number_input('Cantidad', value=1328, step=1)

# Años para la proyección
años = [f'{a}-{a+1}' for a in range(2024, 2044)]

# Cálculo de ingresos proyectados
ingresos = [precio * cantidad for _ in range(20)]

# Creación de DataFrame para mostrar resultados
df = pd.DataFrame({
    'Año': [f'{2024 + i}-{2025 + i}' for i in range(20)],
    'Ingresos (USD)': ingresos
})

# Mostrar DataFrame en la aplicación
st.write('### Ingresos Proyectados a 20 años')
st.dataframe(df, hide_index=True)

# Suma total de ingresos
st.write(f"**Ingreso Total Proyectado:** USD {sum(ingresos):,.2f}")


