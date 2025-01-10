from django.db import models

# Create your models here.
class Dados_Equipamentos(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50)

    #TRANSMISSOR UHF 
    potencia_tx = models.CharField(max_length=100, help_text="Potência nominal do transmissor em Watts")
    modelo_tx = models.CharField(max_length=100, help_text="Marca/Modelo do transmissor UHF")

    #ANTENA DE TRANSMISSÃO
    fabricante_antena_tx = models.CharField(max_length=100)
    modelo_antena_tx = models.CharField(max_length=100)

    #RECEPTOR DE SATÉLITE
    modelo_rx = models.CharField(max_length=100, blank=True, help_text="Marca/Modelo do receptor")

    #ANTENA DE RECEPÇÃO 
    fabricante_antena_rx = models.CharField(max_length=100, blank=True)
    diametro_antena_rx = models.FloatField(null=True, blank=True)

    #TORRE
    tipo_torre = models.CharField(max_length=100, help_text="Ex.: Estaiada, autosuportada etc")
    altura_torre = models.CharField(max_length=100, help_text="Altura da torre em metros")

    #AR CONDICIONADO
    modelo_ar_condicionado = models.CharField(max_length=100, blank=True, help_text="Marca/Modelo do aparelho de ar-condicionado. Deixe em branco se a estação não possui")

    #COMENTÁRIOS
    comentarios = models.TextField(blank=True, help_text="Insira mais informações sobre os equipamentos dessa estação")

    class Meta:
        db_table = 'rede_dados_equipamentos'
        verbose_name = "Dados Equipamentos"  # Singular name
        verbose_name_plural = "Dados Equipamentos"  # Plural name


    def __str__(self):
        return self.cidade