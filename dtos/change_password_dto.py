from config import validador
from marshmallow import fields, validate


class ChangePasswordRequestDTO(validador.Schema):
    token = fields.String(required=True)
    # valido que sea string y ademas que no sea menor a 6 caracteres
    password = fields.String(validate=validate.Length(min=6), required=True)
