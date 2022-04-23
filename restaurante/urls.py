from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autorizacion.urls')),
    path('platos/', include('menu.urls')),
    path('facturacion/', include('fact_electr.urls')),
]
