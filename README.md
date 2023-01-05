# JurassicPark_Grupo2

Grupo2: Álvaro Gutiérrez, Aitor Matilla, Naroa Jauregi y Ainhoa Jauregiberri.

Python, FastAPI, MySQL, Docker

## Incialización

- ### Backend

1. Crear la imagen de la API a través de los archivos [build.bat](build.bat) (Windows) o [build.sh](build.sh) (MacOS/Linux).
2. Ejecutar `docker-compose up -d` para inicializar el stack de contenedores para la API y la BD (junto a Adminer).
3. Ejecutar los archivos [restore.bat](db\Windows\restore.bat) (Windows) o [restore.sh](db\MacOS\restore.sh) (MacOS/Linux) para inicializar los datos de la BD. **IMPORTANTE: Ejecutar desde sus propios directorios**

- ### Frontend

1. Para incializar el frontend en el puerto **8081**, ejecutar `npm run serve` desde el directorio [frontend](frontend).
