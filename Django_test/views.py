from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Mundo locooooooooooooooo")

def canelones(request):
    return HttpResponse("canelones de ricota y verdura")  

def formula_1(request):
    return HttpResponse("Red bull Racing-RB Powertrains")      

def dia_de_hoy(request):
    hoy= datetime.today().date()
    return HttpResponse(f"Hoy es {hoy}")

def saludo_con_nombre(request, nombre, edad):

    return HttpResponse(f"Hola queridisimo {nombre} tu edad es {edad}")

def anio_de_nacimiento(request, anio):
    anio_actual=datetime.today().year
    nacimiento=anio_actual-anio
    return HttpResponse(f"Naciste en el año {nacimiento}")

def plantilla(request):
    return render(request, "plantilla.html", context={})    
    