import streamlit as st
import subprocess
import pandas as pd
from st_aggrid import AgGrid
from extraccion import *

st.title("Boletas descargadas de")
st.sidebar.title("Menu")
app_mode = st.sidebar.selectbox("Seleccione una opcion", ["CGE", "Enel", "ESSBIO"])

if app_mode == "CGE":
    st.title("CGE")
    if st.button("Mostrar boletas procesadas de CGE"):

        result = subprocess.run(["python", "extraccion\extractor_cge.py"], capture_output=True, text=True)
        
        if result.stderr:
            st.text_area("Errores", result.stderr)
    
        try:
            excel_path = r"C:\Users\LukasOrellanaFarías\Desktop\boletas_cge.xlsx"
            st.markdown(f"[El archivo Excel se guardó en: {excel_path}](file:///{excel_path})")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Enel":
    st.title("Enel")
    if st.button("Mostrar boletas procesadas de Enel"):
        print("Enel")

elif app_mode == "ESSBIO":
    st.title("ESSBIO")
    if st.button("Mostrar boletas procesadas de ESSBIO") :
        result = subprocess.run(["python", "extraccion\extractor_essbio.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = r"C:\Users\LukasOrellanaFarías\Desktop\boletas_essbio.xlsx"
            st.markdown(f"[El archivo Excel se guardó en: {excel_path}](file:///{excel_path})")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

        print("ESSBIO")