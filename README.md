# Booking app

## Challenge
> - Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.
> - Proponé los endpoints a crearse para tratar de cubrir el flujo normal de operación de reserva y explicar por qué. Luego que tengas ya todo el código
> - Crear un repositorio para la entrega del código y en un readme del repositorio la justificación de los endpoints creados tenemos 48 hrs para poder resolver el challenge
> - El proyecto debe correrse en un contenedor de docker, se puede usar cualquier gestor de base de datos relacionales
> - Adjuntar también un archivo con ejemplos de consumo de la API para Postman

## 1. Iniciar la aplicación

```bash
# export COMPOSE_FILE=docker-compose.local.yml

# Construir las imágenes
docker-compose COMPOSE_FILE=docker-compose.local.yml build

# Iniciar los contenedores
docker-compose COMPOSE_FILE=docker-compose.local.yml up -d

# Detener los contenedores
docker-compose COMPOSE_FILE=docker-compose.local.yml down
```

## Configurar la aplicación

```bash
# Aplicar las migraciones
docker exec -it booking_api python manage.py migrate

# Crear un super usuario
docker exec -it booking_api python manage.py createsuperuser

# URL para acceder al administrador

http://127.0.0.1:8000/admin
```
