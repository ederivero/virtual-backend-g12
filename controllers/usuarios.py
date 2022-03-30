from flask_restful import Resource, request
from dtos.registro_dto import RegistroDTO, UsuarioResponseDTO, LoginDTO
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion, sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail


class RegistroController(Resource):
    def post(self):
        # me da todo el body convertido en un diccionario
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevoUsuario = Usuario(**data)
            # generar un hash de la contraseña
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevoUsuario)

            return {
                'message': 'Usuario registrado exitosamente',
                'content': respuesta
            }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al registrar al usuario',
                'content': e.args
            }, 400


class LoginController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = LoginDTO().load(body)
            return {
                'message': 'Bievenido'
            }
        except Exception as e:
            return{
                'message': 'Credenciales incorrectas',
                'content': e.args
            }


class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = ResetPasswordRequestDTO().load(body)
            # validar si existe ese usuario en mi bd
            usuarioEncontrado = conexion.session.query(
                Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                # tengo que utilizar los correos verificados en sendgrid ya que si uso uno que no esta verificado entonces el correo nunca llegara
                from_email = Email('ederiveroman@outlook.com')
                to_email = To(usuarioEncontrado.correo)
                subject = 'Reinicia tu contraseña del Monedero App'
                content = Content(
                    'text/plain', 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....')
                mail = Mail(from_email, to_email, subject, content)
                envia_correo = sendgrid.client.mail.send.post(
                    request_body=mail.get())
                # el estado de la respuesta de sendgrid
                print(envia_correo.status_code)
                # el cuerpo de la respuesta de sendgrid
                print(envia_correo.body)
                # las cabeceras de la respuesta de sendgrid
                print(envia_correo.headers)

            return {
                'message': 'Correo enviado exitosamente'
            }
        except Exception as e:
            return {
                'message': 'Error al resetear la password',
                'content': e.args
            }
