from django.contrib import admin
from .models import Telemetria

# Register your models here.

class TelemetriaAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'versao_software')  # Columns to display in the admin list
    list_filter = ('versao_software', 'data_instalacao')  # Fields for filtering
    search_fields = ('cidade', 'versao_software')  # Fields to include in the search

admin.site.register(Telemetria, TelemetriaAdmin)

