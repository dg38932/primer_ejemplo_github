from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def dia_de_hoy(request): 
    dia = datetime.datetime.now()
    documento_de_texto = f"hoy es dia: <br> {dia}"
    return HttpResponse(documento_de_texto)

def mi_nombre_es(self, nombre):
    documento_de_texto = f"mi nombre es: <br><br> {nombre}"
    return HttpResponse(documento_de_texto)


def tercera_vista(request,fecha):
    fecha_actual = date.today()
    anio = fecha_actual.year
    fecha = int(fecha)
    resultado = anio - fecha
    retorno = f"el año que naciste es: {resultado}"
    return HttpResponse(retorno)

def probando_template1(self):
    mi_html = open("C:/Users/Usuario/Documents/python_coder/django/proyecto1/proyecto1/plantillas/template1.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)

def probando_template2(self):
    nom = "Diego"
    ap = "Giordano"
    listadenotas = [2,2,3,7,2,5]
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now(), "notas":listadenotas}
    mi_html = open("C:/Users/Usuario/Documents/python_coder/django/proyecto1/proyecto1/plantillas/template2.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)

def probando_template3(self):
    nom = "Diego"
    ap = "Giordano"
    listadenotas = [2,2,3,7,2,5]
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now(), "notas":listadenotas}
    plantilla = loader.get_template("template3.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def probando_template4(self):
    nombre = "Diego"
    oficio = "Supervisor"
    nuevodiccionario = {"nombre":nombre, "oficio":oficio}
    nuevaplantilla = loader.get_template("template4.html")
    documento = nuevaplantilla.render(nuevodiccionario)
    return HttpResponse(documento)
