from django.urls import path
from .views import (EtiquetasApiView,
                    inicio,
                    PruebaApiView,
                    TareasApiView,
                    TareaApiView,
                    ArchivosApiView,
                    EliminarArchivoApiView)

# seran todas las rutas de esta aplicacion las tendremos que registrara aca y solamente se puede usar esta variable
urlpatterns = [
    path('inicio', inicio),
    path('prueba', PruebaApiView.as_view()),
    path('tareas', TareasApiView.as_view()),
    path('etiquetas', EtiquetasApiView.as_view()),
    path('tarea/<int:pk>', TareaApiView.as_view()),  # pk > Primary Key
    path('subir-imagen', ArchivosApiView.as_view()),
    path('eliminar-imagen', EliminarArchivoApiView.as_view())
]
