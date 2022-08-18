#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


while ! nc -z ${MARIADB_HOST} ${MARIADB_PORT}; do echo "Waiting for Database..." && sleep 1; done;

python manage.py runserver 0.0.0.0:8000
