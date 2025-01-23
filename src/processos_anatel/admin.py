from django.contrib import admin
from .models import Processos_Anatel


class Processos_AnatelAdmin(admin.ModelAdmin):
    list_display = ('cidade','local_especifico','acao','prazo_anatel')  # Columns to display in the admin list
    list_filter = ('acao','prazo_anatel')  # Fields for filtering
    search_fields = ('cidade', 'local_especifico','acao')  # Fields to include in the search

# Register your models here.
admin.site.register(Processos_Anatel, Processos_AnatelAdmin)