import os
import re

import pandas as pd
import requests


def cargarData(archivo):
    if not os.path.exists(archivo):
        print(f"No se control {archivo}")
        return None
    data = pd.read_csv(archivo)
    return data

urlMiembros = cargarData("miembros.csv")

nombre_carpeta = "fotos_miembros"
ruta_carpeta = os.path.join(os.getcwd(), nombre_carpeta)

try:
    os.mkdir(ruta_carpeta)
    print(f"Carpeta {nombre_carpeta} creada exitosamente en {ruta_carpeta}")
except OSError as error:
    print("Folder ya existe")

for url, nombre in zip(urlMiembros["Vínculo al perfil"], urlMiembros["Miembro"]):
    print()
    print(f"{nombre} - {url}")
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        html = content.decode('utf-8')
    else:
        print("No se pudo obtener el contenido de la página.") 
        continue

    patron = r'https://yt3.googleusercontent.com/ytc/(.+?)"'

    resultado = re.search(patron, html)

    if resultado:
        Youtube_id = resultado.group(1)
        base = 'https://yt3.googleusercontent.com/ytc/'
        imgPerfil = base + Youtube_id
        print(f"url: {imgPerfil}")
    else:
        print("No se encontró el texto.")
        continue

    response = requests.get(imgPerfil)

    if response.status_code == 200:
        nombrejpg = f"{nombre_carpeta}/{nombre}.jpg"
        with open(nombrejpg, "wb") as f:
            f.write(response.content)
        print("La imagen se ha guardado exitosamente.")
    else:
        print("No se pudo descargar la imagen.")
