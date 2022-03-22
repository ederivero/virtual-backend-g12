from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey

class Preparacion(conexion.Model):
    __tablename__='preparaciones'

    id = Column(type_= types.Integer, autoincrement= True, primary_key = True)
    descripcion = Column(type_ = types.String(length=45))
    orden = Column(type_=types.Integer, nullable= False)

    # relacion entre preparaciones y recetas
    receta_id = Column(ForeignKey(column='recetas.id'), type_=types.Integer)
    # el relationship me sirve para poder navegar desde un modelo hacia el otro, el foreign key solamente me sirve para que a nivel de base de datos me haga la valicion de relacion mas no para acceder desde un modelo hacia el otro
    # backref > creara un atributo virtual que solamente se podra llamar desde la clase de la cual estamos creando el relationship para devolver todos sus 'hijos' 
    receta = orm.relationship('Receta', backref='preparaciones')
    