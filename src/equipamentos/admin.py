from django.contrib import admin
from .models import Dados_Equipamentos

# Register your models here.

class Dados_EquipamentosAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'uf')  # Columns to display in the admin list
    list_filter = ('modelo_rx', 'modelo_tx', 'tipo_torre')  # Fields for filtering
    search_fields = ('cidade', 'modelo_rx')  # Fields to include in the search

admin.site.register(Dados_Equipamentos, Dados_EquipamentosAdmin)