from config import validador
from marshmallow import fields, validate

# el validador de request
class ValidadorPrueba(validador.Schema):
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#module-marshmallow.validate
    nombre = fields.Str(validate=validate.Length(max=10))
    apellido = fields.Str()
    edad = fields.Int()
    soltero = fields.Bool()

    # class Meta:
        # es una clase que va a ser para poder pasar parametros a la metadata del padre (de la clase de la cual estamos heredando), definimos atributos que van a seri a la clase Schema para poder hacer la validacion correcta
        # en el atributo fields iran lo que seria que valores necesitamos esperar del cliente
        # fields = ['nombre', 'apellido']

# validador de response
class ValidarUsuarioPrueba(validador.Schema):
    nombre = fields.Str()
    apellido = fields.Str()