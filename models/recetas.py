from email.policy import default
from config import conexion
from sqlalchemy import Column, types

class Receta(conexion.Model):
    id = Column(type_= types.Integer, autoincrement= True, primary_key= True)
    nombre = Column(type_= types.String(length=45), nullable= False)
    estado = Column(type_= types.Boolean, default= True)
    comensales = Column(type_= types.Integer)
    duracion = Column(type_= types.String(length= 45))
    dificultad = Column(type_= types.Enum('FACIL', 'INTERMEDIO', 'DIFICIL', 'EXTREMO'), default= 'FACIL')

    __tablename__='recetas'