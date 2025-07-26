import streamlit as st

#? --- PAGE SETUP ---#
inventarios_page = st.Page(
    page="views/inventario.py",
    title="Inventario",
    icon="📋",
    default=True
)

ventas_page = st.Page(
    page="views/ventas.py",
    title="Ventas",
    icon="📈"
)

mermas_page = st.Page(
    page="views/mermas.py",
    title="Mermas",
    icon="📉"
)

#? --- NAVEGATION SETUP [WITH SECTIONS] ---#
pg = st.navigation(
    {
        "Productos en Sucursal": [inventarios_page],
        "Ventas y Mermas": [ventas_page, mermas_page]
    }
)

#? --- RUN NAVEGATION ---#
pg.run()