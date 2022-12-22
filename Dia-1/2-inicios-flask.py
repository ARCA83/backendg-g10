from flask import Flask
# si el archivo es el archivo principal del proyecto su valor de la varible __name__ ser '__main__' caso contrario sera None(vacio)
app = Flask(__name__)
#patron de diseño de software (Singleton)

#un decorador se usa con el '@'sirve para modificar cierto metodo de una clase sin la necesidad de modificar el funcionamiento natural(modificacion parcial) luego de utilizar el decorador se crea una funcion que sera la nueva funcionabilidad de ese metodo.
@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'

@app.route('/mostrar-hora', methods=['GET','POST'])
def mostrarHora():
    #no se suele retornar strings (caden de texto) sino que se utiliza diccionarios
    return{
        'content': '22:50:15'
    }

#debug = cada vez que modifica mos algun archivo  del proyecto y guardamos, se reiniciara el servidor
app.run(debug=True)