from .models import Plato, Stock
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import (PedidoSerializer,
                          PlatoSerializer,
                          StockSerializer,
                          StockCreateSerializer,
                          AgregarDetallePedidoSerializer)
from rest_framework.permissions import (AllowAny,  # sirve para que el controlador sea publico (no se necesite una token)
                                        # Los controladores soliciten una token de acceso
                                        IsAuthenticated,
                                        # Solamente para los metodos GET no sera necesaria la token pero para los demas metodos (POST, PUT, DELETE, PATCH) si sera requerido
                                        IsAuthenticatedOrReadOnly,
                                        # Verifica que en la token de acceso buscara al usuario y vera si es superuser (is_superuser)
                                        IsAdminUser,
                                        SAFE_METHODS
                                        )
from rest_framework.response import Response
from rest_framework.request import Request
from cloudinary import CloudinaryImage
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import Pedido, DetallePedido
from rest_framework import status
from django.utils import timezone
from django.db import transaction, IntegrityError


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

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return StockCreateSerializer
        return StockSerializer


class PedidoApiView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]

    def post(self, request: Request):
        print(request.user)
        # Le agrego al body el usuarioId proveniente de la autenticacion de la token
        request.data['usuarioId'] = request.user.id
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data=data.data, status=status.HTTP_201_CREATED)


class AgregarDetallePedidoApiView(CreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = AgregarDetallePedidoSerializer

    def post(self, request: Request):
        # 1. valido la data con el serializer
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        # 2. verifico que tenga esa cantidad de productos en stock
        # SELECT * FROM stocks WHERE fecha = '...' AND plato_id = '...' AND cantidad >= '...';
        # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#gte

        stock: Stock | None = Stock.objects.filter(fecha=timezone.now(),
                                                   platoId=data.validated_data.get('platoId'), cantidad__gte=data.validated_data.get(
            'cantidad')).first()

        print(stock)
        if stock is None:
            return Response(data={'message': 'No hay stock para ese producto para el dia de hoy'},
                            status=status.HTTP_400_BAD_REQUEST)

        # validar si el pedido existe
        # SELECT * FROM pedidos WHERE id = '...' LIMIT 1;
        pedido: Pedido | None = Pedido.objects.filter(
            id=data.validated_data.get('pedidoId')).first()

        if pedido is None:
            return Response(data={'message': 'No hay ese pedido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # https://docs.djangoproject.com/en/4.0/topics/db/transactions/
            with transaction.atomic():
                # Todo lo que este dentro de esta definicion de atomic() respetara a la creacion de la transaccion
                # guardar ese detalle de ese pedido
                # al agregar un nuevo registro y este tuviese FK no solamente bastara con poner el id sino que tendremos que pasar toda la instancia para que django se cerciore que ese registro (FK) sea valida
                nuevoDetalle = DetallePedido(cantidad=data.validated_data.get(
                    'cantidad'), stockId=stock, pedidoId=pedido)

                # esto hara que se guarde de manera permanente en la bd
                nuevoDetalle.save()

                # disminuir el stock de ese plato en la tabla stock
                stock.cantidad = stock.cantidad - nuevoDetalle.cantidad

                # guarda las modificaciones en la bd de ese registro
                stock.save()

                # modifico el total de la cabecera
                pedido.total = pedido.total + \
                    (nuevoDetalle.cantidad * stock.precio_diario)
                pedido.save()
                # si termina este bloque sin ningun error entonces automaticamente se hara un commit a la bd
        except IntegrityError:
            # ingresara si algo que se ejecutaba en la transaccion es incorrecto o no funciono de la manera esperada
            # se hara un rollback de todas las operaciones que se hicieron dentro de la transaccion
            return Response(data={'message': 'Error al crear el pedido, todo quedo en nada'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # informacion que me envia el front
        # {
        #   "cantidad": 2,
        #   "plato": 1,
        #   "pedido_id": 2
        # }
        # verificar que en el stock este en base al dia de hoy esa cantidad
        # 3. agrego el detalle con su respectivo pedido
        return Response(data={'message': 'Detalle agregado exitosamente'})
