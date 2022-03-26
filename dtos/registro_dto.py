from config import validador
from models.usuarios import Usuario


# DTO > Data Transfer Object
class RegistroDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
