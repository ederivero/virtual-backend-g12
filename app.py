from flask import Flask, render_template
from flask_jwt import JWT
from flask_restful import Api
from controllers.usuarios import LoginController, RegistroController
from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from seguridad import autenticador, identificador


load_dotenv()

app = Flask(__name__)

CORS(app=app)

app.config['SECRET_KEY'] = 'secreto'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


jsonwebtoken = JWT(app=app, authentication_handler=autenticador,
                   identity_handler=identificador)


api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)


@app.route('/')
def inicio():
    # render_template > renderiza un archivo .html o .jinja para q flask lo pueda leer e interpretar al cliente
    return render_template('inicio.jinja', nombre='Eduardo', dia='Jueves', integrantes=[
        'Foca',
        'Lapagol',
        'Ruidiaz',
        'Paolin',
        'Rayo Advincula'
    ], usuario={
        'nombre': 'Juan',
        'direccion': 'Las piedritas 105',
        'edad': '40'
    }, selecciones=[{
        'nombre': 'Bolivia',
        'clasificado': False
    }, {
        'nombre': 'Brasil',
        'clasificado': True
    }, {
        'nombre': 'Chile',
        'clasificado': False
    }, {
        'nombre': 'Peru',
        'timado': True
    }])


api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if(__name__ == '__main__'):
    app.run(debug=True, port=8080)
