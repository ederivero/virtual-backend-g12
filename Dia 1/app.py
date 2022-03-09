from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

clientes = [
    {
        "nombre": "Eduardo",
        "pais": "PERU",
        "edad": 29,
        "id":1,
        "organos": True,
        "casado": False
    }
]

@app.route('/')
def estado():
    hora_del_servidor = datetime.now()

    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S')
    }

@app.route("/clientes", methods=['POST', 'GET'])
def obtener_clientes():
    # solamente puede ser llamado en cada controlador (funcion que se ejecutara cuando se realice una peticion desde el front)
    print(request.method)
    # request.method > mostrara el tipo de metodo al cual esta haciendo la consulta el front
    print(request.get_json())
    # request.get_json() > devolvera la informacion enviada por el body y la convertira a un diccionario para que python lo pueda entender y manipular
    if request.method == 'POST':
        # ingresara cuando el metodo sea POST
        data = request.get_json()
        # data > agregar una llave llamada id que sera la longitud de la lista actual + 1
        data['id'] = len(clientes) + 1
        # data.get('id') > no sirve para cuestiones de asignacion 
        clientes.append(data)

        return {
            'message': 'Cliente agregado exitosamente',
            'client': data
        }
    else:
        # elif request.method == 'GET':
        # ingresara cuando el metodo sea GET
        return {
            'message': 'La lista de clientes',
            'clients': clientes
        }

                        # 
@app.route('/cliente/<int:id>', methods=['GET'])
def gestion_usuario(id):
    print(id)
    # iterar la lista y buscaremos el cliente por ese id y si no existe imprimir un mensaje
    return {
        'id': id
    }



# debug > si esta habilitado (True) se reiniciara automaticamente el servidor cada vez que guardemos cambios en cualquier archivo
# port > indicara que puerto queremos utilizar, por defecto es el 5000
app.run(debug=True, port=8080)