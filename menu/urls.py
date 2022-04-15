from django.urls import path
from .views import PlatoApiView

urlpatterns = [
    path('', PlatoApiView.as_view()),
]
