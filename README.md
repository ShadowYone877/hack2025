# APP projectUGT


## Funcionalidades del project UG

El projectUGT a desarrollar tendrá las siguientes características:

* Existirán n tipos de usuario: supersuser, admin e invitados.
* Un usuario administrador puede añadir, modificar y eliminar usuarios de menor nivel de rol.
* Un usuario administrador puede crear, modificar, eliminar y listar usuarios, además de poder 
asignarles el rol de administrador.

## Stack




## Descarga e instalación del proyecto

Para descargar el proyecto puedes clonar el repositorio:

    git clone https://github.com/
    
    branch git: master, dev, hotfix

### Variables de entorno

Para que el projectUGT funcione debes crear las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP=entrypoint
    export FLASK_ENV="development"

#### Windows

    set "FLASK_APP=main.py"
    set "FLASK_ENV=development"
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv
 
### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno y descargado las dependencias,
puedes arrancar el proyecto ejecutando:

    flask run
