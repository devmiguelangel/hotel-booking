FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # MariaDB dependencies
  && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    mariadb-client \
  && apt-get install -y wget vim netcat

RUN pip install --upgrade pip
COPY ./api/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./compose/api/start.sh /start
RUN chmod +x /start

WORKDIR /api
