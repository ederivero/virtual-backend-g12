from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO
from config import conexion
from models.recetas import Receta

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            # load > valida un diccionario a los parametros definidos en el DTO y retorna un diccionario
            data = PreparacionRequestDTO().load(body)
            print(data)
            nuevaPreparacion = Preparacion(**data)
            conexion.session.add(nuevaPreparacion)
            conexion.session.commit()
            # dump > convierte una instancia a un diccionario
            respuesta = PreparacionResponseDTO().dump(nuevaPreparacion)
            return {
                'message': 'Preparacion creada exitosamente',
                'preparacion': respuesta
            }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Hubo un error al crear la preparacion',
                'content': e.args
            }, 400
    
    def get(self):
        preparacion: Preparacion | None = conexion.session.query(Preparacion).filter_by(id=1).first()
        print(preparacion)
        print(preparacion.orden)
        # ahora desde la preparacion podemos ingresar mediante su relationship al registro al cual pertenece esta preparacion y luego a los atributos de esa tabla (modelo)
        print(preparacion.receta.nombre)
        # mientras que la columna Foreign key solamente nos devolvera un numero que sera el id de la otra tabla (modelo)
        
        print(preparacion.receta_id) # solamente el id de la clase receta, es un numero!
        return {
            'message': 'ok'
        }
