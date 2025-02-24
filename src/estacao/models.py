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

    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=500)
    cep = models.CharField(max_length=100, blank=True, null=True, help_text="CEP do endereço da estação")

    OUTORGAS = [
        ('item1', 'FPA'),
        ('item2', 'PM'),
        ('item3', 'REVOGADA'),
        ('item4', 'AFILIADA - TV JORNAL DE LIMEIRA'),
        ('item5', 'AFILIADA - TV COSTA NORTE'),
        ('item6', 'AFILIADA - TV CULTURA PAULISTA'),
        ('item7', 'OUTROS - INFORMAR EM COMENTÁRIOS'),
    ]

    outorga_estacao = models.CharField(max_length=30, choices=OUTORGAS, default="item1", blank=True)

    #uf = models.CharField(max_length=10)
    canal_virtual = models.CharField(max_length=30)
    potencia_projeto = models.CharField(max_length=30, help_text="Potência de projeto em W", verbose_name="Potência de Projeto/Licença")
    potencia_operacao = models.CharField(max_length=30, help_text="Potência de operação em W")

    _S_N = [
       ('item1', 'SIM'),
       ('item2', 'NÃO'),
    ]

    sfn = models.CharField(max_length=10, choices=_S_N, blank=True)
    sfn_com = models.TextField(null=True, blank=True, help_text="Digite todas as cidades que fazem SFN com essa estação, separadas por vírgula", verbose_name="SFN com")
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

    MARCAS_TX_RX = [
       ('item1', 'TECSYS'),
       ('item2', 'ANYWAVE'),
       ('item3', 'HITACHI'),
       ('item4', 'SCREEN'),
       ('item5', 'LINEAR (CONVERTIDO)'),
    ]

    MARCAS_ANT_TX = [
       ('item1', 'IDEAL'),
       ('item2', 'DIGITAL'),
       ('item3', 'POLIDESIGN'),
       ('item4', 'IF TELECOM'),
       ('item5', 'LUMICOM'),
       ('item6', 'ORIGINAL TELECOM'),
       ('item7', 'PAINEL'),
       ('item8', 'POLITELCO'),
       ('item9', 'TRANSTEL'),
    ]

    TIPOS_TORRE = [
       ('item1', 'AUTOSUPORTADA'),
       ('item2', 'ESTAIADA'),
       ('item3', 'ALVENARIA'),
       ('item4', 'AP'),
       ('item5', 'CAIXA D AGUA'),
       ('item6', 'PRÉDIO'),
       ('item7', 'TUBULÃO DE FERRO'),
       ('item8', 'TUBULÃO GALVANIZADO'),
    ]

    OPERACOES = [
       ('item1', 'OPERACIONAL'),
       ('item2', 'SEM OPERAÇÃO'),
       ('item3', 'OPERANDO SEM LICENÇA'),
    ]

    status_operacao = models.CharField(max_length=100, choices=OPERACOES, verbose_name="Situação da estação retransmissora")
    fabricante_tx = models.CharField(max_length=100, choices=MARCAS_TX_RX, blank=True, null=True)
    modelo_tx = models.CharField(max_length=100)
    codigo_homolog_tx = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código de homologação do transmissor")
    fabricante_antena_tx = models.CharField(max_length=100, choices=MARCAS_ANT_TX, blank=True, null=True, verbose_name="Fabricante da antena de transmissão")
    modelo_antena_tx = models.CharField(max_length=100)
    azimute = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Azimute/Orientação", help_text="Azimute/Direção de orientação da Antena e relação ao norte verdadeiro")
    fabricante_linha_tx = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fabricante da linha de transmissão", help_text="Linha/cabo de Transmissão - Fabricante")
    comp_linha_tx = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Comprimento da linha de transmissão", help_text="Linha/cabo de Transmissão - Comprimento")
    fabricante_rx = models.CharField(max_length=100, choices=MARCAS_TX_RX, null=True, blank=True, help_text="Tecsys, Anywave, Hitachi etc", verbose_name="Fabricante receptor/excitador")
    modelo_rx = models.CharField(max_length=100, null=True, blank=True, verbose_name="Modelo receptor/excitador")
    fabricante_antena_rx = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fabricante da antena de recepção de satélite")
    diametro_antena_rx = models.FloatField(max_length=100, null=True, blank=True, help_text="Diâmetro da antena de recepção de satélite em metros")
    tipo_torre = models.CharField(max_length=100, choices=TIPOS_TORRE, null=True, blank=True)
    altura_torre = models.CharField(max_length=100, help_text="Altura da torre em metros")
    proprietario_torre = models.CharField(max_length=100, help_text="CNPJ ou razão social")
    ar_condicionado = models.CharField(max_length=100, choices=_S_N, null=True, blank=True, help_text="Sim - Possui, Não - Não possui", verbose_name="Ar condicionado")
    fabricante_ar_condicionado = models.CharField(max_length=100, blank=True, help_text="Consul, Eletrolux etc")
    modelo_ar_condicionado = models.CharField(max_length=100, null=True, blank=True, verbose_name="Modelo do aparelho de ar condicionado")

    status_telemetria = models.CharField(max_length=100, choices=_S_N, help_text="Sim = Instalado, Não = não instalado", verbose_name="Status sistema de telemetria", null=True, blank=True)
    proprietario_terreno = models.CharField(max_length=100)
    seguro_estacao = models.CharField(max_length=100, choices=_S_N, null=True, blank=True)


    #energia_paga_por = models.CharField(max_length=100, choices=RESPONSABILIDADE)
    energia_paga_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA etc")

    #agua_paga_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    agua_paga_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA etc")

    #aluguel_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    aluguel_pago_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA etc")

    #iptu_pago_por = models.CharField(max_length=10, choices=RESPONSABILIDADE, default='item1')
    iptu_pago_por = models.CharField(max_length=100, help_text="PM / PMSP / FPA etc")

    ABRIGOS = [
        ('item1', 'ALVENARIA'),
        ('item2', 'CONTAINER'),
    ]

    tipo_abrigo = models.CharField(max_length=100, choices=ABRIGOS, help_text="Alvenaria, container etc", verbose_name="Tipo do abrigo")

    FOTO1 = models.ImageField(upload_to='manutencao/', blank=True, null=True, verbose_name="Foto da estação (1)")
    FOTO2 = models.ImageField(upload_to='manutencao/', blank=True, null=True, verbose_name="Foto da estação (2)")
    FOTO3 = models.ImageField(upload_to='manutencao/', blank=True, null=True, verbose_name="Foto da estação (3)")
    FOTO4 = models.ImageField(upload_to='manutencao/', blank=True, null=True, verbose_name="Foto da estação (4)")
    FOTO5 = models.ImageField(upload_to='manutencao/', blank=True, null=True, verbose_name="Foto da estação (5)")

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