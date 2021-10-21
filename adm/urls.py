from django.urls import path
from . import views

app_name='adm'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('envia_email', views.envia_email, name='envia_email'),
    path('envia/<int:id>', views.envia, name='envia'),
    path('sair', views.sair, name='sair'),
]