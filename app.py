from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api

from models.categoria_model import Categoria
from models.productos_model import Producto
from models.categoria_producto_model import CategoriaProducto

from controllers.categoria_controller import CategoriasController, CategoriaController

#aca utilizaremos el archivo .env para agregarlo a las variables de entorno
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASE_URL')

#inicializamos nuestra clase Api
api = Api(app)

#inicializar la aplicacion de SQLAlchemy con nuestra aplicacion de flask
conexion.init_app(app)

# inicializamos la clase Migrate pasandole nuestra aplicacion de Flask y nuestra conexion a SQLAlchemy
Migrate(app, conexion)


#este controlador se ejecutara antes del primer REQUEST de nuestro servidor
@app.before_first_request
def inicializadora():
    #realizar la creacion de todos los modelos de nuestro proyecto como tablas en la base de datos
    #conexion.create_all()
    pass

api.add_resource(CategoriasController, '/categorias')
api.add_resource(CategoriaController, '/categoria/<int:id>')

if __name__ == '__main__':
    app.run(debug = True)