from django.db import models

# Create your models here.
class Dados_IBGE(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)
    prefeito = models.CharField(max_length=100)
    area_territorial = models.FloatField(blank=True, null=True)
    populacao = models.FloatField(blank=True, null=True)
    densidade_demografica = models.FloatField(blank=True, null=True)
    escolarizacao = models.FloatField(blank=True, null=True)
    cobertura_feita_por = models.CharField(max_length=100)
   
    class Meta:
        db_table = "rede_dados_ibge"
        verbose_name = "Dados Cidades"  # Singular name
        verbose_name_plural = "Dados Cidades"  # Plural name

    def __str__(self):
        return self.cidade