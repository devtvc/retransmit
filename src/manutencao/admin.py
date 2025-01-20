from django.contrib import admin
from .models import Relatorio_Manutencao

class Relatorio_ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'data_reclamacao', 'data_manutencao','tecnico_manutencao','dias_fora_do_ar')
    list_filter = ('data_reclamacao','data_manutencao', 'tecnico_manutencao','tipo_manutencao')
    search_fields = ('cidade', 'data_reclamacao', 'data_manutencao', 'tecnico_manutencao')

    def dias_fora_do_ar(self, obj):
        return obj.difference
    dias_fora_do_ar.short_description = "Dias fora do ar"

    

# Register your models here.
admin.site.register(Relatorio_Manutencao, Relatorio_ManutencaoAdmin)