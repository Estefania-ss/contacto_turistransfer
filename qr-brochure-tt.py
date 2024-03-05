import qrcode
import requests
from PIL import Image
from io import BytesIO

# Función para superponer la imagen del logo en el centro del código QR
def superponer_logo(archivo_qr, archivo_logo):
    # Abrir el código QR generado
    qr = Image.open(archivo_qr)
    # Abrir la imagen del logo
    logo = Image.open(archivo_logo)
    # Obtener las dimensiones del código QR
    ancho_qr, alto_qr = qr.size
    # Escalar el logo para que tenga un tamaño adecuado en el centro del código QR
    factor_escala = 4
    tamaño_logo = (ancho_qr // factor_escala, alto_qr // factor_escala)
    logo = logo.resize(tamaño_logo)
    # Calcular la posición donde se colocará el logo
    posicion = ((ancho_qr - tamaño_logo[0]) // 2, (alto_qr - tamaño_logo[1]) // 2)
    # Superponer el logo en el código QR
    qr.paste(logo, posicion)
    return qr

# Función para descargar el archivo desde Google Drive
def descargar_archivo(desde_enlace, a_archivo):
    id_archivo = desde_enlace.split("/")[5]
    enlace_descarga = "https://drive.google.com/uc?id=" + id_archivo
    respuesta = requests.get(enlace_descarga)
    with open(a_archivo, "wb") as archivo:
        archivo.write(respuesta.content)

# Generar el código QR con el enlace al PDF
enlace_pdf = "https://drive.google.com/file/d/19sVjnZO3w3CjQb65kbrh7D8B7uTgOwww/view?usp=sharing"
qr = qrcode.make(enlace_pdf, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10)
qr.save("codigo_qr.png")  # Guardar el código QR en un archivo de imagen

# Descargar el logo desde Google Drive
enlace_logo = "https://drive.google.com/file/d/1vmeKB6Y7Z379TmyIui15VhQUcTyyo1il/view?usp=sharing"
archivo_logo = "logo.png"
descargar_archivo(enlace_logo, archivo_logo)

# Superponer el logo en el código QR
qr_con_logo = superponer_logo("codigo_qr.png", archivo_logo)

# Guardar el código QR con el logo
qr_con_logo.save("qr-brochure-Tt.png")
