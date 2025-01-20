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

    #uf = models.CharField(max_length=10)
    canal_virtual = models.CharField(max_length=30)
    potencia_projeto = models.CharField(max_length=30, help_text="Potência de projeto em W")
    potencia_operacao = models.CharField(max_length=30, help_text="Potência de operação em W")

    sfn = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
        help_text="Selecione a cidade que faz SFN com essa estação",
    )
    #sfn = models.CharField(max_length=10, blank=True)
    sfn_id = models.CharField(max_length=10, blank=True, help_text="Deixe em branco se a estação não faz SFN")

    equipe = models.CharField(max_length=10, help_text="Equipe de manutenção responsável")
    responsabilidade_operacao = models.CharField(max_length=100, help_text="Empresa responsável pela operação e manutenção da estação")

    # OPERADORA = [
    #    ('item1', 'TV CULTURA'),
    #    ('item2', 'TVC PAULISTA'),
    #    ('item3', 'TV COSTA NORTE'),
    #    ('item4', 'TV JORNAL'),
    # ]
    # responsabilidade_operacao = models.CharField(max_length=10, choices=OPERADORA, default="")

    status_operacao = models.CharField(max_length=100, help_text="OPERACIONAL ou SEM OPERAÇÃO")
    fabricante_tx = models.CharField(max_length=100, help_text="Tecsys, Anywave, Hitachi etc")
    modelo_tx = models.CharField(max_length=100)
    fabricante_antena_tx = models.CharField(max_length=100)
    modelo_antena_tx = models.CharField(max_length=100)
    fabricante_rx = models.CharField(max_length=100, help_text="Tecsys, Anywave, Hitachi etc")
    modelo_rx = models.CharField(max_length=100)
    fabricante_antena_rx = models.CharField(max_length=100)
    diametro_antena_rx = models.CharField(max_length=100, help_text="Diâmetro da antena de recepção de satélite em metros")
    tipo_torre = models.CharField(max_length=100, help_text="Estaiada, autosuportada etc")
    altura_torre = models.CharField(max_length=100, help_text="Altura da torre em metros")
    proprietario_torre = models.CharField(max_length=100, help_text="CNPJ ou razão social")
    fabricante_ar_condicionado = models.CharField(max_length=100, blank=True, help_text="Consul, Eletrolux etc")
    modelo_ar_condicionado = models.CharField(max_length=100)

    status_telemetria = models.CharField(max_length=100, help_text="Instalado ou Não instalado")
    proprietario_terreno = models.CharField(max_length=100)

    # RESPONSABILIDADE = [
    #     ('item1', 'FPA'),
    #     ('item2', 'PM'),
    #     ('item3', 'PMSP'),
    # ]

    #energia_paga_por = models.CharField(max_length=100, choices=RESPONSABILIDADE)
    energia_paga_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA")

    #agua_paga_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    agua_paga_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA")

    #aluguel_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    aluguel_pago_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA")

    #iptu_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    iptu_pago_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA")

    tipo_abrigo = models.CharField(max_length=100, help_text="Alvenaria, container etc")
    endereco = models.CharField(max_length=500)
    anexo_contrato_estacao = models.FileField(upload_to='pdfs/', blank=True, null=True, help_text="Anexo do contrato em PDF")
    comentarios = models.TextField(blank=True, help_text="Insira outras informações relevantes sobre a estação")

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
        ordering = ['cidade']
        db_table = "rede_estacao"
        verbose_name = "Estação"  # Singular name
        verbose_name_plural = "Estações"  # Plural name

    def __str__(self):
        return self.cidade