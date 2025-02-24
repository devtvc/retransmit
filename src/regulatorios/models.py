from django.db import models
from IBGE.models import Dados_IBGE

# Create your models here.
class Dados_Regulatorios(models.Model):
    # def get_cidade_choices():
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
    #      # Fetch choices dynamically from the Cidade model
    #     unique_ufs = Dados_IBGE.objects.values_list('uf', flat=True).distinct()
    #     return [(uf, uf) for uf in unique_ufs]
    
    # uf = models.CharField(
    #     max_length=100,
    #     choices=get_uf_choices,
    #     blank=True,
    #     null=True,
    # )
    #UFS = [
    #    ('item1', 'SP'),
    #    ('item2', 'DF'),
    #]
    #uf = models.CharField(max_length=10, choices=UFS, default='item1')
    uf = models.CharField(max_length=10)
    local_especifico = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name="Endereço da estação")
    

    canal_fisico = models.CharField(max_length=100)
    STATUS = [
       ('item1', 'TV-C1 (Canal Outorgado - Aguardando Ato de RF)'),
       ('item2', 'TV-C2'),
       ('item3', 'TV-C3'),
       ('item4', 'TV-C4 (Canal Licenciado)'),
       ('item5', 'TV-C5 (Canal pendente de outorga)'),
       ('item6', 'AM-C4 (Canal Licenciado)'),
       ('item7', 'FM-C4 (Canal Licenciado)'),
       ('item8', 'PPDUR À PAGAR'),
       ('item9', 'À LICENCIAR'),
       ('item10', 'ENTRAR EM OPERAÇÃO'),
       ('item11', 'OUTROS'),
    ]
    status_anatel = models.CharField(max_length=100, choices=STATUS, help_text="Escolha um item")
    prazo_anatel = models.DateField(null=True, blank=True, verbose_name="Prazo limite junto à Anatel/MCOM")
    observacao_anatel = models.CharField(max_length=200, null=True, blank=True, verbose_name="Observação", help_text="Por exemplo: responder exigências, entrar em operação, pagar TFI etc")
    validade_uso_rf = models.DateField(null=True, blank=True, verbose_name="Validade Uso RF")
    data_emissao_licenca = models.DateField(null=True, blank=True, verbose_name="Data da emissão da licença")
    numero_fistel = models.CharField(max_length=100)
    #CARATERS = [
    #    ('item1', 'P'),
    #    ('item2', 'S'),
    #]
    #carater = models.CharField(max_length=10, choices=CARATERS, default='item1')
    carater = models.CharField(max_length=10, help_text="P,S")
    #FINALIDADES = [
    #    ('item1', 'COMERCIAL'),
    #    ('item2', 'EDUCATIVO'),
    #    ('item3', 'EDUC. PUBLICO'),
    #    ('item4', 'PUBLICO'),
    #]
    #finalidade = models.CharField(max_length=10, choices=FINALIDADES, default='item1')
    finalidade = models.CharField(max_length=100)
    #SERVICOS = [
    #    ('item1', 'RTVD'),
    #    ('item2', 'GTVD'),
    #    ('item3', 'AM'),
    #    ('item4', 'FM'),
    #]
    #servico = models.CharField(max_length=10, choices=SERVICOS, default='item1')
    servico = models.CharField(max_length=100, help_text="RTVD, GTVD, ECRD, AM, FM")
    frequencia = models.CharField(max_length=100, help_text="Frequência do canal em MHz")

    MARCAS_TX = [
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

    fabricante_tx = models.CharField(max_length=100, choices=MARCAS_TX, default="item1", verbose_name="Fabricante do transmissor principal")
    modelo_tx = models.CharField(max_length=100, verbose_name="Modelo do transmissor principal")
    codigo_homolog_tx = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código de homologação do transmissor principal")
    pot_operacao = models.FloatField(max_length=100, verbose_name="Potência de operação aprovada em kW")
    fabricante_tx_aux = models.CharField(max_length=100, choices=MARCAS_TX, default="item1", blank=True, null=True, verbose_name="Fabricante do transmissor auxiliar")
    modelo_tx_aux = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modelo do transmissor auxiliar")
    codigo_homolog_tx_aux = models.CharField(max_length=100, blank=True, null=True, verbose_name="Código de homologação do transmissor auxiliar")
    pot_max_aux = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Potência máxima do transmissor auxiliar")
    fabricante_antena_tx = models.CharField(max_length=100, choices=MARCAS_ANT_TX, default="item1", verbose_name="Fabricante da antena de transmissão")
    modelo_antena_tx = models.CharField(max_length=100, verbose_name="Modelo da antena de transmissão")
    tipo_antena_tx = models.CharField(max_length=100, verbose_name="Tipo da antena de transmissão", help_text="Ex.: Slot")
    azimute = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Azimute/Orientação", help_text="Azimute/Direção de orientação da Antena e relação ao norte verdadeiro")
    tilt = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Tilt", help_text="Tilt da antena de transmissão em graus °")
    hci = models.CharField(max_length=100)
    fabricante_linha_tx = models.CharField(max_length=100, blank=True, null=True, verbose_name="Fabricante da linha de transmissão", help_text="Linha/cabo de Transmissão - Fabricante")
    comp_linha_tx = models.FloatField(max_length=100, blank=True, null=True, verbose_name="Comprimento da linha de transmissão", help_text="Linha/cabo de Transmissão - Comprimento em metros")
    modelo_linha_tx = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modelo da linha de transmissão", help_text="Linha/cabo de Transmissão - Modelo")
    
    #CLASSES = [
    #    ('item1', 'A'),
    #    ('item2', 'B'),
    #    ('item3', 'C'),
    #    ('item4', 'D'),
    #    ('item5', 'E'),
    #    ('item6', 'E2'),
    #]
    #classe = models.CharField(max_length=10, choices=CLASSES, default='item1')
    classe = models.CharField(max_length=100)
    #CATEGORIAS = [
    #    ('item1', 'PRINCIPAL'),
    #    ('item2', 'COMPLEMENTAR'),
    #]
    #categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='item1')

    categoria = models.CharField(max_length=100, help_text="Complementar, principal")
    altitude = models.CharField(max_length=100)
    erp = models.CharField(max_length=100)
    fase = models.CharField(max_length=100)
    anexo_mancha_de_cobertura = models.ImageField(upload_to='imagens_projeto/', blank=True, null=True, verbose_name="Anexo da imagem da mancha de cobertura")
    anexo_licenca = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Anexo da licença da estação")
    relatorio_conformidade = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Relatório de conformidade")
    laudo_vistoria = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Laudo de vistoria")
    comentarios = models.TextField()

    class Meta:
        ordering = ['cidade']
        db_table = 'rede_dados_regulatorios'
        verbose_name = "Dados Regulatórios"  # Singular name
        verbose_name_plural = "Dados Regulatórios"  # Plural name


    def __str__(self):
        return self.cidade