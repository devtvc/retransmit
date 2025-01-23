from django.contrib import admin
from .models import Estacao


# Register your models here.

class EstacaoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'responsabilidade_operacao')  # Columns to display in the admin list
    list_filter = ('uf', 'responsabilidade_operacao', 'status_operacao', 'sfn', 'modelo_tx', 'tipo_torre', 'status_telemetria', 'proprietario_terreno', 'energia_paga_por', 'agua_paga_por', 'aluguel_pago_por', 'iptu_pago_por','seguro_estacao')  # Fields for filtering
    search_fields = ('cidade', 'responsabilidade_operacao')  # Fields to include in the search

admin.site.register(Estacao, EstacaoAdmin)

