from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from .functions import validate_CPF


class CandidatoForm(ModelForm):
    DEFICIENCIA = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    cpf = forms.CharField(label='CPF', max_length=14, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icpf)"}))
    celular = forms.CharField(label= "Celular", max_length=15, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icelular)", 'onload' : 'mascara(this,icelular)'}))
    tel = forms.CharField(label = "Telefone",required=False, max_length=14, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,itelefone)", 'onload' : 'mascara(this,itelefone)'}))
    dt_nascimento = forms.DateField(label='Dt. Nascimento:', required=True, widget=forms.SelectDateWidget(years=range(1900, 2010)))

#    deficiencia = forms.CharField(widget=forms.RadioSelect(choices=DEFICIENCIA))
    deficiencia = forms.ChoiceField(widget=forms.RadioSelect, choices=DEFICIENCIA)

    class Meta:
        model = Candidato
        exclude = ['dt_inclusao']

    def clean_cpf(self):
        cpf = validate_CPF(self.cleaned_data["cpf"])
        return cpf

    def clean_celular(self):
        telefone = self.cleaned_data["celular"]
        telefone = telefone.replace("(",'')
        telefone = telefone.replace(")",'')
        telefone = telefone.replace("-",'')
        telefone = telefone.replace(" ",'')
        if len(telefone) == 10:
            if telefone[2:3] != '2':
                raise ValidationError('Insira um número válido ')
        else:
            if len(telefone) != 11:
                raise ValidationError('Insira um número válido ')
        return telefone
    
    def clean_tel(self):
        telefone = self.cleaned_data["tel"]
        telefone = telefone.replace("(",'')
        telefone = telefone.replace(")",'')
        telefone = telefone.replace("-",'')
        telefone = telefone.replace(" ",'')
        if len(telefone) != 10 and len(telefone) != 0:
            raise ValidationError('Insira um número válido')        
        return telefone
