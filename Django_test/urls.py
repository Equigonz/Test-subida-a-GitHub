"""Django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Django_test.views import saludo
from Django_test.views import canelones
from Django_test.views import formula_1
from Django_test.views import dia_de_hoy, saludo_con_nombre, anio_de_nacimiento, plantilla


urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo, name = "view de saludo"),
    path("canelones/", canelones, name = "comida"),
    path("formula_1/", formula_1, name = "carreras"),
    path("dia_de_hoy/", dia_de_hoy, name = "dia de la fecha"),
    path("saludo_con_nombre/<str:nombre>/<int:edad>/", saludo_con_nombre, name = "saludo con nombre"),
    path("nacimiento/<int:anio>/", anio_de_nacimiento, name= "año de nacimiento"),
    path("plantilla/", plantilla, name = "Plantilla")
]
