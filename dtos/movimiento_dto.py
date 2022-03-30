from config import validador
from models.movimientos import Movimiento
from marshmallow_sqlalchemy import auto_field
from dtos.categoria_dto import CategoriaResponseDTO
from marshmallow import fields


class MovimientoRequestDTO(validador.SQLAlchemyAutoSchema):
    usuario_id = auto_field(dump_only=True)

    class Meta:
        # si queremos que incluyan las FK
        include_fk = True
        model = Movimiento


class MovimientoResponseDTO(validador.SQLAlchemyAutoSchema):
    categoria = fields.Nested(nested=CategoriaResponseDTO)

    class Meta:
        model = Movimiento
        include_relationships = True
