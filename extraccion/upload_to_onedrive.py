import os

def get_onedrive_path():
    # Verifica si la variable de entorno OneDrive existe en el sistema
    onedrive_path = os.getenv('OneDrive')

    if onedrive_path:
        return onedrive_path
    else:
        # Si la variable de entorno no está definida, intenta encontrar la ruta de OneDrive de forma predeterminada
        default_onedrive_path = os.path.join(os.getenv('USERPROFILE'), 'OneDrive')
        if os.path.exists(default_onedrive_path):
            return default_onedrive_path
        else:
            # Si no se encuentra ninguna ruta válida, retorna None
            return None

# Obtén la ruta de OneDrive
ONEDRIVE_PATH = get_onedrive_path()

if ONEDRIVE_PATH:
    print("La ruta de OneDrive es:", ONEDRIVE_PATH)
else:
    print("No se pudo encontrar la ruta de OneDrive en este sistema.")

