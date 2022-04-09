from rest_framework import serializers
from .models import Etiqueta, Tareas
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/


class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length=8, min_length=8, regex="[0-9]")
    # dni = serializers.IntegerField(min_value=10000000, max_value=99999999)
    # 3562745


# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'  # estare indicando que voy a utilizar todos las columnas de mi tabla
        # exclude = ['importancia'] # indicara que columnas NO quiero utilizar
        # NOTA: no se puede utilizar los dos a la vez, es decir, o bien se usa el fields o el exclude
        extra_kwargs = {
            'etiquetas': {
                'write_only': True
            }
        }

        # depth = 1  # Sirve para que en el caso que querramos devolver la informacion de una relacion entre este modelo podemos indicar hasta que grado de profundidad queremos que nos devuelva la informacion, la profundida maxima es de 10

        # la profundidad solamente funcionara cuando en el modelo en el cual lo estemos utilizando sea el modelo en el cual se encuentra la relacion como atributo


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1


class EtiquetaSerializer(serializers.ModelSerializer):
    # indicare que este atributo solamente funcionara para cuando vamos a serializar la data antes de devolverla mas no para cuando querramos usarla para escritura
    # se tiene que llamar igual que el related_name para poder ingresar a esa relacion O podremos definir el parametro source en el cual colocaremos el nombre del related_name
    # NOTA: no podemos utilizar el parametro source si es que tbn colocaremos el mismo valor como nombre del atributo
    tareas = TareasSerializer(many=True, read_only=True)  # , source='tareas')

    class Meta:
        model = Etiqueta
        fields = '__all__'
        # ¿Como puedo mediante un serializador indicar que columnas de determinado modelo seran solamente escritura o solamente lectura sin modificar su comportamiento como atributo de la clase?
        # extra_kwargs y read_only_fields solamente funcionaran para cuando nosotros querramos modificar el comportamiento de los atributos que no los hemos modificado manualemente dentro del serializador
        extra_kwargs = {
            # 'nombre': {
            #     'write_only': True
            # },
            'id': {
                'read_only': True
            }
        }
        # Los campos del modelo que solamente quiero que sean lectura los podre definir en una lista
        read_only_fields = ['createAt']


class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        # exclude = ['nombre'] # funciona tanto para lectura como escritura
        extra_kwargs = {
            'nombre': {
                'read_only': True
            }
        }


class ArchivoSerializer(serializers.Serializer):
    # max_length > indica la longitud maxima DEL NOMBRE del archivo
    # use_url > si es verdadero retornara el link completo de la ubicacion del archivo, caso contrario retornara solamente la ubicacion dentro del proyecto del archivo

    archivo = serializers.ImageField(max_length=100, use_url=True)
