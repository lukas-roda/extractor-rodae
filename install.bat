@echo off
if exist env\Scripts\activate (
    echo Entorno virtual de python ya esta creado
    echo Iniciando aplicacion...
    python -m streamlit run index.py
) else (

    echo Iniciando instalacion...
    REM This script installs the required packages for the project
    echo Creando entorno virtual de python...
    python -m venv env
    echo Entorno creado con exitos
    echo Activando entorno...
    call env\Scripts\activate
    echo Entorno activado
    echo Instalando requerimientos...
    python -m pip install -r requirements.txt
    echo Requerimientos instalados
    echo Instalacion completa, iniciando aplicacion...
    python -m streamlit run index.py
)   