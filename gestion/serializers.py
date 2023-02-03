from rest_framework import serializers
from .models import CategoriaModel

class CategoriaSerializer(serializers.ModelSerializer):
    #cuando utilizamos un serializador basandonos en un modelo se declara la clase Meta
    class Meta:
        #se encargar en mapear todos los modelos del atributo del modelo para concordar el tipo de dato y sus especificaciones
        model = CategoriaModel
        #fields > sirve para indicar que columnas de esa tabla queremos trabajar, si queremos todas la columnas entonces definiremos el valor "__all__" caso contrario lo podremos manejar en un arreglo con los nombres de las columnas
        fields='__all__'
        #fields = ['id','nombre']
        #si queremos excluir una minima cantidad de columnas para no trabajarlas entonces usaremos
        # exclude =['id']

        #NOTA nose puede trabajar con el exclude y el fields a la vez, o es uno o es el otro