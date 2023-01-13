from flask_restful import Resource
from configuracion import conexion
from models.categoria_model import Categoria
from dtos.categoria_dto import CategoriaDto

#ahora en esta clase podre utilizar los metodos HTTP (GET, POST, PUT, DELETE)como si fueses metodos de la clase
#https://docs.sqlalchemy.org/en/14/orm/query.html
class CategoriasController(Resource):
    def get(self):
        # SELECT * FROM categorias
        data=conexion.session.query(Categoria).all()
        print(data[0].nombre)

        #many= True > indicando que le vamos a pasar una lista de instancia y el DTO la tendra que iterar para poder convertir cada una de ellas    
        serializador = CategoriaDto(many=True)
        #dump > convierte la instancia de la clase a un diccionario
        resultado=serializador.dump(data    )
        return {
            
            'content' : resultado
        }
    def post(self):
        return{
            'message':'Me hiciste post'
        }