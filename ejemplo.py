"""En este ejemplo se descargan 5 MDE pertenecientes al IGN."""

# Librerias requeridas

import requests
import zipfile

# Función

def save_file(url, archivo_nombre):
  r= requests.get(url)
  with open(archivo_nombre, 'wb') as f:
    f.write(r.content)

# Lista URL

lista=["https://dnsg.ign.gob.ar/apps/mapas-geodesia/mde_mapa_geoserver_descarga.php?pid=7&gid=ad7d5579886790888642b9b5970945ba",
"https://dnsg.ign.gob.ar/apps/mapas-geodesia/mde_mapa_geoserver_descarga.php?pid=7&gid=3d50a7e7af3f1de5a5d710e51f90a5e7",
"https://dnsg.ign.gob.ar/apps/mapas-geodesia/mde_mapa_geoserver_descarga.php?pid=7&gid=4926f59ecce5c1a5cf8e9a0af16370be",
"https://dnsg.ign.gob.ar/apps/mapas-geodesia/mde_mapa_geoserver_descarga.php?pid=7&gid=9d2c1b2eaf872abfb0115902e14861ad",
"https://dnsg.ign.gob.ar/apps/mapas-geodesia/mde_mapa_geoserver_descarga.php?pid=7&gid=f4c552efcd971e86a70695e555dddd2e"]

# Bucle a través de cada raster en la lista

for i in lista:
  save_file(i,'mde.zip')
  with zipfile.ZipFile("mde.zip", "r") as zip_ref:
    zip_ref.extractall()
