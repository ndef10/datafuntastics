from django.shortcuts import render
from django.http import HttpResponse # Importar
from openpyxl import Workbook
import datetime
 
# Create your views here.
def v_index(request):
    return HttpResponse("Sheetmarker index")

static_values = {
    "direccion": "Las flores 4242424 | Concepcion", 
    "direccion2": "Los Claveles 4242424 | Concepcion",
    "direccion3": "Las Margaritas 4242424 | Concepcion",
    "telefono": "59 34343333",
    "correo": "correo@gmail.com",
    "whatsapp": "+56933378817",
    
}
    
def macros(request):
    context = {
        "static_values": static_values   
    }
    return render(request, "sheetmarker/macros.html", context)

def powerbi(request):
    static_values['direccion'] = static_values['direccion2']
    context = {
        "static_values": static_values 
    }
    return render(request, "sheetmarker/powerbi.html", context)

def analitica(request):
    static_values['direccion'] = static_values['direccion3']
    context = {
        "static_values": static_values 
    }
    return render(request, "sheetmarker/analitica.html", context)


def v_reporte_xls(request):
    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Reporte de Ejemplo"

    # Agregar encabezados
    encabezados = ["ID", "Nombre", "Fecha"]
    worksheet.append(encabezados)

    # Agregar algunos datos de ejemplo
    datos = [
        [1, "Alice", datetime.date(2023, 11, 5)],
        [2, "Bob", datetime.date(2023, 11, 6)],
        [3, "Charlie", datetime.date(2023, 11, 7)],
    ]

    for fila in datos:
        worksheet.append(fila)

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=reporte.xlsx"

    # Guardar el libro en la respuesta
    workbook.save(response)

    return response
