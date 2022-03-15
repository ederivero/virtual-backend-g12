from flask_restful import Resource, request

# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase
class IngredientesController(Resource):
    def get(self):
        return {
            'message':'Yo soy el get de los ingredientes'
        }

    def post(self):
        print(request.get_json())
        return {
            'message': 'Yo soy el post'
        }