from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PreparacionRequestDTO().load(body)
            print(data)

            return {
                'message': 'Preparacion creada exitosamente'
            }, 201

        except Exception as e:
            return {
                'message': 'Hubo un error al crear la preparacion',
                'content': e.args
            }, 400
