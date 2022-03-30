from models.categorias import Categoria
from config import conexion
from sqlalchemy import or_
# leer en la bd si no existe las categorias : 'OCIO', 'COMIDA', 'EDUCACION', 'VIAJES'


def categoriaSeed():
    # si existe las categorias ya no se ingresa
    categorias = conexion.session.query(Categoria).filter(
        or_(Categoria.nombre == 'OCIO', Categoria.nombre == 'COMIDA',
            Categoria.nombre == 'EDUCACION', Categoria.nombre == 'VIAJES')
    ).first()

    if categorias is None:
        # creacion de esas categorias
        nombres = ['OCIO', 'COMIDA', 'EDUCACION', 'VIAJES']
        try:
            for categoria in nombres:
                nuevaCategoria = Categoria(nombre=categoria)
                conexion.session.add(nuevaCategoria)

            conexion.session.commit()
            print('Categorias creadas exitosamente')
        except Exception as e:
            conexion.session.rollback()
            print('Error al alimentar la bd')
