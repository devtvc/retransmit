from django.db import models
from IBGE.models import Dados_IBGE


# Create your models here.
class Telemetria(models.Model):
    def get_cidade_choices():
         # Fetch choices dynamically from the Cidade model
        unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
        return [(cidade, cidade) for cidade in unique_cidades]
    
    cidade = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
    )
    
    # def get_uf_choices():
    #      # Fetch choices dynamically from the Cidade model
    #     unique_ufs = Dados_IBGE.objects.values_list('uf', flat=True).distinct()
    #     return [(uf, uf) for uf in unique_ufs]
    
    # uf = models.CharField(
    #     max_length=100,
    #     choices=get_uf_choices,
    #     blank=True,
    #     null=True,
    # )
    
    UFs = [
        ('item1', 'SP'),
        ('item2', 'DF'),
    ]
    uf = models.CharField(max_length=10, choices=UFs, default='item1')

    VERSAO_SW = [
         ('item1', 'TECSYS'),
         ('item2', 'ANYWAVE V1'),
         ('item3', 'ANYWAVE V2'),
         ('item4', 'HITACHI'),
     ]
    
    OPERADORAS_MOVEIS = [
         ('item1', 'VIVO'),
         ('item2', 'CLARO'),
         ('item3', 'TIM'),
         ('item4', 'OI'),
     ]
    
    STATUS_INSTALACAO = [
         ('item1', 'INSTALADO'),
         ('item2', 'NÃO INSTALADO POR FALTA DE SINAL'),
         ('item3', 'NÃO INSTALADO POR FALHA NO EQUIPAMENTO'),
     ]
    
    TIPO_MODENS = [
         ('item1', 'USB (INTERNO)'),
         ('item2', 'ETHERNET (EXTERNO)'),
     ]
    
    versao_software = models.CharField(max_length=30, choices=VERSAO_SW, default="item1")
    numero_chip = models.CharField(max_length=30, default="")
    id_chip = models.CharField(max_length=30, default="")
    operadora = models.CharField(max_length=30, choices=OPERADORAS_MOVEIS, default="item1")
    serial_number_modem = models.CharField(max_length=50, default="")
    tipo_modem = models.CharField(max_length=30, choices=TIPO_MODENS, default="item1")
    modelo_modem = models.CharField(max_length=100, default="")
    data_instalacao = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_INSTALACAO, default="item1")
    comentarios = models.TextField(help_text="Insira informações relevantes sobre esse sistema de telemetria")

    class Meta:
        ordering = ['cidade']
        db_table = "rede_telemetria"
        verbose_name = "Telemetria"  # Singular name
        verbose_name_plural = "Telemetria"  # Plural name

    def __str__(self):
        return self.cidade