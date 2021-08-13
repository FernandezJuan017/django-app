"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import newapp
from django.contrib import admin
from django.urls import path
# Importo app con la vista
# Forma nº 1: 
from newapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/',views.index,name="inicio"),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:nombre>', views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name="contacto")
]

#Forma nº 2: (mejor forma?)
# import newapp.views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', newapp.views.index, name="index"),
#     path('inicio/',newapp.views.index,name="inicio"),
#     path('hola-mundo/', newapp.views.hola_mundo, name="hola_mundo")
# ]
