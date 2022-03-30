from sqlalchemy import Column, types, orm
from config import conexion
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey


class Movimiento(conexion.Model):
    __tablename__ = 'movimientos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    monto = Column(type_=types.Float(), nullable=False)
    tipo = Column(type_=types.Enum('INGRESO', 'EGRESO'), nullable=False)
    descripcion = Column(type_=types.String(45))
    moneda = Column(type_=types.Enum('SOLES', 'DOLARES', 'EUROS'))
    fecha_creacion = Column(type_=types.DateTime(), default=datetime.now())
    # RELACIONES (fk con sus relationships)

    usuario_id = Column(ForeignKey(column='usuarios.id'),
                        type_=types.Integer, nullable=False)
    usuario = orm.relationship('Usuario', backref='usuario_movimientos')

    categoria_id = Column(ForeignKey(column='categorias.id'),
                          type_=types.Integer, nullable=False)
    categoria = orm.relationship('Categoria', backref='categoria_movimientos')
