from django.urls import path
from . import views # importar el archivo views
 
urlpatterns = [
    path("", views.v_index, name="librarium"),
    path("reporte_pdf", views.v_reporte_pdf , name="v_reporte_pdf ")
]


    
