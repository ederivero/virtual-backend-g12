from django.urls import path
from .views import PlatoApiView, StockApiView, PedidoApiView

urlpatterns = [
    path('', PlatoApiView.as_view()),
    path('stock/', StockApiView.as_view()),
    path('pedido/', PedidoApiView.as_view())
]
