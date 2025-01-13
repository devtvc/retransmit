from django.contrib import admin
from .models import Relatorio_Manutencao

class Relatorio_ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'data_reclamacao', 'data_manutencao','tecnico_manutencao', 'disponibilidade_display')
    list_filter = ('data_reclamacao','data_manutencao', 'tecnico_manutencao','tipo_manutencao')
    search_fields = ('cidade', 'data_reclamacao', 'data_manutencao', 'tecnico_manutencao')

    def disponibilidade_display(self, obj):
        return obj.disponibilidade
    disponibilidade_display.short_description = "Disponibilidade Últimos 30 Dias"

    

# Register your models here.
admin.site.register(Relatorio_Manutencao, Relatorio_ManutencaoAdmin)