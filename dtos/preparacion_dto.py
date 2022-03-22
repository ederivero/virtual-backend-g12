from config import validador
from models.preparaciones import Preparacion

class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion