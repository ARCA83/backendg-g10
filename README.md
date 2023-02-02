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
En `url.py`

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    ...
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
```


