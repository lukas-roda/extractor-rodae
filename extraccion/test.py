import os
import fitz

pdf_path = r"C:\Users\LukasOrellanaFarías\OneDrive - RODA ENERGIA\Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas araucania\RE76215637-7T033F0001113912GEN20241231T123312.pdf"
def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

print(extract_information(pdf_path))