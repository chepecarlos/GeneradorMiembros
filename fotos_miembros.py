#!/usr/bin/env python3
import os
import re
import subprocess
import pandas as pd
import requests
import shutil
from datetime import datetime

#Generador lista mienbros
#comando = "manim -qh -t miembros.py"
comando = "cd /home/Nocheprogramacion/CosasChepe/Videos/GeneradorMiembros/ && manim -qh -t miembros.py"

# Guarda la ruta original de ejecución
ruta_original = os.environ.get('PWD')
print(ruta_original)
input("Presiona cualquier tecla para finalizar el programa...")
directorio_deseado = "/home/Nocheprogramacion/CosasChepe/Videos/GeneradorMiembros"
os.chdir(directorio_deseado)

def cargarData(archivo):
    if not os.path.exists(archivo):
        print(f"No se encontrol {archivo}")
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
        
# Obtener la opción del usuario
while True:
    opcion = input("Ingrese 'S' para general el indice o 'N' para cerrar el programa: ").upper()
    
    if opcion == 'S':
        print("Espera para la genercaion del video.")
        subprocess.run(comando, shell=True)

        # Ruta y Nombre donde se genera el video
        archivo_a_mover = '/home/Nocheprogramacion/CosasChepe/Videos/GeneradorMiembros/media/videos/miembros/1080p60/miembros.mov'
        #print("Ruta del video")
        #input("Presiona cualquier tecla para finalizar el programa...")
        
        #Cambia al directorio donde se encuentra el archivo
        os.chdir(os.path.dirname(archivo_a_mover))
        #print("Detro de ruta del video")
        #input("Presiona cualquier tecla para finalizar el programa...")

        # Regresa a la ruta original de ejecución
        os.chdir(ruta_original)

        # Obtiene la fecha actual y la formatea como texto
        fecha_actual = datetime.now().strftime("%Y-%m-%d")  # Puedes personalizar el formato de fecha según tus necesidades

        # Obtiene la extensión del archivo
        nombre_base, extension = os.path.splitext(os.path.basename(archivo_a_mover))

        # Combina la ruta original con el nombre base, la fecha actual y la extensión
        nuevo_nombre = f"{nombre_base}_{fecha_actual}{extension}"
        nueva_ruta = os.path.join(ruta_original, nuevo_nombre)

        shutil.move(archivo_a_mover, nueva_ruta)

        break
    elif opcion == 'N':
        input("Presiona cualquier tecla para finalizar el programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
exit()