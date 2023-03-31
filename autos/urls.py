from django.contrib import admin
from django.urls import path, include
from .views import*

urlpatterns=[
    path("autos/",autos, name="autos"),
    path("clientes/",clientes, name="clientes"),
    path("",principal, name="principal")
]


