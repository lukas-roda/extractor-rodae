import streamlit as st
import subprocess
import pandas as pd
from st_aggrid import AgGrid
from extraccion import *
import os
import function.upload_to_onedrive as uto
python_interpreter = r"env\Scripts\python.exe"
st.set_page_config(page_title="Boletas")
st.title("Boletas descargadas de")
st.sidebar.title("Menu")
app_mode = st.sidebar.selectbox("Seleccione una opcion", ["CGE", "Enel", "ESSBIO", "Aguas Andinas", "Edelmag", "Aguas Araucania",
                                                           "Aguas del altiplano", "Casablanca","Tiltil", "Aguas magallanes",
                                                           "Chilquinta", "Eepa", "Esval", "Nueva atacama", "Saesa", "Suralis", "Saesa2",
                                                           "Aguas decimas"])

if app_mode == "CGE":
    st.title("CGE")
    if st.button("Mostrar boletas descargadas de CGE"):

        result = subprocess.run([python_interpreter, "extraccion\extractor_cge.py"], capture_output=True, text=True)
        
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
        result = subprocess.run([python_interpreter, "extraccion\extractor_enel.py"], capture_output=True, text=True)

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
        result = subprocess.run([python_interpreter, "extraccion\extractor_essbio.py"], capture_output=True, text=True)
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
        result = subprocess.run([python_interpreter, "extraccion\extractor_aguasandinas.py"], capture_output=True, text=True)
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
        result = subprocess.run([python_interpreter, "extraccion\extractor_edelmag.py"], capture_output=True, text=True)
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
        result = subprocess.run([python_interpreter, "extraccion\extractor_aguasaraucania.py"], capture_output=True, text=True)
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

elif app_mode == "Aguas del altiplano":
    st.title("Aguas del altiplano")
    if st.button("Mostrar boletas descargadas de Aguas del altiplano"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_aguasdelaltiplano.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas del altiplano\boletas_aguasdelaltiplano.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Casablanca":
    st.title("Casablanca")
    if st.button("Mostrar boletas descargadas de Casablanca"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_casablanca.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Casablanca\boletas_casablanca.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Tiltil":
    st.title("Tiltil")
    if st.button("Mostrar boletas descargadas de Tiltil"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_tiltil.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Tiltil\boletas_tiltil.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Aguas magallanes":
    st.title("Aguas magallanes")
    if st.button("Mostrar boletas descargadas de Aguas magallanes"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_aguasmagallanes.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas magallanes\boletas_aguasmagallanes.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Chilquinta":
    st.title("Chilquinta")
    if st.button("Mostrar boletas descargadas de Chilquinta"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_chilquinta.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Chilquinta\boletas_chilquinta.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Eepa":
    st.title("Eepa")
    if st.button("Mostrar boletas descargadas de Eepa"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_eepa.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Eepa\boletas_eepa.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Esval":
    st.title("Esval")
    if st.button("Mostrar boletas descargadas de Esval"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_esval.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Esval\boletas_esval.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Nueva atacama":
    st.title("Nueva atacama")
    if st.button("Mostrar boletas descargadas de Nueva atacama"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_nuevaatacama.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Nueva atacama\boletas_nuevaatacama.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Saesa":
    st.title("Saesa")
    if st.button("Mostrar boletas descargadas de Saesa"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_saesa.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Saesa\boletas_saesa.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Suralis":
    st.title("Suralis")
    if st.button("Mostrar boletas descargadas de Suralis"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_suralis.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Suralis\boletas_suralis.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Saesa2":
    st.title("Saesa2")
    if st.button("Mostrar boletas descargadas de Saesa2"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_saesa2.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Saesa2\boletas_saesa2.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")

elif app_mode == "Aguas decimas":
    st.title("Aguas decimas")
    if st.button("Mostrar boletas descargadas de Aguas decimas"):
        result = subprocess.run([python_interpreter, "extraccion\extractor_aguasdecimas.py"], capture_output=True, text=True)
        if result.stderr:
            st.text_area("Errores", result.stderr)
        try:
            excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas decimas\boletas_aguasdecimas.xlsx")
            if os.path.exists(excel_path):
                st.button("Mostrar excel", on_click=lambda: os.startfile(excel_path))
            else:
                st.error("El archivo Excel no se encontró.")
            df = pd.read_excel(excel_path)
            AgGrid(df)
        except Exception as e:
            st.error(f"Error al leer el archivo Excel o el archivo no fue encontrado: {e}")