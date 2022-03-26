from flask_restful import Resource, request
from dtos.registro_dto import RegistroDTO


class RegistroController(Resource):
    def post(self):
        # me da todo el body convertido en un diccionario
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            return {
                'message': 'Usuario registrado exitosamente'
            }, 201

        except Exception as e:
            return {
                'message': 'Error al registrar al usuario',
                'content': e.args
            }, 400
