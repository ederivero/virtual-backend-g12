from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from .serializers import RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework import status


class RegistroUsuarioApiView(CreateAPIView):
    serializer_class = RegistroUsuarioSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)

        data.is_valid(raise_exception=True)
        data.save()
        return Response(data={
            'message': 'Usuario creado exitosamente',
            'content': data.data
        }, status=status.HTTP_201_CREATED)
