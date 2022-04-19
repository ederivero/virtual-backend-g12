from django.urls import path
from .views import PlatoApiView, StockApiView

urlpatterns = [
    path('', PlatoApiView.as_view()),
    path('stock/', StockApiView.as_view()),
]
