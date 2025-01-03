# Lector de Facturas Locales

Esta aplicación permite listar y visualizar las facturas descargadas en tu entorno local a través de una interfaz web.

## Requisitos

*   Python 3.11 o posterior.
*   Sistema operativo Windows.
*   Debe tener acceso al OneDrive con las carpetas "Digitalización de facturas (Agua) - Banco Estado" y "Digitalización de facturas (Electricidad) - Banco Estado" de Rodae

## Instalación

1.  **Descarga:** Descarga la última versión disponible desde las [Releases](ENLACE_A_LAS_RELEASES_DE_GITHUB).
2.  **Descompresión:** Descomprime el archivo descargado en la ubicación deseada.
3.  **Instalación de dependencias y creación del entorno virtual:**
    *   Navega a la carpeta de la aplicación desde el explorador de archivos.
    *   Ejecuta el archivo `install.bat`. Este script se encargará de:
        *   Crear un entorno virtual Python.
        *   Instalar las dependencias necesarias listadas en `requirements.txt`.
        *   Iniciar la aplicación.
    *   Es posible que Windows muestre una alerta de seguridad al ejecutar el `.bat` por primera vez. Haz clic en "Más información" y luego en "Ejecutar de todas formas".

## Uso

Una vez finalizada la instalación, la aplicación se abrirá automáticamente en tu navegador web predeterminado.

*   **Cerrar la aplicación:** Para cerrar la aplicación, simplemente cierra la pestaña del navegador y la ventana de la terminal.
*   **Reiniciar la aplicación:** Para volver a iniciar la aplicación, ejecuta el archivo `start.bat` que se encuentra en la carpeta de la aplicación.

# Funcionamiento

La interfaz de la aplicación es sencilla e intuitiva. A continuación, se describen las principales funcionalidades con capturas de pantalla:

## Pantalla de Inicio:
<div align="center">
  <img src="https://i.ibb.co/qJ3jstQ/Captura-de-pantalla-2025-01-03-102542.png" alt="Pantalla de inicio" width="600" height="300">
</div>


*   **Botón "Mostrar boletas descargadas de...":** Al hacer clic en este botón, se muestra una tabla con las boletas descargadas para la empresa seleccionada.

## Pantalla con las boletas mostradas:

<div align="center">
  <img src="https://i.ibb.co/YhtRGkw/Captura-de-pantalla-2025-01-03-103215.png" alt="Tabla" width="600" height="400">
</div>

*   **Selector de empresa (a la izquierda):** Permite seleccionar la empresa de la cual se desean ver las boletas.
*   **Tabla de boletas:** Muestra las boletas descargadas con la siguiente información:
    *   Nombre del archivo.
    *   Número de cliente.
    *   Número de boleta.
*   **Botón "Mostrar excel":** Genera y abre un archivo Excel con la lista de boletas descargadas para la empresa seleccionada.

## Solución de problemas

### Instalación manual de dependencias

Si el archivo `install.bat` no funciona correctamente, puedes instalar las dependencias manualmente siguiendo estos pasos:

1.  **Abre la carpeta del proyecto:** Abre la carpeta de la aplicación con Visual Studio Code o abre una terminal en la misma carpeta.
2.  **Crea el entorno virtual:** Ejecuta el siguiente comando en la terminal:

    ```bash
    python -m venv env
    ```

3.  **Activa el entorno virtual:** Ejecuta el siguiente comando en la terminal:

    ```bash
    env/Scripts/activate
    ```

4.  **Instala las dependencias:** Ejecuta el siguiente comando en la terminal:

    ```bash
    pip install -r requirements.txt
    ```

### Inicio manual de la aplicación

Si el archivo `start.bat` no funciona, puedes iniciar la aplicación manualmente ejecutando el siguiente comando en la terminal (asegúrate de tener el entorno virtual activado):

```bash
python -m streamlit run index.py
