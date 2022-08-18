# Booking app

## Iniciar los servicio
```bash
# export COMPOSE_FILE=docker-compose.local.yml

# Construir las imágenes
docker-compose COMPOSE_FILE=docker-compose.local.yml build

# Iniciar los contenedores
docker-compose COMPOSE_FILE=docker-compose.local.yml up -d

# Detener los contenedores
docker-compose COMPOSE_FILE=docker-compose.local.yml down
```
