from config import validador
from models.categorias import Categoria


class CategoriaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
