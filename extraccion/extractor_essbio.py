import fitz 
import re
import os
import pandas as pd
import upload_to_onedrive as uto

pdf_directory = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Essbio")
excel_path = os.path.join(uto.ONEDRIVE_PATH, r"Digitalización de facturas (Agua) - Banco Estado\Facturas a procesar\Essbio\boletas_essbio.xlsx")


patron_boleta = r"N[°º]\s*(\d+)" 
patron_cliente = r"(?:Servicio\s*:\s*|Su\s*número\s*de\s*servicio\s*es\s*)(\d+-\w+)"
countador = 0

data = []

def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text



for archivo in os.listdir(pdf_directory):
    try:
        countador += 1
        archivo_path = os.path.join(pdf_directory, archivo)
        texto_extraido = extract_information(archivo_path)
        resutado_boleta = re.search(patron_boleta, texto_extraido)
        print("boleta numero: ", countador)
        print("Nombre del archivo: ", archivo)
        if resutado_boleta:
            numero_boleta = resutado_boleta.group(1)
            print(f"Número de boleta: {numero_boleta}")
        else:
            print(f"No se encontró un número de boleta en el archivo.------------------------------------------------")

        
        resultado_cliente = re.search(patron_cliente,texto_extraido, re.DOTALL)
        if resultado_cliente:
            numero_cliente = resultado_cliente.group(1)
            print(f"Número de cliente encontrado:", numero_cliente)
        else:
            numero_cliente = None
            print(f"No se encontró el número de cliente--------------------------------------------")
        
        
        
        data.append([archivo, numero_boleta, numero_cliente])
        print("\n")
    except Exception as e:

        
        print(f"Error al procesar el archivo {archivo}: {e}")
        continue

print(data)

#data frame
df = pd.DataFrame(data, columns=["Nombre del archivo", "Número de boleta", "Número de cliente"])


try:
    nombre_archivo = "boletas_essbio.xlsx"
    df.to_excel(os.path.join(pdf_directory, nombre_archivo),index=False)
    print("Fin de la iteracion, archivo guardado en", excel_path)
except Exception as e:
    print(f"Error al guardar el archivo Excel: {e}")






