from django.contrib import admin
from django.urls import path, include
# include > sirve para incluir un archivo con varias rutas al archivo de rutas del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls'))
]
