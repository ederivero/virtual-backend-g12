from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO, RecetaResponseDTO, BuscarRecetaRequestDto
from config import conexion

# CREATE, GET ALL (PAGINATED), UPDATE, FIND por like de nombre, DELETE
class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            # creamos la instancia de la nueva receta PERO no la agregamos a la base de datos
            nuevaReceta = Receta(
                nombre = data.get('nombre'), 
                estado = data.get('estado'), 
                comensales=data.get('comensales'), 
                duracion=data.get('duracion'), 
                dificultad = data.get('dificultad') 
                )
            conexion.session.add(nuevaReceta)
            # https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.commit
            # recien al hacer commit asignara el id correspondiente
            conexion.session.commit()
            respuesta = RecetaResponseDTO().dump(nuevaReceta)

            return {
                'message': 'Receta creada exitosamente',
                'content': respuesta
            }, 201

        except Exception as e:
            # https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session.rollback
            conexion.session.rollback()
            return {
                'message': 'Error al crear la receta',
                'content': e.args
            }
    
    def get(self):
        # TODO: agregar paginacion
        recetas = conexion.session.query(Receta).all()
        respuesta = RecetaResponseDTO(many=True).dump(recetas)
        return {
            'message': 'Las recetas son:',
            'content': respuesta
        }

class BuscarRecetaController(Resource):
    def get(self):
        query_params = request.args
        try:
            parametros = BuscarRecetaRequestDto().load(query_params)
            # si es que no me dan a buscar el nombre entonces hare la busqueda de todas las recetas
            # el filter a comparacion del filter_by se utiliza para comparar valores PERO utilizando su atributo de la clase y se usa doble igual
            # si queremos usar algun filtro especifico del orm (de la bd) entonces usaremos el atributo de la clase el cual nos devolvera metodos para hacer esa busqueda especifica
            recetas2 = conexion.session.query(Receta).filter(Receta.nombre == 'a', Receta.estado== True).all()

            nombre = parametros.get('nombre', '')
            # parametros = {'nombre': 'truji', 'dificultad': 'FACIL'}
            if parametros.get('nombre') is not None:
                del parametros['nombre']
            # parametros = {'dificultad': 'FACIL'}
            # hare la busqueda de todas las recetas y si me pasa el nombre hare una busqueda con su like y para las demas columnas hare la busqueda normal
            recetas = conexion.session.query(Receta).filter(Receta.nombre.like('%{}%'.format(nombre))).filter_by(**parametros).all()
            # (dificultad = 'FACIL', estado = True).all()
            # SELECT * FROM recetas WHERE nombre like '%truji%' AND dificultad = 'FACIL' AND estado = true;
            resultado = RecetaResponseDTO(many=True).dump(recetas)
            
            return {
                'message': '',
                'content': resultado
            }
        except Exception as e:
            return{
                'message': 'Error al hacer la busqueda',
                'content': e.args
            }, 400