from django.db import models
from estacao.models import Estacao
from IBGE.models import Dados_IBGE

# Create your models here.
class Inventario(models.Model):
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
    #EQUIPES = [
    #    ('item1', 'SP-1'),
    #    ('item2', 'SP-2'),
    #    ('item2', 'SP-3'),
    #    ('item2', 'SP-4'),
    #]
    equipe = models.CharField(max_length=100)
    #def get_equipe_choices():
    #    # Fetch unique cidade values dynamically from the Estacao model
    #    unique_equipes = Estacao.objects.values_list('equipe', flat=True).distinct()
    #    return [(equipe, equipe) for equipe in unique_equipes]
    
    #equipe = models.CharField(
    #    max_length=100,
    #    choices=get_equipe_choices(),
    #    blank=True,
    #    null=True,
    #)
   
    descricao = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    ativo_fixo = models.CharField(max_length=100)
    comentarios = models.TextField()

    class Meta:
        db_table = 'rede_inventario'
        verbose_name = "Inventário"  # Singular name
        verbose_name_plural = "Inventário"  # Plural name


    def __str__(self):
        return self.descricao