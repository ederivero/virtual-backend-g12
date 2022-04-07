from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer, TareaSerializer
from .models import Tareas


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
    serializer_class = TareaSerializer
