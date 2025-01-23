from django.contrib import admin
from .models import Dados_Regulatorios


class Dados_RegulatoriosAdmin(admin.ModelAdmin):
    list_display = ('cidade','local_especifico','servico','status_anatel')  # Columns to display in the admin list
    list_filter = ('status_anatel','carater', 'finalidade', 'servico', 'classe', 'categoria')  # Fields for filtering
    search_fields = ('cidade', 'status_anatel')  # Fields to include in the search

# Register your models here.
admin.site.register(Dados_Regulatorios, Dados_RegulatoriosAdmin)