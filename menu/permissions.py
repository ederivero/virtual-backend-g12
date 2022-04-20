from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions


class SoloAdminPuedeEscribir(BasePermission):
    # si queremos modificar el mensaje de error en el caso no se cumpla las condiciones, haciendo uso del atributo message podremos indicar que mensaje mostraremos
    message = 'Este usuario no tiene permisos'

    def has_permission(self, request: Request, view):
        # view > es la vista a la cual intenta acceder el usuario, esto dependera de donde se coloque el middleware

        # Middlewares >  es un intermediario entre la peticion del front y la logica final (se encargara de validar si cumple o no cumple determinados reqs y si no cumple no podra continuar)

        # el request nos dara toda la informacion de los atributos de la peticion
        # en los custom permission SIEMPRE hay que retornar True o False para indicar si cumple o no cumple con los permisos determinados
        # request.user > me brindara la infromacion del usuario autenticado
        print(request.user)
        print(request.user.nombre)
        print(request.user.rol)
        # auth > imprimira la token de autenticacion que se usa para esta solicitud (request)
        print(request.auth)
        # SAFE_METHODS > son los metodos que el usuario no podra modificar la informacion del backend, son GET, HEAD, OPTIONS
        print(request.method)

        print(SAFE_METHODS)
        print(type(view))
        # print(str(type(view)) == "<class 'menu.views.StockApiView'>")
        # hacemos determinada validacion si solamente queremos hacer esa validacion para una determinada vista
        # if str(type(view)) == "<class 'menu.views.StockApiView'>":
        #     return request.user.rol == 'ADMINISTRADOR'

        # Si ES GET, HEAD, OPTIONS no necesito validar si es ADMINISTRADOR o MOZO
        if request.method in SAFE_METHODS:
            return True
        # SI es POST necesitare validar si es administrador
        else:
            return request.user.rol == 'ADMINISTRADOR'

        # return True if request.method in SAFE_METHODS else request.user.rol == 'ADMINISTRADOR'

        # return request.user.rol == 'ADMINISTRADOR'
