# Booking API

API para la reserva de habitaciones en un hotel

## Construir e iniciar la aplicación

> ### Ejecutar los comandos en la raíz del proyecto

```bash
# Copiar y modificar el archivo app.env
cp ./compose/envs/api.env.example ./compose/envs/api.env

# Copiar y modificar el archivo db.env
cp ./compose/envs/db.env.example ./compose/envs/db.env

# export COMPOSE_FILE=docker-compose.local.yml

# Construir las imágenes
docker-compose -f docker-compose.local.yml build

# Iniciar los contenedores
docker-compose -f docker-compose.local.yml up -d

# Detener los contenedores
docker-compose -f docker-compose.local.yml down

# Aplicar las migraciones
docker exec -it booking_api python manage.py migrate

# Cargar datos de habitaciones de prueba
docker exec -it booking_api python manage.py loaddata apps/fixtures/rooms.json

# Crear un super usuario
docker exec -it booking_api python manage.py createsuperuser

# URL para acceder al administrador con el usuario de prueba

http://127.0.0.1:8000/admin
```

## Flujo para realizar una reserva

1. ### http://127.0.0.1:8000/api/rooms

Obtener una lista de habitaciones disponibles para que el cliente pueda elegir una o varias

METHOD: **GET**

2. ### http://127.0.0.1:8000/api/clients

Para realizar una reserva el cliente debe registrarse en la aplicación ingresando su información básica

METHOD: **POST**

3. ### http://127.0.0.1:8000/api/clients/{client_id}

De manera opcional el cliente puede editar los datos ingresados

METHOD: **PUT**

4. ### http://127.0.0.1:8000/api/bookings

Una ves que los datos del cliente fueron registrados se procede a registrar la información de la reserva

Detallando el rango de fechas,  la cantidad de personas y la cantidad de habitaciones con sus respectivas tarifas

METHOD: **POST**

5. ### http://127.0.0.1:8000/api/bookings/{booking_id}/cancel

La reserva en curso puede ser cancelada antes de efectuar el pago

METHOD: **PUT**

6. ### http://127.0.0.1:8000/api/bookings/{booking_id}/pay

La reserva se hace oficial una vez se que se efectúa el pago

Son necesarios los datos de facturación, el tipo de pago y el monto

METHOD: **PUT**

7. ### http://127.0.0.1:8000/api/rooms

Registrar habitaciones en la app (Opcional)

METHOD: **POST**

## Postman documentation

https://documenter.getpostman.com/view/21327328/VUqoQJ85

## Diagrama

<img src="./room _bookings.png" width="500" />
