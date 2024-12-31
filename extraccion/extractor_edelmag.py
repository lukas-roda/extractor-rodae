import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import function.upload_to_onedrive as uto
from function.ex_and_search import *
import re

pdf_directory = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Edelmag")
excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Edelmag\boletas_edelmag.xlsx")
patron_boleta = r"N[°º]\s*(\d+)" 
patron_cliente = r"N° Cliente\s*\n\s*Fecha de vencimiento\s*\n\s*(\d+)"
nombre_archivo = "boletas_edelmag.xlsx"

search_in_text(pdf_directory, patron_boleta, patron_cliente, nombre_archivo, excel_path)