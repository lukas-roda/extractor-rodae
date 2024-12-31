import streamlit as st
import subprocess
import pandas as pd
from st_aggrid import AgGrid
from extraccion import *
import os
import function.upload_to_onedrive as uto

st.set_page_config(page_title="Boletas")
st.title("Boletas descargadas de")
st.sidebar.title("Menu")
app_mode = st.sidebar.selectbox("Seleccione una opcion", ["CGE", "Enel", "ESSBIO", "Aguas Andinas", "Edelmag", "Aguas Araucania"])

if app_mode == "CGE":
    st.title("CGE")
    if st.button("Mostrar boletas descargadas de CGE"):

        result = subprocess.run(["python", "extraccion\extractor_cge.py"], capture_output=True, text=True)
        
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\CGE\boletas_cge.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)  
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Enel":
    st.title("Enel")
    if st.button("Mostrar boletas descargadas de Enel"):
        result = subprocess.run(["python", "extraccion\extractor_enel.py"], capture_output=True, text=True)

        if result.stderr:
            st.text_area("Errores", result.stderr)
        
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Enel\boletas_enel.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")
        print("Enel")

elif app_mode == "ESSBIO":

    st.title("ESSBIO")
    if st.button("Mostrar boletas descargadas de ESSBIO") :
        result = subprocess.run(["python", "extraccion\extractor_essbio.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Essbio\boletas_essbio.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

        print("ESSBIO")

elif app_mode == "Aguas Andinas":
    st.title("Aguas Andinas")
    if st.button("Mostrar boletas descargadas de Aguas Andinas"):
        result = subprocess.run(["python", "extraccion\extractor_aguasandinas.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas andinas\boletas_aguasandinas.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Edelmag":
    st.title("Edelmag")
    if st.button("Mostrar boletas descargadas de Edelmag"):
        result = subprocess.run(["python", "extraccion\extractor_edelmag.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Edelmag\boletas_edelmag.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Aguas Araucania":
    st.title("Aguas Araucania")
    if st.button("Mostrar boletas descargadas de Aguas Araucania"):
        result = subprocess.run(["python", "extraccion\extractor_aguasaraucania.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas araucania\boletas_aguasaraucania.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")