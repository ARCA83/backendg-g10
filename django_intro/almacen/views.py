from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel, CategoriasModel
from .serializers import ProductosSerializer, CategoriasSerializer
from rest_framework import generics
from rest_framework.response import Response

def renderHtml(request):
    return HttpResponse("<button>Dame click</button>")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    return HttpResponse(f'El producto encontrado se llama {producto.nombre} y el precio es: {producto.precio}')

class ProductosView(generics.ListCreateAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer
#https://www.django-rest-framework.org/api-guide/views/
class CategoriasView(generics.GenericAPIView):
    queryset = CategoriasModel.objects.all()
    serializer_class = CategoriasSerializer

    def get(self, request):
        try:
            record = self.get_queryset()
            serializer= self.get_serializer(record, many=True)  
            return Response(serializer.data)
        except:
            return Response({
                'message' : 'Internal server error'
            })
        
    def post(self, request):
        try:
            categoria = self.get_serializer(data=request.data)
            if categoria.is_valid():
                categoria.save( )
                print(categoria.data)
                return Response (categoria.data)
            return Response({
                'message':'Transaccion exitosa'
            })
        except:
            return Response({
                'message' : 'Internal server error'
            })