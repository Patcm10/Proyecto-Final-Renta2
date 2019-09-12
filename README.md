# Proyecto-Final-Renta2

Proyecto final del bootcamp en Data Analytics 2019

PROBLEMA:

- La revisión de las páginas de renta de departamentos es un tarea muy ardua como consecuencia del número de registros por página -en donde en algunos casos llegan a 100 páginas o más-. Y en un contexto en donde las personas disponen de poco tiempo, se vuelve una tarea tediosa.

SOLUCIÓN:

- Este proyecto funciona a través de la respuesta a 3 preguntas (rango de precios de renta, número de personas que habitarán el departamento y lugar de trabajo o estudios(ubicación de usuario)). Su principal objetivo es filtrar (haciendo web scrapping) -de las principales paginas de rentas de bienes inmuebles - las mejores opciones de renta de acuerdo a lo respondido en las preguntas y lo más importante, visualizar las respuestas a través de un mapa (creado con folium y geolocalizaciones) en donde se muestren markers con las mejores opciones.

- Hacer más eficiente la búsqueda de departamentos en la CDMX.

POBLACIÓN OBJETIVO:

- Personas que por razones laborales o académicas busquen opciones de renta en la CDMX.

PASOS REALIZADOS:

1) Primero fue una tarea de búqueda de páginas para hacer el web scrapping, mis primeros intentos fueron fallidos debido a que la seguridad de las páginas detectaron que estaba haciendo esta tarea y me mandaron Captchas. Por esta razón fue necesario seguir buscando, hasta encontrar páginas amigables. Para mi sopresa encontré una muy bien diseñada de la que fue muy sencillo la información a través de loops.

2) El siguiente paso consistió en limpiar los datos obtenidos utilizando diversas herramientas como Regex, con los datos limpios se creó el archivo Web-Scrapping-Proyecto Final.csv.

3) Después de la limpieza (data cleaning), me di cuenta que para poder realizar mi objetivo de mapear necesitaba las coordendas y por esta razón se creo un Data Frame denominado Address con la dirección de las viviendas, sin embargo, no tenían coordenadas. Por esta razón, fue necesario encontrar alguna herramienta qye me ayudara a convertir direcciones en coordenadas y por ello utilicé la API de google maps llamada Geocode y posteriormente hice el archivo Address.csv.

4) Al obtener las coordenadas pude utilizar la libreria de folium para comprobar que las coordenadas obtenidas podían mapear las direcciones recabadas. En este paso se crearon dos archivos "html", en el primero se mapearon todas las viviendas en rentas de la CDMX, mientras que en el segundo se mapeó en un HeatMap la concentración de la mayor oferta de rentas en la CDMX.

5) El archivo final fue un borrador para comenzar a jugar con los inputs y su concatenación con los mapas.

6) Finalmente, en el archivo Final_Final se crearon las funciones para filtrar los departamentos por los criterios de rango de precios, número de habitantes y ubicación del usuario y asimismo en donde se creó el mapa_final en donde se puede observar los resultados arrojados de la aplicación.

CONCLUSIÓN:

Desde un principio se tenía el objetivo definido, si bien fue un reto realizar el web scrapping se obtuvieron y limpiaron los datos. Uno de los mayores retos fue convertir la direcciones en coordenadas pero era la única manera de mapear los resultados. Asimismo, aprender como funcionaba la API de Google Maps fue difícil. Sin embargo, lo más complicado se presentó al realizar la función que recibiera inputs y que filtrara la información de los Data Frame pero que al mismo tiempo mapeara los resultados. Por último, considero que es un proyecto muy interesante y que aún tien mucho camino por delante, por tal motivo, seguiré desarrollándolo para que sea un producto que se pueda utilizar y facilitar la vida de miles de personas que buscan ofertas de renta en la CDMX.

