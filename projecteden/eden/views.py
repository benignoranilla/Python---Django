from django.http import HttpResponse
from django.template import Template, Context

def bienvenida(request):
    return HttpResponse("Bienvenido a Eden")

def home(request):
    #ruta de la plantilla
    plantilla = open("D:\Django\Eden\eden\eden\plantillas\home.html")
    template = Template(plantilla.read())
    plantilla.close()
    contexto = Context()
    document = template.render(contexto)
    return HttpResponse(document)