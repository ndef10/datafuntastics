"""
URL configuration for datafuntastics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("librarium.urls")),
    path("graphify/", include("graphify.urls")),
    # path("librarium/", include("librarium.urls")),
    path("sheetmarker/", include("sheetmarker.urls")),
    path('admin/', admin.site.urls),
]

# http://127.0.0.1:8000/graphify
# http://127.0.0.1:8000/librarium
# http://127.0.0.1:8000/sheetmarker

# http://127.0.0.1:8000/graphify/reporte_png
# http://127.0.0.1:8000/librarium/reporte_pdf
# http://127.0.0.1:8000/sheetmarker/reporte_xls




# http://127.0.0.1:8000/data-analitica

# templetes/librarium/data_analitica.html
# librarium/views.py -> def data_analitica


# http://127.0.0.1:8000/data-frames

# templetes/librarium/data_frames.html
# librarium/views.py -> def data_frames

# http://127.0.0.1:8000/servicios

# templetes/librarium/servicios.html
# librarium/views.py -> def servicios