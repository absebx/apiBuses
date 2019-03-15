
# AppBuses
Aplicación para manejar buses, trayectos, horarios, pasajeros y choferes

## Pre suposiciones 
La siguiente guía de instalacion presupone que existe una instalacion de python junto con pip y sus dependencias dentro del equipo.
Las dependencias de python necesarias básicas de las cuales se hace la pre suposicion son:
``` bash
pip install virtualenv
```


## Build Setup

``` bash
#Ejecutar comandos en la carpeta del proyecto.

# se recomienda usar Virtual Environments para no tener problemas con las dependencias locales
# en caso que no se quiera usar, pasar al punto 'instalar dependencias de python'

# crear virtual Environment en carpeta padre del proyecto
virtualenv ../vappBuses

#activar
#en caso que se creó en otra carpeta activar desde esa dirección
..\vappBuses\Scripts\activate

#instalar dependencias de python
pip install Django==2.1.7  
pip install django-cors-headers==2.5.0  
pip install djangorestframework==3.9.2  
pip install pytz==2018.9

#instalar dependencias de NPM
npm install --no-audit

#hacer build del front
npm run build

#correr proyecto
#por configuraciones con la API, el proyecto se tiene que ejecutar en puerto 8000
py .\manage.py runserver 8000

```

### Posibles problemas
Usar virtual Environments puede generar problemas en windows al activarlas.
Si al ejecutar el comando activate genera un error, puede que windows tenga bloqueada la ejecución de comandos no firmados, para eso se recomienda ejecutar el siguiente comando como adminsitrador en la consola de windows:

``` bash
Set-ExecutionPolicy Unrestricted
```
Si el comando no se ejecuta correctamente, puede que necesite ponerse en contacto con un administrador del sistema para habilitarlo.


## Estado de cumplimiento de requerimientos
Debido a diversas circunstancias técnicas y temporales, no se pudieron completar a cabalidad los requerimientos, el estado se explica a continuación:

- EL crud tanto en el BACKEND como en el FRONT está completo, pero faltan validaciones de tiempo y de cantidad de pasajeros en cada bus.
- Para las funciones especiales se pudo terminar el segundo del enunciado, quedando en la ruta de laa api = 'apiBuses/busesMayorCero/11'
- Por dificultades técnicas el primer requerimiento especial para el enunciado no se pudo terminar para la fecha extra programada, pero de igual forma se pudo acercar mucho a la solución, este acercamiento quedó en la vista especial trayectosAvgPasajes en appBuses/views/viewCustoms.py, no se le asignó una ruta para para evitar errores.
- Para el sistema de horarios, la fecha debió estar dentro en los horarios de salida y entrada como un formato 'DATETIME', de esa manera no habría problemas con horas de llegada en días siguientes. Al encontrar ese error el sistema ya estaba en una etapa finalizada, por lo que se dió prioridad a entregar el requerimiento.

## Extras

El modelo de base de datos actualizado y final, utilizado para el proyecto, está en la siguiente ruta.

https://drive.google.com/open?id=18ProlTcZkwizywwdKnv9mZa_aNKQ6H51

el proyecto front está también, de manera separada en la siguiente ruta:

https://github.com/asder707/clientBuses


## Saludos finales
Se agradece la consideración para este proceso, ha sido muy entretenido aprender estas tecnologías, me hubiera gustado profundizar mucho mas en el tema de ORM, y backend en general, pero por temas de tiempo se tuve que priorizar un entregable.
Espero que estemos en contacto!

Saludos! 

Abner Sebick 🗼  🗾  🗻
