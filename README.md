# eiyachallenge
_Prueba técnica para Backend Developer en Eiya._


### Pre-requisitos 📋

_Para poder correr el proyecto es necesario tener instalado lo siguiente:_


* [Docker](https://www.docker.com/get-started) 
* [Docker Compose](https://docs.docker.com/compose/install/) 

### Clonar el proyecto ⌨️

_Para clonar el proyecto:_
```
git clone https://github.com/UrielJnMartinez/eiyachallenge.git

cd eiyachallenge/
```

### Ejecucion del proyecto 🔧


    Copiar el formato de example.env y darle valor a las variables de entorno, renombrando el archivo a .env


_En el directorio del proyecto eiyachallange/ correr el siguiente comando para construir la imagen del proyecto._

```
docker-compose build
```

_Despues para crear todo el entorno de desarrollo y la base de datos ejecutar el siguiente comando_

```
docker-compose up
```

#

# Proyecto 
## Administrador de flota
Se desea conocer la ubicación de una flota de vehículos en 3 ciudades distintas.

Para ello se plantea realizar una aplicación en Django donde se pueda visualizar una pantalla donde se vean las ciudades en cuestión y los vehículos que se encuentran en ellas.

A la par, se plantea tener una api rest en la aplicación donde se pueden administrar los vehículos. De esta manera:
- Se puede crear, editar o eliminar los vehículos de la flota.
- Se puede listar los vehículos y su estado actual
- Se puede dar la instrucción de que un vehículo viaje a una ciudad determinada

Un vehículo tiene la siguiente información
- ID de Vehículo
- Ubicación actual
- Consumo de combustible (km/lt)
- Distancia recorrida
- Combustible consumido

Las ciudades tienen la siguiente distancia entre sí:

                Ciudad A, Ciudad B,  Ciudad C
    Ciudad A       0 ,        1    ,     2
    Ciudad B         ,        0    ,     4
    Ciudad C         ,             ,     0

_Al dar la instrucción de que un vehículo viaje a una ciudad se debe de actualizar su información. En particular sus atributos de distancia recorrida y combustible consumido._