from flask import Flask, request
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
# si solamente mandamos a llamar a la clase y le pasamos la instancia de la clase Flask creara los permisos para que todos puedan acceder (Allowed-Origin), para que cualquier metodo pueda ser consultado (Allowed-Method) y para cualquier header (Allowed-Header)
# origin > '*' indicar que origenes pueden consumir mi API
# methods > ['GET','POST','PUT','DELETE','PATCH'] siempre se podra acceder al GET pero si indicamos que solamente un metodo puede ser accedido entonces solo se podra consultar el GET y ese metodo definido
# allow_headers > '*' indicar que cabeceran pueden ser enviadas a mi API
# Content-Type es un header que indicara que tipo de contenido estamos enviando , cuando enviemos un json su valor sera 'application/json' , cuando enviemos un xml 'application/xml' o cuando enviemos un archivo binario sera el formato de ese archivo 'image/jpeg'
CORS(app=app, origins=['http://127.0.0.1:5500','https://www.mifrontend.com','https://miapp.vercel.app'], methods='*', allow_headers=['Content-Type'])

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

def buscar_usuario(id):
    # iterar la lista y buscaremos el cliente por ese id y si no existe imprimir un mensaje
    # v1
    # for cliente in clientes:
    #     if cliente.get('id') == id:
    #         return cliente
    # v2
    for posicion in range(0, len(clientes)):
        cliente = clientes[posicion]
        if cliente.get('id') == id:
            return ( cliente, posicion )

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


@app.route('/cliente/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_usuario(id):
    print(id)
    if request.method == 'GET':
        usuario = buscar_usuario(id)
        if usuario:
            return usuario[0]
        else:
            return {
                'message': 'el usuario a buscar no se encontro'
            }, 404

    elif request.method == 'PUT':
        resultado = buscar_usuario(id)
        if resultado is not None: 
            # hacemos la destructuracion de nuestra tupla creando las variables cliente y posicion
            [cliente, posicion] = resultado

            # cliente = resultado[0] 
            # posicion = resultado[1] 

            # modificar el cliente
            # extraemos la informacion del body y la almacenamos en una variable
            data = request.get_json()
            # en ese diccionario agregaremos una llave 'id' y almacenaremos el id del cliente que esta en la posicion 0 de la tupla del cliente encontrado
            data['id'] = id
            # extraeremos la posicion del cliente devuelta en la posicion 1 de la tupla de buscar_cliente
            # posicion = resultado[1]
            # modificar ese cliente con el nuevo valor
            clientes[posicion] = data
            return clientes[posicion]
        else:
            return {
                'message': 'El cliente a modificar no se encontro'
            }, 404
    elif request.method == 'DELETE': # else:
        # eliminar ese cliente luego de validar si existe o no usando el metodo validar_usuario(id) si no existe indicar lo mismo 'cliente a eliminar no se encontro'
        resultado = buscar_usuario(id)
        if resultado:
            [cliente, posicion] = resultado
            cliente_eliminado = clientes.pop(posicion)
            return {
                'message': 'Cliente eliminado exitosamente',
                'cliente': cliente_eliminado
            }
        else:
            return {
                'message': 'El cliente a eliminar no se encontro'
            }, 404


# debug > si esta habilitado (True) se reiniciara automaticamente el servidor cada vez que guardemos cambios en cualquier archivo
# port > indicara que puerto queremos utilizar, por defecto es el 5000
app.run(debug=True, port=8080)