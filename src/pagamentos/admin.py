from django.contrib import admin
from .models import Dados_Pagamento

class Dados_PagamentoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'tipo_conta', 'mes_referencia')  # Columns to display in the admin list
    list_filter = ('tipo_conta', 'mes_referencia')  # Fields for filtering
    search_fields = ('cidade', 'tipo_conta')  # Fields to include in the search

# Register your models here.
admin.site.register(Dados_Pagamento, Dados_PagamentoAdmin)