from .models import Plato, Stock
from rest_framework.generics import ListCreateAPIView
from .serializers import PedidoSerializer, PlatoSerializer, StockSerializer
from rest_framework.permissions import (AllowAny,  # sirve para que el controlador sea publico (no se necesite una token)
                                        # Los controladores soliciten una token de acceso
                                        IsAuthenticated,
                                        # Solamente para los metodos GET no sera necesaria la token pero para los demas metodos (POST, PUT, DELETE, PATCH) si sera requerido
                                        IsAuthenticatedOrReadOnly,
                                        # Verifica que en la token de acceso buscara al usuario y vera si es superuser (is_superuser)
                                        IsAdminUser,

                                        )
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir
from fact_electr.models import Pedido, DetallePedido


class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # sirve para indicar que tipos de permisos necesita el cliente para poder realizar la peticion
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        # hacer una iteracion para modificar la foto de cada plato y devolver el link de la foto
        print(data.data[1].get('foto'))
        # del contenido de la foto solamente extraer el nombre del archivo o si esta en una carpeta extraer la carpeta y el archivo
        link = CloudinaryImage(
            'plato/u3aj7qh0dtmy73yanv5j.jpg').image(secure=True)

        print(link)
        return Response(data=data.data)


class StockApiView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated, SoloAdminPuedeEscribir]


class PedidoApiView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]

    def post(self, request: Request):
        pass
