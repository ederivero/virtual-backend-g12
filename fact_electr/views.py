from rest_framework.generics import CreateAPIView
from .generar_comprobante import generar_comprobante
from rest_framework.response import Response
from .serializers import GenerarComprobanteSerializer


class GenerarComprobanteApiView(CreateAPIView):
    serializer_class = GenerarComprobanteSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)

        data.is_valid(raise_exception=True)
        try:
            generar_comprobante(**data.validated_data)

            return Response(data={'message': 'Comprobante creado exitosamente'}, status=201)

        except Exception as e:
            return Response(data={'message': 'Error al crear el comprobante', 'content': e.args})
