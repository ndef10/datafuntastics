from django.urls import path
from . import views # importar el archivo views
 
urlpatterns = [
    path("", views.v_index, name="graphify"),
    path("reporte_png", views.v_reporte_png, name="v_reporte_png")
]

    