from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

clientes = []

@app.route('/')
def estado():
    hora_del_servidor = datetime.now()

    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S')
    }

@app.route("/clientes", methods=['POST'])
def obtener_clientes():
    # solamente puede ser llamado en cada controlador (funcion que se ejecutara cuando se realice una peticion desde el front)
    print(request.method)
    # request.method > mostrara el tipo de metodo al cual esta haciendo la consulta el front
    print(request.get_json())
    # request.get_json() > devolvera la informacion enviada por el body y la convertira a un diccionario para que python lo pueda entender y manipular
    data = request.get_json()
    clientes.append(data)
    data['nombre']

    return {
        'message': 'Cliente agregado exitosamente',
        'client': data
    }

# debug > si esta habilitado (True) se reiniciara automaticamente el servidor cada vez que guardemos cambios en cualquier archivo
# port > indicara que puerto queremos utilizar, por defecto es el 5000
app.run(debug=True, port=8080)