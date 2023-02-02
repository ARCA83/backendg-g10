## Crear el entorno virtual
```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
deactivate
```
## Instalar Django
```
pip install Django
pip freeze > requirements.txt
```
## Crear nuestro proyecto
```
django-admin startproject django_intro(nombre proyecto)
2(cd django_intro/)
python manage.py runserver
```
## Migrar los modelos
```
python manage.py makemigrations
python manage.py migrate
```
## Crear superuser
```
python manage.py createsuperuser
```
## Crear aplicacion(app)
```
python manage.py startapp almacen(nombre app)
```
## Registramos nuestra app en INSTALLED_APPS `settings.py`

```python
INSTALLED_ADDS =[
    ...,
    'almacen'
]
```
## Crear nuestro nuevo modelo y migrar
```
python manage.py makemigrations
python manage.py migrate
```
## Installar Django Rest Framework
```
pip install djangorestframework
```
## Registramos nuestra app en INSTALLED_APPS `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
 ## Documentar nuestra API CON Swagger y Redoc
 ```
 pip install drf-yasg

 ```
## Configurar la libreria
```python
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```



