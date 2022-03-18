from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba, ValidarUsuarioPrueba
from dtos.ingrediente_dto import IngredienteRequestDTO, IngredienteResponseDTO
from marshmallow.exceptions import ValidationError

# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase
class IngredientesController(Resource):
    def get(self):
        # vamos a crear una sesion en la cual ejecutaremos una query
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        # si nosotros queremos convertir la informacion pero es mas de una colocar many=True y con esto el DTO lo que hara sera iterar cada una de los items y lo serializara al valor correcto
        ingredientesSerializados = IngredienteResponseDTO(many=True).dump(resultado)
        return {
            'message':'Yo soy el get de los ingredientes',
            'content': ingredientesSerializados
        }

    def post(self):
        print(request.get_json())

        data = request.get_json()
        # registramos un nuevo ingrediente
        try:
            data_serializada = IngredienteRequestDTO().load(data)
            # Validara que la data que el usuario me esta enviando cumpla con todos las caracteristicas de mi modelo (que sea un string, que no sea muy largo (mas de 45) )
            print(data_serializada)
            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre = data_serializada.get('nombre')
            # ahora guardo la informacion en la base de datos
            conexion.session.add(nuevoIngrediente)
            # add >  estamos creando una nueva transaccion
            # commit > sirve para guardar los cambios de manera permanente en la bd
            conexion.session.commit()
            ingredienteSerializado = IngredienteResponseDTO().dump(nuevoIngrediente)

            return {
                'message': 'Ingrediente creado exitosamente',
                'ingrediente': ingredienteSerializado
            }, 201 # created ( creado )
            
        except ValidationError as e:
            return {
                'message': 'La informacion es incorrecta',
                'content': e.args
            }, 400 # Bad request ( mala solicitud )

        except Exception as e:
            
            print(e.args[0])
            # si hubo algun error al momento de hacer alguna modificacion a la bd entonces 'retrocederemos' todas esas modificaciones y lo dejaremos sin ningun cambio
            conexion.session.rollback()
            return {
                'message': 'Hubo un error al crear el ingrediente, el ingrediente ya existe',
                'content': e.args[0]
            }, 500 # internal server error (error interno del servidor)

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

class IngredienteController(Resource):
    def get(self, id):
        # filter_by > tenemos que indicar dentro de ese metodo las columnas que queremos usar para hacer el filtro con su respectivo valor
        # el parametro sera el nombre del atributo definido en el modelo y el segundo sera el valor
        # SELECT TOP 1 * FROM ingredientes WHERE id= $id
        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        print(ingrediente)

        if ingrediente:
            # mando a llamar a mi DTO de respuesta del ingrediente
            resultado = IngredienteResponseDTO().dump(ingrediente)
            return {
                'result': resultado
            }
        else:
            return {
                'message': 'El ingrediente a buscar no existe'
            }, 404
    
    def put(self, id):
        ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
        try:
            if ingrediente:
                body = request.get_json()
                # validamos la data enviada por el usuario para que cumpla con lo definido en el DTO
                data_validada = IngredienteRequestDTO().load(body)
                # al ya validar nuestro ingrediente y que este exista procedemos a modificar sus columnas (solo seria nombre) con el nuevo valor enviado por el usuario previamente ya validado
                ingrediente.nombre = data_validada.get('nombre')
                # solamente hacemos un commit ya que no estamos agregando nuevos valores a la base de datos 
                conexion.session.commit()
                # Usando el DTO de response pasar el ingrediente y que me devuelva su informacion para agregarla en el content de la respuesta
                resultado = IngredienteResponseDTO().dump(ingrediente)
                return {
                    'message': 'Ingrediente actualizado exitosamente',
                    'content': resultado
                }
            # que pasa si el ingrediente no existe O si la data es incorrecta ? solucionar esos errores
            else:
                return {
                    'message': 'Ingrediente a actualizar no existe'
                }, 404
        except Exception as e:
            return {
                'message': 'Error al actualizar el ingrediente',
                'content': e.args
            }, 400