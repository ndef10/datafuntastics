from django.urls import path
from . import views # importar el archivo views
 
urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reporte_xls", views.v_reporte_xls, name="v_reporte_xls"),
    path("macros", views.macros, name="macros"),
    path("powerbi", views.powerbi, name="powerbi"),
    path("analitica", views.analitica, name="analitica")
]