from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba, ValidarUsuarioPrueba
from dtos.ingrediente_dto import IngredienteRequestDTO

# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase
class IngredientesController(Resource):
    def get(self):
        # vamos a crear una sesion en la cual ejecutaremos una query
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        return {
            'message':'Yo soy el get de los ingredientes',
            'content': {
                'id': resultado[0].id,
                'nombre': resultado[0].nombre
            }
        }

    def post(self):
        print(request.get_json())

        data = request.get_json()
        # registramos un nuevo ingrediente
        try:
            # Validara que la data que el usuario me esta enviando cumpla con todos las caracteristicas de mi modelo (que sea un string, que no sea muy largo (mas de 45) )
            data_serializada = IngredienteRequestDTO().load(data)
            print(data_serializada)
            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre = data_serializada.get('nombre')
            # ahora guardo la informacion en la base de datos
            conexion.session.add(nuevoIngrediente)
            # add >  estamos creando una nueva transaccion
            # commit > sirve para guardar los cambios de manera permanente en la bd
            conexion.session.commit()

            return {
                'message': 'Ingrediente creado exitosamente'
            }

        except Exception as e:
            print(e.args[0])
            # si hubo algun error al momento de hacer alguna modificacion a la bd entonces 'retrocederemos' todas esas modificaciones y lo dejaremos sin ningun cambio
            conexion.session.rollback()
            return {
                'message': 'Hubo un error al crear el ingrediente, el ingrediente ya existe',
                'content': e.args[0]
            }

class PruebaController(Resource):

    def post(self):
        try:
            data = request.get_json()
            validacion = ValidadorPrueba().load(data)
            # https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#module-marshmallow.validate
            # validacionLongitud = validate.Length(max=10)
            # validacionLongitud(validacion.get('nombre'))
            # si todo fue exitoso y las validaciones pasaron bien entonces nos devolvera un diccionario con todos las llaves con sus valores
            print(validacion)
            return {
                'message': 'ok',
                'data': validacion
            }
        except Exception as e:
            print(e.args)
            return {
                'message': 'error al recibir los datos',
                'content': e.args
            }

    def get(self):
        usuario = {
            'nombre': 'Eduardo',
            'apellido': 'Manrique',
            'nacionalidad': 'Peru',
            'password': 'Mimamamemima123'
        }
        resultado = ValidarUsuarioPrueba().dump(usuario)
        return {
            'message': 'El usuario es',
            'content': usuario,
            'resultado': resultado
        }

