from rest_framework import serializers
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length= 8, min_length= 8, regex="[0-9]")
    # dni = serializers.IntegerField(min_value=10000000, max_value=99999999)