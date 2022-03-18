from config import validador
from models.recetas import Receta

# https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta