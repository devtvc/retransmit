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

    canal_fisico = models.CharField(max_length=100)
    #STATUS = [
    #    ('item1', 'TV-C1 (Canal Outorgado - Aguardando Ato de RF)'),
    #    ('item2', 'TV-C2'),
    #    ('item3', 'TV-C3'),
    #    ('item4', 'TV-C4 (Canal Licenciado)'),
    #    ('item5', 'TV-C5 (Canal pendente de outorga)'),
    #    ('item6', 'AM-C4 (Canal Licenciado)'),
    #    ('item7', 'FM-C4 (Canal Licenciado)'),
    #]
    #status_anatel = models.CharField(max_length=100, choices=STATUS, default='item1')
    status_anatel = models.CharField(max_length=100, help_text="C1 à C5")
    validade = models.DateField(null=True, blank=True)
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
    servico = models.CharField(max_length=100, help_text="RTVD, GTVD, AM, FM")
    frequencia = models.CharField(max_length=100, help_text="Frequência do canal em MHz")
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
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)
    erp = models.CharField(max_length=100)
    hci = models.CharField(max_length=100)
    fase = models.CharField(max_length=100)
    anexo_mancha_de_cobertura = models.ImageField(upload_to='imagens_projeto/', blank=True, null=True)
    anexo_licenca = models.FileField(upload_to='pdfs/', blank=True, null=True)
    comentarios = models.TextField()

    class Meta:
        ordering = ['cidade']
        db_table = 'rede_dados_regulatorios'
        verbose_name = "Dados Regulatórios"  # Singular name
        verbose_name_plural = "Dados Regulatórios"  # Plural name


    def __str__(self):
        return self.cidade