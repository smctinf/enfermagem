from django.urls import path
from . import views

app_name='selecao'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),
]