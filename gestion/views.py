from rest_framework.generics import ListCreateAPIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
#List > Listar(get)
#Create > Crear(post)

class CategoriaApiView(ListCreateAPIView):
    # al utiliza una vista generica que ya no es necesario definir el comportamiento para cuando se get o post
    #queryset> el comando que utilizar para llamar a la informcion de nuestra base de datos
    #SELECT * FROM categorias
    queryset =CategoriaModel.objects.all()
    #serializer_class > se define una clase que se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamo hacia el cliene en datos legibles
    serializer_class =CategoriaSerializer
    # ya no es necesario definir los metodos 'get' y 'post'
    #def get(self):
    #    pass
#
    #def post(self):
    #    pass