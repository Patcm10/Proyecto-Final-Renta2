
# Se instala esta extensión para poder utilizar las APIS de google maps

#pip install python-google-places


# Importar librerias


import pandas as pd
import os
from dotenv import load_dotenv
import googlemaps
from geopy import distance
import folium
import numpy as np
import urllib.request
import json
import requests
from googleplaces import GooglePlaces, types, lang


# Importar CSV con la lista de rentas de departamentos como resultado del web scrapping


data = pd.read_csv('lista_final.csv',sep='|')


#Con esto se carga una función para esconder la API key de google maps


load_dotenv()


# Así se obtiene la API KEY para que no se vea la llave


API_key=os.getenv('API')


# Se llama la API KEY de google maps


gmaps_key = googlemaps.Client(key=API_key)


# Se llama la API KEY de google places


google_places = GooglePlaces(API_key)


# Función para utilizar google geocode


def get_coord(string):
    geocode_result = gmaps_key.geocode(string)
    try:
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        return [lat,lon]
    except:
        return [None,None]


# función para conseguir coordenadas de la geolocalización que estamos haciendo


def get_distance(pointx, pointy):
    return distance.distance(pointx,pointy)


# Se comprueba que la función funciona y nos da como resultado coordenadas (latitud y longitud)


get_distance([-39, 99], [-40, 98])


# Esta URL nos sirve para utilizar la API de google SEARCH PLACES


url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/output?parameters"


# Con esta función ponemos los criterios a través de los cuales filtraremos nuestros resulatdos (Rango de precios, Número Habitantes y  Ubicaciñon).


def rentas():
    rango_precios = {'1':'5000-10000','2':'10000-15000','3':'15000-20000','4':'20000-25000','5':'25000-30000','6':'30000-35000','7':'35000-40000','8':'40000-45000','9':'45000-50000','10':'>50000'}
    dummy = data.copy()
    
    indice_precios = rango_precios[input(f'Selecciona un rango de precios: {str(rango_precios)}')].split('-')
    
    dummy = dummy[dummy['Price(MX$)'].between(int(indice_precios[0]), int(indice_precios[1]))]
    
    indice_hab = int(input((f'Selecciona número de habitantes: ')))
    dummy = dummy[dummy['Bedrooms'] == indice_hab]

    coord_trab = input(f'¿Cuál es tu ubicacion? : ')

    ubicacion = get_coord(coord_trab)
    dummy['Distance'] = dummy['Coordinates'].str.split(',').apply(                        lambda x:get_distance(x, ubicacion))
    
    #hobby = input(f'¿Cuál es tu hobby? : ')
    
    dummy = dummy[dummy['Distance']<=5]
    
    dummy['Phone Number'] = np.random.randint(100000000, 10000000000, dummy.shape[0])
    
    dummy.drop_duplicates(subset='Address', inplace=True)
    
    return  dummy, ubicacion


# Con esto probamos la función


test, ubi = rentas()


# Ubi nos da las coordendaas de nuestra ubicación


ubi


# test es el data frame con los resultados de nuetros criterios filtrados


test


# All_places es una lista vacía en donde almacenaremos los resultados de obtenidos de la API google places


all_places = []


# Este loop nos ayuda a buscar restaurantes cercanos a los resultados de los departamentos más cercanos a nuestra ubicación


for address in test.Address:
    query_result = google_places.nearby_search(
    location= address, keyword='Restaurants',
    radius=1000, types=[types.TYPE_RESTAURANT])
    all_places= all_places+query_result.places


# Probamos all_places


all_places

# Convertimos en un Data Frame los resultados obtenidos


pd.DataFrame(query_result.places)


# Dentro de los resultado obtenidos buscamos ordenar la información y sobre todo, obtener la latitud y longitud para poder mapear


places = {('place'+ str(v)): [all_places[v].name,all_places[v]._geo_location['lat'],all_places[v]._geo_location['lng']] for v in range(len(all_places))}


# Convertimos nuestros datos ordenados en un Data Frame y trasponemos la filas y columnas


places = pd.DataFrame(places).T


# Comprobamos que funcione places


places


# Comprobamos que conseguimos las coordenadas 


query_result.places[0]._geo_location

# Ordenamos nuestro Data Frame de test con base en la distancia para que nos de la ubicaciónn más cercana a nuestra ubicación


test.sort_values(by='Distance').head(10)


# Aquí utilizamos folium para mapear con todos los criterios y Data Frames que utilizamos para conseguir y filtrar la información de las mejores opciones de departamentos en renta en la CDMX y los restaurantes más cercanos a ellos


mapa2 = folium.Map(
    location=ubi,
    zoom_start=12,
    tiles='openstreetmap')
tooltip = 'Click me!'


for index, row in test.sort_values(by='Distance').head(10).iterrows():
    folium.Marker([row['Latitud'], row['Longitud']], 
                  radius=500,
                  popup=row[['Address','Bedrooms','Price(MX$)','Bathrooms','Phone Number']],
                  icon=folium.Icon(color='purple',icon='home')
                 ).add_to(mapa2)
    
folium.Marker(ubi, icon=folium.Icon(color='green',icon='home')).add_to(mapa2)
  
for index, row in places.iterrows():
    folium.Marker([row.iloc[1], row.iloc[2]],                 
    radius=500,  
    popup=row[0],              
    icon=folium.Icon(color='blue',icon='info-sign')).add_to(mapa2)

mapa2
