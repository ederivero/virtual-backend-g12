from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import (   RecetaRequestDTO, 
                                RecetaResponseDTO, 
                                BuscarRecetaRequestDto,
                                RecetaPreparacionesResponseDTO)
from dtos.paginacion_dto import PaginacionRequestDTO
from config import conexion
from math import ceil

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
        # page > que pagina queremos
        # perPage
        query_params = request.args
        paginacion = PaginacionRequestDTO().load(query_params)
        perPage = paginacion.get('perPage')
        page= paginacion.get('page')

        if(perPage < 1 or page < 1):
            return {
                'message': 'Los parametros no pueden recibir valores negativos'
            }, 400

        skip = perPage * (page - 1)
        # page = 2 | perPage = 5
        recetas = conexion.session.query(Receta).limit(perPage).offset(skip).all()
        # SELECT COUNT(*) FROM recetas; > me da el total de registros que tengo en esa tabla
        total = conexion.session.query(Receta).count()
        # indica cuantos elementos por pagina vamos a tener, en el caso que se pida mas de lo que tengamos sera su valor total caso contrario sera el valor que se solicita
        # Helper de paginacion 
        itemsXPage = perPage if total >= perPage else total
        totalPages = ceil(total / itemsXPage) if itemsXPage > 0 else None
        prevPage = page - 1 if page > 1 and page <= totalPages else None
        nextPage = page + 1 if totalPages > 1 and page < totalPages else None
        
        respuesta = RecetaResponseDTO(many=True).dump(recetas)

        return {
            'message': 'Las recetas son:',
            'pagination':{
                'total': total,
                'itemsXPage':itemsXPage,
                'totalPages': totalPages,
                'prevPage': prevPage,
                'nextPage': nextPage
            },
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


class RecetaController(Resource):
    def get(self, id):
        # buscar la receta segun su id
        # https://docs.sqlalchemy.org/en/14/orm/query.html?highlight=filter_by#sqlalchemy.orm.Query.filter
        receta: Receta | None = conexion.session.query(Receta).filter(Receta.id == id).first()
        # si no hay la receta devolver un message: 'Receta no encontrada' con un estado NOT FOUND
        if receta is None:

            return{
                'message': 'Receta no encontrada'
            }, 404
        # si hay la receta devolver message : 'Receta encontrada' con un estado OK
        else:
            print(receta.preparaciones)
            respuesta = RecetaPreparacionesResponseDTO().dump(receta)
            return {
                'message': 'Receta encontrada',
                'content': respuesta
            }, 200
