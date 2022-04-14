from django.urls import path
from .views import RegistroUsuarioApiView

urlpatterns = [
    path('registro/', RegistroUsuarioApiView.as_view())
]
