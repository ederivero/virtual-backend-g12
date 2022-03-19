from config import validador
from models.recetas import Receta
from marshmallow import fields, validate
# https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class BuscarRecetaRequestDto(validador.Schema):
    nombre = fields.String(required=False)
    estado = fields.Boolean(required=False)
    comensales = fields.Integer(required=False)
    dificultad = fields.String(required=False, validate=validate.OneOf(choices=['FACIL', 'INTERMEDIO', 'DIFICIL', 'EXTREMO']))