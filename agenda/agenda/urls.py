from django.contrib import admin
from django.urls import path, include
# include > sirve para incluir un archivo con varias rutas al archivo de rutas del proyecto
from django.conf.urls.static import static
# se puede utilizar todas las variables definidas en el archivo SETTINGS del proyecto
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# el metodo static sirve para retorna una lista de URLPatterns pero que establecere que archivos y que rutas retornaran
