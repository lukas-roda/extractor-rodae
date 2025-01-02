@echo off
echo Iniciando aplicacion...
if exist env\Scripts\activate (
    call env\Scripts\activate
    python -m streamlit run index.py
) else (
    echo No se ha encontrado la ruta env\Scripts\activate, recuerda ejecutar install.bat antes de start.bat o crear entorno virtual de python con "python -m venv env"
)
pause