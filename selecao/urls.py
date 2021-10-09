from django.urls import path
from . import views

app_name='selecao'

urlpatterns = [
    path('inicio_teste', views.inicio_teste, name='inicio_teste'),
    #
    path('', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('imprime/<str:chave>', views.imprime, name='imprime'),
    path('consulta', views.consulta, name='consulta'),
]