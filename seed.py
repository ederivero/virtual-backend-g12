from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_
# leer en la bd si no existe las categorias : 'OCIO', 'COMIDA', 'EDUCACION', 'VIAJES'


def categoriaSeed():
    # si existe las categorias ya no se ingresa
    conexion.session.query(Categoria).filter(
        or_(Categoria.nombre == 'OCIO', Categoria.nombre == 'COMIDA')
    ).first()
