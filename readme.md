# Proyecto Final

+ Alumno: Gabriel Reyes
+ Curso: Python
+ Comisión: 55350
+ Año: 2023


## Descripción de proyecto
El proyecto final consistía en desarrollar una una aplicación web estilo blog programada en Python y Django. 
Para su creación se utilizaron todos los conceptos trabajados en el curso. Se crearon 3 módulos (app_blog, app_perfiles, app_contacto3), creación de formularios utilizando la API form de Django, modalidad de herencias para las plantillas, el uso del framework Bootstrap para el estilizado de las plantillas html, e integración con PostgreSQL para la base de datos.


## Requisitos

- python 3.11.4
- Django 4.2.3
- django-ckeditor 6.7.0
- django-js-asset 2.1.0
- Pillow 10.0.0
- psycopg2 2.9.7


## Instrucciones y requisitos instalar el proyecto

+ Crea una carpeta contenedora madre.
+ Abre la consola y ubicate en la carpeta madre.
+ Clona este repositorio a tu máquina local en la carpeta madre.

```
git clone
```
+ Entra en la carpeta que acabas de clonar.
+ Instala las las dependencias:
```
pip install -r requirements.txt
```
+ Aplica las migraciones: 
```
python manage.py migrate
```
+ Crea un superusuario: 
```
python manage.py createsuperuser
```
+ Inicia el servidor:
```
python manage.py runserver
```


## Funcionalidades de web

La web ademas de contar con una "Home" inicial, una página "Acerca de mi", una página "Contacto" para dejar conultas y sugerencias, nos permite acceder a una lista de articulos creados para su lectura (Blog)

También, nos permite el registro de usuarios por medio de un formulario accediendo a la posibilidad de crear, editar y eliminar articulos (creados por el propio usuario), con un editor de texto avanzado y añadir incluso imagenes. 


## Instrucciones acceder al panel aministrativo de Django

+ Acceder a la url:
```
127.0.0.1:8000/admin
```

+ Ingresar con los datos del superusuario:

username: admin

contraseña: Super_2023