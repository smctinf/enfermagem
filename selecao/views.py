from django.core.checks.messages import Error
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def inicio_teste(request):
    return render(request, 'inicio.html')


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
    from django.template import Context
    from django.template.loader import render_to_string, get_template
    from django.core.mail import EmailMessage
    import uuid
    from ipware import get_client_ip

    if request.method == 'POST':
        form = CandidatoForm(request.POST)

        if form.is_valid():
            cadastro = form.save(commit=False)

            chave = str(uuid.uuid4())
            cadastro.chave = chave

            # Busca IP

            client_ip, is_routable = get_client_ip(request)
            if client_ip is None:
                # Unable to get the client's IP address
                print(client_ip)
                client_ip = '0.0.0.0'
            else:
                # We got the client's IP address
                if is_routable:
                    print('sim:', is_routable)
                    # The client's IP address is publicly routable on the Internet
                else:
                    print('não:', is_routable)
                    # The client's IP address is privat

            cadastro.ip = client_ip

            cadastro.save()

            # Envia e-mail

            dados = {
                'id': cadastro.id,
                'nome': cadastro.nome,
                'dt_nascimento': cadastro.dt_nascimento,
                'cpf': cadastro.cpf,
                'celular': cadastro.celular,
                'tel': cadastro.tel,
                'email': cadastro.email,
                'deficiencia': cadastro.deficiencia,
                'qual_deficiencia': cadastro.qual_deficiencia,
                'necessidade': cadastro.necessidade,
                'dt_inclusao': cadastro.dt_inclusao,
                'ip': cadastro.ip,
            }

            mensagem = get_template('mail.html').render(dados)

            msg = EmailMessage(
                'Inscrição do Processo Seletivo para Curso de Técnico em Enfermagem',
                mensagem,
                'Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima - Inscrição <inscricao@sme.novafriburgo.rj.gov.br>',
                [cadastro.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            return render(request, 'cadastrook.html', { 'chave': chave })

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


def imprime(request, chave):
    candidato = Candidato.objects.get(chave=chave)

    return render(request, 'ficha.html', { 'candidato': candidato })


def consulta(request):
    from django.template import Context
    from django.template.loader import render_to_string, get_template
    from django.core.mail import EmailMessage
    import uuid

    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():

            cpf = form.cleaned_data['cpf']

            try:
                candidato = Candidato.objects.get(cpf=cpf)
            except ObjectDoesNotExist:
                messages.error(request, 'CPF não cadastrado.')
                return render(request, 'consulta.html', { 'form': form })

            # Envia e-mail

            dados = {
                'id': candidato.id,
                'nome': candidato.nome,
                'cpf': candidato.cpf,
                'email': candidato.email,
                'dt_inclusao': candidato.dt_inclusao,
                'ip': candidato.ip,
                'chave': candidato.chave,
            }

            mensagem = get_template('mail_consulta.html').render(dados)

            msg = EmailMessage(
                'Consulta a inscrição do Processo Seletivo para Curso de Técnico em Enfermagem',
                mensagem,
                'Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima - Inscrição <inscricao@sme.novafriburgo.rj.gov.br>',
                [candidato.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()


            messages.error(request, 'Enviamos um e-mail para o endereço informado, que dará acesso ao cadastro.')

            return redirect ('/')

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
        form = ConsultaForm()

    return render(request, 'consulta.html', { 'form': form })


def consulta_chave(request, chave):

    try:
        candidato = Candidato.objects.get(chave=chave)
    except ObjectDoesNotExist:
        messages.error(request, 'Chave não cadastrada.')
        return redirect ('/consulta')

    return render(request, 'cadastro_mostra.html', { 'candidato': candidato })



def cadastro_corrige(request, chave):
    from django.template import Context
    from django.template.loader import render_to_string, get_template
    from django.core.mail import EmailMessage
    import uuid
    from ipware import get_client_ip

    try:
        candidato = Candidato.objects.get(chave=chave)
    except ObjectDoesNotExist:
        messages.error(request, 'Chave não cadastrada.')
        return redirect ('/consulta')


    if request.method == 'POST':
        form = CandidatoForm(request.POST, instance=candidato)

        if form.is_valid():
            cadastro = form.save(commit=False)

            chave = str(uuid.uuid4())
            cadastro.chave = chave

            # Busca IP

            client_ip, is_routable = get_client_ip(request)
            if client_ip is None:
                # Unable to get the client's IP address
                print(client_ip)
                client_ip = '0.0.0.0'
            else:
                # We got the client's IP address
                if is_routable:
                    print('sim:', is_routable)
                    # The client's IP address is publicly routable on the Internet
                else:
                    print('não:', is_routable)
                    # The client's IP address is privat

            cadastro.ip = client_ip

            cadastro.save()

            # Envia e-mail

            dados = {
                'id': cadastro.id,
                'nome': cadastro.nome,
                'dt_nascimento': cadastro.dt_nascimento,
                'cpf': cadastro.cpf,
                'celular': cadastro.celular,
                'tel': cadastro.tel,
                'email': cadastro.email,
                'deficiencia': cadastro.deficiencia,
                'qual_deficiencia': cadastro.qual_deficiencia,
                'necessidade': cadastro.necessidade,
                'dt_inclusao': cadastro.dt_inclusao,
                'ip': cadastro.ip,
            }

            mensagem = get_template('mail.html').render(dados)

            msg = EmailMessage(
                'Correção da inscrição do Processo Seletivo para Curso de Técnico em Enfermagem',
                mensagem,
                'Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima - Inscrição <inscricao@sme.novafriburgo.rj.gov.br>',
                [cadastro.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            return render(request, 'cadastrook.html', { 'chave': chave })

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
        form = CandidatoForm(instance=candidato)

    return render(request, 'cadastro.html', { 'form': form })


def contato(request):
    from django.template import Context
    from django.template.loader import render_to_string, get_template
    from django.core.mail import EmailMessage

    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():

            # Envia e-mail

            dados = {
                'nome': form.cleaned_data['nome'],
                'cpf': form.cleaned_data['cpf'],
                'celular': form.cleaned_data['celular'],
                'email': form.cleaned_data['email'],
                'duvida': form.cleaned_data['duvida'],
            }

            mensagem = get_template('mail_contato.html').render(dados)

            msg = EmailMessage(
                'Dúvidas',
                mensagem,
                'Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima - Inscrição <inscricao@sme.novafriburgo.rj.gov.br>',
                ['inscricao@sme.novafriburgo.rj.gov.br', 'loyola@sme.novafriburgo.rj.gov.br', 'eenfermagemnsf@sme.novafriburgo.rj.gov.br'],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            messages.error(request, 'E-Mail enviado. Entraremos em contato em breve para sanar sua dúvida.')

            return redirect ('/')

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
        form = ContatoForm()

    return render(request, 'contato.html', { 'form': form })
