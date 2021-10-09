from django.shortcuts import render
from .forms import *
from django.contrib import messages

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

            print('ip:', client_ip)

            cadastro.ip = client_ip

            cadastro.save()


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
                '<Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima> inscricao@sme.novafriburgo.rj.gov.br',
                [cadastro.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            """
            send_mail(
                'Inscrição do Processo Seletivo para Curso de Técnico em Enfermagem',
                mensagem,
                'enfermagem@sme.novafriburgo.rj.gov.br',
                [email],
                fail_silently=False,
            )

            msg = EmailMessage('Inscrição do Processo Seletivo para Curso de Técnico em Enfermagem', template.render(mensagem), 'enfermagem@sme.novafriburgo.rj.gov.br', email)
            msg.content_subtype = "html"
            msg.send()

            # TODO: enviar por e-mail o protocolo de inscrição
            """

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

            print('ip:', client_ip)

            cadastro.ip = client_ip

            cadastro.save()


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
                '<Escola de Auxiliares e Técnicos de Enfermagem Nossa Senhora de Fátima> inscricao@sme.novafriburgo.rj.gov.br',
                [cadastro.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

            """
            send_mail(
                'Inscrição do Processo Seletivo para Curso de Técnico em Enfermagem',
                mensagem,
                'enfermagem@sme.novafriburgo.rj.gov.br',
                [email],
                fail_silently=False,
            )

            msg = EmailMessage('Inscrição do Processo Seletivo para Curso de Técnico em Enfermagem', template.render(mensagem), 'enfermagem@sme.novafriburgo.rj.gov.br', email)
            msg.content_subtype = "html"
            msg.send()

            # TODO: enviar por e-mail o protocolo de inscrição
            """

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
        form = ConsultaForm()

    return render(request, 'consulta.html', { 'form': form })
