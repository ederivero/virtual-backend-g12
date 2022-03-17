from config import validador
from models.ingredientes import Ingrediente

class IngredienteRequestDTO(validador.SQLAlchemyAutoSchema):
    # al nosotros heredar de SQLAlchemyAutoSchema estamos indicando que usaremos un modelo como mapeo de los atributos necesarios para hacer la validacion de nuestra informacion
    class Meta:
        model = Ingrediente