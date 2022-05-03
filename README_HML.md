# PRUEBA BACKEND 
## Realizada por Humberto montes de Oca <humbertoha18@gmail.com>

Prueba solicitada por parte de worky -- zentric
Productos utilizado
- Docker
- Django app
- React
- Postgresql


## docker-compose file
```yaml
version: '3'

services:
  db:
    image: postgres
    env_file:
      - ./.envs/.postgres
    ports:
      - "5432:5432"
    volumes:
      - /opt/postgres-data:/var/lib/postgresql/data
    networks:
      - db-net
  django:
    build: ./api
    command: python manage.py runserver 0.0.0.0:8000
    env_file:
      - ./.envs/.postgres
    volumes:
      - ./api:/app/api
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - db-net
  frontend:
    restart: always
    build: ./frontend
    environment:
      - CHOKIDAR_USEPOLLING=true
    command: npm start
    volumes:
      - ./frontend:/app/frontend
    ports:
      - "3000:3000"
    depends_on:
      - django
    networks:
      - db-net
networks:
  db-net:
    driver: bridge
```
## Requerimientos

Esta prueba se construyo con docker-compose se necesita que este instalado 
enlace de descarga en 
windows 
https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
linux
Consulta la instalacion de tu distribucion

## Para empezar
```sh
git clone https://gitlab.com/luis.iriberri.buenfil/pruebas-back-end.git
cd pruebas-back-end
docker-compose up -d --build
```
## Django app
http://127.0.0.1:8000

admin 
http://127.0.0.1:8000
usuario : admin 
contraseña : "F\vN6`mq#%4<R2m

## React app
http://127.0.0.1:3000