import re
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista Controlador
# (En python) MVT = Modelo Vista(es el Controlador) Template(es la Vista)

navbar = """
    <h1> Inicio</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio </a>
        </li>
        <li>
            <a href="/hola-mundo"> Primer pagina </a>
        </li>
        <li>
            <a href="/contacto"> Contacto </a>
        </li>
    </ul> 
    <hr/>  
"""
footer = """
    <hr/>
        <h3 style="text-align: center;"> SuSTI Corrientes 2021</h3>
    <hr/>  
"""
def index(request):
    html= """
     <h1>Inicio</h1>
     <h4>Años</h4>
     <ul>
    """
    year = 2021
    while year <=2040:
        if year % 2 == 0:
            html += f"<li> {str(year)}</li>"
        year += 1
    html += "</ul>"

    # return HttpResponse(navbar + html + footer) 
    return render(request, 'index.html') 

def hola_mundo(request): 
    html="""
    <h1>App en Django</h1>
    <h3>Hola Mundo</h3>
    """
    return render(request, 'saludo.html') 

def contacto(request, nombre = "", apellido = ""): # parametros opcionales: var = "valor"
    html="""
    <h3>Contacto:
    """
    if nombre and apellido:
        html += f" {nombre}, {apellido}.</h3>"  
    else:
        html += f"Nombre no asignado.</h3>"
        return redirect('inicio')
    return render(request, 'contacto.html') 