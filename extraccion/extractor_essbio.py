import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import function.upload_to_onedrive as uto
from function.ex_and_search import *

pdf_directory = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Essbio")
excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Essbio\boletas_essbio.xlsx")
patron_boleta = r"N[°º]\s*(\d+)" 
patron_cliente = r"(?:Servicio\s*:\s*|Su\s*número\s*de\s*servicio\s*es\s*)(\d+-\w+)"
nombre_archivo = "boletas_essbio.xlsx"

search_in_text(pdf_directory, patron_boleta, patron_cliente, nombre_archivo, excel_path)