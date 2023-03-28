from django.contrib import admin
from django.urls import path, include
from .views import home, consultar, retornar

urlpatterns = [
    path('', home),
    path('consultar/', consultar, name='consultar'),
    path('', retornar, name='retornar'),
]