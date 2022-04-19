from rest_framework.permissions import BasePermission
from rest_framework.request import Request
# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions


class SoloAdminPuedeEscribir(BasePermission):
    def has_permission(self, request: Request, view):
        # el request nos dara toda la informacion de los atributos de la peticion
        # en los custom permission SIEMPRE hay que retornar True o False para indicar si cumple o no cumple con los permisos determinados
        # request.user > me brindara la infromacion del usuario autenticado
        print(request.user)
        return True
