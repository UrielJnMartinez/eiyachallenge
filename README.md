# eiyachallenge
_Prueba t茅cnica para Backend Developer en Eiya._


### Pre-requisitos 馃搵

_Para poder correr el proyecto es necesario tener instalado lo siguiente:_


* [Docker](https://www.docker.com/get-started) 
* [Docker Compose](https://docs.docker.com/compose/install/) 

### Clonar el proyecto 鈱笍

_Para clonar el proyecto:_
```
git clone https://github.com/UrielJnMartinez/eiyachallenge.git

cd eiyachallenge/
```

### Ejecucion del proyecto 馃敡


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
Se desea conocer la ubicaci贸n de una flota de veh铆culos en 3 ciudades distintas.

Para ello se plantea realizar una aplicaci贸n en Django donde se pueda visualizar una pantalla donde se vean las ciudades en cuesti贸n y los veh铆culos que se encuentran en ellas.

A la par, se plantea tener una api rest en la aplicaci贸n donde se pueden administrar los veh铆culos. De esta manera:
- Se puede crear, editar o eliminar los veh铆culos de la flota.
- Se puede listar los veh铆culos y su estado actual
- Se puede dar la instrucci贸n de que un veh铆culo viaje a una ciudad determinada

Un veh铆culo tiene la siguiente informaci贸n
- ID de Veh铆culo
- Ubicaci贸n actual
- Consumo de combustible (km/lt)
- Distancia recorrida
- Combustible consumido

Las ciudades tienen la siguiente distancia entre s铆:

                Ciudad A, Ciudad B,  Ciudad C
    Ciudad A       0 ,        1    ,     2
    Ciudad B         ,        0    ,     4
    Ciudad C         ,             ,     0

_Al dar la instrucci贸n de que un veh铆culo viaje a una ciudad se debe de actualizar su informaci贸n. En particular sus atributos de distancia recorrida y combustible consumido._