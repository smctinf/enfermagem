from django.contrib import admin
from .models import *

# Register your models here.

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'dt_nascimento', 'tel', 'deficiencia', 'dt_inclusao']
    list_filter = ['deficiencia']
    search_fields = ['nome']

admin.site.register(Candidato, CandidatoAdmin)
