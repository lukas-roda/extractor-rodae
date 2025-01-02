import os
import fitz

pdf_path = r"C:\Users\LukasOrellanaFarías\OneDrive - RODA ENERGIA\Digitalización de facturas (Electricidad) - Banco Estado\Facturas a procesar\Chilquinta\132367_111893123.pdf"
def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

print(extract_information(pdf_path))