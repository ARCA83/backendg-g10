from django.urls import path
from .views import CategoriaApiView

urlpatterns=[
    #cuando se acceda a la ruta /categorias/ se mandara a llamar a la funcionalidad de nuestro CategoriaApiView
    path('categorias/', CategoriaApiView.as_view())
]