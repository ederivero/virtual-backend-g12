from config import validador
from models.preparaciones import Preparacion
from models.recetas import Receta
from marshmallow import fields
class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Preparacion
        # Si queremos que el DTO tambien valide el tipo de dato y algunas propiedades que le hemos dado a nuestra relacion entonces tendremos que agregar el atributo include_fk para que incluya en las validaciones a esa llave foranea
        include_fk = True


class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    # Nested > es un tipo de campo que sirve para relacionar un DTO con otro DTO y usamos el parametro nested para indicar a que DTO nos queremos relacionar, tiene que ser el mismo nombre que el relationship pero si quisieramos tener un nombre diferente entonces agregamos el parametro data_key en el cual indicaremos como se llamara nuestra llave en el resultado pero de igual forma tendremos que utilizar el nombre de nuestro relationship como atributo de la clase
    receta = fields.Nested(nested=RecetaResponseDTO, data_key= 'receta_relacion')
    class Meta:
        model = Preparacion
        # Cargara las instancias relacionadas al modelo preparacion
        load_instance = True
        include_fk = False
        # Agregar al DTO las relaciones que puede tener este modelo con algun otro, esto lo usara mediante los atributos que hemos creado de tipo 'orm.relationship'
        # include_relationship > internamente hace un join con las tablas relacionas a esta
        include_relationships = True