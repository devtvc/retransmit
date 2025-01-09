from django.db import models

# Create your models here.
class Dados_Equipamentos(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50)
    potencia_tx = models.CharField(max_length=100)
    modelo_tx = models.CharField(max_length=100)
    fabricante_antena_tx = models.CharField(max_length=100)
    modelo_antena_tx = models.CharField(max_length=100)
    modelo_rx = models.CharField(max_length=100, blank=True)
    nivel_recepcao = models.CharField(max_length=100, blank=True)
    fabricante_antena_rx = models.CharField(max_length=100, blank=True)
    diametro_antena_rx = models.FloatField(null=True, blank=True)
    tipo_torre = models.CharField(max_length=100)
    altura_torre = models.CharField(max_length=100)
    modelo_ar_condicionado = models.CharField(max_length=100, blank=True)
    comentarios = models.TextField(blank=True)

    class Meta:
        db_table = 'rede_dados_equipamentos'
        verbose_name = "Dados Equipamentos"  # Singular name
        verbose_name_plural = "Dados Equipamentos"  # Plural name


    def __str__(self):
        return self.cidade