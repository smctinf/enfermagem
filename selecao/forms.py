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
    dt_nascimento = forms.DateField(label='Dt. Nascimento:', required=True, widget=forms.SelectDateWidget(years=range(1900, 2010)))

#    deficiencia = forms.CharField(widget=forms.RadioSelect(choices=DEFICIENCIA))
    deficiencia = forms.ChoiceField(widget=forms.RadioSelect, choices=DEFICIENCIA)

    class Meta:
        model = Candidato
        exclude = ['dt_inclusao']

    def clean_cpf(self):
        cpf = validate_CPF(self.cleaned_data["cpf"])
        return cpf
