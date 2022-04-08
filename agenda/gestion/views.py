from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (PruebaSerializer,
                          TareasSerializer,
                          EtiquetaSerializer,
                          TareaSerializer,
                          TareaPersonalizableSerializer)
from .models import Etiqueta, Tareas
# https://www.django-rest-framework.org/api-guide/status-codes/#status-codes
from rest_framework import status
# son un conjunto de librerias que django nos provee para poder utilizar de una manera mas rapida ciertas configuraciones, timezone sirve para, que en base a la configuracion que colocamos en el settings.py TIME_ZONE se basara en esta para darnos la hora y fecha con esa configuracion
from django.utils import timezone


@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    # request sera toda la informacion enviada por el cliente > https://www.django-rest-framework.org/api-guide/requests/
    print(request.method)
    print(request)
    if request.method == 'GET':
        # comportamiento cuando sea GET
        return Response(data={
            'message': 'Bienvenido a mi API de agenda'
        })

    elif request.method == 'POST':
        # comportamiento cuando sea POST
        return Response(data={
            'message': 'Hiciste un post'
        }, status=201)


class PruebaApiView(ListAPIView):
    # sirve para ayudarnos a cuando se llame este request nos haga el trabajo de serializar y de deserializar la informacion (es igual que un DTO)
    serializer_class = PruebaSerializer
    # queryset > encargado de hacer la busqueda para este controlador (para todos sus metodos)
    queryset = [{
        'nombre': 'Eduardo',
        'apellido': 'De Rivero',
        'correo': 'ederiv@gmail.com',
        'dni': '73500746',
        'estado_civil': 'viudo'},
        {
        'nombre': 'Maria',
        'apellido': 'Perez',
        'correo': 'ederiv@gmail.com',
        'dni': '73501746',
        'estado_civil': 'casado'}]

    def get(self, request: Request):
        # dentro de las vistas genericas se puede sobre escribir la logica inicial del controlador
        # si modifico la logica original de cualquier generico en base a su metodo a utilizar ya no sera necesario definir los atributos serializer_class y queryset ya que estos se usan para cuando no se modifica lo logica original
        informacion = self.queryset
        # Uso el serializador para filtar la informacion necesaria y no mostrar alguna informacion de mas pero en este caso como le voy a pasar uno o mas registros de usuario entonces para que el serializador los pueda iterar le coloco el parametro many=True que lo que hara sera iterar
        informacion_serializada = self.serializer_class(
            data=informacion, many=True)
        # para utilizar la informacion serializada OBLIGATORIAMENTE tengo que llamar al metodo is_valid() el cual internamente hara la validacion de los campos y sus configuraciones
        # el parametro raise_exception hara la emision del error si es que hay indicando cual es el error
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message': 'Hola',
            'content': informacion_serializada.data
        })


class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all()  # SELECT * FROM tareas;
    serializer_class = TareasSerializer

    def post(self, request: Request):
        # serializo la data para validar sus valores y su configuracion
        serializador = self.serializer_class(data=request.data)

        # llamo al metodo validar que retornara True si cumple o False si no
        if serializador.is_valid():
            # serializador.initial_data > data inicial sin la validacion
            # serializador.validated_data > data ya validada (solo se puede llamar luego de llamar al metodo is_valid())
            # validare que la fecha_caducidad no sea menor que hoy
            fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
            importancia = serializador.validated_data.get('importancia')

            # validar que la importancia sea entre 0 y 10
            if importancia < 0 or importancia > 10:
                return Response(data={
                    'message': 'La importancia puede ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)

            if timezone.now() > fechaCaducidad:
                return Response(data={
                    'message': 'La fecha no puede ser menor que la fecha actual'
                }, status=status.HTTP_400_BAD_REQUEST)
            # El metodo save() se podra llamar siempre que el serializado sea un ModelSerializer y este servira para poder guardar la informacion actual del serializador en la bd
            serializador.save()

            return Response(data=serializador.data, status=status.HTTP_201_CREATED)
        else:
            # mostrara todos los errores que hicieron que el is_valid() no cumpla la condicion
            # serializador.errors
            return Response(data={
                'message': 'La data no es valida',
                'content': serializador.errors},
                status=status.HTTP_400_BAD_REQUEST)


class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer


class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer  # TareaPersonalizableSerializer
    queryset = Tareas.objects.all()
