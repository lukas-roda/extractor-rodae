import os
import fitz

pdf_path = r"C:\Users\LukasOrellanaFarías\OneDrive - RODA ENERGIA\Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\factura_1295128 - 1295128.pdf"

def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

print(extract_information(pdf_path))