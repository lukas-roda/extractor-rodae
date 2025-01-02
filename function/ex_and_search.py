import fitz 
import re
import os
import pandas as pd
import function.upload_to_onedrive as uto


data = []

def extract_information(pdf_path):
    text = ''
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text


def search_in_text(pdf_directory, patron_boleta, patron_cliente, nombre_archivo, excel_path):
    countador = 0
    data = []
    for archivo in os.listdir(pdf_directory):
        try:
            numero_boleta = None
            numero_cliente = None
            countador += 1
            archivo_path = os.path.join(pdf_directory, archivo)
            texto_extraido = extract_information(archivo_path)
            resutado_boleta = re.search(patron_boleta, texto_extraido)
            print("boleta numero: ", countador)
            print("Nombre del archivo: ", archivo)
            if resutado_boleta:
                numero_boleta = resutado_boleta.group(1) or resutado_boleta.group(2)
                print(f"Número de boleta: {numero_boleta}")
            else:
                numero_boleta = "No encontrado"
                print(f"No se encontró un número de boleta en el archivo.------------------------------------------------")

        
            resultado_cliente = re.search(patron_cliente,texto_extraido, re.DOTALL)
            if resultado_cliente:
                numero_cliente = resultado_cliente.group(1) or resultado_cliente.group(2) or resultado_cliente.group(3)
                print(f"Número de cliente encontrado:", numero_cliente)
            else:
                numero_cliente = "No encontrado"
                print(f"No se encontró el número de cliente--------------------------------------------")
            
            
            
            data.append([archivo, numero_boleta, numero_cliente])
            
            print("\n")
        except Exception as e:

            print(f"Error al procesar el archivo {archivo}: {e}")
            continue

    print(data)
    df = pd.DataFrame(data, columns=["Nombre del archivo", "Número de boleta", "Número de cliente"])
    try:
            
        df = pd.DataFrame(data, columns=["Nombre del archivo", "Número de boleta", "Número de cliente"])
        df.to_excel(os.path.join(pdf_directory, nombre_archivo), index=False)
        print("Fin de la iteracion, archivo guardado en", excel_path)
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")









