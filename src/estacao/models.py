from django.db import models
from IBGE.models import Dados_IBGE
from manutencao.models import Relatorio_Manutencao



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
    id = models.AutoField(primary_key=True)
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
    potencia_projeto = models.CharField(max_length=30, help_text="Potência de projeto em W")
    potencia_operacao = models.CharField(max_length=30, help_text="Potência de operação em W")

    # sfn = models.CharField(
    #     max_length=100,
    #     choices=get_cidade_choices,
    #     blank=True,
    #     null=True,
    #     help_text="Selecione a cidade que faz SFN com essa estação",
    # )
    sfn = models.CharField(max_length=10, blank=True)
    sfn_id = models.CharField(max_length=10, blank=True, help_text="Deixe em branco se a estação não faz SFN")

    equipe = models.CharField(max_length=10, help_text="Equipe de manutenção responsável")
    responsabilidade_operacao = models.CharField(max_length=100, help_text="Empresa responsável pela operação e manutenção da estação")
    status_operacao = models.CharField(max_length=100)
    status_telemetria = models.CharField(max_length=100)
    proprietario_torre = models.CharField(max_length=100)
    proprietario_terreno = models.CharField(max_length=100)

    # RESPONSABILIDADE = [
    #     ('item1', 'FPA'),
    #     ('item2', 'PM'),
    #     ('item3', 'PMSP'),
    # ]

    #energia_paga_por = models.CharField(max_length=100, choices=RESPONSABILIDADE)
    energia_paga_por = models.CharField(max_length=100)

    #agua_paga_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    agua_paga_por = models.CharField(max_length=100)

    #aluguel_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    aluguel_pago_por = models.CharField(max_length=100)

    #iptu_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    iptu_pago_por = models.CharField(max_length=100)

    tipo_abrigo = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=500)
    comentarios = models.TextField(blank=True, help_text="Insira outras informações relevantes sobre a estação")

    # disponibilidade_30_dias = models.FloatField(null=True, blank=True, editable=False)

    # def save(self, *args, **kwargs):
    #     # Example: Automatically set 'disponibilidade_30_dias' to a default value if it's None
    #     if self.disponibilidade_30_dias is None:
    #         self.disponibilidade_30_dias = 0.0  # Set a default value if None

    #     # Call the parent class's save method to save the instance to the database
    #     super().save(*args, **kwargs)

    # @staticmethod
    # def get_disponibilidade_by_cidade(cidade):
    #     # Filter RelatorioManutencao where cidade matches
    #     disponibilidade_estacoes = Relatorio_Manutencao.objects.filter(cidade=Estacao.cidade).values_list('disponibilidade_30_dias', flat=True)
        
    #     # Return the filtered disponibilidade_30_dias values in tuple form
    #     return [(disponibilidade_estacao, disponibilidade_estacao) for disponibilidade_estacao in disponibilidade_estacoes if disponibilidade_estacao is not None]
    

    
    
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