from django.contrib import admin
from .models import Inventario

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'equipe')  # Columns to display in the admin list
    list_filter = ('descricao', 'equipe')  # Fields for filtering
    search_fields = ('cidade', 'ativo_fixo', 'serial_number', 'descricao')  # Fields to include in the search


# Register your models here.
admin.site.register(Inventario, InventarioAdmin)