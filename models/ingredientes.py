# las tablas que queremos crear en python se representaran en forma de clases y cada columna sera su atributo

# create table ingredientes (id int primary key ....)
from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
    # ahora esta clase tendra un comportamiento en forma de un Model (tabla en la bd)
    # id seria considerada como una columna de mi modelo (tabla) ingrediente
    # https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=column#sqlalchemy.schema.Column
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.String
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre= Column(type_=types.String(length=45), nullable=False, unique=True)

    # indicara cual es el nombre de la tabla en la base de datos, si no le ponemos o no definimos este atributo entonces sera el nombre de la clase
    __tablename__ = 'ingredientes'