from django.shortcuts import render
from .forms import *
from django.contrib import messages

# Create your views here.

def inicio(request):
    from datetime import date, datetime

    hoje = date.today()
    data_inicio = datetime.strptime('11/10/2021', '%d/%m/%Y').date()
    data_fim = datetime.strptime('15/10/2021', '%d/%m/%Y').date()

    if hoje >= data_inicio and hoje <= data_fim:
        return render(request, 'inicio.html')
    else:
        return render(request, 'inicio_aguardar.html')


def cadastro(request):

    if request.method == 'POST':
        form = CandidatoForm(request.POST)

        if form.is_valid():
            form.save()

            form = CandidatoForm()

        else:
            # Se teve erro:
            print('Erro: ', form.errors)
            erro_tmp = str(form.errors)
            erro_tmp = erro_tmp.replace('<ul class="errorlist">', '')
            erro_tmp = erro_tmp.replace('</li>', '')
            erro_tmp = erro_tmp.replace('<ul>', '')
            erro_tmp = erro_tmp.replace('</ul>', '')
            erro_tmp = erro_tmp.split('<li>')

            messages.error(request, erro_tmp[2])

    else:
        form = CandidatoForm()

    return render(request, 'cadastro.html', { 'form': form })
