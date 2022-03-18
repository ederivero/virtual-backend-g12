from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO, RecetaResponseDTO
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