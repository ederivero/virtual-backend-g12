from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import (  IngredientesController, 
                                        PruebaController, 
                                        IngredienteController )
from controllers.recetas import (   RecetasController, 
                                    BuscarRecetaController, 
                                    RecetaController )
from controllers.preparaciones import PreparacionesController
from controllers.ingredientes_recetas import IngredientesRecetasController
from config import conexion, validador
from dotenv import load_dotenv
from os import environ

# carga todas las variables definidas en el archivo .env para que sean tratadas como variables de entorno sin la necesidad de agregarlas al servidor o maquina.
load_dotenv()

app = Flask(__name__)
# Creamos la instancia de flask_restful.Api y le indicamos que toda la configuracion que haremos se agrege a nuestra instancia de Flask
api = Api(app=app)

# aca se almacenaran todas las variables de configuracion de mi proyecto Flask, en ella se podran encontrar algunas variables como DEBUG y ENV , entre otras
# app.config > es un diccionario en el cual se almaceran las variables por LLAVE: Valor 
# print(app.config)

# Ahora asignaremos la cadena de conexion a nuestra base de datos
#                                       tipo://usuario:password@dominio:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] =environ.get('DATABASE_URL')
# Si se establece True entonces SQLALCHEMY rastreara las modificaciones de los objectos (modelos) y emitira señales cuando cambie algun modelo, su valor por defecto es None
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# para jalar la configuracion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)

# para jalar la configuracion de mi flask y poder agregar la validacion a nuestro proyecto
validador.init_app(app)

# con el siguiente comando indicaremos la creacion de todas las tablas en la bd
# emitira un error si es que no hay ninguna tabla a crear 
# emitira un error si no le hemos instalado el conector correctamente
# tenemos que declarar en el parametro app nuestra aplicacion de flask
conexion.create_all(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {
        'status': True,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
def inicio():
    return 'Bienvenido a mi API de recetas'


# Ahora definimos las rutas que van a ser utilizadas con un determinado controlador
api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')
api.add_resource(PruebaController, '/pruebas')
api.add_resource(IngredienteController, '/ingrediente/<int:id>')
api.add_resource(RecetasController, '/recetas', '/receta')
api.add_resource(BuscarRecetaController, '/buscar_receta')
api.add_resource(PreparacionesController, '/preparacion')
api.add_resource(RecetaController, '/receta/<int:id>')
api.add_resource(IngredientesRecetasController, '/ingrediente_receta')

# comprobara que la instancia de la clase Flask se este ejecutando en el archivo principal del proyecto, esto se usa para no crear multiples instancias y generar un posible error de Flask 
if __name__ == '__main__':
    app.run(debug=True)
