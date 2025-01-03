import os
import fitz

pdf_path = r"C:\Users\LukasOrellanaFarías\OneDrive - RODA ENERGIA\Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Aguas decimas\RE96703230-1T033F0000256835GEN20250102T050103.pdf"
def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

print(extract_information(pdf_path))