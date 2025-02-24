from django.db import models
from estacao.models import Estacao
from IBGE.models import Dados_IBGE

# Create your models here.
class Inventario(models.Model):
    def get_cidade_choices():
         # Fetch choices dynamically from the Cidade model
        unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
        return [(cidade, cidade) for cidade in unique_cidades]
    
    cidade = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
        verbose_name="Cidade/Estação"
    )
    #cidade = models.CharField(max_length=100)
    EQUIPES = [
       ('item1', 'SP-1'),
       ('item2', 'SP-2'),
       ('item3', 'SP-3'),
       ('item4', 'SP-4'),
    ]
    equipe = models.CharField(max_length=500, choices=EQUIPES, verbose_name="Equipe")

    EQUIPAMENTOS = [
       ('item1', 'AR CONDICIONADO'),
       ('item2', 'TRANSMISSOR UHF'),
       ('item3', 'RECEPTOR SAT'),
       ('item4', 'ANTENA RX'),
       ('item5', 'ANTENA TX'),
       ('item6', 'OUTROS - DETALHAR EM COMENTÁRIOS'),
    ]
    
    descricao = models.CharField(max_length=100, choices=EQUIPAMENTOS, verbose_name="Descrição do ativo")
    serial_number = models.CharField(max_length=100)
    ativo_fixo = models.CharField(max_length=100)
    foto_ativo_frontal = models.ImageField(upload_to='fotos_ativos/', blank=True, null=True, help_text="Carregue uma foto da parte de frente do ativo")
    foto_ativo_traseira = models.ImageField(upload_to='fotos_ativos/', blank=True, null=True, help_text="Carregue uma foto da parte traseira do ativo")
    comentarios = models.TextField(help_text="Insira informações relevantes sobre esse ativo")

    class Meta:
        ordering = ['cidade']
        db_table = 'rede_inventario'
        verbose_name = "Inventário"  # Singular name
        verbose_name_plural = "Inventário"  # Plural name


    def __str__(self):
        return self.get_descricao_display()