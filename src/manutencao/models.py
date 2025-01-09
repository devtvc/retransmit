from django.db import models
from estacao.models import Estacao
from django.utils import timezone

# Create your models here.
class Relatorio_Manutencao(models.Model):
    # def get_cidade_choices():
    #     from rede.models import Dados_IBGE
    #      # Fetch choices dynamically from the Cidade model
    #     unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
    #     return [(cidade, cidade) for cidade in unique_cidades]
    
    # cidade = models.CharField(
    #     max_length=100,
    #     choices=get_cidade_choices,
    #     blank=True,
    #     null=True,
    # )

    cidade = models.CharField(max_length=100)

    # def get_uf_choices():
    #     from rede.models import Dados_IBGE
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

    data_reclamacao = models.DateTimeField(null=True, blank=True)
    data_manutencao = models.DateTimeField(null=True, blank=True)
    autor_manutencao = models.CharField(max_length=100, blank=True)
    TIPO_MANUT = [
        ('item1', 'PREVENTIVA'),
        ('item2', 'CORRETIVA'),
        ('item3', 'EMERGENCIAL'),
    ]
    tipo_manutencao = models.CharField(max_length=10, choices=TIPO_MANUT, default='item1')
    comentario_manutencao = models.TextField(blank=True)
    pot_direta = models.FloatField(null=True, blank=True)
    pot_refletida = models.FloatField(null=True, blank=True)
    exciter_power = models.FloatField(null=True, blank=True)
    nivel_CN = models.FloatField(null=True, blank=True)
    nivel_recepcao = models.FloatField(null=True, blank=True)
    VISTA_FRONTAL_TX = models.ImageField(upload_to='images/', blank=True, null=True)
    VISTA_TRASEIRA_TX = models.ImageField(upload_to='images/', blank=True, null=True)
    ANTENA_DE_RECEPCAO = models.ImageField(upload_to='images/', blank=True, null=True)
    ANTENA_DE_TRANSMISSAO_E_DA_TORRE = models.ImageField(upload_to='images/', blank=True, null=True)
    ABRIGO_1_INTERNO = models.ImageField(upload_to='images/', blank=True, null=True)
    ABRIGO_2_INTERNO = models.ImageField(upload_to='images/', blank=True, null=True)
    ABRIGO_1_EXTERNO = models.ImageField(upload_to='images/', blank=True, null=True)
    ABRIGO_2_EXTERNO = models.ImageField(upload_to='images/', blank=True, null=True)
    VISAO_GERAL = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'rede_relatorio_manutencao'
        verbose_name = "Relatório Manutenção"  # Singular name
        verbose_name_plural = "Relatório Manutenção"  # Plural name


    def __str__(self):
        data_manutencao_local = timezone.localtime(self.data_manutencao) if self.data_manutencao else None
        return f"{self.cidade} - {data_manutencao_local}"