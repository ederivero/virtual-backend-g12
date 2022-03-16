from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
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
        # registramos un nuevo ingrediente
        try:
            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre = 'Leche evaporada'
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
                'message': 'Hubo un error al crear el ingrediente',
                'content': e.args[0]
            }