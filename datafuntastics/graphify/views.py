from django.shortcuts import render
from django.http import HttpResponse # Importar
import matplotlib.pyplot as plt
from io import BytesIO
 
# Create your views here.
def v_index(request):
    # return HttpResponse("index Graphify")
    return render(request, "graphify/index.html", {})

def v_reporte_png(request):
    # Datos para el gráfico (puedes adaptarlos según tus necesidades)
    labels = ['Category A', 'Category B', 'Category C']
    values = [40, 30, 20]

    # Crear el gráfico con Matplotlib
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Sample Chart")

    # Guardar el gráfico en un buffer en memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Cerrar la figura para liberar memoria
    buffer.seek(0)

    # Devolver el archivo PNG como respuesta
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="chart.png"'
    return response