# sistDist1

https://github.com/tomasrasymas/flask-restful-api-template/blob/master/app.py

# Tarea 3 BDDA

## Integrantes
- Lester Carrasco.
- Miguel Contreras.
- Nicolás Poza.

## Tecnologias 
En el presente proyecto se desea hacer un buscador para el cual se utilizaron las siguientes tecnologias: 

- Flask - es un microframework para Python para crear WebApps
- Redis - motor de base de datos desarrollado por Amazon, que cumple la funcion de cache.
- [gRPC] - es un sistema de tipo RPC open source desarrollado por google, que utiliza como transporte HTTP/3 y Protocol Buffers como lenguaje de descripcion de interfaz.
- [JSON] - formato de texto sencillo para el intercambio de datos. 
- [visual Studio Code] - Editor de texto desarrollado por Microsoft 

## Referencias
-[Flask] - [https://github.com/tomasrasymas/flask-restful-api-template/blob/master/app.py]
-[gRPC] - [https://github.com/yerkortiz/distributed-systems-notes/blob/main/grpc/example2/client.py]

## Dependencias
- [Flask] -
```sh
pip install FLask
```
- Redis -
```sh

```
- Docker -
```sh
sudo apt install p
```
## Ejecucion
```sh
docker run --name some-redis -d -p 6379:6379 redis
```
```sh
git clone https://github.com/Darthzner/sistDist1.git
```
```sh
cd sistDist1
python3 index.py 
```
## Servicio
Un vez corriendo el servidor y el contenedor de redis ejecutamos la siguiente consulta:
```sh
curl http://localhost:5000/api/getprod
```
