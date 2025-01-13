from django.contrib import admin
from .models import Dados_IBGE
from django.db.models import Count

class Dados_IBGEAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'populacao')  # Columns to display in the admin list
    list_filter = ('uf', 'cobertura_tvc', 'cobertura_feita_por')  # Fields for filtering
    search_fields = ('cidade', 'cobertura_feita_por')  # Fields to include in the search

# Register your model with the admin site
admin.site.register(Dados_IBGE, Dados_IBGEAdmin)