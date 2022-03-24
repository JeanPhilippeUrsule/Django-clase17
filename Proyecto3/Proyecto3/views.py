from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context

def saludo(request):
    
    return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
    
    return HttpResponse('<br>Ya entendiste eso, es muy simple :) <br>')#codigo HTLM

def diaDeHoy(request):
    
    dia = datetime.datetime.now()
    
    documentoDeTexto = f'Hoy es el dia: <br><br> {dia}'
    
    return HttpResponse(documentoDeTexto)
    
def miNombreEs(self, nombre):
   
    documentoDeTexto = f'Mi nombre es <br><br> {nombre}'
    
    return HttpResponse(documentoDeTexto)

def tercera_vista(request, fecha):
    
    fecha_actual = date.today()
    
    anio = fecha_actual.year
    
    fecha = int(fecha)
    
    resultado = anio - fecha
    
    retorno = f'El año en que naciste es: {resultado}'
    
    return HttpResponse(retorno)

def probandoTemplate(self):
    
    miHtml = open('/Users/jean-philippeursule/Downloads/Django/Proyecto3/Proyecto3/plantillas/template1.html')
    
    plantilla = Template(miHtml.read())#Se carga en memoria nuestra plantilla
    
    miHtml.close() #Cerrqmos el archivo
    
    miContexto = Context()#Se tiene que crear si o si aunque este vacio
    
    documento = plantilla.render(miContexto)#Aca renderizamos la plantilla en documento
    
    return HttpResponse(documento)
    