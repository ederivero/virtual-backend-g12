from config import validador
from marshmallow import fields


class ResetPasswordRequestDTO(validador.Schema):
    correo = fields.Email()
