# Librerias requeridas

import requests
import zipfile

# Función

def save_file(url, archivo_nombre):
  r= requests.get(url)
  with open(archivo_nombre, 'wb') as f:
    f.write(r.content)

# Lista URL

lista=[<URL1>, <URL2>, <URL3>, <...>]

# Bucle a través de cada raster en la lista

for i in lista:
  save_file(i,'mde.zip')
  with zipfile.ZipFile("mde.zip", "r") as zip_ref:
    zip_ref.extractall()
