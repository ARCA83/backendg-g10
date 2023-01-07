from flask import Flask, render_template
from os import environ
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <p>
    Hola desde el  backend
    </p> 
    <h1>
     Hola
     </h1> """

@app.route("/productos")
def productos():
    lista_productos = [
        {
            'id':1,
            'nombre':'coliflor',
            'precio': 5.8
        },
        {
            'id':1,
            'nombre':'pepino',
            'precio': 3
        },
        {
            'id':1,
            'nombre':'berenjen',
            'precio': 4
        },
        ]
    return render_template("listar-productos.html", nombre='Anthony', lista_productos=lista_productos)

app.run(debug=True)