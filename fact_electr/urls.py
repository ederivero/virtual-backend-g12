from django.urls import path
from .views import GenerarComprobanteApiView

urlpatterns = [
    path('generar-comprobante/', GenerarComprobanteApiView.as_view()),
]
