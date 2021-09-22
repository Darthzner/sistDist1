# Tarea 1 Sistemas Distribuidos

## Integrantes
- Lester Carrasco.
- Miguel Contreras.
- Nicolás Poza.

## Tecnologías 
En el presente proyecto se desea hacer un buscador para el cual se utilizaron las siguientes tecnologías: 

- Flask - Es un microframework para Python para crear WebApps.
- Redis - Motor de base de datos desarrollado por Amazon, que cumple la función de cache.
- gRPC - Es un sistema de tipo RPC open source desarrollado por google, que utiliza como transporte HTTP/3 y Protocol Buffers como lenguaje de descripción de interfaz.
- JSON - Formato de texto sencillo para el intercambio de datos. 
- visual Studio Code - Editor de texto desarrollado por Microsoft 

## Referencias
- [Flask] - https://github.com/tomasrasymas/flask-restful-api-template/blob/master/app.py
- [gRPC] - https://github.com/yerkortiz/distributed-systems-notes/blob/main/grpc/example2/client.py

## Dependencias
- Flask 
```sh
pip install Flask
```
- gRPC
```sh
python -m pip install grpcio
python -m grpc_tools.protoc (protocol buffer) --proto_path=. ./search.proto --python_out=. --grpc_python_out=.
```
- Redis 
```sh
brew install redis (Para MacOS con homebrew).
Para linux descargar imagen
Para windows descargar .exe 
```
- Docker 
```sh
brew install docker (Para MacOS con homebrew)
```
## Ejecución
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
## Configuración redis 
La configuración de redis se hizo dentro del codigo index.py
```sh
if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.config_set('maxmemory', '100mb')
    r.config_set('maxmemory-policy', 'allkeys-lru')
```
