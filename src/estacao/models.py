from django.db import models
from IBGE.models import Dados_IBGE


# Create your models here.
class Estacao(models.Model):
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
    #cidade = models.CharField(max_length=100)
    def get_uf_choices():
         # Fetch choices dynamically from the Cidade model
        unique_ufs = Dados_IBGE.objects.values_list('uf', flat=True).distinct()
        return [(uf, uf) for uf in unique_ufs]
    
    uf = models.CharField(
        max_length=100,
        choices=get_uf_choices,
        blank=True,
        null=True,
    )
    #uf = models.CharField(max_length=10)
    canal_virtual = models.CharField(max_length=30)
    potencia_projeto = models.CharField(max_length=30)
    potencia_operacao = models.CharField(max_length=30)

    sfn = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
        help_text="Selecione a cidade que faz SFN com essa estação",
    )

    #sfn = models.CharField(max_length=10)
    equipe = models.CharField(max_length=10)
    operacao = models.CharField(max_length=100)
    status_operacao = models.CharField(max_length=100)
    status_telemetria = models.CharField(max_length=100)
    proprietario_torre = models.CharField(max_length=100)
    proprietario_terreno = models.CharField(max_length=100)
    tipo_abrigo = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=500)
    comentarios = models.TextField()
    #RESPONSABILIDADE = [
    #    ('item1', 'FPA'),
    #   ('item2', 'PM'),
    #    ('item3', 'PMSP'),
    #]
    #proprietario_terreno = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    #proprietario_torre = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    #pgto_energia = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    #pgto_agua = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    #pgto_aluguel = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    #OPERADORA = [
    #    ('item1', 'TV CULTURA'),
    #    ('item2', 'TVC PAULISTA'),
    #    ('item3', 'TV COSTA NORTE'),
    #    ('item4', 'TV JORNAL'),
    #]
    #operacao = models.CharField(max_length=10, choices=OPERADORA, default='item1')
    
    #EQUIPES = [
    #    ('item1', 'SP1'),
    #    ('item2', 'SP2'),
    #    ('item3', 'SP3'),
    #   ('item4', 'SP4'),
    #]
    #equipe = models.CharField(max_length=10, choices=EQUIPES)
    #SFN_IDS = [
    #    ('item1', '1'),
    #   ('item2', '2'),
    #    ('item3', '3'),
    #    ('item4', '4'),
    #    ('item5', '5'),
    #    ('item6', '6'),
    #    ('item7', '7'),
    #]

    class Meta:
        db_table = "rede_estacao"
        verbose_name = "Estação"  # Singular name
        verbose_name_plural = "Estações"  # Plural name

    def __str__(self):
        return self.cidade