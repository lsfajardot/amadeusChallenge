import pandas as pd
import gzip
import numpy as np
import matplotlib.pyplot as plt
# Ruta del archivo CSV comprimido en formato .csv.gz
airports_file = '/Users/luigifajardo/Desktop/empresasPruebas/amadeus/optd-airports-sample.csv.gz'
users_file = '/Users/luigifajardo/Desktop/empresasPruebas/amadeus/user-geo-sample.csv.gz'
# Abrir el archivo CSV comprimido y leerlo en un DataFrame
with gzip.open(airports_file, 'rt') as archivo:
    airports = pd.read_csv(archivo)
with gzip.open(users_file, 'rt') as archivo:
    users = pd.read_csv(archivo)
#Agregar etiqueta de centros a los aeropuertos
airports['centros'] = range(1, len(airports) + 1)
#Para la prueba inicial se usara solo el 10% de la data para comprobar funcionalidad
long = 0.001
long_centers = int(round(len(airports)*long, 0))
long_data = int(round(len(users)*long, 0))
users = users.head(long_data)
airports = airports.head(long_centers)
#Se toman solamente las columnas del analisis
centers = airports[['latitude', 'longitude']]
data = users[['geoip_latitude', 'geoip_longitude']]
def distancia_euclidiana(punto1, punto2):
    return np.sqrt(np.sum((punto1 - punto2) ** 2))

array_centers = centers[['latitude', 'longitude']].values
array_data = data[['geoip_latitude', 'geoip_longitude']].values
etiquetas = []
contador = 1
for punto in array_data:
    distancias_a_centros = [distancia_euclidiana(punto, centro) for centro in array_centers]
    etiqueta = np.argmin(distancias_a_centros)
    etiquetas.append(etiqueta)
    print(contador)
    contador += 1
users['Etiquetas'] = etiquetas
out_users = pd.merge(airports, users, left_on='centros', right_on='Etiquetas', how='inner')
out_users = out_users[['uuid', 'iata_code']]
print(out_users)

