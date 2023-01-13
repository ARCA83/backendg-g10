from flask_restful import Resource, request
from configuracion import conexion
from models.categoria_model import Categoria
from dtos.categoria_dto import CategoriaDto
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError

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
        data = request.get_json()
        print (data)
        serializador = CategoriaDto()
        try:
            #loas > valida el diccionario que cumpla todas las caracteristicas de columnas de nuestro modelo y nos devolvera un diccionario con la informacion necesaria
            resultado=serializador.load(data)
            print (resultado)
            #Inicializamos nuestra nueva categoria PERO aun no la guardamos
            nuevaCategoria=Categoria(nombre = resultado.get('nombre'))
            #agregamos este nuevo elemento en la base de datos
            conexion.session.add(nuevaCategoria)
            #indicamos que se guarde de manera permanente
            conexion.session.commit()

            return{
                'message':'Categoria creada exitosamente'
            }
        except IntegrityError as error_integridad:
            #Aca se ingresara si al momento de guardar la categoria, esta ya existe(porque el nombre es unico)
            return {
                'message': 'Error al crear la categoria, esa categoria ya existe',
                
            }    
        except ValidationError as error_validacion:
            # Aca se ingresara cuando nos de un error de la validacion del DTO
            return {
                'message': 'Error al crear la categoria, vea el content',
                'content': error_validacion.args
            }
        except Exception as error:
            # Aca se ingresara si el error que no cumple  con los anteriores 
            return {
                'message': 'Error al crear la categoria',
                'content': error.args #aqui es donde almacenan todos los mensaje de error
            }

class CategoriaController(Resource):
    def get(self, id):
        print(id)
        # SELECT * FROM categorias WHERE id = ... LIMIT 1;
        # first > no me devuelve una lista (arreglo) sino me devuelve solo una instancia o None si es que no hay
        # all > me devolver una lista con todas las coincidencias 
        categoria = conexion.session.query(Categoria).filter_by(id= id).first()
        print(categoria)

        # TODO: convertir esta categoria para mostrar en el content, Si es que la categoria no existe (None) indicar que la categoria no existe en el 'message'
        return {
            'content': ''
        }