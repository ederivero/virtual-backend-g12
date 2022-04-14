from rest_framework import serializers
from .models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        # creo una instancia de mi usuario con los campos ya validados (validated_data)
        nuevoUsuario = Usuario(**self.validated_data)

        # encripto la password
        nuevoUsuario.set_password(self.validated_data.get('password'))

        # guardo el usuario en la bd
        nuevoUsuario.save()

        return nuevoUsuario

    class Meta:
        model = Usuario
        exclude = ['groups', 'user_permissions']
        # fields = '__all__'
        # mediante el atributo extra_kwargs indicar que la password sera de solo escritura y ademas que el id sea solo lectura
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }
