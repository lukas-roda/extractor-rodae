import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import function.upload_to_onedrive as uto
from function.ex_and_search import *
import re

pdf_directory = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas andinas")
excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas andinasboletas_aguasandinas.xlsx")
patron_boleta = r"N[°º]\s*(\d{5,9})" 
patron_cliente = r"\bNro de cuenta\b.*?\b(\d+-[0-9Kk])\b"
nombre_archivo = "boletas_aguasandinas.xlsx"

search_in_text(pdf_directory, patron_boleta, patron_cliente, nombre_archivo, excel_path)